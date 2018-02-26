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

#TODO finalise breadcrumb nodes
BREADCRUMBS = [
  {'name': 'Personal', 'node_id': 'root', 
    'sub': [
         {'name': 'Personal details', 'node_id': 'root'}, 
         {'name': 'Addresses', 'node_id': 'node_68_1519021622252'}, 
         {'name': 'Employment', 'node_id': 'slot_50_1519019902036'}
    ]
  },
  {'name': 'Financials', 'node_id': 'null', 
    'sub': [
      {'name': 'Assets', 'node_id': 'null'},
      {'name': 'Liabilities', 'node_id': 'null'},
      {'name': 'Expenses', 'node_id': 'null'},
      {'name': 'Funds position', 'node_id': 'null'}
    ]
  },
  {'name': 'Loan requirements', 'node_id': 'null', 
    'sub': [
      {'name': 'Purpose', 'node_id': 'null'},
      {'name': 'Loan structure', 'node_id': 'null'},
      {'name': 'Offset', 'node_id': 'null'},
      {'name': 'Master Limit', 'node_id': 'null'},
      {'name': 'LMI', 'node_id': 'null'},
      {'name': 'SRG', 'node_id': 'null'}
    ]
  },
  {'name': 'Additional', 'node_id': 'null', 
    'sub': [
      {'name': 'Security', 'node_id': 'null'},
      {'name': 'Solicitor', 'node_id': 'null'},
      {'name': 'Source of wealth', 'node_id': 'null'},
      {'name': 'Communications', 'node_id': 'null'}
    ]
  },
  {'name': 'Privacy', 'node_id': 'null', 
    'sub': [
      {'name': 'Loan requirements', 'node_id': 'null'},
      {'name': 'Identification', 'node_id': 'null'},
      {'name': 'Tax', 'node_id': 'null'},
      {'name': 'Fee payments', 'node_id': 'null'},
      {'name': 'Privacy statement', 'node_id': 'null'},
      {'name': 'Declaration', 'node_id': 'null'}
    ]
  },
  {'name': 'Documents', 'node_id': 'null', 
    'sub': [
      {'name': 'Identification', 'node_id': 'null'},
      {'name': 'Income', 'node_id': 'null'},
      {'name': 'Property', 'node_id': 'null'}
    ]
  }
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
