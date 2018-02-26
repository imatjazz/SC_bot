# -*- coding: utf-8 -*-
"""
    Log Model
    ~~~~~~~~~~~~~~

    Log Models for the Flask app, using SQLAlchemy.
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
class LogSQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        # pre_pool_ping
        # options.update({
        #     'pool_pre_ping': True
        # })
        super(LogSQLAlchemy, self).apply_driver_hacks(app, info, options)

log = LogSQLAlchemy()
app = Flask('logmodel')

####################### Models ##############################
class LogEntry(log.Model):
    """A user with access to the web application.

    :param user_name: user's id
    :param session_id: session id
    :param timestamp: account creation timestamp
    :param event_type: type of event (request, restart, return)
    :param context: content of the context
    :param dialog: content of the dialog
    :param state: state of UI elements buttons, tiles and breadcrumb

    """
    __tablename__ = 'log'
    __bind_key__ = 'log'

    log_id = log.Column('log_id', log.Integer, primary_key=True)
    timestamp = log.Column('timestamp', log.DateTime(True))
    user_name = log.Column('user_name', log.String(50))
    session_id = log.Column('session_id', log.String(100))
    event_type = log.Column('event_type', log.String(50))
    context = log.Column('context', log.TEXT)
    dialog = log.Column('dialog', log.TEXT)
    state = log.Column('state', log.TEXT)

    pass

