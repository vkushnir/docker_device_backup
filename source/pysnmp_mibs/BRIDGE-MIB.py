#
# PySNMP MIB module BRIDGE-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/BRIDGE-MIB.txt
# Produced by pysmi-0.0.7 at Fri Feb 17 12:48:35 2017
# On host 5641388e757d platform Linux version 4.4.0-62-generic by user root
# Using Python version 2.7.13 (default, Dec 22 2016, 09:22:15) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, MacAddress, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
dot1dBridge = ModuleIdentity((1, 3, 6, 1, 2, 1, 17)).setRevisions(("2005-09-19 00:00", "1993-07-31 00:00", "1991-12-31 00:00",))
class BridgeId(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8

class Timeout(Integer32, TextualConvention):
    displayHint = 'd'

dot1dNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 0))
dot1dBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 1))
dot1dStp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 2))
dot1dSr = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 3))
dot1dTp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 4))
dot1dStatic = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 5))
dot1dConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 8))
dot1dBaseBridgeAddress = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 1), MacAddress()).setMaxAccess("readonly")
dot1dBaseNumPorts = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 2), Integer32()).setUnits('ports').setMaxAccess("readonly")
dot1dBaseType = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4,)).clone(namedValues=NamedValues(("unknown", 1), ("transparent-only", 2), ("sourceroute-only", 3), ("srt", 4),))).setMaxAccess("readonly")
dot1dBasePortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 1, 4), )
dot1dBasePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 1, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
dot1dBasePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,65535))).setMaxAccess("readonly")
dot1dBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
dot1dBasePortCircuit = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
dot1dBasePortDelayExceededDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
dot1dBasePortMtuExceededDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
dot1dStpProtocolSpecification = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 1), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3),))).setMaxAccess("readonly")
dot1dStpPriority = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readwrite")
dot1dStpTimeSinceTopologyChange = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 3), TimeTicks()).setUnits('centi-seconds').setMaxAccess("readonly")
dot1dStpTopChanges = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 4), Counter32()).setMaxAccess("readonly")
dot1dStpDesignatedRoot = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 5), BridgeId()).setMaxAccess("readonly")
dot1dStpRootCost = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 6), Integer32()).setMaxAccess("readonly")
dot1dStpRootPort = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 7), Integer32()).setMaxAccess("readonly")
dot1dStpMaxAge = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 8), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
dot1dStpHelloTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 9), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
dot1dStpHoldTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 10), Integer32()).setUnits('centi-seconds').setMaxAccess("readonly")
dot1dStpForwardDelay = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 11), Timeout()).setUnits('centi-seconds').setMaxAccess("readonly")
dot1dStpBridgeMaxAge = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 12), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600,4000))).setUnits('centi-seconds').setMaxAccess("readwrite")
dot1dStpBridgeHelloTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 13), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100,1000))).setUnits('centi-seconds').setMaxAccess("readwrite")
dot1dStpBridgeForwardDelay = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 14), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400,3000))).setUnits('centi-seconds').setMaxAccess("readwrite")
dot1dStpPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 2, 15), )
dot1dStpPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 2, 15, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dStpPort"))
dot1dStpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,65535))).setMaxAccess("readonly")
dot1dStpPortPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,255))).setMaxAccess("readwrite")
dot1dStpPortState = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6,)).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6),))).setMaxAccess("readonly")
dot1dStpPortEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2),))).setMaxAccess("readwrite")
dot1dStpPortPathCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,65535))).setMaxAccess("readwrite")
dot1dStpPortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 6), BridgeId()).setMaxAccess("readonly")
dot1dStpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 7), Integer32()).setMaxAccess("readonly")
dot1dStpPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 8), BridgeId()).setMaxAccess("readonly")
dot1dStpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2,2)).setFixedLength(2)).setMaxAccess("readonly")
dot1dStpPortForwardTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 10), Counter32()).setMaxAccess("readonly")
dot1dStpPortPathCost32 = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,200000000))).setMaxAccess("readwrite")
dot1dTpLearnedEntryDiscards = MibScalar((1, 3, 6, 1, 2, 1, 17, 4, 1), Counter32()).setMaxAccess("readonly")
dot1dTpAgingTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10,1000000))).setUnits('seconds').setMaxAccess("readwrite")
dot1dTpFdbTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 3), )
dot1dTpFdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dTpFdbAddress"))
dot1dTpFdbAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
dot1dTpFdbPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
dot1dTpFdbStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5,)).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5),))).setMaxAccess("readonly")
dot1dTpPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 4), )
dot1dTpPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dTpPort"))
dot1dTpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,65535))).setMaxAccess("readonly")
dot1dTpPortMaxInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 2), Integer32()).setUnits('bytes').setMaxAccess("readonly")
dot1dTpPortInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 3), Counter32()).setUnits('frames').setMaxAccess("readonly")
dot1dTpPortOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 4), Counter32()).setUnits('frames').setMaxAccess("readonly")
dot1dTpPortInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 5), Counter32()).setUnits('frames').setMaxAccess("readonly")
dot1dStaticTable = MibTable((1, 3, 6, 1, 2, 1, 17, 5, 1), )
dot1dStaticEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 5, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dStaticAddress"), (0, "BRIDGE-MIB", "dot1dStaticReceivePort"))
dot1dStaticAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 1), MacAddress()).setMaxAccess("readcreate")
dot1dStaticReceivePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readcreate")
dot1dStaticAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,512))).setMaxAccess("readcreate")
dot1dStaticStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5,)).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5),))).setMaxAccess("readcreate")
newRoot = NotificationType((1, 3, 6, 1, 2, 1, 17, 0, 1)).setObjects(*())
topologyChange = NotificationType((1, 3, 6, 1, 2, 1, 17, 0, 2)).setObjects(*())
dot1dGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 8, 1))
dot1dCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 8, 2))
dot1dBaseBridgeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 1)).setObjects(*(("BRIDGE-MIB", "dot1dBaseBridgeAddress"), ("BRIDGE-MIB", "dot1dBaseNumPorts"), ("BRIDGE-MIB", "dot1dBaseType"),))
dot1dBasePortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 2)).setObjects(*(("BRIDGE-MIB", "dot1dBasePort"), ("BRIDGE-MIB", "dot1dBasePortIfIndex"), ("BRIDGE-MIB", "dot1dBasePortCircuit"), ("BRIDGE-MIB", "dot1dBasePortDelayExceededDiscards"), ("BRIDGE-MIB", "dot1dBasePortMtuExceededDiscards"),))
dot1dStpBridgeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 3)).setObjects(*(("BRIDGE-MIB", "dot1dStpProtocolSpecification"), ("BRIDGE-MIB", "dot1dStpPriority"), ("BRIDGE-MIB", "dot1dStpTimeSinceTopologyChange"), ("BRIDGE-MIB", "dot1dStpTopChanges"), ("BRIDGE-MIB", "dot1dStpDesignatedRoot"), ("BRIDGE-MIB", "dot1dStpRootCost"), ("BRIDGE-MIB", "dot1dStpRootPort"), ("BRIDGE-MIB", "dot1dStpMaxAge"), ("BRIDGE-MIB", "dot1dStpHelloTime"), ("BRIDGE-MIB", "dot1dStpHoldTime"), ("BRIDGE-MIB", "dot1dStpForwardDelay"), ("BRIDGE-MIB", "dot1dStpBridgeMaxAge"), ("BRIDGE-MIB", "dot1dStpBridgeHelloTime"), ("BRIDGE-MIB", "dot1dStpBridgeForwardDelay"),))
dot1dStpPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 4)).setObjects(*(("BRIDGE-MIB", "dot1dStpPort"), ("BRIDGE-MIB", "dot1dStpPortPriority"), ("BRIDGE-MIB", "dot1dStpPortState"), ("BRIDGE-MIB", "dot1dStpPortEnable"), ("BRIDGE-MIB", "dot1dStpPortPathCost"), ("BRIDGE-MIB", "dot1dStpPortDesignatedRoot"), ("BRIDGE-MIB", "dot1dStpPortDesignatedCost"), ("BRIDGE-MIB", "dot1dStpPortDesignatedBridge"), ("BRIDGE-MIB", "dot1dStpPortDesignatedPort"), ("BRIDGE-MIB", "dot1dStpPortForwardTransitions"),))
dot1dStpPortGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 5)).setObjects(*(("BRIDGE-MIB", "dot1dStpPort"), ("BRIDGE-MIB", "dot1dStpPortPriority"), ("BRIDGE-MIB", "dot1dStpPortState"), ("BRIDGE-MIB", "dot1dStpPortEnable"), ("BRIDGE-MIB", "dot1dStpPortDesignatedRoot"), ("BRIDGE-MIB", "dot1dStpPortDesignatedCost"), ("BRIDGE-MIB", "dot1dStpPortDesignatedBridge"), ("BRIDGE-MIB", "dot1dStpPortDesignatedPort"), ("BRIDGE-MIB", "dot1dStpPortForwardTransitions"), ("BRIDGE-MIB", "dot1dStpPortPathCost32"),))
dot1dStpPortGroup3 = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 6)).setObjects(*(("BRIDGE-MIB", "dot1dStpPortPathCost32"),))
dot1dTpBridgeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 7)).setObjects(*(("BRIDGE-MIB", "dot1dTpLearnedEntryDiscards"), ("BRIDGE-MIB", "dot1dTpAgingTime"),))
dot1dTpFdbGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 8)).setObjects(*(("BRIDGE-MIB", "dot1dTpFdbAddress"), ("BRIDGE-MIB", "dot1dTpFdbPort"), ("BRIDGE-MIB", "dot1dTpFdbStatus"),))
dot1dTpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 9)).setObjects(*(("BRIDGE-MIB", "dot1dTpPort"), ("BRIDGE-MIB", "dot1dTpPortMaxInfo"), ("BRIDGE-MIB", "dot1dTpPortInFrames"), ("BRIDGE-MIB", "dot1dTpPortOutFrames"), ("BRIDGE-MIB", "dot1dTpPortInDiscards"),))
dot1dStaticGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 10)).setObjects(*(("BRIDGE-MIB", "dot1dStaticAddress"), ("BRIDGE-MIB", "dot1dStaticReceivePort"), ("BRIDGE-MIB", "dot1dStaticAllowedToGoTo"), ("BRIDGE-MIB", "dot1dStaticStatus"),))
dot1dNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 17, 8, 1, 11)).setObjects(*(("BRIDGE-MIB", "newRoot"), ("BRIDGE-MIB", "topologyChange"),))
bridgeCompliance1493 = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 8, 2, 1)).setObjects(*(("BRIDGE-MIB", "dot1dBaseBridgeGroup"), ("BRIDGE-MIB", "dot1dBasePortGroup"), ("BRIDGE-MIB", "dot1dStpBridgeGroup"), ("BRIDGE-MIB", "dot1dStpPortGroup"), ("BRIDGE-MIB", "dot1dTpBridgeGroup"), ("BRIDGE-MIB", "dot1dTpFdbGroup"), ("BRIDGE-MIB", "dot1dTpGroup"), ("BRIDGE-MIB", "dot1dStaticGroup"), ("BRIDGE-MIB", "dot1dNotificationGroup"),))
bridgeCompliance4188 = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 8, 2, 2)).setObjects(*(("BRIDGE-MIB", "dot1dBaseBridgeGroup"), ("BRIDGE-MIB", "dot1dBasePortGroup"), ("BRIDGE-MIB", "dot1dStpBridgeGroup"), ("BRIDGE-MIB", "dot1dStpPortGroup2"), ("BRIDGE-MIB", "dot1dStpPortGroup3"), ("BRIDGE-MIB", "dot1dTpBridgeGroup"), ("BRIDGE-MIB", "dot1dTpFdbGroup"), ("BRIDGE-MIB", "dot1dTpGroup"), ("BRIDGE-MIB", "dot1dStaticGroup"), ("BRIDGE-MIB", "dot1dNotificationGroup"),))
mibBuilder.exportSymbols("BRIDGE-MIB", dot1dStpPortTable=dot1dStpPortTable, dot1dStpPort=dot1dStpPort, dot1dTpPortInDiscards=dot1dTpPortInDiscards, PYSNMP_MODULE_ID=dot1dBridge, dot1dStaticStatus=dot1dStaticStatus, newRoot=newRoot, dot1dStpPortDesignatedRoot=dot1dStpPortDesignatedRoot, dot1dTpFdbEntry=dot1dTpFdbEntry, dot1dStpRootPort=dot1dStpRootPort, dot1dTpAgingTime=dot1dTpAgingTime, dot1dTpLearnedEntryDiscards=dot1dTpLearnedEntryDiscards, dot1dStpMaxAge=dot1dStpMaxAge, dot1dStaticEntry=dot1dStaticEntry, dot1dStaticAllowedToGoTo=dot1dStaticAllowedToGoTo, dot1dBasePortCircuit=dot1dBasePortCircuit, dot1dTpBridgeGroup=dot1dTpBridgeGroup, dot1dStpHoldTime=dot1dStpHoldTime, dot1dTpPortEntry=dot1dTpPortEntry, dot1dTpFdbTable=dot1dTpFdbTable, dot1dStaticTable=dot1dStaticTable, dot1dStpPortPriority=dot1dStpPortPriority, topologyChange=topologyChange, dot1dStpHelloTime=dot1dStpHelloTime, bridgeCompliance1493=bridgeCompliance1493, bridgeCompliance4188=bridgeCompliance4188, dot1dStaticReceivePort=dot1dStaticReceivePort, dot1dStatic=dot1dStatic, dot1dStpPortGroup=dot1dStpPortGroup, dot1dConformance=dot1dConformance, dot1dTpFdbStatus=dot1dTpFdbStatus, dot1dTpFdbPort=dot1dTpFdbPort, dot1dSr=dot1dSr, dot1dCompliances=dot1dCompliances, dot1dStpPortDesignatedCost=dot1dStpPortDesignatedCost, dot1dBasePort=dot1dBasePort, dot1dTpGroup=dot1dTpGroup, dot1dGroups=dot1dGroups, dot1dStpPortEntry=dot1dStpPortEntry, dot1dStpPortPathCost=dot1dStpPortPathCost, dot1dBasePortDelayExceededDiscards=dot1dBasePortDelayExceededDiscards, dot1dTpPortInFrames=dot1dTpPortInFrames, dot1dStpPortGroup2=dot1dStpPortGroup2, dot1dStpPortPathCost32=dot1dStpPortPathCost32, dot1dBasePortEntry=dot1dBasePortEntry, dot1dStpPortEnable=dot1dStpPortEnable, dot1dStpPortGroup3=dot1dStpPortGroup3, dot1dStpBridgeHelloTime=dot1dStpBridgeHelloTime, dot1dStaticGroup=dot1dStaticGroup, dot1dTpPortOutFrames=dot1dTpPortOutFrames, BridgeId=BridgeId, dot1dNotificationGroup=dot1dNotificationGroup, dot1dStpPortDesignatedPort=dot1dStpPortDesignatedPort, dot1dBasePortGroup=dot1dBasePortGroup, dot1dBasePortTable=dot1dBasePortTable, dot1dStpBridgeMaxAge=dot1dStpBridgeMaxAge, dot1dStpRootCost=dot1dStpRootCost, dot1dTpFdbAddress=dot1dTpFdbAddress, dot1dTpFdbGroup=dot1dTpFdbGroup, dot1dBase=dot1dBase, dot1dTpPortTable=dot1dTpPortTable, dot1dStpTopChanges=dot1dStpTopChanges, dot1dStpBridgeForwardDelay=dot1dStpBridgeForwardDelay, dot1dTpPortMaxInfo=dot1dTpPortMaxInfo, dot1dStpPortState=dot1dStpPortState, dot1dStaticAddress=dot1dStaticAddress, dot1dStpPortForwardTransitions=dot1dStpPortForwardTransitions, dot1dBaseBridgeGroup=dot1dBaseBridgeGroup, dot1dStpTimeSinceTopologyChange=dot1dStpTimeSinceTopologyChange, dot1dTpPort=dot1dTpPort, dot1dBaseNumPorts=dot1dBaseNumPorts, dot1dBasePortIfIndex=dot1dBasePortIfIndex, dot1dStp=dot1dStp, dot1dStpBridgeGroup=dot1dStpBridgeGroup, dot1dBaseType=dot1dBaseType, dot1dStpPriority=dot1dStpPriority, dot1dBasePortMtuExceededDiscards=dot1dBasePortMtuExceededDiscards, Timeout=Timeout, dot1dTp=dot1dTp, dot1dStpDesignatedRoot=dot1dStpDesignatedRoot, dot1dNotifications=dot1dNotifications, dot1dBaseBridgeAddress=dot1dBaseBridgeAddress, dot1dBridge=dot1dBridge, dot1dStpProtocolSpecification=dot1dStpProtocolSpecification, dot1dStpForwardDelay=dot1dStpForwardDelay, dot1dStpPortDesignatedBridge=dot1dStpPortDesignatedBridge)
