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
from .logmodel import *

#package improts
import api
import buttons
import tiles

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

    #imported loop controls for a feature in development, not used at the moment - delete if not needed.
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    # Set DSN to link to SQL Server
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_BINDS'] = {
        'users':    'sqlite:///database.db',
        'log':      'sqlite:///log.db'
    }
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 7200
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #Initialise flask session
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    ##### Initialize db from dbmodel ###
    db.init_app(app)
    log.init_app(app)

    ########### Login Manager ##########
    # Set Up Login Management for the application
    login_manager = LoginManager()
    # Configure the application for login
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = 'You must be logged in to view this page. Please Log In'

    ###########################################################
    # Views
    ###########################################################
    @app.route('/')
    @app.route('/start')
    @app.route('/start/<nosession>')
    @login_required
    def start(nosession=False):
        '''
        Show start page.
        '''
        if 'uid' not in session:
            session['uid'] = str(uuid.uuid4())
        if nosession:
            session['context'] = None
            if 'dialog' in session: session.pop('dialog')
            if 'state' in session: session.pop('state')
            session['uid'] = str(uuid.uuid4())

        #Log restart to audit log
        LogEntry(user_name = current_user.user_name, event_type = 'start loaded').save()

        #Get data from session
        #Existing messages
        messages = session['dialog'] if 'dialog' in session else []

        #Breadcrumb
        breadcrumb_current = session['state']['breadcrumb'] if 'state' in session else [1, 1] #this is 1 indexed, not 0 indexed!
        
        #Current tiles & buttons
        tiles = session['state']['tiles'] if 'state' in session else []
        buttons = session['state']['buttons']  if 'state' in session else []

        return render_template('start.html', breadcrumbs = config.BREADCRUMBS, breadcrumb_current = breadcrumb_current, messages = messages, tiles = tiles, buttons = buttons)

    @app.route('/message', methods=['POST'])
    @login_required
    def message():
        '''
        Exchange messages with the front end.
        '''
        if 'uid' not in session:
            session['uid'] = str(uuid.uuid4())
        message_received = request.form.get('message')
        if message_received is None:
            message_received = ''
        #Save for session restoration
        if 'dialog' not in session:
            session['dialog'] = []
        session['dialog'].append({'who': 'human', 'message': message_received})
        #Log to audit log
        LogEntry(user_name = current_user.user_name, event_type = 'received message').save()

        #Send current user text + old context to Watson
        context = session['context'] if 'context' in session else None
        response = Me.watson_message(query=message_received,
                                     context=context)

        #Get new context + current node
        new_context = response['context']
        print(json.dumps(new_context, indent=2))
        current_node = new_context['system']['dialog_stack'][0]['dialog_node']

        #Validate data if current node validateable
        if current_node in config.VALIDATEABLE_FIELDS:      #TODO could validate based on context variable name
            api.validate(current_node)       #TODO

        #Data from DB
        if 'piiConfirm' in new_context.keys() and 'autofillConfirm' in new_context.keys():
            if new_context['autofillConfirm'] == 'false':
                new_context = {**new_context, **config.EXAMPLE_USER}            #merge an example users data into current context
                new_context['autofillConfirm'] = 'true'

        session['context'] = new_context
        api.update_form_DB(new_context)

        #Generate UI bits (tiles, buttons, breadcrumb, message)
        ts = tile_generation(new_context)
        bs = button_generation(new_context)
        breadcrumb_current = [3, 2]
        message_send = response['output']['text']
        
        #Save data for session restoration
        if 'state' not in session:
            session['state'] = {'buttons': [], 'tiles': [], 'breadcrumb': [1, 1]}
        session['state']['buttons'] = bs
        session['state']['tiles'] = ts
        session['state']['breadcrumb'] = breadcrumb_current
        for m in message_send:
            session['dialog'].append({'who': 'bot', 'message': m})
        #Log to audit log
        LogEntry(user_name = current_user.user_name, event_type = 'response sent').save()
        
        return json.dumps({'message': message_send, 'tiles': ts, 'buttons': bs, 'breadcrumb_current': breadcrumb_current})

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

    ############################################################################################
    ###################### User authentication and management ##################################
    ############################################################################################
    @login_manager.user_loader
    def user_loader(user_name):
        """Given user_name - unique user identifier - return User Object"""
        return User.query.get(user_name)

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

                    session['uid'] = str(uuid.uuid4())


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

        log.create_all(bind='log')
        log.session.commit()
        return json.dumps({"status": "Success"})

    return app
