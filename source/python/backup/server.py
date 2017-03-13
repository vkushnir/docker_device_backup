# !/usr/bin/python2
""" SERVER """

__all__ = ['server']

# Import required python libraries
import os, sys
from subprocess import Popen, PIPE
from syslog.utils import sprint, eprint, str_to_bool

class server(object):
    def __init__(self, srv_type):
        self.srv_type = srv_type.upper()
        self.addr = os.getenv('SRV_' + self.srv_type + "_ADDR")
        self.folder = os.getenv('SRV_' + self.srv_type + "_PATH")
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)

    def get_path(self, srv_file):
        return os.path.join(self.folder, srv_file)

max_threads = int(os.getenv('SRV_THREADS'))
sleep = int(os.getenv('SRV_SLEEP'))
max_hits = int(os.getenv('SRV_HITS'))
save_timeout = int(os.getenv('SRV_SAVE_TIMEOUT'))
tftp = server('TFTP')
ftp = server('FTP')
