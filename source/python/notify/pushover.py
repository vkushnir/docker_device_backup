# !/usr/bin/python2
""" PUSHOVER """

import os, copy
import database
from pushover_complete import PushoverAPI
from syslog.utils import sprint, eprint, str_to_bool
from syslog.classes import PushoverError
from backup.config import get_l0ip

def send(msg, title=None, message=None):
    params = update_defaults(msg['SOURCEIP'])
    if title is None:
        params['title'] = get_l0ip(msg['SOURCEIP'])
    else:
        params['title'] = title
    if message is None
        params['message'] = msg['MESSAGE']
    else:
        params['message'] = message
    params['timestamp'] = int(msg['R_UNIXTIME'])
    pushover.send_message(**params)

def update_defaults(ip):
    result = copy.deepcopy(defaults)
    new = database.get_pushover(ip)
    if new is not None:
        for key, value in new.iteritems():
            if key is not None:
                result[key] = value
    return result

pushover = PushoverAPI(os.getenv('PUSHOVER_TOKEN'))
defaults = dict()

if os.getenv('PUSHOVER_USER') != '':
    defaults['user'] = os.getenv('PUSHOVER_USER')
if os.getenv('PUSHOVER_DEVICE') != '':
    defaults['device'] = os.getenv('PUSHOVER_DEVICE')
if os.getenv('PUSHOVER_SOUND') != '':
    defaults['sound'] = os.getenv('PUSHOVER_SOUND')
if  os.getenv('PUSHOVER_PRIORITY') != '':
    defaults['priority'] = int(os.getenv('PUSHOVER_PRIORITY'))
