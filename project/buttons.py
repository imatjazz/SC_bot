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
    bs = ['Part-time', 'Full-time', 'Casual', 'Contractor', 'Self-employed']
    return bs, True
def personal_details_redirect(context):
    bs = []
    locked = False
    if 'borrowerType' not in context.keys():
        bs, locked = type_of_borrower(context)
    return bs, locked
def calendar_one(context):
	bs = ['I moved in on: <div id="calendar_one" class="input-group date datepicker"><input type="text" class="form-control"><span class="input-group-addon"><i class="glyphicon glyphicon-th"></i></span><button class="chat-button-submit btn btn-default"><i class="fa fa-paper-plane"></i></button></div>']
	return bs, True
def loan_purpose(context):
    bs = ['Purchase', 'Refinance', 'Increase']
    return bs, False
def primary_purpose(context):
    bs = ['Owner Occupied', 'Investment']
    return bs, False
def product_type(context):
    bs = ['AMP First', 'Other']
    return bs, False
def interest_type(context):
    bs = ['Fixed', 'Variable']
    return bs, False
def repayment_type(context):
    bs = ['Principal & Interest', 'Interest Only']
    return bs, False


##################### Buttons index ##########################################
BUTTONS_INDEX = {
    'root': purpose_1,
    'slot_23_1519017868184': purpose_1,
    'slot_90_1519083513311': type_of_borrower,
    'node_7_1519188615948': personal_details_redirect,
    'node_20_1519017279147': type_of_applicant,
    'node_6_1519866498803': employment_type,
    'slot_50_1519019902036': employment_type,
    'node_23_1519782186402': marital_status,
    'node_79_1519796324896': calendar_one,
    'node_11_1519775732721': calendar_one,
    'node_1_1520204741645': loan_purpose,
    'slot_3_1520205669786': loan_purpose,
    'slot_7_1520205884325': loan_purpose,
    'node_14_1519789207619': primary_purpose,
    'node_23_1519790232269': product_type,
    'slot_19_1520225026182': product_type,
    'node_18_1520224926068': interest_type,
    'slot_28_1520225452278': interest_type,
    'node_26_1520225384213': repayment_type,
    'slot_39_1520225912958': repayment_type,
}
