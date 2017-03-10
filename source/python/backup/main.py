#!/usr/bin/python2
""" BACKUP MAIN """

__all__ = ['backup']

# Import required python libraries
import os, sys
import sqlite3
import config
import database
import server
from threads import BackupThread
from utils import eprint, sprint

class syslog(object):

    def open(self):
        """Open a connection to the target service"""
        return True

    def close(self):
        """Close the connection to the target service"""
        pass

    def is_opened(self):
        """Check if the connection to the target is able to receive messages"""
        return True

    def init(self):
        """This method is called at initialization time"""
        return True

    def deinit(self):
        """This method is called at deinitialization time"""
        pass

    def send(self, msg):
        """Send a message to the target service

        It should return True to indicate success, False will suspend the
        destination for a period specified by the time-reopen() option."""
        pass

class backup(syslog):
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
