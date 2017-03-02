#
# PySNMP MIB module CISCO-ST-TC (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-ST-TC
# Produced by pysmi-0.0.7 at Tue Feb  7 11:41:27 2017
# On host e436de1e4e9d platform Linux version 4.4.0-59-generic by user root
# Using Python version 2.7.13 (default, Dec 22 2016, 09:22:15) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ciscoModules, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
storageTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 4)).setRevisions(("2008-05-16 00:00", "2005-12-17 00:00", "2004-05-18 00:00", "2003-09-26 00:00", "2003-08-07 00:00", "2002-10-04 00:00", "2002-09-24 00:00",))
class VsanIndex(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,4094)

class DomainId(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,239)

class DomainIdOrZero(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,239)

class FcAddressId(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(3,3)
    fixedLength = 3

class FcNameId(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8

class FcNameIdOrZero(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),)
class FcClassOfServices(Bits, TextualConvention):
    namedValues = NamedValues(("classF", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6),)

class FcPortTypes(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,)
    namedValues = NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("bPort", 5), ("fxPort", 6), ("sdPort", 7), ("tlPort", 8), ("nPort", 9), ("nlPort", 10), ("nxPort", 11), ("tePort", 12), ("fvPort", 13), ("portOperDown", 14), ("stPort", 15), ("npPort", 16), ("tfPort", 17), ("tnpPort", 18),)

class FcPortTxTypes(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,)
    namedValues = NamedValues(("unknown", 1), ("longWaveLaser", 2), ("shortWaveLaser", 3), ("longWaveLaserCostReduced", 4), ("electrical", 5), ("tenGigBaseSr", 6), ("tenGigBaseLr", 7), ("tenGigBaseEr", 8), ("tenGigBaseLx4", 9), ("tenGigBaseSw", 10), ("tenGigBaseLw", 11), ("tenGigBaseEw", 12),)

class FcPortModuleTypes(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,)
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("gbic", 3), ("embedded", 4), ("glm", 5), ("gbicWithSerialID", 6), ("gbicWithoutSerialID", 7), ("sfpWithSerialID", 8), ("sfpWithoutSerialID", 9), ("xfp", 10), ("x2Short", 11), ("x2Medium", 12), ("x2Tall", 13), ("xpakShort", 14), ("xpakMedium", 15), ("xpakTall", 16), ("xenpak", 17), ("sfpDwdm", 18), ("qsfp", 19), ("x2Dwdm", 20),)

class FcIfSpeed(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5,)
    namedValues = NamedValues(("auto", 1), ("oneG", 2), ("twoG", 3), ("fourG", 4), ("autoMaxTwoG", 5),)

class PortMemberList(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,64)

class FcAddress(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(3,3),ValueSizeConstraint(8,8),)
class FcAddressType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("wwn", 1), ("fcid", 2),)

class InterfaceOperMode(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,)
    namedValues = NamedValues(("auto", 1), ("fPort", 2), ("flPort", 3), ("ePort", 4), ("bPort", 5), ("fxPort", 6), ("sdPort", 7), ("tlPort", 8), ("nPort", 9), ("nlPort", 10), ("nxPort", 11), ("tePort", 12), ("fvPort", 13), ("portOperDown", 14), ("stPort", 15), ("mgmtPort", 16), ("ipsPort", 17), ("evPort", 18), ("npPort", 19), ("tfPort", 20), ("tnpPort", 21),)

class FcIfServiceStateType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("inService", 1), ("outOfService", 2),)

class FcIfSfpDiagLevelType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4, 5, 6,)
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("lowWarning", 3), ("lowAlarm", 4), ("highWarning", 5), ("highAlarm", 6),)

mibBuilder.exportSymbols("CISCO-ST-TC", FcClassOfServices=FcClassOfServices, PYSNMP_MODULE_ID=storageTextualConventions, PortMemberList=PortMemberList, FcAddress=FcAddress, storageTextualConventions=storageTextualConventions, FcIfServiceStateType=FcIfServiceStateType, FcAddressType=FcAddressType, FcPortTypes=FcPortTypes, FcIfSpeed=FcIfSpeed, FcAddressId=FcAddressId, DomainId=DomainId, DomainIdOrZero=DomainIdOrZero, FcNameIdOrZero=FcNameIdOrZero, FcIfSfpDiagLevelType=FcIfSfpDiagLevelType, FcNameId=FcNameId, InterfaceOperMode=InterfaceOperMode, VsanIndex=VsanIndex, FcPortTxTypes=FcPortTxTypes, FcPortModuleTypes=FcPortModuleTypes)
