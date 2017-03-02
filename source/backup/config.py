# !/usr/bin/python2
""" DEVICE CONFIGURATION FILES """

__all__ = ['options_snmp', 'options_config', 'options_database', 'options_threads']

# Import required python libraries
import os, sys
import time
from shutil import copyfile
from subprocess import Popen, PIPE
from stat import ST_MTIME
from utils import eprint, sprint, str_to_bool, ConfigFileError, DiffProcedureError

compare = str_to_bool(os.getenv('CONFIG_COMPARE'))
""" generate diff file for configurations in one folder """
no_duplicates = str_to_bool(os.getenv('CONFIG_NODUP'))
""" delete new configurations without changes """
folder = os.getenv('CONFIG_FOLDER')
""" folder to store device configurations in 'format' macro, fields syslog, l0ip """
file = os.getenv('CONFIG_FILE')
""" device configuration names in 'format' macro, fields syslog, l0ip, n """
diff = os.getenv('CONFIG_DIFF')
""" device configuration different file name in 'format' macro, fields syslog, l0ip """
_diff_cmp = ['/usr/bin/diff', '-qs']
_diff_out = ['/usr/bin/diff', os.getenv('CONFIG_DIFF_OPT')]

def do_save(src, msg, opt):
    l0ip = get_l0ip(msg['SOURCEIP'])
    dst_folder = get_config_folder(msg, l0ip=l0ip)
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
        os.chmod(dst_folder, 0o775)
        os.chown(dst_folder, -1, 4)
    n = 0
    dst = get_config_path(msg, config_folder=dst_folder, l0ip=l0ip)
    if no_duplicates:
        file_first, file_last = get_first_last(dst_folder)
        if file_first is not None:
            if file_last is None:
                file_test = file_first
            else:
                file_test = file_last
            if same(file_test, src, opt):
                sprint("backup", msg['SOURCEIP'], "complete, configs are same")
                return False
    sprint("backup", msg['SOURCEIP'], 'complete', dst)
    copyfile(src, dst)
    os.chmod(dst, 0o664)
    os.chown(dst, -1, 4)
    return True

def do_compare(msg, opt=[]):
    l0ip = get_l0ip(msg['SOURCEIP'])
    diff_folder = folder.format(syslog=msg, l0ip=l0ip)
    diff_path = get_diff_path(msg, config_folder=diff_folder, l0ip=l0ip)

    file_first, file_last = get_first_last(diff_folder)
    if (file_last is None):
        return False
    elif same(file_first, file_last, opt):
        if os.path.exists(diff_path):
            os.remove(diff_path)
        return False
    diff_cmd = _diff_out + opt + [file_first, file_last]
    sprint("Generate difference", diff_path)
    with open(diff_path, 'w') as df:
        diff = Popen(diff_cmd, stdout = df)
        diff.communicate()
        if diff.returncode > 1:
            raise DiffProcedureError(' '.join(diff_cmd))
        return True
    os.chmod(diff_path, 0o664)
    os.chown(diff_path, -1, 4)

def get_first_last(folder):
    files = os.listdir(folder)
    if len(files) == 0:
        return None, None
    elif len(files) == 1:
        return os.path.join(folder, files[0]), None

    file_first = file_last = os.path.join(folder, files[0])
    time_first = time_last = os.stat(file_first)[ST_MTIME]

    paths = (os.path.join(folder, fn) for fn in files)
    items = ((os.stat(path)[ST_MTIME], path) for path in paths)

    for st, fp in items:
        if st < time_first:
            time_first = st
            file_first = fp
        elif st > time_last:
            time_last = st
            file_last = fp
    return file_first, file_last

def same(first, second, opt=[]):
    diff_cmd = _diff_cmp + opt + [first, second]
    diff = Popen(diff_cmd, stdout=PIPE)
    diff.communicate()
    if diff.returncode < 2:
        return diff.returncode == 0
    raise DiffProcedureError(' '.join(diff_cmd))

def get_l0ip(ip):
    return "{0[0]:0>3}.{0[1]:0>3}.{0[2]:0>3}.{0[3]:0>3}".format(ip.split('.'))

def get_config_folder(msg, l0ip=None):
    if l0ip is None:
        l0ip = get_l0ip(msg['SOURCEIP'])
    return folder.format(syslog=msg, l0ip=l0ip)

def get_config_path(msg, config_folder=None, l0ip=None):
    if l0ip is None:
        l0ip = get_l0ip(msg['SOURCEIP'])
    if config_folder is None:
        config_folder = get_config_folder(msg, l0ip=l0ip)
    n = 0
    config_path = os.path.join(config_folder, file.format(syslog=msg, l0ip=l0ip, n=n))
    start = time.time()
    while os.path.exists(config_path):
        n +=1
        if n == sys.maxsize:
            raise ConfigFileError("n value too mush '{}'".format(n))
        sec = time.time() - start
        if sec > 10:
            raise ConfigFileError("file name generation too long {} sec".format(sec))
        config_path = os.path.join(config_folder, file.format(syslog=msg, l0ip=l0ip, n=n))
    return config_path

def get_diff_path(msg, config_folder=None, l0ip=None):
    if l0ip is None:
        l0ip = get_l0ip(msg['SOURCEIP'])
    if config_folder is None:
        config_folder = get_config_folder(msg, l0ip=l0ip)
    return os.path.join(config_folder, diff.format(syslog=msg, l0ip=l0ip))
