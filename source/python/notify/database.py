# !/usr/bin/python2
""" DATABASE """

__all__ = ['database']

# Import required python libraries
import os, sys
import sqlite3
from syslog.utils import sprint, eprint, str_to_bool

count = 0
folder = '/var/sqlite'
file = os.getenv('DB_FILE')
path = os.path.join(folder, file)
in_memory = str_to_bool(os.getenv('DB_MEMORY'))
if in_memory:
    database = ":memory:"
else:
    database = path
save_on_exit = str_to_bool(os.getenv('DB_SAVE'))

# Init database
if not os.path.exists(folder):
    os.makedirs(folder)
try:
    with sqlite3.connect(database) as sql:
        sql.execute("CREATE TABLE IF NOT EXISTS pushover(ip TEXT PRIMARY KEY, token TEXT, user TEXT, device TEXT,  url TEXT, url_title TEXT, priority INTEGER, retry INTEGER, expire INTEGER, callback_url TEXT, timestamp INTEGER, sound TEXT, html INTEGER);")
except:
    eprint ("can't create database", sys.exc_info()[0])
    raise

if in_memory:
    load(path)

def get_pushover(ip):
    with sqlite3.connect(database) as sql:
        sql.row_factory = sqlite3.Row
        cur = sql.cursor()
        cur.execute("SELECT * FROM pushover WHERE ip=?", (ip, ))
        row = cur.fetchone()
        return row

def load(src):
    if in_memory:
        try:
            with sqlite3.connect(database) as sql:
                sql.execute("ATTACH DATABASE ? AS source; INSERT OR FAIL INTO main.pushover SELECT * FROM source.pushover;", (src, ))
        except:
            eprint ("can't transfer database from source", sys.exc_info()[0])

def save():
    pass
