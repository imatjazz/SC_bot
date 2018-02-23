###################### Tile views ###########################################
def applicant_details_from_sys(context):
    productType = context['productType']
    employmentTypePrevious = context['employmentTypePrevious'] if 'employmentTypePrevious' in context.keys() else None
    if employmentTypePrevious is not None:
        template = 'tiles/applicant_employment_details_full.html'
        args = {'employmentTypePrevious': context['employmentTypePrevious'], 'businessDescription': context['businessDescription']}
        title = 'Please validate your employment history'
    else: 
        template = 'tiles/applicant_details_from_sys.html'
        title = 'Please validate your details'
        args = {}
    return [title, template, args]

def applicant_employment_details_from_sys(context):
    template = 'tiles/applicant_employment_details_from_sys.html'
    title = 'Your employment history'
    args = {}
    return [title, template, args]

###################### Tile index
TILES_INDEX = {
    'node_68_1519021622252': [applicant_details_from_sys],
    'slot_50_1519019902036': [applicant_employment_details_from_sys]
}
