# !/usr/bin/python2
""" THREADS """

# Import required python libraries
import os
import threading, time, random
import snmp, config, database, server
from pysnmp.hlapi import *
from syslog.utils import sprint, eprint

class BackupThread(object):
    def __init__(self):
        self.count = 0

    def run(self, args):
        sprint("add", args['SOURCEIP'], "to queue")
        # TODO: add hits to table to count trys
        BackupDevice(args).start()
        return True

class BackupDevice(threading.Thread):
    def __init__(self, data):
        self.data = data
        self.conn = snmp.ConnectionData(self.data['SOURCEIP'])
        database.lock(self.data['SOURCEIP'])
        threading.Thread.__init__(self)

    def run(self):
        #database.lock(self.data['SOURCEIP'])
        varBinds, err = snmp.get(self.conn, snmp.sysObjectID)
        if err:
            database.release(self.data['SOURCEIP'])
            return False
        else:
            sprint("Start Thread for device", self.data['SOURCEIP'], varBinds[0][1].prettyPrint())
            if varBinds[0][1][6] == 9:
                backup_class = BackupDeviceCISCO
            elif varBinds[0][1][6] == 890:
                backup_class = BackupDeviceZyXEL
            else:
                eprint("Unknown device vendor", self.data['SOURCEIP'], varBinds[0][1].prettyPrint())
                database.update_vendor_oid(self.data['SOURCEIP'], str(varBinds[0][1].prettyPrint()))
                database.release(self.data['SOURCEIP'])
                return False

        with backup_class(varBinds, self.data, self.conn) as backup:
            if backup.run():
                if backup.save() and config.compare:
                    backup.compare()
                database.clear(self.data['SOURCEIP'])
            else:
                eprint("Backup", self.data['SOURCEIP'], "error")
        database.release(self.data['SOURCEIP'])
        #sprint("Finish Thread for device", self.data['SOURCEIP'])

class BackupDeviceVendor(object):
    def __init__(self, id, data, conn, srv):
        self.id = id
        self.data = data
        self.conn = conn
        self.rnd = random.randint(1, 2147483647)
        self.diff_opt = None
        self.mib = self.id[0][1].getMibSymbol()[0]
        self.srv_file = self.data['SOURCEIP']+'.conf'
        self.srv_path = srv.get_path(self.srv_file)
        open(self.srv_path, 'w+')
        os.chmod(self.srv_path, 0o666)
        self.cs_waiting=1
        self.cs_running=2
        self.cs_successful=3
        self.cs_failed=4

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.remove(self.srv_path)

    def setup(self, data):
        for obj, idx, value in data:
            sprint("def setup", obj, idx, value)
            ot = ObjectType(ObjectIdentity(self.mib, obj, idx), value)
            result, err = snmp.set(self.conn, ot)
            if err:
                return None
        return True

    def wait(self, obj, idx):
        ot = ObjectType(ObjectIdentity(self.mib, obj, idx))
        cs, err = snmp.get(self.conn, ot)
        if err:
            return False
        sprint("init", self.data['SOURCEIP'], self.mib, cs[0].prettyPrint())

        i = server.save_timeout // 2
        while i > 0 and cs[0][1] == self.cs_waiting and not err:
            time.sleep(1)
            i -= 1
            cs, err = snmp.get(self.conn, ot)
            sprint("wait", i, self.data['SOURCEIP'], self.mib, cs[0].prettyPrint())
            if err:
                return False
        if i <= 0:
            eprint("Download config", self.data['SOURCEIP'], self.mib, 'did not start in timeout!')

        i = server.save_timeout
        while i > 0 and cs[0][1] == self.cs_running and not err:
            time.sleep(1)
            i -= 1
            cs, err = snmp.get(self.conn, ot)
            sprint("downloading", i, self.data['SOURCEIP'], self.mib, cs[0].prettyPrint())
            if err:
                return False
        if i <= 0:
            eprint("Download config", self.data['SOURCEIP'], self.mib, 'timeout!')
        elif cs[0][1] == self.cs_successful:
            if os.path.getsize(self.srv_path) <= 0:
                eprint("Downloaded config", self.data['SOURCEIP'], self.mib, 'size zero!')
                return False
            return True
        else:
            eprint("Save config", self.data['SOURCEIP'], self.mib, 'exit with', cs[0][1].prettyPrint())
        return False

    def run(self):
        pass

    def save(self):
        return config.do_save(self.srv_path, self.data, self.diff_opt)

    def compare(self):
        return config.do_compare(self.data, self.diff_opt)

class BackupDeviceCISCO(BackupDeviceVendor):
    def __init__(self, id, data, conn):
        super(BackupDeviceCISCO, self).__init__(id, data, conn, server.tftp)
        self.mib = 'CISCO-CONFIG-COPY-MIB'
        self.diff_opt = ['--ignore-matching-lines=^!']
        self.cs_waiting=1
        self.cs_running=2
        self.cs_successful=3
        self.cs_failed=4
        """
        ccCopyState:
            waiting=1,
            running=2,
            successful=3,
            failed=4
        """
    def run(self):
        data = (('ccCopyProtocol', self.rnd, 'tftp'),
                ('ccCopySourceFileType', self.rnd, 'runningConfig'),
                ('ccCopyDestFileType', self.rnd, 'networkFile'),
                ('ccCopyServerAddress', self.rnd, server.tftp.addr),
                ('ccCopyFileName', self.rnd, self.srv_file),
                ('ccCopyEntryRowStatus', self.rnd, 'active'))
        if super(BackupDeviceCISCO, self).setup(data):
            return super(BackupDeviceCISCO, self).wait('ccCopyState', self.rnd)
        return False

class BackupDeviceZyXEL(BackupDeviceVendor):
    def __init__(self, id, data, conn):
        super(BackupDeviceZyXEL, self).__init__(id, data, conn, server.tftp)
        self.model = self.id[0][1].getMibSymbol()[1]
        self.diff_opt = ['--ignore-matching-lines=^!']
        self.cs_waiting=0
        self.cs_running=3
        self.cs_successful=1
        self.cs_failed=2
        """
        sysMgmtTftpActionStatus:
            none(0),
            success(1),
            fail(2),
            under-action(3)
        """
    def run(self):
        data = (('sysMgmtTftpServerIp', 0, server.tftp.addr),
                ('sysMgmtTftpRemoteFileName', 0, self.srv_file),
                #('sysMgmtTftpConfigIndex', 0, 'config-1'),
                ('sysMgmtTftpAction', 0, 'backup-config'))
        if super(BackupDeviceZyXEL, self).setup(data):
            time.sleep(1)
            result = super(BackupDeviceZyXEL, self).wait('sysMgmtTftpActionStatus', 0)
            return result
        return False
