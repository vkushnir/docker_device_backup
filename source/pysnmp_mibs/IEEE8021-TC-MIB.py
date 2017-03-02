#
# PySNMP MIB module IEEE8021-TC-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/IEEE8021-TC-MIB
# Produced by pysmi-0.0.7 at Fri Feb 17 12:48:35 2017
# On host 5641388e757d platform Linux version 4.4.0-62-generic by user root
# Using Python version 2.7.13 (default, Dec 22 2016, 09:22:15) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, org, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "org", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ieee8021TcMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 1)).setRevisions(("2012-02-15 00:00", "2011-08-23 00:00", "2011-04-06 00:00", "2011-02-27 00:00", "2008-11-18 00:00", "2008-10-15 00:00",))
ieee802dot1mibs = MibIdentifier((1, 3, 111, 2, 802, 1, 1))
class IEEE8021PbbComponentIdentifier(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)

class IEEE8021PbbComponentIdentifierOrZero(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295),)
class IEEE8021PbbServiceIdentifier(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(256,16777214)

class IEEE8021PbbServiceIdentifierOrUnassigned(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(256,16777214),)
class IEEE8021PbbIngressEgress(Bits, TextualConvention):
    namedValues = NamedValues(("ingress", 0), ("egress", 1),)

class IEEE8021PriorityCodePoint(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("codePoint8p0d", 1), ("codePoint7p1d", 2), ("codePoint6p2d", 3), ("codePoint5p3d", 4),)

class IEEE8021BridgePortNumber(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,65535)

class IEEE8021BridgePortNumberOrZero(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,65535)

class IEEE8021BridgePortType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,)
    namedValues = NamedValues(("none", 1), ("customerVlanPort", 2), ("providerNetworkPort", 3), ("customerNetworkPort", 4), ("customerEdgePort", 5), ("customerBackbonePort", 6), ("virtualInstancePort", 7), ("dBridgePort", 8), ("remoteCustomerAccessPort", 9), ("stationFacingBridgePort", 10), ("uplinkAccessPort", 11), ("uplinkRelayPort", 12),)

class IEEE8021VlanIndex(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(4096,4294967295),)
class IEEE8021VlanIndexOrWildcard(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)

class IEEE8021MstIdentifier(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4094)

class IEEE8021ServiceSelectorType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("vlanId", 1), ("isid", 2), ("tesid", 3), ("segid", 4),)

class IEEE8021ServiceSelectorValueOrNone(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295),)
class IEEE8021ServiceSelectorValue(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)

class IEEE8021PortAcceptableFrameTypes(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("admitAll", 1), ("admitUntaggedAndPriority", 2), ("admitTagged", 3),)

class IEEE8021PriorityValue(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,7)

class IEEE8021PbbTeProtectionGroupId(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,429467295)

class IEEE8021PbbTeEsp(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(14,14)
    fixedLength = 14

class IEEE8021PbbTeTSidId(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,42947295)

class IEEE8021PbbTeProtectionGroupConfigAdmin(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5,)
    namedValues = NamedValues(("clear", 1), ("lockOutProtection", 2), ("forceSwitch", 3), ("manualSwitchToProtection", 4), ("manualSwitchToWorking", 5),)

class IEEE8021PbbTeProtectionGroupActiveRequests(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("noRequest", 1), ("loP", 2), ("fs", 3), ("pSFH", 4), ("wSFH", 5), ("manualSwitchToProtection", 6), ("manualSwitchToWorking", 7),)

class IEEE8021TeipsIpgid(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,429467295)

class IEEE8021TeipsSegid(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,42947295)

class IEEE8021TeipsSmpid(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(14,14)
    fixedLength = 14

class IEEE8021TeipsIpgConfigAdmin(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5,)
    namedValues = NamedValues(("clear", 1), ("lockOutProtection", 2), ("forceSwitch", 3), ("manualSwitchToProtection", 4), ("manualSwitchToWorking", 5),)

class IEEE8021TeipsIpgConfigActiveRequests(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7,)
    namedValues = NamedValues(("noRequest", 1), ("loP", 2), ("fs", 3), ("pSFH", 4), ("wSFH", 5), ("manualSwitchToProtection", 6), ("manualSwitchToWorking", 7),)

mibBuilder.exportSymbols("IEEE8021-TC-MIB", IEEE8021ServiceSelectorType=IEEE8021ServiceSelectorType, IEEE8021BridgePortNumberOrZero=IEEE8021BridgePortNumberOrZero, IEEE8021PbbComponentIdentifier=IEEE8021PbbComponentIdentifier, IEEE8021BridgePortNumber=IEEE8021BridgePortNumber, ieee8021TcMib=ieee8021TcMib, IEEE8021PriorityValue=IEEE8021PriorityValue, IEEE8021BridgePortType=IEEE8021BridgePortType, IEEE8021PbbComponentIdentifierOrZero=IEEE8021PbbComponentIdentifierOrZero, IEEE8021PbbTeProtectionGroupId=IEEE8021PbbTeProtectionGroupId, ieee802dot1mibs=ieee802dot1mibs, PYSNMP_MODULE_ID=ieee8021TcMib, IEEE8021PbbTeProtectionGroupActiveRequests=IEEE8021PbbTeProtectionGroupActiveRequests, IEEE8021TeipsIpgConfigAdmin=IEEE8021TeipsIpgConfigAdmin, IEEE8021TeipsSegid=IEEE8021TeipsSegid, IEEE8021VlanIndex=IEEE8021VlanIndex, IEEE8021TeipsSmpid=IEEE8021TeipsSmpid, IEEE8021PbbTeEsp=IEEE8021PbbTeEsp, IEEE8021PriorityCodePoint=IEEE8021PriorityCodePoint, IEEE8021TeipsIpgConfigActiveRequests=IEEE8021TeipsIpgConfigActiveRequests, IEEE8021TeipsIpgid=IEEE8021TeipsIpgid, IEEE8021PbbTeTSidId=IEEE8021PbbTeTSidId, IEEE8021ServiceSelectorValueOrNone=IEEE8021ServiceSelectorValueOrNone, IEEE8021VlanIndexOrWildcard=IEEE8021VlanIndexOrWildcard, IEEE8021PbbServiceIdentifierOrUnassigned=IEEE8021PbbServiceIdentifierOrUnassigned, IEEE8021PortAcceptableFrameTypes=IEEE8021PortAcceptableFrameTypes, IEEE8021MstIdentifier=IEEE8021MstIdentifier, IEEE8021PbbIngressEgress=IEEE8021PbbIngressEgress, IEEE8021PbbTeProtectionGroupConfigAdmin=IEEE8021PbbTeProtectionGroupConfigAdmin, IEEE8021PbbServiceIdentifier=IEEE8021PbbServiceIdentifier, IEEE8021ServiceSelectorValue=IEEE8021ServiceSelectorValue)
