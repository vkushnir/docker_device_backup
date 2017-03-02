# Device Backup Service
*Listen syslog messages and if someone do something download config from device*

Service listen syslog messages and if find something like "**User some_user logout**" or "**%SYS-5-CONFIG_I:**", run python class **backup.main.backup.send(msg)**.

msg &mdash; is value-pairs dict wich contains all variables from syslog message wich can be used for fomating data folders and stored config files.

Use volume from docerised TFTP and/or FTP server.

### RUN
    docker run -d --name tftpd -p 69/udp vkushnir/tftp-hpa
    docker run -d --volumes-from tftpd --name device-backup -p 514/udp --link tftpd -v /data/config:/var/config -e SNMP_COMMUNITY="public" -e SRV_TFTP_ADDR="8.8.8.8" vkushnir/device-backup
    
## Docker Variables

### SNMP
- SNMP_VERSION=**2c** &mdash; snmp version 1,2c,3

#### SNMP Version 1 or 2c specific
- SNMP_COMMUNITY="**public**" &mdash; default community string

#### SNMP Version 3 specific
- SNMP_APROTOCOL="**MD5**" &mdash; default authentication protocol (**MD5**|**SHA**)
- SNMP_APASSPHRASE="**pass**" &mdash; default authentication protocol pass phrase
- SNMP_SENGINE-ID="**00000000**" &mdash; default security engine ID (e.g. 800000020109840301)
- SNMP_CENGINE-ID="**00000000**" &mdash; default context engine ID (e.g. 800000020109840301)
- SNMP_LEVEL="**noAuthNoPriv**" &mdash; default security level (**noAuthNoPriv**|**authNoPriv**|**authPriv**)
- SNMP_CONTEXT="**backup**" &mdash; default context name (e.g. bridge1)
- SNMP_USER-NAME="**backup**" &mdash; default security name (e.g. bert)
- SNMP_PPROTOCOL="**DES**" &mdash; default privacy protocol (**DES**|**AES**)
- SNMP_PPASSPHRASE="**pass**" &mdash; default privacy protocol pass phrase
- SNMP_BOOTS="" &mdash; default destination engine boots/time

#### SNMP Others
- SNMP_TIMEOUT=**3** &mdash; timeout in seconds to wait snmp device answer
- SNMP_RETRIES=**1** &mdash; count retry requests from snmp device

### Device configuration store settings
- CONFIG_COMPARE=**1** &mdash; compare downloaded config with previous in the same folder
- CONFIG_NODUP=**1** &mdash; don't store config if previous is the same (require CONFIG_COMPARE=1)
- CONFIG_DIFF_OPT="**-iEZbBu**" &mdash; options for linux diff
- CONFIG_FOLDER="**/var/config/{syslog[R_YEAR]}/{l0ip}/{syslog[R_YEAR]}-{syslog[R_MONTH]}**" &mdash; template for config folder
- CONFIG_FILE="**{l0ip}_{syslog[R_YEAR]}{syslog[R_MONTH]}{syslog[R_DAY]}_{n:02}.conf**" &mdash; template for config file
- CONFIG_DIFF="**{l0ip}_{syslog[R_YEAR]}{syslog[R_MONTH]}{syslog[R_DAY]}.diff**" &mdash; template for different file
> format using str.format(msg=&lt;syslog-ng_message[]&gt;, l0ip=&lt;leading zero source ip (172.000.000.001)&gt;, n=&lt;count fies with same name&gt;)

### Database
- DB_FILE="**devices.db**" &mdash; SQLite database file name
- DB_PATH="**/var/sqlite**" &mdash; SQLite database file location
- DB_MEMORY=**1** &mdash; Load full database to memory on init stage
- DB_SAVE=**1** &mdash; Save database to disk on uninit stage (require DB_MEMORY=1)

### Server
- SRV_SLEEP=**60** &mdash; *not yet reliased*
- SRV_SAVE_TIMEOUT=**15** &mdash; Timeout for waiting tftp transfer from device
- SRV_THREADS=**10** &mdash; Maximum count simultaneous threads (*not yet reliased*)
- SRV_HITS=**10** &mdash; Maximum hits for single device before generate error message (*not yet reliased*)
- SRV_TFTP_ADDR="**172.0.0.1**" &mdash; Default external TFTP server address
- SRV_TFTP_PATH="**/var/tftp**" &mdash; Default TFTP server volume location
- SRV_FTP_ADDR="**172.0.0.1**" &mdash; Default external FTP server address
- SRV_FTP_PATH="**/var/ftp**" &mdash; Default FTP server volume location

### Others
- PYTHONPATH="/usr/local/lib/python" &mdash; Path to python modules volume

## Docker Volumes
- /usr/local/bin &mdash; folder for python executables
- /usr/local/lib/python &mdash; Python modules
- /usr/local/share/snmp/mibs &mdash; ASN1 mib files
- /usr/local/share/snmp/pysnmp_mibs &mdash; PySNMP compiled modules 
- /etc/syslog-ng &mdash; Syslog-ng configuration folder
- /etc/dev-backup &mdash; Device backup configuration folder
- /var/config &mdash; Downloaded config files
- /var/tftp &mdash; TFTP folder
- /var/ftp &mdash; FTP folder
- /var/sqlite &mdash; SQL folder
