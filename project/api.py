#Third party libraries
import watson_developer_cloud as watson

#Standard python libraries
import json
import re
import datetime as dt

#Local libraries
# from project import config
import config
# from project.dbmodel import CRM, FormDB



#modified watson object
class Watson(watson.ConversationV1):

    def __init__(self):
        super().__init__(username=config.WATSON_USERNAME, password=config.WATSON_PASSWORD, version=config.WATSON_VERSION)



    def watson_message(self, query, context=None):

        response = self.message(
            workspace_id=config.WATSON_WORKPLACE_ID,
            input={'text': str(query)},
            context=context
        )
        return response


def validate(context, uname):
    if 'piiConfirm' in context.keys() and 'autofillConfirm' in context.keys():
        if context['autofillConfirm'] == 'false':
            context['twoYearsAgo'] = (dt.datetime.today() - dt.timedelta(days=2*365)).strftime("%Y-%m-%d")
            context = {**context, **access_CRM(uname)}                          #merge an example users data into current context
            context['driversLicenceValid'] = "true" if 'driversLicence' in context else "false" #TODO remove HACK and actually validate
            if 'currEmploymentStartDate' in context.keys():
                 start_date = dt.datetime.strptime(str(context['currEmploymentStartDate']), "%Y-%m-%d")
                 todays_date = dt.datetime.today()
                 context['yearsTenure'] = round(float((todays_date - start_date).days/365),2)

            context['autofillConfirm'] = 'true'
            return context

    current_node = context['system']['dialog_stack'][0]['dialog_node']
    print('Current node: ', current_node)
    if current_node in ['node_73_1519022013998']:
        if 'prevEmploymentDateStart' in context.keys():
            print(json.dumps(context, indent=2))
            start_date = context['prevEmploymentDateStart'] if 'prevEmploymentDateStart' in context else context['currEmploymentDateStart']
            print(start_date)
            earliest_date = dt.datetime.strptime(str(start_date), "%Y-%m-%d")
            todays_date = dt.datetime.today()
            years = int((todays_date - earliest_date).days/365)
            context['yearsTenure'] = years
    if current_node in ['node_30_1519792519750']:
        if 'isRezOwned' in context.keys():
            if context['isRezOwned'] == 'true':
                context['propertyOwned1Address'] = context['residentialAddress'] + ' ' + context['residentialSuburb'] + ' ' + context['residentialState']
    return context



def retrive_cached_context(session):
    try:                                                                        #TODO robust session recovery
        context = session['context']
    except KeyError as e:
        context = None
        
        print(e)         
                                                                                #TODO log exception
    return context


def cache_context(context, session):

    pass

def log_response(response):
    print("===============================")
    print(response)
    print("###############################")
    pass

def update_form_DB(context, uname):

    if context:
        d = {}
        current_node = context['system']['dialog_stack'][0]['dialog_node']

        for key in context.keys():
            if key in config.FORM_FIELDS:
                row = FormDB.query.get(uname)
                if key in row.__table__.columns:
                    d[key] = context[key]
                else:
                    print("[DataBase Error]: Context variable " + key + " in config, but not in DB")
            else:
                print("Context variable not mapped in config:", key)

        if current_node == 'node_4_1519016328035' and False:                    #the confirmation node ID
            #TODO Update table using these commands
            """
            db.session.query(FormDB).update(d)
            db.session.commit()
            """
            pass
    pass


def tile_generation(context):
    tiles = []
    if context:
        current_node = context['system']['dialog_stack'][0]['dialog_node']
        print(current_node)
        print_context(context)
        if current_node == 'node_68_1519021622252':
            tile_title = "Your Personal Details"
            tiles.append(tile_table(title=tile_title, content=config.EXAMPLE_USER))


        if current_node == 'slot_50_1519019902036':
            tile_title = 'Employment history'
            tiles.append(tile_table(title=tile_title, content=config.EXAMPLE_CURRENT_EMPLOYMENT_HISTORY))



    return tiles

def tile_table(title, content):
    tile_title = title.title()
    tile_content = '<table><tr>'
    content_list = []
    if not isinstance(content, dict):
        raise TypeError('Content provided is not in a dictionary format. Cannot generate table')

    for key in content:
        content_list.append('<td>' + str(re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', key)).title() + '</td><td>' + str(content[key]) + '</td>')
    tile_content += "<tr></tr>".join(content_list) + '</tr></table>'
    tile = {'title': tile_title, 'body': tile_content}

    return tile

def print_context(context):
    for key in context:
        if key != 'system':
            print(key, context[key])

def print_entities(entities_list):
    for item in entities_list:
        print("Entity:", '"' + item['entity'] + '"', "| Value:", '"' + item['value'] + '"')

def access_CRM(uname):
    row = CRM.query.get(uname)
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d
