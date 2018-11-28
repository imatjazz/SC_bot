# -*- coding: utf-8 -*-
"""
    Config
    ~~~~~~~~~~~~~~

    Flask app config.
"""
HOST = '127.0.0.1'
PORT = 9999
DEBUG = True

# FairValue Bot
WATSON_USERNAME= 'a3f43306-bc4a-4637-978d-2f442fc52395'
WATSON_PASSWORD= 'T6IyGv4zTZfG' 
WATSON_VERSION='2018-02-16'
WATSON_WORKPLACE_ID = 'cfe80d70-dd0b-48a7-a11d-21a67827bdca' 

# ASA Bot
# WATSON_USERNAME= 'a3f43306-bc4a-4637-978d-2f442fc52395'#'601885ca-73d2-4cfa-aefd-07d1c3f3401a'
# WATSON_PASSWORD= 'T6IyGv4zTZfG'#'DGm2hKYjVnV3'
# WATSON_VERSION='2018-02-16'
# WATSON_WORKPLACE_ID = 'ae8ddb74-7201-481a-ba2b-9698f58459bd' #'281b119d-0c8c-471b-885d-313507c967ae'

# WATSON_USERNAME= 'b2d05851-c9f9-424e-964f-343be7b48fd9'
# WATSON_PASSWORD= 'BoDxQM57T0OR'
# WATSON_VERSION='2018-02-16'
# WATSON_WORKPLACE_ID = 'ae8ddb74-7201-481a-ba2b-9698f58459bd' #'281b119d-0c8c-471b-885d-313507c967ae'

VALIDATEABLE_FIELDS = ['node_31_1519018934185', 'node_22_1519017849723', '[applicant_details_from_sys]', 'node_68_1519021622252', 'node_35_1519792742214', 'node_30_1519792519750']

#TODO finalise breadcrumb nodes
BREADCRUMBS = [
  {'name': 'Information', 'node_id': 'root',
    'sub': [
         {'name': 'INFORMATION', 'node_id': 'root'}
    ]
  }
]

FORM_FIELDS = [
                'employeeNumber',
                'title',
                'firstName',
                'middleNames',
                'surname',
                'previousNames',
                'dateOfBirth',
                'gender',
                'driversLicence',
                'contactNumber',
                'mobileNumber',
                'email',
                'residentialAddress',
                'residentialSuburb',
                'residentialState',
                'residentialPostcode',
                'postalAddress',
                'postalSuburb',
                'postalState',
                'postalPostcode',
                'currJobTitle',
                'currEmploymentType',
                'currEmploymentStartDate',
                'currEmployer',
                'currEmployerAddress',
                'currEmployerSuburb',
                'currEmployerState',
                'currEmployerPostcode',
                'accountNumber',
                'ampEmployeeFlag',
                'productType',
                'prevEmploymentType'
                ]


EXAMPLE_USER = {
               'firstName': 'Marlin',
               'lastName': 'Anemone',
               'employmentType': 'Full-time',
               'employmentTitle': 'Explorer',
               'firstName': 'John',
               'middleName': 'Bla bla',
               'lastName': 'Doe',
               'DOB': '02/05/1990',
               'currentAddress': '123 ABC Lane, Sydney',
               'employmentType': 'Part-time',
               'employmentTitle': 'Senior Analyst',
               'employmentStartDate': '02/2017',
               'yearsTenure': '2',
               'employer': 'Fish-finding services',
               'employerSubburb': 'Sydney',
               'employerState': 'NSW',
               'employerPostcode': '2000',
               'officeLocation': 'AMP Circular Quay',
               'driversLicence': '4581651651'
              }
EXAMPLE_CURRENT_EMPLOYMENT_HISTORY = {
                                     'employmentType': 'Part-time',
                                     'employmentTitle': 'Senior Analyst',
                                     'employmentStartDate': '02/2017',
                                     'yearsTenure': '1',
                                     'employer': 'Fish-finding services',
                                     'employerSubburb': 'Sydney',
                                     'employerState': 'NSW',
                                     'employerPostcode': '2000',
                                     'officeLocation': 'AMP Circular Quay'
                                     }
