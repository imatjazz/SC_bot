# -*- coding: utf-8 -*-
"""
Views
~~~~~~~~~~~~~~

Views for the Flask app.
Python 36
"""
###################### Imports ####################
import sys
import os, inspect, uuid, json
from datetime import datetime, timedelta
from flask import Flask, request, render_template, session, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime

from werkzeug.utils import secure_filename
from jinja2 import Environment
import urllib.request
import requests
import requests_cache
from sqlalchemy import text
from sqlalchemy import types
import random
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
#from smtplib import smtp
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#from email.mime.base import MIMEBa
import smtplib
#from email import encoders
from wtforms import SubmitField
#import FlaskForm

# CV Extraction Imp
import logging
import pandas as pd
import numpy as np
import string
import urllib
from tika import parser
import nltk
import re
import csv
import codecs
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import urllib.parse as parse
import urllib.request
from shutil import copyfile

#testv##
from sqlalchemy import or_
from sqlalchemy.engine import  RowProxy
from sqlalchemy.orm import aliased
from sqlalchemy import desc

#Path
sys.path.append('project/src')
sys.path.append('project')

#local imports
from project import config
from dbmodel import *


############################### Init ################################
def create_app(debug = False):

    requests_cache.install_cache()

    # Create the Flask app
    app = Flask(__name__)
    app.secret_key = "A57B93E359fjgj564D1B83A"

    app.debug = debug

    #Path
    DIR_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(
        inspect.currentframe())))
    STATIC_ROOT = DIR_ROOT + '/static/'

    #App config
    #app.config['UPLOADS'] = STATIC_ROOT + 'uploads'

    #imported loop controls for a feature in development, not used at the moment - delete if not needed.
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    # Set DSN to link to SQL Server
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 7200
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    ##### Initialize db from dbmodel ###
    db.init_app(app)

    ########### Login Manager ##########
    # Set Up Login Management for the application
    login_manager = LoginManager()
    # Configure the application for login
    login_manager.init_app(app)
    # Set the login view
    login_manager.login_view = 'login'
    # Set custom log-in message
    login_manager.login_message = 'You must be logged in to view this page. Please Log In'
    # Keep track of logged in user
    user_logged_in = ''

    @login_manager.user_loader
    def user_loader(user_name):
        """Given user_name - unique user identifier - return User Object"""
        return User.query.get(user_name)

    ###########################################################
    # Views
    ###########################################################
    @app.route('/')
    @app.route('/start')
    @login_required
    def start():
        '''
        Show start page.
        '''
        return 'Success!'

    ###################### Registration helper ##################################
    @app.route('/register')
    def register():
        """
        Register a user in the DB with a username and password
        """
        # Registering KPMG employees
        user_add = User(user_name = 'csuder1', user_pass = generate_password_hash('password'), registered_on = datetime.utcnow(), is_admin = 1)

        # Adding to the database
        db.session.add(user_add)
        db.session.commit()

        print('User successfully registered')


        # Returning to 'start' page after registering the users
        return redirect(url_for('start'))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        """
        On POST try to authenticate the user, on GET show the login page
        """
        if request.method == 'POST':
            uname = request.form['user_name']
            upass = request.form['user_pass']


            # Authenticate User
            user = User.query.get(uname)

            # Check if User exists
            if user:

                # Checking if the password is correct
                if check_password_hash(user.user_pass, upass):
                    user_logged_in = user.user_name
                    user.authenticated = True

                    # Add user to session
                    db.session.add(user)
                    db.session.commit()
                    login_user(user, remember=True)

                    next = request.args.get('next')
                    # Login successful - go to start page or next page
                    return redirect(next or url_for('start'))
                else:
                    # Login failed - return to login page with error message
                    return render_template(
                        'login.html',
                        error="Invalid password. Please try again.")
            else:
                # Login failed - return to login page with error message
                return render_template(
                    'login.html',
                    error="You are not registered in the system. Please Register before logging in.")
        # GET Request - show login page
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        """
        Logout the user and redirect to login
        """
        logout_user()
        return redirect(url_for('login'))

    @app.route('/updateDBModel')
    #@login_required
    def updateDBModel():
        '''
        Create all tables.
        '''
        db.create_all()
        db.session.commit()
        return json.dumps({"status": "Success"})

    return app
