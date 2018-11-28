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

# ASA bot 
def assurance_type(context):
    bs = ['Reasonable', 'Limited']
    return bs, True

def yes_or_no(context):
    bs = ['Yes', 'No']
    return bs, True

def yes_or_no_otheronly(context):
    bs = ['Yes, its a combination', 'No, other info only']
    return bs, True

def assurance_type_moreInfo(context):
    bs = ['Reasonable', 'Limited', 'More Information']
    return bs, False

def end_conversation(context):
    bs = ['Yes, I have more question', 'No, thats all.']
    return bs, False

##################### Buttons index ##########################################
BUTTONS_INDEX = {
    #'node_5_1520314268627': assurance_type_moreInfo,
    'node_8_1520395975530': yes_or_no,
    'node_9_1520396160695': yes_or_no,
    'node_1_1520384004385':yes_or_no_otheronly,
    'node_1_1521069602168':assurance_type

}
