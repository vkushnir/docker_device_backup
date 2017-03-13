#!/usr/bin/python2
""" BACKUP MAIN """

__all__ = ['syslog',
           'ValueError', 'DeviceError', 'DiffError', 'FileError', 'ConfigError',
           'PushoverError']

# Import required python libraries
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

# Exceptions
class ValueError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class DeviceError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class DiffError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class FileError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class ConfigError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class PushoverError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
