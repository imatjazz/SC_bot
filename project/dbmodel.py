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

    userName = db.Column('userName', db.String(50), primary_key = True)
    firstName = db.Column('firstName', db.String(100))
    middleName = db.Column('middleName', db.String(100))
    lastName = db.Column('lastName', db.String(100))
    dateOfBirth = db.Column('dateOfBirth', db.String(100))
    currAddress = db.Column('currAddress', db.String(200))
    currJobTitle = db.Column('currJobTitle', db.String(100))
    currEmploymentType = db.Column('currEmploymentType', db.String(100))
    currEmploymentStartDate = db.Column('currEmploymentStartDate', db.String(100))
    currEmployer = db.Column('currEmployer', db.String(100), default = 'AMP')
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

    userName = db.Column('userName', db.String(50), primary_key = True)
    firstName = db.Column('firstName', db.String(100))
    middleName = db.Column('middleName', db.String(100))
    lastName = db.Column('lastName', db.String(100))
    dateOfBirth = db.Column('dateOfBirth', db.String(100))
    currAddress = db.Column('currAddress', db.String(200))
    currJobTitle = db.Column('currJobTitle', db.String(100))
    currEmploymentType = db.Column('currEmploymentType', db.String(100))
    currEmploymentStartDate = db.Column('currEmploymentStartDate', db.String(100))
    currEmployer = db.Column('currEmployer', db.String(100), default = 'AMP')
    currEmployerSuburb = db.Column('currEmployerSuburb', db.String(100), default = 'Sydney')
    currEmployerState = db.Column('currEmployerState', db.String(100), default = 'NSW')
    currEmployerPostcode = db.Column('currEmployerPostcode', db.Integer(), default = 2000)
    accountNumber = db.Column('accountNumber', db.Integer(), default = 58495743895)
    ampEmployeeFlag = db.Column('ampEmployeeFlag', db.Boolean(100), default = True)

    pass
