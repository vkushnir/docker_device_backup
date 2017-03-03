FROM vkushnir/pysnmp-py2
MAINTAINER Vladimir Kushnir <vkushnir@gmail.com>

LABEL \
    version="1.1" \
    description="Backup running-config from network devices"

ENV \
    SNMP_TIMEOUT=3 \
    SNMP_RETRIES=1 \
    CONFIG_COMPARE=1 \ 
    CONFIG_NODUP=1 \
    CONFIG_DIFF_OPT="-iEZbBu" \
    CONFIG_FOLDER="/var/config/{syslog[R_YEAR]}/{l0ip}/{syslog[R_YEAR]}-{syslog[R_MONTH]}" \
    CONFIG_FILE="{l0ip}_{syslog[R_YEAR]}{syslog[R_MONTH]}{syslog[R_DAY]}_{n:02}.conf" \
    CONFIG_DIFF="{l0ip}_{syslog[R_YEAR]}{syslog[R_MONTH]}{syslog[R_DAY]}.diff" \
    DB_FILE="devices.db" \
    DB_PATH="/var/sqlite" \
    DB_MEMORY=0 \
    DB_SAVE=1 \
    SRV_SLEEP=60 \
    SRV_SAVE_TIMEOUT=15 \
    SRV_THREADS=10 \
    SRV_HITS=10 \
    SRV_TFTP_ADDR="172.0.0.1" \
    SRV_TFTP_PATH="/var/tftp" \
    SRV_FTP_ADDR="172.0.0.1" \
    SRV_FTP_PATH="/var/ftp"

RUN apk update && apk upgrade && \
    apk add --no-cache --update diffutils syslog-ng sqlite && \
    rm /var/cache/apk/*

VOLUME \
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

