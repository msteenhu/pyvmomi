# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******
from pyVmomi.VmomiSupport import CreateDataType, CreateManagedType, CreateEnumType, AddVersion, AddVersionParent, F_LINK, F_LINKABLE, F_OPTIONAL, F_SECRET
from pyVmomi.VmomiSupport import newestVersions, currentVersions, stableVersions, matureVersions, publicVersions, oldestVersions

AddVersion("pbm.version.version1", "pbm", "1.0", 0, "pbm")
AddVersion("pbm.version.version2", "pbm", "2.0", 0, "pbm")
AddVersion("vmodl.version.version2", "", "", 0, "vim25")
AddVersion("vmodl.version.version1", "", "", 0, "vim25")
AddVersion("vmodl.version.version0", "", "", 0, "vim25")
AddVersionParent("pbm.version.version1", "pbm.version.version1")
AddVersionParent("pbm.version.version1", "vmodl.version.version2")
AddVersionParent("pbm.version.version1", "vmodl.version.version1")
AddVersionParent("pbm.version.version1", "vmodl.version.version0")
AddVersionParent("pbm.version.version2", "pbm.version.version1")
AddVersionParent("pbm.version.version2", "pbm.version.version2")
AddVersionParent("pbm.version.version2", "vmodl.version.version2")
AddVersionParent("pbm.version.version2", "vmodl.version.version1")
AddVersionParent("pbm.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.version.version2", "vmodl.version.version2")
AddVersionParent("vmodl.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.version.version0", "vmodl.version.version0")

newestVersions.Add("pbm.version.version2")
currentVersions.Add("pbm.version.version2")
stableVersions.Add("pbm.version.version2")
matureVersions.Add("pbm.version.version2")
publicVersions.Add("pbm.version.version2")
oldestVersions.Add("pbm.version.version1")

CreateDataType("pbm.AboutInfo", "PbmAboutInfo", "vmodl.DynamicData", "pbm.version.version1", [("name", "string", "pbm.version.version1", 0), ("version", "string", "pbm.version.version1", 0), ("instanceUuid", "string", "pbm.version.version1", 0)])
CreateDataType("pbm.ExtendedElementDescription", "PbmExtendedElementDescription", "vmodl.DynamicData", "pbm.version.version1", [("label", "string", "pbm.version.version1", 0), ("summary", "string", "pbm.version.version1", 0), ("key", "string", "pbm.version.version1", 0), ("messageCatalogKeyPrefix", "string", "pbm.version.version1", 0), ("messageArg", "vmodl.KeyAnyValue[]", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.ServerObjectRef", "PbmServerObjectRef", "vmodl.DynamicData", "pbm.version.version1", [("objectType", "string", "pbm.version.version1", 0), ("key", "string", "pbm.version.version1", 0), ("serverUuid", "string", "pbm.version.version1", F_OPTIONAL)])
CreateEnumType("pbm.ServerObjectRef.VvolType", "PbmVvolType", "pbm.version.version1", ["Config", "Data", "Swap"])
CreateEnumType("pbm.ServerObjectRef.ObjectType", "PbmObjectType", "pbm.version.version1", ["virtualMachine", "virtualDiskId", "virtualDiskUUID", "datastore", "unknown"])
CreateManagedType("pbm.ServiceInstance", "PbmServiceInstance", "vmodl.ManagedObject", "pbm.version.version1", [("content", "pbm.ServiceInstanceContent", "pbm.version.version1", 0, "System.Anonymous")], [("retrieveContent", "PbmRetrieveServiceContent", "pbm.version.version1", (), (0, "pbm.ServiceInstanceContent", "pbm.ServiceInstanceContent"), "System.Anonymous", None)])
CreateDataType("pbm.ServiceInstanceContent", "PbmServiceInstanceContent", "vmodl.DynamicData", "pbm.version.version1", [("aboutInfo", "pbm.AboutInfo", "pbm.version.version1", 0), ("sessionManager", "pbm.auth.SessionManager", "pbm.version.version1", 0), ("capabilityMetadataManager", "pbm.capability.CapabilityMetadataManager", "pbm.version.version1", 0), ("profileManager", "pbm.profile.ProfileManager", "pbm.version.version1", 0), ("complianceManager", "pbm.compliance.ComplianceManager", "pbm.version.version1", 0), ("placementSolver", "pbm.placement.PlacementSolver", "pbm.version.version1", 0)])
CreateManagedType("pbm.auth.SessionManager", "PbmSessionManager", "vmodl.ManagedObject", "pbm.version.version1", None, None)
CreateDataType("pbm.capability.CapabilityMetadata", "PbmCapabilityMetadata", "vmodl.DynamicData", "pbm.version.version1", [("id", "pbm.capability.CapabilityMetadata.UniqueId", "pbm.version.version1", 0), ("summary", "pbm.ExtendedElementDescription", "pbm.version.version1", 0), ("mandatory", "boolean", "pbm.version.version1", F_OPTIONAL), ("hint", "boolean", "pbm.version.version1", F_OPTIONAL), ("keyId", "string", "pbm.version.version1", F_OPTIONAL), ("allowMultipleConstraints", "boolean", "pbm.version.version1", F_OPTIONAL), ("propertyMetadata", "pbm.capability.PropertyMetadata[]", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.CapabilityMetadata.UniqueId", "PbmCapabilityMetadataUniqueId", "vmodl.DynamicData", "pbm.version.version1", [("namespace", "string", "pbm.version.version1", 0), ("id", "string", "pbm.version.version1", 0)])
CreateManagedType("pbm.capability.CapabilityMetadataManager", "PbmCapabilityMetadataManager", "vmodl.ManagedObject", "pbm.version.version1", None, None)
CreateDataType("pbm.capability.ConstraintInstance", "PbmCapabilityConstraintInstance", "vmodl.DynamicData", "pbm.version.version1", [("propertyInstance", "pbm.capability.PropertyInstance[]", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.PropertyInstance", "PbmCapabilityPropertyInstance", "vmodl.DynamicData", "pbm.version.version1", [("id", "string", "pbm.version.version1", 0), ("value", "anyType", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.PropertyMetadata", "PbmCapabilityPropertyMetadata", "vmodl.DynamicData", "pbm.version.version1", [("id", "string", "pbm.version.version1", 0), ("summary", "pbm.ExtendedElementDescription", "pbm.version.version1", 0), ("mandatory", "boolean", "pbm.version.version1", 0), ("type", "pbm.capability.TypeInfo", "pbm.version.version1", F_OPTIONAL), ("defaultValue", "anyType", "pbm.version.version1", F_OPTIONAL), ("allowedValue", "anyType", "pbm.version.version1", F_OPTIONAL), ("requirementsTypeHint", "string", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.capability.TypeInfo", "PbmCapabilityTypeInfo", "vmodl.DynamicData", "pbm.version.version1", [("typeName", "string", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.provider.CapabilityObjectMetadataPerCategory", "PbmCapabilityMetadataPerCategory", "vmodl.DynamicData", "pbm.version.version1", [("subCategory", "string", "pbm.version.version1", 0), ("capabilityMetadata", "pbm.capability.CapabilityMetadata[]", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.provider.CapabilityObjectSchema", "PbmCapabilitySchema", "vmodl.DynamicData", "pbm.version.version1", [("vendorInfo", "pbm.capability.provider.CapabilityObjectSchema.VendorInfo", "pbm.version.version1", 0), ("namespaceInfo", "pbm.capability.provider.CapabilityObjectSchema.NamespaceInfo", "pbm.version.version1", 0), ("capabilityMetadataPerCategory", "pbm.capability.provider.CapabilityObjectMetadataPerCategory[]", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.provider.CapabilityObjectSchema.VendorInfo", "PbmCapabilitySchemaVendorInfo", "vmodl.DynamicData", "pbm.version.version1", [("vendorUuid", "string", "pbm.version.version1", 0), ("info", "pbm.ExtendedElementDescription", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.provider.CapabilityObjectSchema.NamespaceInfo", "PbmCapabilityNamespaceInfo", "vmodl.DynamicData", "pbm.version.version1", [("version", "string", "pbm.version.version1", 0), ("namespace", "string", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo", "PbmCapabilityVendorResourceTypeInfo", "vmodl.DynamicData", "pbm.version.version1", [("resourceType", "string", "pbm.version.version1", 0), ("vendorNamespaceInfo", "pbm.capability.provider.CapabilityObjectSchema.VendorNamespaceInfo[]", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.provider.CapabilityObjectSchema.VendorNamespaceInfo", "PbmCapabilityVendorNamespaceInfo", "vmodl.DynamicData", "pbm.version.version1", [("vendorInfo", "pbm.capability.provider.CapabilityObjectSchema.VendorInfo", "pbm.version.version1", 0), ("namespaceInfo", "pbm.capability.provider.CapabilityObjectSchema.NamespaceInfo", "pbm.version.version1", 0)])
CreateEnumType("pbm.capability.types.BuiltinGenericTypesEnum", "PbmBuiltinGenericType", "pbm.version.version1", ["VMW_RANGE", "VMW_SET"])
CreateEnumType("pbm.capability.types.BuiltinTypesEnum", "PbmBuiltinType", "pbm.version.version1", ["XSD_LONG", "XSD_SHORT", "XSD_INTEGER", "XSD_INT", "XSD_STRING", "XSD_BOOLEAN", "XSD_DOUBLE", "XSD_DATETIME", "VMW_TIMESPAN"])
CreateDataType("pbm.capability.types.DescriptiveValue", "PbmCapabilityDescription", "vmodl.DynamicData", "pbm.version.version1", [("description", "pbm.ExtendedElementDescription", "pbm.version.version1", 0), ("value", "anyType", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.types.DiscreteSet", "PbmCapabilityDiscreteSet", "vmodl.DynamicData", "pbm.version.version1", [("values", "anyType[]", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.types.Range", "PbmCapabilityRange", "vmodl.DynamicData", "pbm.version.version1", [("min", "anyType", "pbm.version.version1", 0), ("max", "anyType", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.types.TimeSpan", "PbmCapabilityTimeSpan", "vmodl.DynamicData", "pbm.version.version1", [("value", "int", "pbm.version.version1", 0), ("unit", "string", "pbm.version.version1", 0)])
CreateEnumType("pbm.capability.types.TimeUnitEnum", "PbmCapabilityTimeUnitType", "pbm.version.version1", ["SECONDS", "MINUTES", "HOURS", "DAYS", "WEEKS", "MONTHS", "YEARS"])
CreateManagedType("pbm.compliance.ComplianceManager", "PbmComplianceManager", "vmodl.ManagedObject", "pbm.version.version1", None, [("checkCompliance", "PbmCheckCompliance", "pbm.version.version1", (("entities", "pbm.ServerObjectRef[]", "pbm.version.version1", 0, None),("profile", "pbm.profile.ProfileId", "pbm.version.version1", F_OPTIONAL, None),), (F_OPTIONAL, "pbm.compliance.ComplianceResult[]", "pbm.compliance.ComplianceResult[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ]), ("fetchComplianceResult", "PbmFetchComplianceResult", "pbm.version.version1", (("entities", "pbm.ServerObjectRef[]", "pbm.version.version1", 0, None),("profile", "pbm.profile.ProfileId", "pbm.version.version1", F_OPTIONAL, None),), (F_OPTIONAL, "pbm.compliance.ComplianceResult[]", "pbm.compliance.ComplianceResult[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ]), ("checkRollupCompliance", "PbmCheckRollupCompliance", "pbm.version.version1", (("entity", "pbm.ServerObjectRef[]", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.compliance.RollupComplianceResult[]", "pbm.compliance.RollupComplianceResult[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ]), ("fetchRollupComplianceResult", "PbmFetchRollupComplianceResult", "pbm.version.version1", (("entity", "pbm.ServerObjectRef[]", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.compliance.RollupComplianceResult[]", "pbm.compliance.RollupComplianceResult[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ])])
CreateDataType("pbm.compliance.ComplianceResult", "PbmComplianceResult", "vmodl.DynamicData", "pbm.version.version1", [("checkTime", "vmodl.DateTime", "pbm.version.version1", 0), ("entity", "pbm.ServerObjectRef", "pbm.version.version1", 0), ("profile", "pbm.profile.ProfileId", "pbm.version.version1", F_OPTIONAL), ("complianceStatus", "string", "pbm.version.version1", 0), ("mismatch", "boolean", "pbm.version.version1", 0), ("violatedPolicies", "pbm.compliance.PolicyStatus[]", "pbm.version.version1", F_OPTIONAL), ("operationalStatus", "pbm.compliance.OperationalStatus", "pbm.version.version1", F_OPTIONAL)])
CreateEnumType("pbm.compliance.ComplianceResult.ComplianceStatus", "PbmComplianceStatus", "pbm.version.version1", ["compliant", "nonCompliant", "unknown", "notApplicable"])
CreateDataType("pbm.compliance.OperationalStatus", "PbmComplianceOperationalStatus", "vmodl.DynamicData", "pbm.version.version1", [("healthy", "boolean", "pbm.version.version1", F_OPTIONAL), ("operationETA", "vmodl.DateTime", "pbm.version.version1", F_OPTIONAL), ("operationProgress", "long", "pbm.version.version1", F_OPTIONAL), ("transitional", "boolean", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.compliance.PolicyStatus", "PbmCompliancePolicyStatus", "vmodl.DynamicData", "pbm.version.version1", [("expectedValue", "pbm.capability.CapabilityInstance", "pbm.version.version1", 0), ("currentValue", "pbm.capability.CapabilityInstance", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.compliance.RollupComplianceResult", "PbmRollupComplianceResult", "vmodl.DynamicData", "pbm.version.version1", [("oldestCheckTime", "vmodl.DateTime", "pbm.version.version1", 0), ("entity", "pbm.ServerObjectRef", "pbm.version.version1", 0), ("overallComplianceStatus", "string", "pbm.version.version1", 0), ("result", "pbm.compliance.ComplianceResult[]", "pbm.version.version1", F_OPTIONAL), ("profileMismatch", "boolean", "pbm.version.version1", 0)])
CreateDataType("pbm.fault.PBMFault", "PbmFault", "vmodl.MethodFault", "pbm.version.version1", None)
CreateDataType("pbm.fault.ProfileStorageFault", "PbmFaultProfileStorageFault", "pbm.fault.PBMFault", "pbm.version.version1", None)
CreateDataType("pbm.fault.ResourceInUse", "PbmResourceInUse", "pbm.fault.PBMFault", "pbm.version.version1", [("type", "vmodl.TypeName", "pbm.version.version1", F_OPTIONAL), ("name", "string", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.placement.CompatibilityResult", "PbmPlacementCompatibilityResult", "vmodl.DynamicData", "pbm.version.version1", [("hub", "pbm.placement.PlacementHub", "pbm.version.version1", 0), ("warning", "vmodl.MethodFault[]", "pbm.version.version1", F_OPTIONAL), ("error", "vmodl.MethodFault[]", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.placement.PlacementHub", "PbmPlacementHub", "vmodl.DynamicData", "pbm.version.version1", [("hubType", "string", "pbm.version.version1", 0), ("hubId", "string", "pbm.version.version1", 0)])
CreateManagedType("pbm.placement.PlacementSolver", "PbmPlacementSolver", "vmodl.ManagedObject", "pbm.version.version1", None, [("queryMatchingHub", "PbmQueryMatchingHub", "pbm.version.version1", (("hubsToSearch", "pbm.placement.PlacementHub[]", "pbm.version.version1", F_OPTIONAL, None),("profile", "pbm.profile.ProfileId", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.placement.PlacementHub[]", "pbm.placement.PlacementHub[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ]), ("queryMatchingHubWithSpec", "PbmQueryMatchingHubWithSpec", "pbm.version.version1", (("hubsToSearch", "pbm.placement.PlacementHub[]", "pbm.version.version1", F_OPTIONAL, None),("createSpec", "pbm.profile.CapabilityBasedProfileCreateSpec", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.placement.PlacementHub[]", "pbm.placement.PlacementHub[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ]), ("checkCompatibility", "PbmCheckCompatibility", "pbm.version.version1", (("hubsToSearch", "pbm.placement.PlacementHub[]", "pbm.version.version1", F_OPTIONAL, None),("profile", "pbm.profile.ProfileId", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.placement.CompatibilityResult[]", "pbm.placement.CompatibilityResult[]"), "StorageProfile.View", None), ("checkCompatibilityWithSpec", "PbmCheckCompatibilityWithSpec", "pbm.version.version1", (("hubsToSearch", "pbm.placement.PlacementHub[]", "pbm.version.version1", F_OPTIONAL, None),("profileSpec", "pbm.profile.CapabilityBasedProfileCreateSpec", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.placement.CompatibilityResult[]", "pbm.placement.CompatibilityResult[]"), "StorageProfile.View", None)])
CreateDataType("pbm.profile.CapabilityBasedProfileCreateSpec", "PbmCapabilityProfileCreateSpec", "vmodl.DynamicData", "pbm.version.version1", [("name", "string", "pbm.version.version1", 0), ("description", "string", "pbm.version.version1", F_OPTIONAL), ("resourceType", "pbm.profile.ResourceType", "pbm.version.version1", 0), ("constraints", "pbm.profile.CapabilityConstraints", "pbm.version.version1", 0)])
CreateDataType("pbm.profile.CapabilityBasedProfileUpdateSpec", "PbmCapabilityProfileUpdateSpec", "vmodl.DynamicData", "pbm.version.version1", [("name", "string", "pbm.version.version1", F_OPTIONAL), ("description", "string", "pbm.version.version1", F_OPTIONAL), ("constraints", "pbm.profile.CapabilityConstraints", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.profile.CapabilityConstraints", "PbmCapabilityConstraints", "vmodl.DynamicData", "pbm.version.version1", None)
CreateDataType("pbm.profile.DefaultProfileInfo", "PbmDefaultProfileInfo", "vmodl.DynamicData", "pbm.version.version2", [("datastores", "pbm.placement.PlacementHub[]", "pbm.version.version2", 0), ("defaultProfile", "pbm.profile.Profile", "pbm.version.version2", F_OPTIONAL)])
CreateEnumType("pbm.profile.IofilterInfo.FilterType", "PbmIofilterInfoFilterType", "pbm.version.version1", ["INSPECTION", "COMPRESSION", "ENCRYPTION", "REPLICATION", "CACHE"])
CreateDataType("pbm.profile.Profile", "PbmProfile", "vmodl.DynamicData", "pbm.version.version1", [("profileId", "pbm.profile.ProfileId", "pbm.version.version1", 0), ("name", "string", "pbm.version.version1", 0), ("description", "string", "pbm.version.version1", F_OPTIONAL), ("creationTime", "vmodl.DateTime", "pbm.version.version1", 0), ("createdBy", "string", "pbm.version.version1", 0), ("lastUpdatedTime", "vmodl.DateTime", "pbm.version.version1", 0), ("lastUpdatedBy", "string", "pbm.version.version1", 0)])
CreateDataType("pbm.profile.ProfileId", "PbmProfileId", "vmodl.DynamicData", "pbm.version.version1", [("uniqueId", "string", "pbm.version.version1", 0)])
CreateManagedType("pbm.profile.ProfileManager", "PbmProfileProfileManager", "vmodl.ManagedObject", "pbm.version.version1", None, [("fetchResourceType", "PbmFetchResourceType", "pbm.version.version1", (), (F_OPTIONAL, "pbm.profile.ResourceType[]", "pbm.profile.ResourceType[]"), "StorageProfile.View", None), ("fetchVendorInfo", "PbmFetchVendorInfo", "pbm.version.version1", (("resourceType", "pbm.profile.ResourceType", "pbm.version.version1", F_OPTIONAL, None),), (F_OPTIONAL, "pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo[]", "pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo[]"), "StorageProfile.View", None), ("fetchCapabilityMetadata", "PbmFetchCapabilityMetadata", "pbm.version.version1", (("resourceType", "pbm.profile.ResourceType", "pbm.version.version1", F_OPTIONAL, None),("vendorUuid", "string", "pbm.version.version1", F_OPTIONAL, None),), (F_OPTIONAL, "pbm.capability.provider.CapabilityObjectMetadataPerCategory[]", "pbm.capability.provider.CapabilityObjectMetadataPerCategory[]"), "StorageProfile.View", None), ("create", "PbmCreate", "pbm.version.version1", (("createSpec", "pbm.profile.CapabilityBasedProfileCreateSpec", "pbm.version.version1", 0, None),), (0, "pbm.profile.ProfileId", "pbm.profile.ProfileId"), "StorageProfile.Update", ["vmodl.fault.InvalidArgument", "pbm.fault.ProfileStorageFault", "pbm.fault.DuplicateName", ]), ("update", "PbmUpdate", "pbm.version.version1", (("profileId", "pbm.profile.ProfileId", "pbm.version.version1", 0, None),("updateSpec", "pbm.profile.CapabilityBasedProfileUpdateSpec", "pbm.version.version1", 0, None),), (0, "void", "void"), "StorageProfile.Update", ["vmodl.fault.InvalidArgument", "pbm.fault.ProfileStorageFault", ]), ("delete", "PbmDelete", "pbm.version.version1", (("profileId", "pbm.profile.ProfileId[]", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.profile.ProfileOperationOutcome[]", "pbm.profile.ProfileOperationOutcome[]"), "StorageProfile.Update", None), ("queryProfile", "PbmQueryProfile", "pbm.version.version1", (("resourceType", "pbm.profile.ResourceType", "pbm.version.version1", 0, None),("profileCategory", "string", "pbm.version.version1", F_OPTIONAL, None),), (F_OPTIONAL, "pbm.profile.ProfileId[]", "pbm.profile.ProfileId[]"), "StorageProfile.View", ["vmodl.fault.InvalidArgument", ]), ("retrieveContent", "PbmRetrieveContent", "pbm.version.version1", (("profileIds", "pbm.profile.ProfileId[]", "pbm.version.version1", 0, None),), (0, "pbm.profile.Profile[]", "pbm.profile.Profile[]"), "StorageProfile.View", ["vmodl.fault.InvalidArgument", ]), ("queryAssociatedProfiles", "PbmQueryAssociatedProfiles", "pbm.version.version1", (("entities", "pbm.ServerObjectRef[]", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.profile.QueryProfileResult[]", "pbm.profile.QueryProfileResult[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ]), ("queryAssociatedProfile", "PbmQueryAssociatedProfile", "pbm.version.version1", (("entity", "pbm.ServerObjectRef", "pbm.version.version1", 0, None),), (F_OPTIONAL, "pbm.profile.ProfileId[]", "pbm.profile.ProfileId[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ]), ("queryAssociatedEntity", "PbmQueryAssociatedEntity", "pbm.version.version1", (("profile", "pbm.profile.ProfileId", "pbm.version.version1", 0, None),("entityType", "string", "pbm.version.version1", F_OPTIONAL, None),), (F_OPTIONAL, "pbm.ServerObjectRef[]", "pbm.ServerObjectRef[]"), "StorageProfile.View", ["pbm.fault.PBMFault", ]), ("queryDefaultRequirementProfile", "PbmQueryDefaultRequirementProfile", "pbm.version.version2", (("hub", "pbm.placement.PlacementHub", "pbm.version.version2", 0, None),), (F_OPTIONAL, "pbm.profile.ProfileId", "pbm.profile.ProfileId"), "StorageProfile.View", ["vmodl.fault.InvalidArgument", "pbm.fault.NonExistentHubs", "pbm.fault.PBMFault", ]), ("resetDefaultRequirementProfile", "PbmResetDefaultRequirementProfile", "pbm.version.version1", (("profile", "pbm.profile.ProfileId", "pbm.version.version1", F_OPTIONAL, None),), (0, "void", "void"), "StorageProfile.Update", None), ("assignDefaultRequirementProfile", "PbmAssignDefaultRequirementProfile", "pbm.version.version2", (("profile", "pbm.profile.ProfileId", "pbm.version.version2", 0, None),("datastores", "pbm.placement.PlacementHub[]", "pbm.version.version2", 0, None),), (0, "void", "void"), "StorageProfile.Update", ["vmodl.fault.InvalidArgument", "pbm.fault.LegacyHubsNotSupported", "pbm.fault.NonExistentHubs", "pbm.fault.PBMFault", ]), ("findApplicableDefaultProfile", "PbmFindApplicableDefaultProfile", "pbm.version.version2", (("datastores", "pbm.placement.PlacementHub[]", "pbm.version.version2", 0, None),), (F_OPTIONAL, "pbm.profile.Profile[]", "pbm.profile.Profile[]"), "StorageProfile.View", ["pbm.fault.LegacyHubsNotSupported", "pbm.fault.NonExistentHubs", "pbm.fault.PBMFault", "vmodl.fault.InvalidArgument", ]), ("queryDefaultRequirementProfiles", "PbmQueryDefaultRequirementProfiles", "pbm.version.version2", (("datastores", "pbm.placement.PlacementHub[]", "pbm.version.version2", 0, None),), (0, "pbm.profile.DefaultProfileInfo[]", "pbm.profile.DefaultProfileInfo[]"), "StorageProfile.View", ["vmodl.fault.InvalidArgument", "pbm.fault.NonExistentHubs", "pbm.fault.PBMFault", ]), ("resetVSanDefaultProfile", "PbmResetVSanDefaultProfile", "pbm.version.version2", (), (0, "void", "void"), "StorageProfile.Update", None), ("querySpaceStatsForStorageContainer", "PbmQuerySpaceStatsForStorageContainer", "pbm.version.version2", (("datastore", "pbm.ServerObjectRef", "pbm.version.version2", 0, None),("capabilityProfileId", "pbm.profile.ProfileId[]", "pbm.version.version2", F_OPTIONAL, None),), (F_OPTIONAL, "pbm.profile.provider.DatastoreSpaceStatistics[]", "pbm.profile.provider.DatastoreSpaceStatistics[]"), "StorageProfile.View", ["vmodl.fault.InvalidArgument", "pbm.fault.PBMFault", ])])
CreateDataType("pbm.profile.ProfileOperationOutcome", "PbmProfileOperationOutcome", "vmodl.DynamicData", "pbm.version.version1", [("profileId", "pbm.profile.ProfileId", "pbm.version.version1", 0), ("fault", "vmodl.MethodFault", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.profile.ProfileType", "PbmProfileType", "vmodl.DynamicData", "pbm.version.version1", [("uniqueId", "string", "pbm.version.version1", 0)])
CreateDataType("pbm.profile.QueryProfileResult", "PbmQueryProfileResult", "vmodl.DynamicData", "pbm.version.version1", [("object", "pbm.ServerObjectRef", "pbm.version.version1", 0), ("profileId", "pbm.profile.ProfileId[]", "pbm.version.version1", F_OPTIONAL), ("fault", "vmodl.MethodFault", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.profile.ResourceType", "PbmProfileResourceType", "vmodl.DynamicData", "pbm.version.version1", [("resourceType", "string", "pbm.version.version1", 0)])
CreateEnumType("pbm.profile.ResourceTypeEnum", "PbmProfileResourceTypeEnum", "pbm.version.version1", ["STORAGE"])
CreateDataType("pbm.profile.SubProfileCapabilityConstraints", "PbmCapabilitySubProfileConstraints", "pbm.profile.CapabilityConstraints", "pbm.version.version1", [("subProfiles", "pbm.profile.SubProfileCapabilityConstraints.SubProfile[]", "pbm.version.version1", 0)])
CreateDataType("pbm.profile.SubProfileCapabilityConstraints.SubProfile", "PbmCapabilitySubProfile", "vmodl.DynamicData", "pbm.version.version1", [("name", "string", "pbm.version.version1", 0), ("capability", "pbm.capability.CapabilityInstance[]", "pbm.version.version1", 0), ("forceProvision", "boolean", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.profile.provider.DatastoreSpaceStatistics", "PbmDatastoreSpaceStatistics", "vmodl.DynamicData", "pbm.version.version2", [("profileId", "string", "pbm.version.version2", F_OPTIONAL), ("physicalTotalInMB", "long", "pbm.version.version2", 0), ("physicalFreeInMB", "long", "pbm.version.version2", 0), ("physicalUsedInMB", "long", "pbm.version.version2", 0), ("logicalLimitInMB", "long", "pbm.version.version2", F_OPTIONAL), ("logicalFreeInMB", "long", "pbm.version.version2", 0), ("logicalUsedInMB", "long", "pbm.version.version2", 0)])
CreateEnumType("pbm.provider.AtomFeedQsProviderType", "PbmAtomFeedQsProviderTye", "pbm.version.version1", ["ASSOCIATION", "COMPLIANCE", "CAPABILITY_METADATA", "CAPABILITY_PROFILE", "REQUIREMENTS_PROFILE"])
CreateManagedType("pbm.provider.Provider", "PbmProvider", "vmodl.ManagedObject", "pbm.version.version1", None, None)
CreateDataType("pbm.capability.CapabilityInstance", "PbmCapabilityInstance", "vmodl.DynamicData", "pbm.version.version1", [("id", "pbm.capability.CapabilityMetadata.UniqueId", "pbm.version.version1", 0), ("constraint", "pbm.capability.ConstraintInstance[]", "pbm.version.version1", 0)])
CreateDataType("pbm.capability.GenericTypeInfo", "PbmCapabilityGenericTypeInfo", "pbm.capability.TypeInfo", "pbm.version.version1", [("genericTypeName", "string", "pbm.version.version1", 0)])
CreateDataType("pbm.fault.AlreadyExists", "PbmAlreadyExists", "pbm.fault.PBMFault", "pbm.version.version1", [("name", "string", "pbm.version.version1", F_OPTIONAL)])
CreateDataType("pbm.fault.CompatibilityCheckFault", "PbmCompatibilityCheckFault", "pbm.fault.PBMFault", "pbm.version.version1", [("hub", "pbm.placement.PlacementHub", "pbm.version.version1", 0)])
CreateDataType("pbm.fault.DefaultProfileAppliesFault", "PbmDefaultProfileAppliesFault", "pbm.fault.CompatibilityCheckFault", "pbm.version.version1", None)
CreateDataType("pbm.fault.DuplicateName", "PbmDuplicateName", "pbm.fault.PBMFault", "pbm.version.version1", [("name", "string", "pbm.version.version1", 0)])
CreateDataType("pbm.fault.InvalidLogin", "PbmFaultInvalidLogin", "pbm.fault.PBMFault", "pbm.version.version2", None)
CreateDataType("pbm.fault.LegacyHubsNotSupported", "PbmLegacyHubsNotSupported", "pbm.fault.PBMFault", "pbm.version.version2", [("hubs", "pbm.placement.PlacementHub[]", "pbm.version.version2", 0)])
CreateDataType("pbm.fault.NonExistentHubs", "PbmNonExistentHubs", "pbm.fault.PBMFault", "pbm.version.version2", [("hubs", "pbm.placement.PlacementHub[]", "pbm.version.version2", 0)])
CreateDataType("pbm.fault.NotFound", "PbmFaultNotFound", "pbm.fault.PBMFault", "pbm.version.version1", None)
CreateDataType("pbm.fault.PropertyMismatchFault", "PbmPropertyMismatchFault", "pbm.fault.CompatibilityCheckFault", "pbm.version.version1", [("capabilityInstanceId", "pbm.capability.CapabilityMetadata.UniqueId", "pbm.version.version1", 0), ("requirementPropertyInstance", "pbm.capability.PropertyInstance", "pbm.version.version1", 0)])
CreateDataType("pbm.profile.CapabilityBasedProfile", "PbmCapabilityProfile", "pbm.profile.Profile", "pbm.version.version1", [("profileCategory", "string", "pbm.version.version1", 0), ("resourceType", "pbm.profile.ResourceType", "pbm.version.version1", 0), ("constraints", "pbm.profile.CapabilityConstraints", "pbm.version.version1", 0), ("generationId", "long", "pbm.version.version1", F_OPTIONAL), ("isDefault", "boolean", "pbm.version.version1", 0), ("systemCreatedProfileType", "string", "pbm.version.version2", F_OPTIONAL)])
CreateEnumType("pbm.profile.CapabilityBasedProfile.ProfileCategoryEnum", "PbmProfileCategoryEnum", "pbm.version.version1", ["REQUIREMENT", "RESOURCE"])
CreateEnumType("pbm.profile.CapabilityBasedProfile.SystemCreatedProfileType", "PbmSystemCreatedProfileType", "pbm.version.version2", ["VsanDefaultProfile", "VVolDefaultProfile"])
CreateDataType("pbm.profile.DefaultCapabilityBasedProfile", "PbmDefaultCapabilityProfile", "pbm.profile.CapabilityBasedProfile", "pbm.version.version1", [("vvolType", "string[]", "pbm.version.version1", 0), ("containerId", "string", "pbm.version.version1", 0)])
CreateDataType("pbm.fault.CapabilityProfilePropertyMismatchFault", "PbmCapabilityProfilePropertyMismatchFault", "pbm.fault.PropertyMismatchFault", "pbm.version.version1", [("resourcePropertyInstance", "pbm.capability.PropertyInstance", "pbm.version.version1", 0)])
CreateDataType("pbm.fault.IncompatibleVendorSpecificRuleSet", "PbmIncompatibleVendorSpecificRuleSet", "pbm.fault.CapabilityProfilePropertyMismatchFault", "pbm.version.version1", None)