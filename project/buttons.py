###################### Button views ###########################################
### returns : buttons list, locked flag for chat input locking 
def purpose_1(context):
    bs = ['New home loan', 'Refinance']
    return bs, False
def type_of_borrower(context):
    bs = ['Individual account', 'Joint account', 'Company', 'Trust']
    return bs, True
def type_of_applicant(context):
    bs = ['Borrower', 'Guarantor', 'Sole director', 'Director']
    return bs, True
def marital_status(context):
    bs = ['Single', 'Married', 'Divorced', 'Widowed', 'De facto', 'Registered couple']
    return bs, False
def employment_type(context):
    bs = ['Part-time', 'Full-time', 'Casual', 'Contractor', 'Self-employed', 'Other']
    return bs, True
def personal_details_redirect(context):
    bs = []
    locked = False
    if 'borrowerType' not in context.keys():
        bs, locked = type_of_borrower(context)
    return bs, locked
##################### Buttons index ##########################################
BUTTONS_INDEX = {
    'root': purpose_1,
    'slot_90_1519083513311': type_of_borrower,
    'node_7_1519188615948': personal_details_redirect,
    'node_20_1519017279147': type_of_applicant,
    'node_6_1519866498803': employment_type,
    'slot_50_1519019902036': employment_type,
    'node_23_1519782186402': marital_status,
}
