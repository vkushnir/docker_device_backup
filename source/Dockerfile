FROM alpine:3.5
MAINTAINER Vladimir Kushnir <vkushnir@gmail.com>

LABEL \
    version="1.1" \
    description="Backup running-config from network devices"

ENV \
    SNMP_VERSION=2c \
    SNMP_COMMUNITY="public" \
    SNMP_APROTOCOL="MD5" \
    SNMP_APASSPHRASE="pass" \
    SNMP_SENGINE-ID="00000000" \
    SNMP_CENGINE-ID="00000000" \
    SNMP_LEVEL="noAuthNoPriv" \
    SNMP_CONTEXT="backup" \
    SNMP_USER-NAME="backup" \
    SNMP_PPROTOCOL="DES" \
    SNMP_PPASSPHRASE="pass" \
    SNMP_BOOTS_TIME="" \
    SNMP_TIMEOUT=3 \
    SNMP_RETRIES=1 \
    CONFIG_COMPARE=1 \ 
    CONFIG_NODUP=1 \
    CONFIG_DIFF_OPT="-iEZbBu" \
    CONFIG_FOLDER="/var/config/{syslog[R_YEAR]}/{l0ip}/{syslog[R_YEAR]}-{syslog[R_MONTH]}" \
    CONFIG_FILE="{l0ip}_{syslog[R_YEAR]}{syslog[R_MONTH]}{syslog[R_DAY]}_{n:02}.conf" \
    CONFIG_DIFF="{l0ip}_{syslog[R_YEAR]}{syslog[R_MONTH]}{syslog[R_DAY]}.diff" \
    DB_FILE="devices.db" \
    DB_PATH="/var/mysqlite" \
    DB_MEMORY=0 \
    DB_SAVE=1 \
    SRV_SLEEP=60 \
    SRV_SAVE_TIMEOUT=15 \
    SRV_THREADS=10 \
    SRV_HITS=10 \
    SRV_TFTP_ADDR="172.0.0.1" \
    SRV_TFTP_PATH="/var/tftp" \
    SRV_FTP_ADDR="172.0.0.1" \
    SRV_FTP_PATH="/var/ftp" \
    PYTHONPATH="/usr/local/lib/python"

RUN apk update && apk upgrade && \
    apk del --purge rsyslog && \
    rm -f /var/log/* /sbin/rsyslogd && \
    apk add --no-cache --update diffutils syslog-ng sqlite python2 py2-pip py2-snmp && \
    pip install --upgrade pip && \
    pip install pysmi pysnmp_mibs pysnmp_apps && \
    rm /var/cache/apk/*

VOLUME \
    /usr/local/bin \
    /usr/local/lib/python \
    /usr/local/share/snmp/mibs \
    /usr/local/share/snmp/pysnmp_mibs \
    /etc/syslog-ng \
    /etc/dev-backup \
    /etc/vsftpd \
    /var/config \
    /var/tftp \
    /var/ftp \
    /var/sqlite \
    /var/log

COPY syslog-ng.conf /etc/syslog-ng/
COPY backup /usr/local/lib/python/backup
COPY mibs/* /usr/local/share/snmp/mibs/
COPY pysnmp_mibs/* /usr/local/share/snmp/pysnmp_mibs/

EXPOSE 514/udp 514/tcp

ENTRYPOINT ["syslog-ng"]
CMD ["--foreground", "--verbose", "--trace"]

