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

VALIDATEABLE_FIELDS = ['driversLicence']

EXAMPLE_USER = {
               'firstName': 'John',
               'middleName': 'Bla bla',
               'lastName': 'Doe',
               'DOB': '02/05/1990',
               'address': '123 ABC Lane, Sydney',
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
