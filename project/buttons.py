###################### Button views ###########################################
def purpose_1(context):
    bs = ['New home loan', 'Refinance']
    return bs
def type_of_borrower(context):
    bs = ['Individual applicant', 'Joint applicants', 'Company', 'Trust'] 
    return bs

##################### Buttons index ##########################################
BUTTONS_INDEX = {
    'root': purpose_1,
    'node_15_1519016713312': type_of_borrower
}	