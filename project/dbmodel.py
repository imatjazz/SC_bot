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

    user_name = db.Column('user_name', db.String(50), primary_key=True)
    user_pass = db.Column('user_pass', db.String(100))
    registered_on = db.Column('registered_on', db.DateTime(True))
    is_admin = db.Column('is_admin', db.Boolean, default = False)

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

