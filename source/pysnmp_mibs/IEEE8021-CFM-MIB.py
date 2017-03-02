#
# PySNMP MIB module IEEE8021-CFM-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/IEEE8021-CFM-MIB
# Produced by pysmi-0.0.7 at Fri Feb 17 12:48:35 2017
# On host 5641388e757d platform Linux version 4.4.0-62-generic by user root
# Using Python version 2.7.13 (default, Dec 22 2016, 09:22:15) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ieee802dot1mibs, IEEE8021VlanIndex, ) = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs", "IEEE8021VlanIndex")
( InterfaceIndexOrZero, InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
( LldpPortIdSubtype, LldpChassisId, LldpChassisIdSubtype, LldpPortId, ) = mibBuilder.importSymbols("LLDP-MIB", "LldpPortIdSubtype", "LldpChassisId", "LldpChassisIdSubtype", "LldpPortId")
( VlanIdOrNone, VlanId, ) = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone", "VlanId")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( TimeInterval, MacAddress, TextualConvention, TruthValue, TimeStamp, RowStatus, DisplayString, TAddress, TDomain, ) = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "MacAddress", "TextualConvention", "TruthValue", "TimeStamp", "RowStatus", "DisplayString", "TAddress", "TDomain")
ieee8021CfmMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 8)).setRevisions(("2011-02-27 00:00", "2008-11-18 00:00", "2008-10-15 00:00", "2007-06-10 00:00",))
dot1agNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 0))
dot1agMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1))
dot1agCfmConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 2))
dot1agCfmStack = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 1))
dot1agCfmDefaultMd = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 2))
dot1agCfmVlan = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 3))
dot1agCfmConfigErrorList = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 4))
dot1agCfmMd = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 5))
dot1agCfmMa = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 6))
dot1agCfmMep = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 7))
class Dot1agCfmMaintDomainNameType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("none", 1), ("dnsLikeName", 2), ("macAddressAndUint", 3), ("charString", 4),)

class Dot1agCfmMaintDomainName(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,43)

class Dot1agCfmMaintAssocNameType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 32,)
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4), ("ICCformat", 32),)

class Dot1agCfmMaintAssocName(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,45)

class Dot1agCfmMDLevel(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,7)

class Dot1agCfmMDLevelOrNone(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,7),)
class Dot1agCfmMpDirection(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("down", 1), ("up", 2),)

class Dot1agCfmPortStatus(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("psNoPortStateTLV", 0), ("psBlocked", 1), ("psUp", 2),)

class Dot1agCfmInterfaceStatus(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("isNoInterfaceStatusTLV", 0), ("isUp", 1), ("isDown", 2), ("isTesting", 3), ("isUnknown", 4), ("isDormant", 5), ("isNotPresent", 6), ("isLowerLayerDown", 7),)

class Dot1agCfmHighestDefectPri(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5,)
    namedValues = NamedValues(("none", 0), ("defRDICCM", 1), ("defMACstatus", 2), ("defRemoteCCM", 3), ("defErrorCCM", 4), ("defXconCCM", 5),)

class Dot1agCfmLowestAlarmPri(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6,)
    namedValues = NamedValues(("allDef", 1), ("macRemErrXcon", 2), ("remErrXcon", 3), ("errXcon", 4), ("xcon", 5), ("noXcon", 6),)

class Dot1agCfmMepId(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,8191)

class Dot1agCfmMepIdOrZero(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,8191),)
class Dot1agCfmMhfCreation(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3), ("defMHFdefer", 4),)

class Dot1agCfmIdPermission(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5,)
    namedValues = NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4), ("sendIdDefer", 5),)

class Dot1agCfmCcmInterval(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("intervalInvalid", 0), ("interval300Hz", 1), ("interval10ms", 2), ("interval100ms", 3), ("interval1s", 4), ("interval10s", 5), ("interval1min", 6), ("interval10min", 7),)

class Dot1agCfmFngState(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5,)
    namedValues = NamedValues(("fngReset", 1), ("fngDefect", 2), ("fngReportDefect", 3), ("fngDefectReported", 4), ("fngDefectClearing", 5),)

class Dot1agCfmRelayActionFieldValue(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("rlyHit", 1), ("rlyFdb", 2), ("rlyMpdb", 3),)

class Dot1agCfmIngressActionFieldValue(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4,)
    namedValues = NamedValues(("ingNoTlv", 0), ("ingOk", 1), ("ingDown", 2), ("ingBlocked", 3), ("ingVid", 4),)

class Dot1agCfmEgressActionFieldValue(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4,)
    namedValues = NamedValues(("egrNoTlv", 0), ("egrOK", 1), ("egrDown", 2), ("egrBlocked", 3), ("egrVid", 4),)

class Dot1agCfmRemoteMepState(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("rMepIdle", 1), ("rMepStart", 2), ("rMepFailed", 3), ("rMepOk", 4),)

class Dot1afCfmIndexIntegerNextFree(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)

class Dot1agCfmMepDefects(Bits, TextualConvention):
    namedValues = NamedValues(("bDefRDICCM", 0), ("bDefMACstatus", 1), ("bDefRemoteCCM", 2), ("bDefErrorCCM", 3), ("bDefXconCCM", 4),)

class Dot1agCfmConfigErrors(Bits, TextualConvention):
    namedValues = NamedValues(("cfmLeak", 0), ("conflictingVids", 1), ("excessiveLevels", 2), ("overlappedLevels", 3),)

class Dot1agCfmPbbComponentIdentifier(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)

dot1agCfmStackTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1), )
dot1agCfmStackEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmStackifIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmStackVlanIdOrNone"), (0, "IEEE8021-CFM-MIB", "dot1agCfmStackMdLevel"), (0, "IEEE8021-CFM-MIB", "dot1agCfmStackDirection"))
dot1agCfmStackifIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 1), InterfaceIndex())
dot1agCfmStackVlanIdOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 2), VlanIdOrNone())
dot1agCfmStackMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 3), Dot1agCfmMDLevel())
dot1agCfmStackDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 4), Dot1agCfmMpDirection())
dot1agCfmStackMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
dot1agCfmStackMaIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
dot1agCfmStackMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 7), Dot1agCfmMepIdOrZero()).setMaxAccess("readonly")
dot1agCfmStackMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
dot1agCfmVlanTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1), )
dot1agCfmVlanEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmVlanComponentId"), (0, "IEEE8021-CFM-MIB", "dot1agCfmVlanVid"))
dot1agCfmVlanComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 1), Dot1agCfmPbbComponentIdentifier())
dot1agCfmVlanVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 2), VlanId())
dot1agCfmVlanPrimaryVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 3), VlanId()).setMaxAccess("readcreate")
dot1agCfmVlanRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
dot1agCfmDefaultMdDefLevel = MibScalar((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 1), Dot1agCfmMDLevel()).setMaxAccess("readwrite")
dot1agCfmDefaultMdDefMhfCreation = MibScalar((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 2), Dot1agCfmMhfCreation().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3),)).clone('defMHFnone')).setMaxAccess("readwrite")
dot1agCfmDefaultMdDefIdPermission = MibScalar((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 3), Dot1agCfmIdPermission().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4,)).clone(namedValues=NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4),)).clone('sendIdNone')).setMaxAccess("readwrite")
dot1agCfmDefaultMdTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4), )
dot1agCfmDefaultMdEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmDefaultMdComponentId"), (0, "IEEE8021-CFM-MIB", "dot1agCfmDefaultMdPrimaryVid"))
dot1agCfmDefaultMdComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 1), Dot1agCfmPbbComponentIdentifier())
dot1agCfmDefaultMdPrimaryVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 2), VlanId())
dot1agCfmDefaultMdStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 3), TruthValue()).setMaxAccess("readonly")
dot1agCfmDefaultMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 4), Dot1agCfmMDLevelOrNone().clone(-1)).setMaxAccess("readwrite")
dot1agCfmDefaultMdMhfCreation = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 5), Dot1agCfmMhfCreation().clone('defMHFdefer')).setMaxAccess("readwrite")
dot1agCfmDefaultMdIdPermission = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 6), Dot1agCfmIdPermission().clone('sendIdDefer')).setMaxAccess("readwrite")
dot1agCfmConfigErrorListTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1), )
dot1agCfmConfigErrorListEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListVid"), (0, "IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListIfIndex"))
dot1agCfmConfigErrorListVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 1), VlanId())
dot1agCfmConfigErrorListIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 2), InterfaceIndex())
dot1agCfmConfigErrorListErrorType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 3), Dot1agCfmConfigErrors()).setMaxAccess("readonly")
dot1agCfmMdTableNextIndex = MibScalar((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 1), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
dot1agCfmMdTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2), )
dot1agCfmMdEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"))
dot1agCfmMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
dot1agCfmMdFormat = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 2), Dot1agCfmMaintDomainNameType().clone('charString')).setMaxAccess("readcreate")
dot1agCfmMdName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 3), Dot1agCfmMaintDomainName().clone('DEFAULT')).setMaxAccess("readcreate")
dot1agCfmMdMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 4), Dot1agCfmMDLevel()).setMaxAccess("readcreate")
dot1agCfmMdMhfCreation = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 5), Dot1agCfmMhfCreation().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3),)).clone('defMHFnone')).setMaxAccess("readcreate")
dot1agCfmMdMhfIdPermission = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 6), Dot1agCfmIdPermission().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4,)).clone(namedValues=NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4),)).clone('sendIdNone')).setMaxAccess("readcreate")
dot1agCfmMdMaNextIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 7), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
dot1agCfmMdRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
dot1agCfmMaNetTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1), )
dot1agCfmMaNetEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"))
dot1agCfmMaIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
dot1agCfmMaNetFormat = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 2), Dot1agCfmMaintAssocNameType()).setMaxAccess("readcreate")
dot1agCfmMaNetName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 3), Dot1agCfmMaintAssocName()).setMaxAccess("readcreate")
dot1agCfmMaNetCcmInterval = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 4), Dot1agCfmCcmInterval().clone('interval1s')).setMaxAccess("readcreate")
dot1agCfmMaNetRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
dot1agCfmMaCompTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2), )
dot1agCfmMaCompEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMaComponentId"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"))
dot1agCfmMaComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 1), Dot1agCfmPbbComponentIdentifier())
dot1agCfmMaCompPrimaryVlanId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 2), VlanIdOrNone()).setMaxAccess("readcreate")
dot1agCfmMaCompMhfCreation = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 3), Dot1agCfmMhfCreation().clone('defMHFdefer')).setMaxAccess("readcreate")
dot1agCfmMaCompIdPermission = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 4), Dot1agCfmIdPermission().clone('sendIdDefer')).setMaxAccess("readcreate")
dot1agCfmMaCompNumberOfVids = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
dot1agCfmMaCompRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
dot1agCfmMaMepListTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3), )
dot1agCfmMaMepListEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaMepListIdentifier"))
dot1agCfmMaMepListIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1, 1), Dot1agCfmMepId())
dot1agCfmMaMepListRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
dot1agCfmMepTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1), )
dot1agCfmMepEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
dot1agCfmMepIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 1), Dot1agCfmMepId())
dot1agCfmMepIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
dot1agCfmMepDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 3), Dot1agCfmMpDirection()).setMaxAccess("readcreate")
dot1agCfmMepPrimaryVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,16777215))).setMaxAccess("readcreate")
dot1agCfmMepActive = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
dot1agCfmMepFngState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 6), Dot1agCfmFngState().clone('fngReset')).setMaxAccess("readonly")
dot1agCfmMepCciEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
dot1agCfmMepCcmLtmPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,7))).setMaxAccess("readcreate")
dot1agCfmMepMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
dot1agCfmMepLowPrDef = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 10), Dot1agCfmLowestAlarmPri().clone('macRemErrXcon')).setMaxAccess("readcreate")
dot1agCfmMepFngAlarmTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 11), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(250,1000)).clone(250)).setMaxAccess("readcreate")
dot1agCfmMepFngResetTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 12), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(250,1000)).clone(1000)).setMaxAccess("readcreate")
dot1agCfmMepHighestPrDefect = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 13), Dot1agCfmHighestDefectPri()).setMaxAccess("readonly")
dot1agCfmMepDefects = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 14), Dot1agCfmMepDefects()).setMaxAccess("readonly")
dot1agCfmMepErrorCcmLastFailure = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1,1522))).setMaxAccess("readonly")
dot1agCfmMepXconCcmLastFailure = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1,1522))).setMaxAccess("readonly")
dot1agCfmMepCcmSequenceErrors = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 17), Counter32()).setMaxAccess("readonly")
dot1agCfmMepCciSentCcms = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 18), Counter32()).setMaxAccess("readonly")
dot1agCfmMepNextLbmTransId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
dot1agCfmMepLbrIn = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 20), Counter32()).setMaxAccess("readonly")
dot1agCfmMepLbrInOutOfOrder = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 21), Counter32()).setMaxAccess("readonly")
dot1agCfmMepLbrBadMsdu = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 22), Counter32()).setMaxAccess("readonly")
dot1agCfmMepLtmNextSeqNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
dot1agCfmMepUnexpLtrIn = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 24), Counter32()).setMaxAccess("readonly")
dot1agCfmMepLbrOut = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 25), Counter32()).setMaxAccess("readonly")
dot1agCfmMepTransmitLbmStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 26), TruthValue().clone('false')).setMaxAccess("readcreate")
dot1agCfmMepTransmitLbmDestMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 27), MacAddress()).setMaxAccess("readcreate")
dot1agCfmMepTransmitLbmDestMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 28), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
dot1agCfmMepTransmitLbmDestIsMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 29), TruthValue()).setMaxAccess("readcreate")
dot1agCfmMepTransmitLbmMessages = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,1024)).clone(1)).setMaxAccess("readcreate")
dot1agCfmMepTransmitLbmDataTlv = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 31), OctetString()).setMaxAccess("readcreate")
dot1agCfmMepTransmitLbmVlanPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,7))).setMaxAccess("readcreate")
dot1agCfmMepTransmitLbmVlanDropEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 33), TruthValue().clone('false')).setMaxAccess("readcreate")
dot1agCfmMepTransmitLbmResultOK = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 34), TruthValue().clone('true')).setMaxAccess("readonly")
dot1agCfmMepTransmitLbmSeqNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 35), Unsigned32()).setMaxAccess("readonly")
dot1agCfmMepTransmitLtmStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 36), TruthValue().clone('true')).setMaxAccess("readcreate")
dot1agCfmMepTransmitLtmFlags = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 37), Bits().clone(namedValues=NamedValues(("useFDBonly", 0),)).clone(namedValues=NamedValues(("useFDBonly", 0),))).setMaxAccess("readcreate")
dot1agCfmMepTransmitLtmTargetMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 38), MacAddress()).setMaxAccess("readcreate")
dot1agCfmMepTransmitLtmTargetMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 39), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
dot1agCfmMepTransmitLtmTargetIsMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 40), TruthValue()).setMaxAccess("readcreate")
dot1agCfmMepTransmitLtmTtl = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 41), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,255)).clone(64)).setMaxAccess("readcreate")
dot1agCfmMepTransmitLtmResult = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 42), TruthValue().clone('true')).setMaxAccess("readonly")
dot1agCfmMepTransmitLtmSeqNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 43), Unsigned32()).setMaxAccess("readonly")
dot1agCfmMepTransmitLtmEgressIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 44), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8,8)).setFixedLength(8)).setMaxAccess("readcreate")
dot1agCfmMepRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 45), RowStatus()).setMaxAccess("readcreate")
dot1agCfmMepPbbTeCanReportPbbTePresence = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 46), TruthValue().clone('false')).setMaxAccess("readcreate")
dot1agCfmMepPbbTeTrafficMismatchDefect = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 47), TruthValue()).setMaxAccess("readonly")
dot1agCfmMepPbbTransmitLbmLtmReverseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 48), IEEE8021VlanIndex()).setMaxAccess("readcreate")
dot1agCfmMepPbbTeMismatchAlarm = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 49), TruthValue().clone('false')).setMaxAccess("readcreate")
dot1agCfmMepPbbTeLocalMismatchDefect = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 50), TruthValue()).setMaxAccess("readonly")
dot1agCfmMepPbbTeMismatchSinceReset = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 51), TruthValue()).setMaxAccess("readonly")
dot1agCfmLtrTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2), )
dot1agCfmLtrEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "IEEE8021-CFM-MIB", "dot1agCfmLtrSeqNumber"), (0, "IEEE8021-CFM-MIB", "dot1agCfmLtrReceiveOrder"))
dot1agCfmLtrSeqNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,4294967295)))
dot1agCfmLtrReceiveOrder = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
dot1agCfmLtrTtl = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,255))).setMaxAccess("readonly")
dot1agCfmLtrForwarded = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
dot1agCfmLtrTerminalMep = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
dot1agCfmLtrLastEgressIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8,8)).setFixedLength(8)).setMaxAccess("readonly")
dot1agCfmLtrNextEgressIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8,8)).setFixedLength(8)).setMaxAccess("readonly")
dot1agCfmLtrRelay = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 8), Dot1agCfmRelayActionFieldValue()).setMaxAccess("readonly")
dot1agCfmLtrChassisIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 9), LldpChassisIdSubtype()).setMaxAccess("readonly")
dot1agCfmLtrChassisId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 10), LldpChassisId()).setMaxAccess("readonly")
dot1agCfmLtrManAddressDomain = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 11), TDomain()).setMaxAccess("readonly")
dot1agCfmLtrManAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 12), TAddress()).setMaxAccess("readonly")
dot1agCfmLtrIngress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 13), Dot1agCfmIngressActionFieldValue()).setMaxAccess("readonly")
dot1agCfmLtrIngressMac = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 14), MacAddress()).setMaxAccess("readonly")
dot1agCfmLtrIngressPortIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 15), LldpPortIdSubtype()).setMaxAccess("readonly")
dot1agCfmLtrIngressPortId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 16), LldpPortId()).setMaxAccess("readonly")
dot1agCfmLtrEgress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 17), Dot1agCfmEgressActionFieldValue()).setMaxAccess("readonly")
dot1agCfmLtrEgressMac = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 18), MacAddress()).setMaxAccess("readonly")
dot1agCfmLtrEgressPortIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 19), LldpPortIdSubtype()).setMaxAccess("readonly")
dot1agCfmLtrEgressPortId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 20), LldpPortId()).setMaxAccess("readonly")
dot1agCfmLtrOrganizationSpecificTlv = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 21), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,1500),))).setMaxAccess("readonly")
dot1agCfmMepDbTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3), )
dot1agCfmMepDbEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"))
dot1agCfmMepDbRMepIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 1), Dot1agCfmMepId())
dot1agCfmMepDbRMepState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 2), Dot1agCfmRemoteMepState()).setMaxAccess("readonly")
dot1agCfmMepDbRMepFailedOkTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
dot1agCfmMepDbMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
dot1agCfmMepDbRdi = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
dot1agCfmMepDbPortStatusTlv = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 6), Dot1agCfmPortStatus().clone('psNoPortStateTLV')).setMaxAccess("readonly")
dot1agCfmMepDbInterfaceStatusTlv = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 7), Dot1agCfmInterfaceStatus().clone('isNoInterfaceStatusTLV')).setMaxAccess("readonly")
dot1agCfmMepDbChassisIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 8), LldpChassisIdSubtype()).setMaxAccess("readonly")
dot1agCfmMepDbChassisId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 9), LldpChassisId()).setMaxAccess("readonly")
dot1agCfmMepDbManAddressDomain = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 10), TDomain()).setMaxAccess("readonly")
dot1agCfmMepDbManAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 11), TAddress()).setMaxAccess("readonly")
dot1agCfmMepDbRMepIsActive = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 12), TruthValue()).setMaxAccess("readwrite")
dot1agCfmFaultAlarm = NotificationType((1, 3, 111, 2, 802, 1, 1, 8, 0, 1)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmMepHighestPrDefect"),))
dot1agCfmCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 2, 1))
dot1agCfmGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 2, 2))
dot1agCfmStackGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 1)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmStackMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmStackMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmStackMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmStackMacAddress"),))
dot1agCfmDefaultMdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 2)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefLevel"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefIdPermission"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdLevel"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdIdPermission"),))
dot1agCfmVlanIdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 3)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmVlanPrimaryVid"), ("IEEE8021-CFM-MIB", "dot1agCfmVlanRowStatus"),))
dot1agCfmConfigErrorListGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 4)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListErrorType"),))
dot1agCfmMdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 5)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmMdTableNextIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMdName"), ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"), ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"), ("IEEE8021-CFM-MIB", "dot1agCfmMdMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmMdMhfIdPermission"), ("IEEE8021-CFM-MIB", "dot1agCfmMdMaNextIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMdRowStatus"),))
dot1agCfmMaGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 6)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetCcmInterval"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetRowStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompIdPermission"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompRowStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompNumberOfVids"), ("IEEE8021-CFM-MIB", "dot1agCfmMaMepListRowStatus"),))
dot1agCfmMepGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 7)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"), ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"), ("IEEE8021-CFM-MIB", "dot1agCfmMepActive"), ("IEEE8021-CFM-MIB", "dot1agCfmMepFngState"), ("IEEE8021-CFM-MIB", "dot1agCfmMepCciEnabled"), ("IEEE8021-CFM-MIB", "dot1agCfmMepCcmLtmPriority"), ("IEEE8021-CFM-MIB", "dot1agCfmMepMacAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLowPrDef"), ("IEEE8021-CFM-MIB", "dot1agCfmMepFngAlarmTime"), ("IEEE8021-CFM-MIB", "dot1agCfmMepFngResetTime"), ("IEEE8021-CFM-MIB", "dot1agCfmMepHighestPrDefect"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDefects"), ("IEEE8021-CFM-MIB", "dot1agCfmMepErrorCcmLastFailure"), ("IEEE8021-CFM-MIB", "dot1agCfmMepXconCcmLastFailure"), ("IEEE8021-CFM-MIB", "dot1agCfmMepCcmSequenceErrors"), ("IEEE8021-CFM-MIB", "dot1agCfmMepCciSentCcms"), ("IEEE8021-CFM-MIB", "dot1agCfmMepNextLbmTransId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrIn"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrInOutOfOrder"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrBadMsdu"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLtmNextSeqNumber"), ("IEEE8021-CFM-MIB", "dot1agCfmMepUnexpLtrIn"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrOut"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestMacAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestIsMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmMessages"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDataTlv"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmVlanPriority"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmVlanDropEnable"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmResultOK"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmSeqNumber"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmFlags"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMacAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetIsMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTtl"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmResult"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmSeqNumber"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmEgressIdentifier"), ("IEEE8021-CFM-MIB", "dot1agCfmMepRowStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrForwarded"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrRelay"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrChassisIdSubtype"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrChassisId"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrManAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrManAddressDomain"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngress"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressMac"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressPortIdSubtype"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressPortId"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgress"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressMac"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressPortIdSubtype"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressPortId"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrTerminalMep"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrLastEgressIdentifier"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrNextEgressIdentifier"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrTtl"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrOrganizationSpecificTlv"),))
dot1agCfmMepDbGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 8)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepState"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepFailedOkTime"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbMacAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRdi"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbPortStatusTlv"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbInterfaceStatusTlv"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbChassisIdSubtype"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbChassisId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbManAddressDomain"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbManAddress"),))
dot1agCfmNotificationsGroup = NotificationGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 9)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmFaultAlarm"),))
ieee8021CfmMaNetGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 10)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetCcmInterval"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetRowStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMaMepListRowStatus"),))
ieee8021CfmDefaultMdDefGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 11)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefLevel"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefIdPermission"),))
ieee8021CfmPbbTeExtensionGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 12)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIsActive"), ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTransmitLbmLtmReverseVid"),))
ieee8021CfmPbbTeTrafficBitGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 13)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmMepDbManAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeCanReportPbbTePresence"), ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeMismatchAlarm"), ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeTrafficMismatchDefect"), ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeLocalMismatchDefect"), ("IEEE8021-CFM-MIB", "dot1agCfmMepPbbTeMismatchSinceReset"),))
dot1agCfmCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 8, 2, 1, 1)).setObjects(*(("IEEE8021-CFM-MIB", "dot1agCfmStackGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMdGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMaGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMepGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmNotificationsGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmVlanIdGroup"),))
mibBuilder.exportSymbols("IEEE8021-CFM-MIB", Dot1agCfmPbbComponentIdentifier=Dot1agCfmPbbComponentIdentifier, ieee8021CfmPbbTeTrafficBitGroup=ieee8021CfmPbbTeTrafficBitGroup, dot1agCfmMepPbbTeMismatchSinceReset=dot1agCfmMepPbbTeMismatchSinceReset, dot1agCfmMepUnexpLtrIn=dot1agCfmMepUnexpLtrIn, dot1agCfmConfigErrorListEntry=dot1agCfmConfigErrorListEntry, dot1agCfmMepDbRMepFailedOkTime=dot1agCfmMepDbRMepFailedOkTime, Dot1agCfmMDLevelOrNone=Dot1agCfmMDLevelOrNone, Dot1agCfmRemoteMepState=Dot1agCfmRemoteMepState, dot1agCfmMepPbbTeTrafficMismatchDefect=dot1agCfmMepPbbTeTrafficMismatchDefect, dot1agCfmVlanRowStatus=dot1agCfmVlanRowStatus, dot1agCfmStackMepId=dot1agCfmStackMepId, dot1agCfmDefaultMdDefIdPermission=dot1agCfmDefaultMdDefIdPermission, dot1agCfmMepDbChassisId=dot1agCfmMepDbChassisId, dot1agCfmMepTransmitLbmStatus=dot1agCfmMepTransmitLbmStatus, dot1agCfmMepNextLbmTransId=dot1agCfmMepNextLbmTransId, dot1agCfmConfigErrorListTable=dot1agCfmConfigErrorListTable, dot1agCfmMepDbRMepIdentifier=dot1agCfmMepDbRMepIdentifier, dot1agCfmLtrEgressPortId=dot1agCfmLtrEgressPortId, dot1agCfmMepTransmitLbmVlanPriority=dot1agCfmMepTransmitLbmVlanPriority, Dot1agCfmMaintDomainName=Dot1agCfmMaintDomainName, dot1agCfmMaNetName=dot1agCfmMaNetName, dot1agCfmStackGroup=dot1agCfmStackGroup, dot1agCfmMepPrimaryVid=dot1agCfmMepPrimaryVid, dot1agCfmDefaultMdLevel=dot1agCfmDefaultMdLevel, dot1agCfmLtrLastEgressIdentifier=dot1agCfmLtrLastEgressIdentifier, dot1agCfmVlanTable=dot1agCfmVlanTable, dot1agCfmLtrIngress=dot1agCfmLtrIngress, dot1agCfmStackVlanIdOrNone=dot1agCfmStackVlanIdOrNone, ieee8021CfmDefaultMdDefGroup=ieee8021CfmDefaultMdDefGroup, Dot1agCfmHighestDefectPri=Dot1agCfmHighestDefectPri, dot1agCfmMdMhfIdPermission=dot1agCfmMdMhfIdPermission, dot1agCfmMepTransmitLbmDestMepId=dot1agCfmMepTransmitLbmDestMepId, dot1agCfmMaNetFormat=dot1agCfmMaNetFormat, dot1agCfmStackMdIndex=dot1agCfmStackMdIndex, dot1agCfmMdGroup=dot1agCfmMdGroup, dot1agCfmDefaultMdTable=dot1agCfmDefaultMdTable, dot1agCfmMepDbRMepIsActive=dot1agCfmMepDbRMepIsActive, dot1agCfmLtrRelay=dot1agCfmLtrRelay, dot1agCfmMepHighestPrDefect=dot1agCfmMepHighestPrDefect, dot1agCfmMaNetRowStatus=dot1agCfmMaNetRowStatus, dot1agCfmConfigErrorListVid=dot1agCfmConfigErrorListVid, Dot1agCfmIdPermission=Dot1agCfmIdPermission, Dot1agCfmMaintDomainNameType=Dot1agCfmMaintDomainNameType, dot1agCfmMepPbbTransmitLbmLtmReverseVid=dot1agCfmMepPbbTransmitLbmLtmReverseVid, dot1agCfmMepTransmitLtmTargetMacAddress=dot1agCfmMepTransmitLtmTargetMacAddress, dot1agCfmMepTransmitLtmTargetIsMepId=dot1agCfmMepTransmitLtmTargetIsMepId, dot1agCfmMepDbGroup=dot1agCfmMepDbGroup, dot1agCfmMdRowStatus=dot1agCfmMdRowStatus, dot1agCfmMepTransmitLbmVlanDropEnable=dot1agCfmMepTransmitLbmVlanDropEnable, dot1agCfmDefaultMd=dot1agCfmDefaultMd, dot1agCfmDefaultMdDefMhfCreation=dot1agCfmDefaultMdDefMhfCreation, dot1agCfmMepTransmitLtmEgressIdentifier=dot1agCfmMepTransmitLtmEgressIdentifier, dot1agCfmVlanIdGroup=dot1agCfmVlanIdGroup, dot1agCfmCompliance=dot1agCfmCompliance, Dot1afCfmIndexIntegerNextFree=Dot1afCfmIndexIntegerNextFree, Dot1agCfmPortStatus=Dot1agCfmPortStatus, dot1agCfmMepTransmitLbmMessages=dot1agCfmMepTransmitLbmMessages, dot1agMIBObjects=dot1agMIBObjects, dot1agCfmMepTransmitLbmDestMacAddress=dot1agCfmMepTransmitLbmDestMacAddress, dot1agCfmLtrSeqNumber=dot1agCfmLtrSeqNumber, dot1agCfmMepTransmitLbmDestIsMepId=dot1agCfmMepTransmitLbmDestIsMepId, Dot1agCfmMaintAssocNameType=Dot1agCfmMaintAssocNameType, dot1agCfmMep=dot1agCfmMep, dot1agCfmDefaultMdGroup=dot1agCfmDefaultMdGroup, ieee8021CfmMaNetGroup=ieee8021CfmMaNetGroup, dot1agCfmMepLowPrDef=dot1agCfmMepLowPrDef, dot1agCfmConfigErrorList=dot1agCfmConfigErrorList, dot1agCfmMa=dot1agCfmMa, Dot1agCfmLowestAlarmPri=Dot1agCfmLowestAlarmPri, Dot1agCfmIngressActionFieldValue=Dot1agCfmIngressActionFieldValue, dot1agCfmConfigErrorListErrorType=dot1agCfmConfigErrorListErrorType, dot1agCfmMepMacAddress=dot1agCfmMepMacAddress, dot1agCfmMepCciEnabled=dot1agCfmMepCciEnabled, PYSNMP_MODULE_ID=ieee8021CfmMib, dot1agCfmMaMepListEntry=dot1agCfmMaMepListEntry, Dot1agCfmMpDirection=Dot1agCfmMpDirection, dot1agCfmLtrNextEgressIdentifier=dot1agCfmLtrNextEgressIdentifier, dot1agCfmVlan=dot1agCfmVlan, dot1agCfmMepTransmitLtmTargetMepId=dot1agCfmMepTransmitLtmTargetMepId, dot1agCfmMd=dot1agCfmMd, dot1agCfmMaMepListIdentifier=dot1agCfmMaMepListIdentifier, dot1agCfmMepPbbTeLocalMismatchDefect=dot1agCfmMepPbbTeLocalMismatchDefect, Dot1agCfmMepIdOrZero=Dot1agCfmMepIdOrZero, dot1agCfmMaCompMhfCreation=dot1agCfmMaCompMhfCreation, dot1agCfmMaNetCcmInterval=dot1agCfmMaNetCcmInterval, dot1agCfmLtrReceiveOrder=dot1agCfmLtrReceiveOrder, Dot1agCfmConfigErrors=Dot1agCfmConfigErrors, dot1agCfmMepDbPortStatusTlv=dot1agCfmMepDbPortStatusTlv, dot1agCfmLtrEgressPortIdSubtype=dot1agCfmLtrEgressPortIdSubtype, dot1agCfmMaComponentId=dot1agCfmMaComponentId, dot1agCfmMaCompTable=dot1agCfmMaCompTable, dot1agCfmMepDirection=dot1agCfmMepDirection, dot1agCfmMepDbRdi=dot1agCfmMepDbRdi, dot1agCfmMepDbMacAddress=dot1agCfmMepDbMacAddress, dot1agCfmMdName=dot1agCfmMdName, dot1agCfmMepErrorCcmLastFailure=dot1agCfmMepErrorCcmLastFailure, dot1agCfmLtrIngressPortId=dot1agCfmLtrIngressPortId, dot1agCfmLtrTable=dot1agCfmLtrTable, dot1agCfmConformance=dot1agCfmConformance, dot1agCfmCompliances=dot1agCfmCompliances, dot1agCfmMepDbInterfaceStatusTlv=dot1agCfmMepDbInterfaceStatusTlv, dot1agCfmMaIndex=dot1agCfmMaIndex, dot1agCfmLtrForwarded=dot1agCfmLtrForwarded, dot1agCfmMepLbrOut=dot1agCfmMepLbrOut, dot1agCfmMepIfIndex=dot1agCfmMepIfIndex, dot1agCfmMaMepListRowStatus=dot1agCfmMaMepListRowStatus, ieee8021CfmMib=ieee8021CfmMib, dot1agCfmMepTransmitLtmFlags=dot1agCfmMepTransmitLtmFlags, dot1agCfmMepIdentifier=dot1agCfmMepIdentifier, Dot1agCfmMaintAssocName=Dot1agCfmMaintAssocName, dot1agCfmMepDbManAddressDomain=dot1agCfmMepDbManAddressDomain, Dot1agCfmInterfaceStatus=Dot1agCfmInterfaceStatus, Dot1agCfmEgressActionFieldValue=Dot1agCfmEgressActionFieldValue, dot1agCfmMaCompRowStatus=dot1agCfmMaCompRowStatus, Dot1agCfmRelayActionFieldValue=Dot1agCfmRelayActionFieldValue, dot1agCfmMaNetTable=dot1agCfmMaNetTable, dot1agCfmLtrEgressMac=dot1agCfmLtrEgressMac, Dot1agCfmMhfCreation=Dot1agCfmMhfCreation, dot1agCfmMepXconCcmLastFailure=dot1agCfmMepXconCcmLastFailure, dot1agCfmLtrIngressPortIdSubtype=dot1agCfmLtrIngressPortIdSubtype, dot1agCfmLtrTtl=dot1agCfmLtrTtl, dot1agCfmMepFngResetTime=dot1agCfmMepFngResetTime, dot1agCfmMepDbChassisIdSubtype=dot1agCfmMepDbChassisIdSubtype, dot1agCfmMepEntry=dot1agCfmMepEntry, dot1agCfmMepDefects=dot1agCfmMepDefects, dot1agCfmStackifIndex=dot1agCfmStackifIndex, dot1agCfmMepDbTable=dot1agCfmMepDbTable, ieee8021CfmPbbTeExtensionGroup=ieee8021CfmPbbTeExtensionGroup, dot1agCfmVlanEntry=dot1agCfmVlanEntry, dot1agCfmLtrManAddress=dot1agCfmLtrManAddress, dot1agCfmMaCompPrimaryVlanId=dot1agCfmMaCompPrimaryVlanId, Dot1agCfmFngState=Dot1agCfmFngState, dot1agCfmMepTable=dot1agCfmMepTable, dot1agCfmMepTransmitLtmSeqNumber=dot1agCfmMepTransmitLtmSeqNumber, dot1agCfmMepLbrBadMsdu=dot1agCfmMepLbrBadMsdu, dot1agCfmMdTableNextIndex=dot1agCfmMdTableNextIndex, dot1agCfmMepActive=dot1agCfmMepActive, dot1agCfmStackTable=dot1agCfmStackTable, dot1agCfmMdIndex=dot1agCfmMdIndex, dot1agCfmConfigErrorListGroup=dot1agCfmConfigErrorListGroup, Dot1agCfmMepDefects=Dot1agCfmMepDefects, dot1agCfmMepCciSentCcms=dot1agCfmMepCciSentCcms, Dot1agCfmMepId=Dot1agCfmMepId, dot1agCfmStackMdLevel=dot1agCfmStackMdLevel, Dot1agCfmMDLevel=Dot1agCfmMDLevel, dot1agCfmMepFngState=dot1agCfmMepFngState, dot1agCfmMaGroup=dot1agCfmMaGroup, dot1agCfmMepPbbTeCanReportPbbTePresence=dot1agCfmMepPbbTeCanReportPbbTePresence, dot1agCfmNotificationsGroup=dot1agCfmNotificationsGroup, dot1agCfmDefaultMdDefLevel=dot1agCfmDefaultMdDefLevel, dot1agCfmDefaultMdPrimaryVid=dot1agCfmDefaultMdPrimaryVid, dot1agCfmMdFormat=dot1agCfmMdFormat, dot1agCfmLtrEgress=dot1agCfmLtrEgress, dot1agCfmMepPbbTeMismatchAlarm=dot1agCfmMepPbbTeMismatchAlarm, dot1agCfmMepCcmLtmPriority=dot1agCfmMepCcmLtmPriority, Dot1agCfmCcmInterval=Dot1agCfmCcmInterval, dot1agCfmLtrChassisIdSubtype=dot1agCfmLtrChassisIdSubtype, dot1agCfmDefaultMdIdPermission=dot1agCfmDefaultMdIdPermission, dot1agCfmStackMacAddress=dot1agCfmStackMacAddress, dot1agCfmMepTransmitLbmResultOK=dot1agCfmMepTransmitLbmResultOK, dot1agCfmMepLtmNextSeqNumber=dot1agCfmMepLtmNextSeqNumber, dot1agCfmStackDirection=dot1agCfmStackDirection, dot1agCfmMepDbManAddress=dot1agCfmMepDbManAddress, dot1agCfmStackMaIndex=dot1agCfmStackMaIndex, dot1agCfmFaultAlarm=dot1agCfmFaultAlarm, dot1agCfmMepDbEntry=dot1agCfmMepDbEntry, dot1agCfmStack=dot1agCfmStack, dot1agCfmStackEntry=dot1agCfmStackEntry, dot1agCfmMdMhfCreation=dot1agCfmMdMhfCreation, dot1agCfmGroups=dot1agCfmGroups, dot1agCfmVlanPrimaryVid=dot1agCfmVlanPrimaryVid, dot1agCfmMepRowStatus=dot1agCfmMepRowStatus, dot1agNotifications=dot1agNotifications, dot1agCfmMepFngAlarmTime=dot1agCfmMepFngAlarmTime, dot1agCfmMdMaNextIndex=dot1agCfmMdMaNextIndex, dot1agCfmLtrIngressMac=dot1agCfmLtrIngressMac, dot1agCfmMepLbrInOutOfOrder=dot1agCfmMepLbrInOutOfOrder, dot1agCfmVlanVid=dot1agCfmVlanVid, dot1agCfmDefaultMdMhfCreation=dot1agCfmDefaultMdMhfCreation, dot1agCfmMepTransmitLtmTtl=dot1agCfmMepTransmitLtmTtl, dot1agCfmMepCcmSequenceErrors=dot1agCfmMepCcmSequenceErrors, dot1agCfmLtrOrganizationSpecificTlv=dot1agCfmLtrOrganizationSpecificTlv, dot1agCfmMepDbRMepState=dot1agCfmMepDbRMepState, dot1agCfmMepLbrIn=dot1agCfmMepLbrIn, dot1agCfmDefaultMdStatus=dot1agCfmDefaultMdStatus, dot1agCfmMepGroup=dot1agCfmMepGroup, dot1agCfmMepTransmitLbmDataTlv=dot1agCfmMepTransmitLbmDataTlv, dot1agCfmMaCompNumberOfVids=dot1agCfmMaCompNumberOfVids, dot1agCfmConfigErrorListIfIndex=dot1agCfmConfigErrorListIfIndex, dot1agCfmMepTransmitLbmSeqNumber=dot1agCfmMepTransmitLbmSeqNumber, dot1agCfmMaNetEntry=dot1agCfmMaNetEntry, dot1agCfmMaMepListTable=dot1agCfmMaMepListTable, dot1agCfmMdTable=dot1agCfmMdTable, dot1agCfmMdMdLevel=dot1agCfmMdMdLevel, dot1agCfmDefaultMdComponentId=dot1agCfmDefaultMdComponentId, dot1agCfmMepTransmitLtmStatus=dot1agCfmMepTransmitLtmStatus, dot1agCfmLtrTerminalMep=dot1agCfmLtrTerminalMep, dot1agCfmLtrChassisId=dot1agCfmLtrChassisId, dot1agCfmVlanComponentId=dot1agCfmVlanComponentId, dot1agCfmLtrEntry=dot1agCfmLtrEntry, dot1agCfmMaCompEntry=dot1agCfmMaCompEntry, dot1agCfmMaCompIdPermission=dot1agCfmMaCompIdPermission, dot1agCfmDefaultMdEntry=dot1agCfmDefaultMdEntry, dot1agCfmMepTransmitLtmResult=dot1agCfmMepTransmitLtmResult, dot1agCfmLtrManAddressDomain=dot1agCfmLtrManAddressDomain, dot1agCfmMdEntry=dot1agCfmMdEntry)
