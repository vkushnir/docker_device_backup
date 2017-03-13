#!/usr/bin/python2
""" BACKUP MAIN """

__all__ = ['backup']

# Import required python libraries
import os, sys
import sqlite3
import config, database, server
from threads import BackupThread
from syslog.utils import eprint, sprint
from syslog import classes

class backup(classes.syslog):
    def __init__(self):
        sprint('Create BACKUP instance')
        self.thread = BackupThread()

    def init(self, msg):
        sprint('Initialise BACKUP instance', msg)
        if not os.path.exists('/usr/local/share/snmp/mibs'):
            os.mkdir('/usr/local/share/snmp/mibs')
        if not os.path.exists('/usr/local/share/snmp/pymibs'):
            os.mkdir('/usr/local/share/snmp/pymibs')
        database.clear_locks()
        return True

    def deinit(self):
        sprint('DeInitialise BACKUP instance')
        database.clear_locks()
        if database.save_on_exit:
            database.save
        return True

    def send(self, msg):
        #sprint('Send message to BACKUP instance', msg['SOURCEIP'])
        self.thread.run(msg)
        return True
