# -*- coding: utf-8 -*-
"""
    Config
    ~~~~~~~~~~~~~~

    Flask app config.
"""
HOST = '127.0.0.1'
PORT = 8080
DEBUG = True
WATSON_USERNAME='601885ca-73d2-4cfa-aefd-07d1c3f3401a'
WATSON_PASSWORD='DGm2hKYjVnV3'
WATSON_VERSION='2018-02-16'
WATSON_WORKPLACE_ID = '281b119d-0c8c-471b-885d-313507c967ae'

VALIDATEABLE_FIELDS = ['node_68_1519021622252']
BREADCRUMBS = [
  {'name': 'Personal & employment', 'sub': ['Personal details', 'Employment history', 'Family situation']},
  {'name': 'Financials', 'sub': ['Loan purpose', 'Loan structure', 'Loan financing']},
  {'name': 'Offset accounts', 'sub':['Loan purpose', 'Loan structure', 'Loan financing']},
  {'name': 'Additional information', 'sub':['Loan purpose', 'Loan structure', 'Loan financing']},
  {'name': 'Privacy', 'sub': []},
  {'name': 'Documents', 'sub': []}
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
                'currEmployerStartDate',
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
