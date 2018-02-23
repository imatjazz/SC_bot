#Third party libraries
import watson_developer_cloud as watson

#Standard python libraries
import json
import re
import datetime as dt

#Local libraries
import config


#modified watson object
class Watson(watson.ConversationV1):

    def __init__(self):
        super().__init__(username=config.WATSON_USERNAME, password=config.WATSON_PASSWORD, version=config.WATSON_VERSION)



    def watson_message(self, query, context=None):

        response = self.message(
            workspace_id=config.WATSON_WORKPLACE_ID,
            input={'text': str(query)},
            context=context)
        return response


def validate(context):
    if 'piiConfirm' in context.keys() and 'autofillConfirm' in context.keys():
        if context['autofillConfirm'] == 'false':
            context = {**context, **config.EXAMPLE_USER}            #merge an example users data into current context
            context['autofillConfirm'] = 'true'
            return context

    current_node = context['system']['dialog_stack'][0]['dialog_node']
    if current_node in ['node_68_1519021622252', 'slot_82_1519023646210'] or 'dates' in context.keys():
        earliest_date = dt.datetime.strptime(str(context['dates'][0]), "%Y-%m-%d")
        todays_date = dt.datetime.today()
        years = str((todays_date - earliest_date).days/365)
        context['yearsTenure'] = years



    return context


def cache_context(context, session):

    pass

def log_response(response):
    pass

def update_form_DB(context):
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
