#!/usr/bin/python2
""" NOTIFY MAIN """

__all__ = ['notify']

# Import required python libraries
import os, sys
import database, pushover
from syslog.utils import eprint, sprint
from syslog import classes

class notify(classes.syslog):
    def __init__(self):
        sprint('Create NOTIFY instance')

    def init(self, msg):
        sprint('Initialise BACKUP instance', msg)
        return True

    def deinit(self):
        sprint('DeInitialise NOTIFY instance')
        if database.save_on_exit:
            database.save
        return True

    def send(self, msg):
        pushover.send(msg)
        return True
