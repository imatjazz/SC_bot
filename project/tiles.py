###################### Tile views ###########################################
def applicant_details_from_sys(context):
    productType = context['productType']
    employment = context['prevEmploymentType'] if 'prevEmploymentType' in context.keys() else None
    if employment is not None:
        # template = 'tiles/applicant_employment_details_full.html'
        # args = {'employmentTypePrevious': context['employmentTypePrevious'], 'businessDescription': context['businessDescription']}
        # title = 'Please validate your employment history'
        template = 'tiles/validation_table.html'
        title = 'Please validate your employment history'
        args = [
            {'field': 'prevEmploymentType', 'name': 'Previous job type','value': context['prevEmploymentType']},
            {'field': 'prevEmploymentBusinessDescription', 'name': 'Previous employer/industry of business','value': context['prevEmploymentBusinessDescription']},
            {'field': 'prevEmploymentDateStart', 'name': 'Previous employment start','value': context['prevEmploymentDateStart']},
            {'field': 'prevEmploymentDateEnd', 'name': 'Previous employment end','value': context['prevEmploymentDateEnd']},
        ]
    else: 
        template = 'tiles/validation_table.html'
        title = 'Please validate your details'
        args = [
            {'field': 'firstName', 'name': 'First name','value': context['firstName']},
            {'field': 'middleName', 'name': 'Middle name(s)','value': context['middleName']},
            {'field': 'lastName', 'name': 'Last name','value': context['lastName']},
            {'field': 'dateOfBirth', 'name': 'Date of birth','value': context['dateOfBirth']},
            {'field': 'currAddress', 'name': 'Address','value': context['currAddress']},
            {'field': 'currJobTitle', 'name': 'Job title','value': context['currJobTitle']},
            {'field': 'currEmploymentType', 'name': 'Job type','value': context['currEmploymentType']},
            {'field': 'currEmploymentStartDate', 'name': 'Start date (YYYY-MM-DD)','value': context['currEmploymentStartDate']},
            {'field': 'currEmployer', 'name': 'Employer name','value': context['currEmployer']},
            {'field': 'currEmployerSuburb', 'name': 'Employer suburb','value': context["currEmployerSuburb"]},
            {'field': 'currEmployerState', 'name': 'Employer state','value': context['currEmployerState']},
            {'field': 'currEmployerPostcode', 'name': 'Employer postcode','value': context['currEmployerPostcode']},
            {'field': 'accountNumber', 'name': 'AMP account number','value': context['currEmployerSuburb']},
        ]
    return [title, template, args]

def applicant_employment_details_from_sys(context):
    template = 'tiles/applicant_employment_details_from_sys.html'
    title = 'Your employment history'
    args = [{}]
    return [title, template, args]

## Breadcrumb validation tiles
def breadcrumb_personal_validation(context):
    template = 'tiles/validation_table.html'
    title = 'Personal details'
    args = [
        {'field': 'firstName', 'name': 'First name','value': context['firstName']},
        {'field': 'middleName', 'name': 'Middle name(s)','value': context['middleName']},
        {'field': 'lastName', 'name': 'Last name','value': context['lastName']},
        {'field': 'dateOfBirth', 'name': 'Date of birth','value': context['dateOfBirth']},
        {'field': 'currAddress', 'name': 'Address','value': context['currAddress']},
        {'field': 'currJobTitle', 'name': 'Job title','value': context['currJobTitle']},
        {'field': 'currEmploymentType', 'name': 'Job type','value': context['currEmploymentType']},
        {'field': 'currEmploymentStartDate', 'name': 'Start date (YYYY-MM-DD)','value': context['currEmploymentStartDate']},
        {'field': 'currEmployer', 'name': 'Employer name','value': context['currEmployer']},
        {'field': 'currEmployerSuburb', 'name': 'Employer suburb','value': context["currEmployerSuburb"]},
        {'field': 'currEmployerState', 'name': 'Employer state','value': context['currEmployerState']},
        {'field': 'currEmployerPostcode', 'name': 'Employer postcode','value': context['currEmployerPostcode']},
        {'field': 'accountNumber', 'name': 'AMP account number','value': context['currEmployerSuburb']},
        {'field': 'prevEmploymentType', 'name': 'Job type','value': context['prevEmploymentType']},
        {'field': 'prevEmploymentBusinessDescription', 'name': 'Previous employer/industry of business','value': context['prevEmploymentBusinessDescription']},
        {'field': 'prevEmploymentDateStart', 'name': 'Previous employment start','value': context['prevEmploymentDateStart']},
        {'field': 'prevEmploymentDateEnd', 'name': 'Previous employment end','value': context['prevEmploymentDateEnd']},
    ]
    return [title, template, args]

###################### Tile index
TILES_INDEX = {
    'node_68_1519021622252': [applicant_details_from_sys],
    'slot_50_1519019902036': [applicant_employment_details_from_sys],
    'breadcrumb_Personal': [breadcrumb_personal_validation]
}
