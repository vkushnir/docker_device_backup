# !/usr/bin/python2
""" DATABASE """

__all__ = ['database']

# Import required python libraries
import os, sys
import sqlite3
from utils import sprint, eprint, str_to_bool

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
        sql.execute("CREATE TABLE IF NOT EXISTS queue(ip TEXT PRIMARY KEY, lock BOOL DEFAULT 0, hits INTEGER DEFAULT 0, date DATETIME);")
        sql.execute("CREATE TABLE IF NOT EXISTS auth(ip TEXT PRIMARY KEY, snmp_version TEXT, snmp_community TEXT, snmp_aprot TEXT, snmp_apass TEXT, snmp_seng_id TEXT, snmp_ceng_id TEXT, snmp_level TEXT, snmp_context TEXT, snmp_user TEXT, snmp_pprot TEXT, snmp_ppass TEXT, snmp_boots TEXT);")
        sql.execute("CREATE TABLE IF NOT EXISTS servers(ip TEXT PRIMARY KEY, type TEXT, addr TEXT, path TEXT)")
        sql.execute("CREATE TABLE IF NOT EXISTS vendors(ip TEXT PRIMARY KEY, sysObjectID TEXT, app TEXT, model TEXT, vendor TEXT, hits INTEGER, last DATETIME);")
except:
    eprint ("can't create database", sys.exc_info()[0])
    raise

if in_memory:
    load(path)

def clear_locks():
    with sqlite3.connect(database) as sql:
        sql.execute("UPDATE queue SET lock=0")

def lock(ip):
    try:
        with sqlite3.connect(database) as sql:
            sql.execute("INSERT INTO queue(ip, lock) values(?, 1)", (ip, ))
        return True
    except:
        with sqlite3.connect(database) as sql:
            sql.execute("UPDATE queue SET lock=1, hits=hits+1 WHERE ip=?", (ip, ))
        eprint("device '"+ip+"' already in list")
        return False

def release(ip):
    with sqlite3.connect(database) as sql:
        sql.execute("UPDATE OR IGNORE queue SET lock=0, hits=0 WHERE ip=?", (ip, ))

def clear(ip):
    with sqlite3.connect(database) as sql:
        sql.execute("DELETE FROM queue WHERE ip=?", (ip, ))

def update_vendor_oid(ip, oid):
    with sqlite3.connect(database) as sql:
        sql.execute("UPDATE OR IGNORE vendors SET sysObjectID=?, app=NULL, model=NULL, vendor=NULL WHERE ip=?", (oid, ip))
        sql.execute("INSERT OR IGNORE INTO vendors(sysObjectID, ip) values(?, ?)", (oid, ip))

def get_auth(ip):
    with sqlite3.connect(database) as sql:
        sql.row_factory = sqlite3.Row
        cur = sql.cursor()
        cur.execute("SELECT * FROM auth WHERE ip=?", (ip, ))
        row = cur.fetchone()
        return row

def load(src):
    if in_memory:
        try:
            with sqlite3.connect(database) as sql:
                sql.execute("ATTACH DATABASE ? AS source; INSERT OR FAIL INTO main.queue SELECT * FROM source.queue;", (path, ))
                sql.execute("ATTACH DATABASE ? AS source; INSERT OR FAIL INTO main.auth SELECT * FROM source.auth;", (path, ))
                sql.execute("ATTACH DATABASE ? AS source; INSERT OR FAIL INTO main.vendors SELECT * FROM source.vendors;", (path, ))
        except:
            eprint ("can't transfer database from source", sys.exc_info()[0])

def save():
    pass
