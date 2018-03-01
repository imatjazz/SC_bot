###################### Button views ###########################################
def purpose_1(context):
    bs = ['New home loan', 'Refinance']
    return bs
def type_of_borrower(context):
    bs = ['Individual account', 'Joint account', 'Company', 'Trust']
    return bs
def type_of_applicant(context):
    bs = ['Borrower', 'Guarantor', 'Sole director', 'Director']
    return bs
def marital_status(context):
    bs = ['Single', 'Married', 'Divorced', 'Widowed', 'De facto', 'Registered couple']
    return bs
def employment_type(context):
    bs = ['Part-time', 'Full-time', 'Casual', 'Contractor', 'Self-employed', 'Other']
    return bs
def personal_details_redirect(context):
    bs = []
    if 'borrowerType' not in context.keys():
        bs = type_of_borrower(context)
    return bs
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
