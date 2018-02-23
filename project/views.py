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
from datetime import datetime
from flask import Flask, request, render_template, session, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
from flask_session import Session

#Path
sys.path.append('project')

#local imports
from project import config
from .dbmodel import *
from project import api, buttons, tiles



#######################
#Major HACK HACK HACK
Me = api.Watson()
#Major HACK HACK HACK
#######################


############################### Init ################################
def create_app(debug = False):

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
    #Initialise flask session
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    #initialise API to Watson


    ##### Initialize db from dbmodel ###
    db.init_app(app)

    ########### Login Manager ##########
    # Set Up Login Management for the application
    login_manager = LoginManager()
    # Configure the application for login
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = 'You must be logged in to view this page. Please Log In'

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
        #Breadcrumb
        #TODO get this from DB or config
        breadcrumbs = ['Personal & employment', 'Financials', 'Loan requirements', 'Offset accounts', 'Additional information', 'Privacy', 'Documents'];
        #TODO get this from session
        breadcrumb_current = 1; #this is 1 indexed, not 0 indexed!

        #Existing messages
        #TODO change to session
        messages = []

        #TODO Reload session context
        session['context'] = None

        #Current tiles
        #TODO change to session
        tiles = []
        return render_template('start.html', breadcrumbs = breadcrumbs, breadcrumb_current = breadcrumb_current, messages = messages, tiles = tiles)

    @app.route('/message', methods=['POST'])
    @login_required
    def message():
        '''
        Exchange messages with the front end.
        '''
        message_received = request.form.get('message')
        if message_received is None:
            message_received = ''

        context = api.retrive_cached_context(session)                           #now behind a try except wrapper
        response = Me.watson_message(query=message_received,
                                     context=context)

        new_context = response['context']
        current_node = new_context['system']['dialog_stack'][0]['dialog_node']

        if current_node in config.VALIDATEABLE_FIELDS:                          #validate now performs preppulation. TODO may need to run a DB query though
            new_context = api.validate(new_context)
            if new_context is None:
                raise TypeError('Context was set to None in validate function')

        session['context'] = new_context
        api.log_response(response)
        api.update_form_DB(new_context)
        ts = tile_generation(new_context)
        bs = button_generation(new_context)
        message_send = response['output']['text']

        breadcrumb_current = 1
        return json.dumps({'message': message_send,
                           'tiles': ts,
                           'buttons': bs,
                           'breadcrumb_current': breadcrumb_current})

    ###################### Buttons ########################################
    def button_generation(context):
        '''
        Check if buttons are available for current node and generate list
        '''

        current_node = context['system']['dialog_stack'][0]['dialog_node']
        if current_node not in buttons.BUTTONS_INDEX.keys():
            return []

        button_path = buttons.BUTTONS_INDEX[current_node]
        bs = button_path(context)
        return bs

    ###################### Tile ###########################################
    def tile_generation(context):
        '''
        Check if tiles are available for current node and generate html
        '''
        current_node = context['system']['dialog_stack'][0]['dialog_node']
        print(json.dumps(context, indent=2))
        if current_node not in tiles.TILES_INDEX.keys():
            return []

        tile_paths = tiles.TILES_INDEX[current_node]
        ts = []
        for path in tile_paths:
           res = path(context)
           template = render_template(res[1], args = res[2])
           tile = {'title': res[0], 'body': template}
           ts.append(tile)
        return ts


    ###################### Registration helper ##################################
    @app.route('/register/<uname>/<upass>')
    @login_required
    def register(uname = 'csuder1', upass= 'password'):
        """
        Register a user in the DB with a username and password
        """
        # Registering KPMG employees
        user_add = User(user_name = uname, user_pass = generate_password_hash(upass), registered_on = datetime.utcnow())

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
