import watson_developer_cloud as watson
import json

import config


class Watson(watson.ConversationV1):

    def __init__(self):
        super().__init__(username=config.WATSON_USERNAME, password=config.WATSON_PASSWORD, version=config.WATSON_VERSION)



    def watson_message(self, query, context=None):

        response = self.message(
            workspace_id=config.WATSON_WORKPLACE_ID,
            input={'text': str(query)},
            context=context)
        return response



def validate(node_id, value=None):
    return True

def cache_context(context, session):

    pass

def log_response(response):
    pass

def update_form_DB(context):
    pass
