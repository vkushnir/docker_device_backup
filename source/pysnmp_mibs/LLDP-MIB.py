#
# PySNMP MIB module LLDP-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/LLDP-MIB
# Produced by pysmi-0.0.7 at Fri Feb 17 12:48:35 2017
# On host 5641388e757d platform Linux version 4.4.0-62-generic by user root
# Using Python version 2.7.13 (default, Dec 22 2016, 09:22:15) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( AddressFamilyNumbers, ) = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( TruthValue, TimeStamp, DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "TextualConvention")
lldpMIB = ModuleIdentity((1, 0, 8802, 1, 1, 2)).setRevisions(("2004-11-22 00:00",))
lldpNotifications = MibIdentifier((1, 0, 8802, 1, 1, 2, 0))
lldpObjects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1))
lldpConformance = MibIdentifier((1, 0, 8802, 1, 1, 2, 2))
lldpConfiguration = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 1))
lldpStatistics = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 2))
lldpLocalSystemData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 3))
lldpRemoteSystemsData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 4))
lldpExtensions = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5))
class TimeFilter(TimeTicks, TextualConvention):
    pass

class ZeroBasedCounter32(Gauge32, TextualConvention):
    pass

class LldpChassisIdSubtype(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7),)

class LldpChassisId(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)

class LldpPortIdSubtype(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7),)

class LldpPortId(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)

class LldpManAddrIfSubtype(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("unknown", 1), ("ifIndex", 2), ("systemPortNumber", 3),)

class LldpManAddress(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,31)

class LldpSystemCapabilitiesMap(Bits, TextualConvention):
    namedValues = NamedValues(("other", 0), ("repeater", 1), ("bridge", 2), ("wlanAccessPoint", 3), ("router", 4), ("telephone", 5), ("docsisCableDevice", 6), ("stationOnly", 7),)

class LldpPortNumber(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,4096)

class LldpPortList(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,512)

lldpMessageTxInterval = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5,32768)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
lldpMessageTxHoldMultiplier = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2,10)).clone(4)).setMaxAccess("readwrite")
lldpReinitDelay = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,10)).clone(2)).setUnits('seconds').setMaxAccess("readwrite")
lldpTxDelay = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,8192)).clone(2)).setUnits('seconds').setMaxAccess("readwrite")
lldpNotificationInterval = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5,3600)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
lldpPortConfigTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 1, 6), )
lldpPortConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1), ).setIndexNames((0, "LLDP-MIB", "lldpPortConfigPortNum"))
lldpPortConfigPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 1), LldpPortNumber())
lldpPortConfigAdminStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4,)).clone(namedValues=NamedValues(("txOnly", 1), ("rxOnly", 2), ("txAndRx", 3), ("disabled", 4),)).clone('txAndRx')).setMaxAccess("readwrite")
lldpPortConfigNotificationEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
lldpPortConfigTLVsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 4), Bits().clone(namedValues=NamedValues(("portDesc", 0), ("sysName", 1), ("sysDesc", 2), ("sysCap", 3),))).setMaxAccess("readwrite")
lldpConfigManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 1, 7), )
lldpConfigManAddrPortsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 7, 1, 1), LldpPortList().clone(hexValue="")).setMaxAccess("readwrite")
lldpStatsRemTablesLastChangeTime = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
lldpStatsRemTablesInserts = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 2), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
lldpStatsRemTablesDeletes = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 3), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
lldpStatsRemTablesDrops = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 4), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
lldpStatsRemTablesAgeouts = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 5), ZeroBasedCounter32()).setMaxAccess("readonly")
lldpStatsTxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 2, 6), )
lldpStatsTxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1), ).setIndexNames((0, "LLDP-MIB", "lldpStatsTxPortNum"))
lldpStatsTxPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 1), LldpPortNumber())
lldpStatsTxPortFramesTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 2, 7), )
lldpStatsRxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1), ).setIndexNames((0, "LLDP-MIB", "lldpStatsRxPortNum"))
lldpStatsRxPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 1), LldpPortNumber())
lldpStatsRxPortFramesDiscardedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortFramesErrors = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortFramesTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortTLVsDiscardedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortTLVsUnrecognizedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 6), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortAgeoutsTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
lldpLocChassisIdSubtype = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 1), LldpChassisIdSubtype()).setMaxAccess("readonly")
lldpLocChassisId = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 2), LldpChassisId()).setMaxAccess("readonly")
lldpLocSysName = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readonly")
lldpLocSysDesc = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readonly")
lldpLocSysCapSupported = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 5), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
lldpLocSysCapEnabled = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 6), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
lldpLocPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 3, 7), )
lldpLocPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
lldpLocPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 1), LldpPortNumber())
lldpLocPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 2), LldpPortIdSubtype()).setMaxAccess("readonly")
lldpLocPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 3), LldpPortId()).setMaxAccess("readonly")
lldpLocPortDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readonly")
lldpLocManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 3, 8), )
lldpLocManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocManAddrSubtype"), (0, "LLDP-MIB", "lldpLocManAddr"))
lldpConfigManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 1, 7, 1), )
lldpLocManAddrEntry.registerAugmentions(("LLDP-MIB", "lldpConfigManAddrEntry"))
lldpConfigManAddrEntry.setIndexNames(*lldpLocManAddrEntry.getIndexNames())
lldpLocManAddrSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 1), AddressFamilyNumbers())
lldpLocManAddr = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 2), LldpManAddress())
lldpLocManAddrLen = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 3), Integer32()).setMaxAccess("readonly")
lldpLocManAddrIfSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 4), LldpManAddrIfSubtype()).setMaxAccess("readonly")
lldpLocManAddrIfId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 5), Integer32()).setMaxAccess("readonly")
lldpLocManAddrOID = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
lldpRemTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 1), )
lldpRemEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
lldpRemTimeMark = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 1), TimeFilter())
lldpRemLocalPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 2), LldpPortNumber())
lldpRemIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
lldpRemChassisIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 4), LldpChassisIdSubtype()).setMaxAccess("readonly")
lldpRemChassisId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 5), LldpChassisId()).setMaxAccess("readonly")
lldpRemPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 6), LldpPortIdSubtype()).setMaxAccess("readonly")
lldpRemPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 7), LldpPortId()).setMaxAccess("readonly")
lldpRemPortDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readonly")
lldpRemSysName = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readonly")
lldpRemSysDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readonly")
lldpRemSysCapSupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 11), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
lldpRemSysCapEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 12), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
lldpRemManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 2), )
lldpRemManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemManAddrSubtype"), (0, "LLDP-MIB", "lldpRemManAddr"))
lldpRemManAddrSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 1), AddressFamilyNumbers())
lldpRemManAddr = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 2), LldpManAddress())
lldpRemManAddrIfSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 3), LldpManAddrIfSubtype()).setMaxAccess("readonly")
lldpRemManAddrIfId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
lldpRemManAddrOID = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
lldpRemUnknownTLVTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 3), )
lldpRemUnknownTLVEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemUnknownTLVType"))
lldpRemUnknownTLVType = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(9,126)))
lldpRemUnknownTLVInfo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,511))).setMaxAccess("readonly")
lldpRemOrgDefInfoTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 4), )
lldpRemOrgDefInfoEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemOrgDefInfoOUI"), (0, "LLDP-MIB", "lldpRemOrgDefInfoSubtype"), (0, "LLDP-MIB", "lldpRemOrgDefInfoIndex"))
lldpRemOrgDefInfoOUI = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3,3)).setFixedLength(3))
lldpRemOrgDefInfoSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,255)))
lldpRemOrgDefInfoIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
lldpRemOrgDefInfo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,507))).setMaxAccess("readonly")
lldpNotificationPrefix = MibIdentifier((1, 0, 8802, 1, 1, 2, 0, 0))
lldpRemTablesChange = NotificationType((1, 0, 8802, 1, 1, 2, 0, 0, 1)).setObjects(*(("LLDP-MIB", "lldpStatsRemTablesInserts"), ("LLDP-MIB", "lldpStatsRemTablesDeletes"), ("LLDP-MIB", "lldpStatsRemTablesDrops"), ("LLDP-MIB", "lldpStatsRemTablesAgeouts"),))
lldpCompliances = MibIdentifier((1, 0, 8802, 1, 1, 2, 2, 1))
lldpGroups = MibIdentifier((1, 0, 8802, 1, 1, 2, 2, 2))
lldpCompliance = ModuleCompliance((1, 0, 8802, 1, 1, 2, 2, 1, 1)).setObjects(*(("LLDP-MIB", "lldpConfigGroup"), ("LLDP-MIB", "lldpConfigRxGroup"), ("LLDP-MIB", "lldpConfigTxGroup"), ("LLDP-MIB", "lldpStatsRxGroup"), ("LLDP-MIB", "lldpStatsTxGroup"), ("LLDP-MIB", "lldpLocSysGroup"), ("LLDP-MIB", "lldpRemSysGroup"), ("LLDP-MIB", "lldpNotificationsGroup"),))
lldpConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 1)).setObjects(*(("LLDP-MIB", "lldpPortConfigAdminStatus"),))
lldpConfigRxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 2)).setObjects(*(("LLDP-MIB", "lldpNotificationInterval"), ("LLDP-MIB", "lldpPortConfigNotificationEnable"),))
lldpConfigTxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 3)).setObjects(*(("LLDP-MIB", "lldpMessageTxInterval"), ("LLDP-MIB", "lldpMessageTxHoldMultiplier"), ("LLDP-MIB", "lldpReinitDelay"), ("LLDP-MIB", "lldpTxDelay"), ("LLDP-MIB", "lldpPortConfigTLVsTxEnable"), ("LLDP-MIB", "lldpConfigManAddrPortsTxEnable"),))
lldpStatsRxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 4)).setObjects(*(("LLDP-MIB", "lldpStatsRemTablesLastChangeTime"), ("LLDP-MIB", "lldpStatsRemTablesInserts"), ("LLDP-MIB", "lldpStatsRemTablesDeletes"), ("LLDP-MIB", "lldpStatsRemTablesDrops"), ("LLDP-MIB", "lldpStatsRemTablesAgeouts"), ("LLDP-MIB", "lldpStatsRxPortFramesDiscardedTotal"), ("LLDP-MIB", "lldpStatsRxPortFramesErrors"), ("LLDP-MIB", "lldpStatsRxPortFramesTotal"), ("LLDP-MIB", "lldpStatsRxPortTLVsDiscardedTotal"), ("LLDP-MIB", "lldpStatsRxPortTLVsUnrecognizedTotal"), ("LLDP-MIB", "lldpStatsRxPortAgeoutsTotal"),))
lldpStatsTxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 5)).setObjects(*(("LLDP-MIB", "lldpStatsTxPortFramesTotal"),))
lldpLocSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 6)).setObjects(*(("LLDP-MIB", "lldpLocChassisIdSubtype"), ("LLDP-MIB", "lldpLocChassisId"), ("LLDP-MIB", "lldpLocPortIdSubtype"), ("LLDP-MIB", "lldpLocPortId"), ("LLDP-MIB", "lldpLocPortDesc"), ("LLDP-MIB", "lldpLocSysDesc"), ("LLDP-MIB", "lldpLocSysName"), ("LLDP-MIB", "lldpLocSysCapSupported"), ("LLDP-MIB", "lldpLocSysCapEnabled"), ("LLDP-MIB", "lldpLocManAddrLen"), ("LLDP-MIB", "lldpLocManAddrIfSubtype"), ("LLDP-MIB", "lldpLocManAddrIfId"), ("LLDP-MIB", "lldpLocManAddrOID"),))
lldpRemSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 7)).setObjects(*(("LLDP-MIB", "lldpRemChassisIdSubtype"), ("LLDP-MIB", "lldpRemChassisId"), ("LLDP-MIB", "lldpRemPortIdSubtype"), ("LLDP-MIB", "lldpRemPortId"), ("LLDP-MIB", "lldpRemPortDesc"), ("LLDP-MIB", "lldpRemSysName"), ("LLDP-MIB", "lldpRemSysDesc"), ("LLDP-MIB", "lldpRemSysCapSupported"), ("LLDP-MIB", "lldpRemSysCapEnabled"), ("LLDP-MIB", "lldpRemManAddrIfSubtype"), ("LLDP-MIB", "lldpRemManAddrIfId"), ("LLDP-MIB", "lldpRemManAddrOID"), ("LLDP-MIB", "lldpRemUnknownTLVInfo"), ("LLDP-MIB", "lldpRemOrgDefInfo"),))
lldpNotificationsGroup = NotificationGroup((1, 0, 8802, 1, 1, 2, 2, 2, 8)).setObjects(*(("LLDP-MIB", "lldpRemTablesChange"),))
mibBuilder.exportSymbols("LLDP-MIB", lldpStatsRxPortFramesErrors=lldpStatsRxPortFramesErrors, lldpConfigTxGroup=lldpConfigTxGroup, LldpChassisIdSubtype=LldpChassisIdSubtype, lldpConfiguration=lldpConfiguration, lldpPortConfigPortNum=lldpPortConfigPortNum, TimeFilter=TimeFilter, lldpConfigGroup=lldpConfigGroup, lldpRemSysCapEnabled=lldpRemSysCapEnabled, lldpStatsTxPortEntry=lldpStatsTxPortEntry, lldpStatsRemTablesDeletes=lldpStatsRemTablesDeletes, lldpRemOrgDefInfoTable=lldpRemOrgDefInfoTable, lldpRemManAddrEntry=lldpRemManAddrEntry, lldpRemManAddrIfId=lldpRemManAddrIfId, lldpStatsTxPortTable=lldpStatsTxPortTable, lldpConfigManAddrEntry=lldpConfigManAddrEntry, lldpRemPortIdSubtype=lldpRemPortIdSubtype, ZeroBasedCounter32=ZeroBasedCounter32, lldpRemEntry=lldpRemEntry, lldpStatsRemTablesLastChangeTime=lldpStatsRemTablesLastChangeTime, lldpExtensions=lldpExtensions, lldpLocPortEntry=lldpLocPortEntry, lldpRemoteSystemsData=lldpRemoteSystemsData, lldpLocSysGroup=lldpLocSysGroup, lldpStatsRxPortFramesTotal=lldpStatsRxPortFramesTotal, lldpLocManAddrIfSubtype=lldpLocManAddrIfSubtype, lldpLocManAddrOID=lldpLocManAddrOID, lldpStatsRxPortEntry=lldpStatsRxPortEntry, lldpStatsRxPortTable=lldpStatsRxPortTable, lldpPortConfigTable=lldpPortConfigTable, lldpGroups=lldpGroups, PYSNMP_MODULE_ID=lldpMIB, LldpSystemCapabilitiesMap=LldpSystemCapabilitiesMap, lldpRemTimeMark=lldpRemTimeMark, lldpRemOrgDefInfoEntry=lldpRemOrgDefInfoEntry, lldpRemChassisId=lldpRemChassisId, lldpRemChassisIdSubtype=lldpRemChassisIdSubtype, lldpLocalSystemData=lldpLocalSystemData, lldpLocManAddrTable=lldpLocManAddrTable, lldpStatsTxPortFramesTotal=lldpStatsTxPortFramesTotal, lldpStatsRemTablesAgeouts=lldpStatsRemTablesAgeouts, lldpPortConfigAdminStatus=lldpPortConfigAdminStatus, lldpRemSysDesc=lldpRemSysDesc, lldpLocPortNum=lldpLocPortNum, lldpRemManAddrTable=lldpRemManAddrTable, lldpStatsRxPortTLVsUnrecognizedTotal=lldpStatsRxPortTLVsUnrecognizedTotal, lldpLocSysName=lldpLocSysName, lldpStatistics=lldpStatistics, lldpRemOrgDefInfoOUI=lldpRemOrgDefInfoOUI, lldpMessageTxInterval=lldpMessageTxInterval, lldpNotifications=lldpNotifications, LldpPortId=LldpPortId, lldpLocPortTable=lldpLocPortTable, lldpLocPortIdSubtype=lldpLocPortIdSubtype, lldpMIB=lldpMIB, lldpRemSysGroup=lldpRemSysGroup, lldpRemManAddrOID=lldpRemManAddrOID, lldpRemUnknownTLVTable=lldpRemUnknownTLVTable, lldpRemIndex=lldpRemIndex, lldpCompliance=lldpCompliance, lldpStatsRemTablesDrops=lldpStatsRemTablesDrops, lldpCompliances=lldpCompliances, lldpObjects=lldpObjects, lldpNotificationPrefix=lldpNotificationPrefix, lldpLocManAddrEntry=lldpLocManAddrEntry, lldpRemLocalPortNum=lldpRemLocalPortNum, lldpConfigManAddrTable=lldpConfigManAddrTable, LldpChassisId=LldpChassisId, lldpStatsTxPortNum=lldpStatsTxPortNum, lldpRemTablesChange=lldpRemTablesChange, lldpRemOrgDefInfo=lldpRemOrgDefInfo, lldpLocManAddr=lldpLocManAddr, lldpRemManAddrSubtype=lldpRemManAddrSubtype, lldpRemManAddr=lldpRemManAddr, lldpLocManAddrSubtype=lldpLocManAddrSubtype, lldpRemPortDesc=lldpRemPortDesc, LldpManAddrIfSubtype=LldpManAddrIfSubtype, lldpRemSysCapSupported=lldpRemSysCapSupported, lldpTxDelay=lldpTxDelay, lldpRemOrgDefInfoSubtype=lldpRemOrgDefInfoSubtype, lldpStatsRxPortNum=lldpStatsRxPortNum, lldpStatsRemTablesInserts=lldpStatsRemTablesInserts, lldpStatsRxPortFramesDiscardedTotal=lldpStatsRxPortFramesDiscardedTotal, lldpLocChassisIdSubtype=lldpLocChassisIdSubtype, lldpRemTable=lldpRemTable, lldpLocSysDesc=lldpLocSysDesc, lldpLocPortDesc=lldpLocPortDesc, lldpStatsRxPortTLVsDiscardedTotal=lldpStatsRxPortTLVsDiscardedTotal, LldpManAddress=LldpManAddress, lldpConfigManAddrPortsTxEnable=lldpConfigManAddrPortsTxEnable, lldpLocSysCapSupported=lldpLocSysCapSupported, lldpRemUnknownTLVType=lldpRemUnknownTLVType, lldpLocPortId=lldpLocPortId, lldpStatsRxPortAgeoutsTotal=lldpStatsRxPortAgeoutsTotal, lldpConformance=lldpConformance, lldpLocManAddrIfId=lldpLocManAddrIfId, lldpStatsTxGroup=lldpStatsTxGroup, lldpRemUnknownTLVEntry=lldpRemUnknownTLVEntry, LldpPortIdSubtype=LldpPortIdSubtype, lldpNotificationInterval=lldpNotificationInterval, lldpPortConfigNotificationEnable=lldpPortConfigNotificationEnable, lldpPortConfigEntry=lldpPortConfigEntry, LldpPortNumber=LldpPortNumber, lldpRemPortId=lldpRemPortId, lldpNotificationsGroup=lldpNotificationsGroup, lldpRemUnknownTLVInfo=lldpRemUnknownTLVInfo, lldpLocSysCapEnabled=lldpLocSysCapEnabled, lldpLocManAddrLen=lldpLocManAddrLen, lldpReinitDelay=lldpReinitDelay, lldpRemOrgDefInfoIndex=lldpRemOrgDefInfoIndex, lldpStatsRxGroup=lldpStatsRxGroup, lldpPortConfigTLVsTxEnable=lldpPortConfigTLVsTxEnable, lldpRemSysName=lldpRemSysName, lldpMessageTxHoldMultiplier=lldpMessageTxHoldMultiplier, lldpConfigRxGroup=lldpConfigRxGroup, lldpRemManAddrIfSubtype=lldpRemManAddrIfSubtype, LldpPortList=LldpPortList, lldpLocChassisId=lldpLocChassisId)