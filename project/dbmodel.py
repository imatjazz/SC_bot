# -*- coding: utf-8 -*-
"""
    DB Model
    ~~~~~~~~~~~~~~

    DB Models for the Flask SkillFinder app, using SQLAlchemy.
    Python 36
"""
###################### Imports and Init ####################
import sys
import os
from datetime import datetime
from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from project import config

# Parameters to be used by views.py
class MySQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        # pre_pool_ping
        # options.update({
        #     'pool_pre_ping': True
        # })
        super(MySQLAlchemy, self).apply_driver_hacks(app, info, options)

db = MySQLAlchemy()
app = Flask('dbmodel')

####################### Models ##############################
class User(db.Model):
    """A user with access to the web application.

    :param user_name: user's id
    :param user_pass: password
    :param registered_on: account creation timestamp

    """
    __tablename__ = 'users'
    __bind_key__ = 'users'

    user_name = db.Column('userName', db.String(50), primary_key=True)
    user_pass = db.Column('userPass', db.String(100))
    registered_on = db.Column('registereOn', db.DateTime(True))
    is_admin = db.Column('isAdmin', db.Boolean, default = False)

    def is_active(self):
        """ All users are active by default"""
        return True

    def get_id(self):
        """Return the unique username"""
        return self.user_name

    def is_authenticated(self):
        """Returns whether the user has already been authenticated"""
        return self.is_authenticated

    def is_anonymous(self):
        """Anonymous users are not supported"""
        return False

    pass


class CRM(db.Model):


    __tablename__ = "crm"
    __bind_key__ = 'users'

    employeeNumber = db.Column('employeeNumber', db.String(50), primary_key = True)
    title = db.Column('title', db.String(20))
    firstName = db.Column('firstName', db.String(100))
    middleNames = db.Column('middleNames', db.String(100))
    surname = db.Column('surname', db.String(100))
    previousNames = db.Column('previousNames', db.String(100))
    dateOfBirth = db.Column('dateOfBirth', db.String(10))
    gender = db.Column('gender', db.String(1))
    driversLicence = db.Column('driversLicence', db.Integer())
    contactNumber = db.Column('contactNumber', db.String(10))
    mobileNumber = db.Column('mobileNumber', db.String(10))
    email = db.Column('email', db.String(100))
    residentialAddress = db.Column('residentialAddress', db.String(200))
    residentialSuburb = db.Column('residentialSuburb', db.String(100))
    residentialState = db.Column('residentialState', db.String(100))
    residentialPostcode = db.Column('residentialPostcode', db.Integer())
    postalAddress = db.Column('postalAddress', db.String(100))
    postalSuburb = db.Column('postalSuburb', db.String(100))
    postalState = db.Column('postalState', db.String(100))
    postalPostcode = db.Column('postalPostcode', db.Integer())
    currJobTitle = db.Column('currJobTitle', db.String(100))
    currEmploymentType = db.Column('currEmploymentType', db.String(100))
    currEmployerStartDate = db.Column('currEmployerStartDate', db.String(10))
    currEmployer = db.Column('currEmployer', db.String(100), default = 'AMP')
    currEmployerAddress = db.Column('currEmployerAddress', db.String(100))
    currEmployerSuburb = db.Column('currEmployerSuburb', db.String(100), default = 'Sydney')
    currEmployerState = db.Column('currEmployerState', db.String(100), default = 'NSW')
    currEmployerPostcode = db.Column('currEmployerPostcode', db.Integer(), default = 2000)
    accountNumber = db.Column('accountNumber', db.Integer(), default = 58495743895)
    ampEmployeeFlag = db.Column('ampEmployeeFlag', db.Boolean(100), default = True)

    pass


class Form_DB(db.Model):
    """
    stores the identified variables from end user
    """

    __tablename__ = 'form'
    __bind_key__ = 'users'

    employeeNumber = db.Column('employeeNumber', db.String(50), primary_key = True)
    title = db.Column('title', db.String(20))
    firstName = db.Column('firstName', db.String(100))
    middleNames = db.Column('middleNames', db.String(100))
    surname = db.Column('surname', db.String(100))
    previousNames = db.Column('previousNames', db.String(100))
    dateOfBirth = db.Column('dateOfBirth', db.String(10))
    gender = db.Column('gender', db.String(1))
    driversLicence = db.Column('driversLicence', db.Integer())
    contactNumber = db.Column('contactNumber', db.String(10))
    mobileNumber = db.Column('mobileNumber', db.String(10))
    email = db.Column('email', db.String(100))
    residentialAddress = db.Column('residentialAddress', db.String(200))
    residentialSuburb = db.Column('residentialSuburb', db.String(100))
    residentialState = db.Column('residentialState', db.String(100))
    residentialPostcode = db.Column('residentialPostcode', db.Integer())
    postalAddress = db.Column('postalAddress', db.String(100))
    postalSuburb = db.Column('postalSuburb', db.String(100))
    postalState = db.Column('postalState', db.String(100))
    postalPostcode = db.Column('postalPostcode', db.Integer())
    currJobTitle = db.Column('currJobTitle', db.String(100))
    currEmploymentType = db.Column('currEmploymentType', db.String(100))
    currEmployerStartDate = db.Column('currEmployerStartDate', db.String(10))
    currEmployer = db.Column('currEmployer', db.String(100))
    currEmployerAddress = db.Column('currEmployerAddress', db.String(100))
    currEmployerSuburb = db.Column('currEmployerSuburb', db.String(100))
    currEmployerState = db.Column('currEmployerState', db.String(100))
    currEmployerPostcode = db.Column('currEmployerPostcode', db.Integer())
    accountNumber = db.Column('accountNumber', db.Integer())
    ampEmployeeFlag = db.Column('ampEmployeeFlag', db.Boolean(100))
    productType = db.Column('productType', db.Boolean(100))

    pass
