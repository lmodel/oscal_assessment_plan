
export enum PartyTypeEnum {
    
    person = "person",
    organization = "organization",
};

export enum HashAlgorithmEnum {
    
    SHA_224 = "SHA-224",
    SHA_256 = "SHA-256",
    SHA_384 = "SHA-384",
    SHA_512 = "SHA-512",
    SHA3_224 = "SHA3-224",
    SHA3_256 = "SHA3-256",
    SHA3_384 = "SHA3-384",
    SHA3_512 = "SHA3-512",
};

export enum PhoneTypeEnum {
    
    home = "home",
    office = "office",
    mobile = "mobile",
};

export enum AddressTypeEnum {
    
    home = "home",
    work = "work",
};

export enum ParameterCardinalityEnum {
    
    one = "one",
    one_or_more = "one-or-more",
};

export enum WithChildControlsEnum {
    
    True = "True",
    False = "False",
};

export enum TaskTypeEnum {
    
    milestone = "milestone",
    action = "action",
};

export enum TimingUnitEnum {
    
    seconds = "seconds",
    minutes = "minutes",
    hours = "hours",
    days = "days",
    months = "months",
    years = "years",
};

export enum AssessmentSubjectTypeEnum {
    
    component = "component",
    inventory_item = "inventory-item",
    location = "location",
    party = "party",
    user = "user",
};

export enum SelectSubjectTypeEnum {
    
    component = "component",
    inventory_item = "inventory-item",
    location = "location",
    party = "party",
    user = "user",
    resource = "resource",
};

export enum OriginActorTypeEnum {
    
    tool = "tool",
    assessment_platform = "assessment-platform",
    party = "party",
};

export enum ObservationMethodEnum {
    
    EXAMINE = "EXAMINE",
    INTERVIEW = "INTERVIEW",
    TEST = "TEST",
    UNKNOWN = "UNKNOWN",
};

export enum ObservationTypeEnum {
    
    ssp_statement_issue = "ssp-statement-issue",
    control_objective = "control-objective",
    mitigation = "mitigation",
    finding = "finding",
    discovery = "discovery",
    historic = "historic",
};

export enum RiskStatusEnum {
    
    open = "open",
    investigating = "investigating",
    remediating = "remediating",
    deviation_requested = "deviation-requested",
    deviation_approved = "deviation-approved",
    closed = "closed",
};

export enum FindingTargetTypeEnum {
    
    statement_id = "statement-id",
    objective_id = "objective-id",
};

export enum ObjectiveStatusStateEnum {
    
    satisfied = "satisfied",
    not_satisfied = "not-satisfied",
};

export enum ObjectiveStatusReasonEnum {
    
    pass = "pass",
    fail = "fail",
    other = "other",
};

export enum ImplementationStatusStateEnum {
    
    implemented = "implemented",
    partial = "partial",
    planned = "planned",
    alternative = "alternative",
    not_applicable = "not-applicable",
};

export enum ComponentTypeEnum {
    
    this_system = "this-system",
    system = "system",
    interconnection = "interconnection",
    software = "software",
    hardware = "hardware",
    service = "service",
    policy = "policy",
    physical = "physical",
    process_procedure = "process-procedure",
    plan = "plan",
    guidance = "guidance",
    standard = "standard",
    validation = "validation",
    network = "network",
};

export enum ComponentStateEnum {
    
    under_development = "under-development",
    operational = "operational",
    disposition = "disposition",
    other = "other",
};

export enum TransportEnum {
    
    TCP = "TCP",
    UDP = "UDP",
};

export enum AssessmentPartNameEnum {
    
    asset = "asset",
    method = "method",
    objective = "objective",
};

export enum ResponseLifecycleEnum {
    
    recommendation = "recommendation",
    planned = "planned",
    completed = "completed",
};


/**
 * Mixin providing the props and links slots that are common to many OSCAL objects.
 */
export interface HasPropsAndLinks {
    /** A list of properties. */
    props?: Property[],
    /** A list of links. */
    links?: Link[],
}


/**
 * Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
 */
export interface OscalCommon extends HasPropsAndLinks {
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Mixin providing the responsible-roles slot for objects that carry role assignments.
 */
export interface HasResponsibleRoles {
    /** Responsible role assignments. */
    responsible_roles?: ResponsibleRole[],
}


/**
 * Mixin providing the responsible-parties slot for objects that carry party assignments.
 */
export interface HasResponsibleParties {
    /** Responsible party assignments. */
    responsible_parties?: ResponsibleParty[],
}


/**
 * A root wrapper for an OSCAL document, which may be of any OSCAL document type (e.g. Catalog, Profile, Assessment Plan, SSP).
 */
export interface OscalDocument {
}


/**
 * Root wrapper for an OSCAL Catalog document.
 */
export interface CatalogDocument extends OscalDocument {
    /** Root catalog document. */
    catalog: Catalog,
}


/**
 * A structured, organized collection of control information.
 */
export interface Catalog {
    /** Provides a globally unique means to identify a given catalog instance. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
    /** Parameters providing a mechanism for the dynamic assignment of value(s) in a control. */
    params?: Parameter[],
    /** A collection of controls. */
    controls?: Control[],
    /** A collection of control groups. */
    groups?: Group[],
}


/**
 * A group of controls, or of groups of controls.
 */
export interface Group extends OscalCommon {
    /** Identifies the group for the purpose of cross-linking within the defining instance or from other instances that reference the catalog. */
    id?: string,
    /** A textual label that provides a sub-type or characterization of the group. */
    _class?: string,
    /** A name given to the group, which may be used by a tool for display and navigation. */
    title: string,
    /** Parameters providing a mechanism for the dynamic assignment of value(s) in a control. */
    params?: Parameter[],
    /** A collection of parts. */
    parts?: Part[],
    /** A collection of control groups. */
    groups?: Group[],
    /** A collection of controls. */
    controls?: Control[],
}


/**
 * A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk related to an information system and its information.
 */
export interface Control extends OscalCommon {
    /** Identifies a control such that it can be referenced in the defining catalog and other OSCAL instances (e.g., profiles). */
    id: string,
    /** A textual label that provides a sub-type or characterization of the control. */
    _class?: string,
    /** A name given to the control, which may be used by a tool for display and navigation. */
    title: string,
    /** Parameters providing a mechanism for the dynamic assignment of value(s) in a control. */
    params?: Parameter[],
    /** A collection of parts. */
    parts?: Part[],
    /** A collection of controls. */
    controls?: Control[],
}


/**
 * Provides information about the containing document, and defines concepts shared across the document.
 */
export interface Metadata extends OscalCommon, HasResponsibleParties {
    /** A name given to the document. */
    title: string,
    /** The date and time the document was last made available. */
    published?: string,
    /** The date and time the document was last stored for later retrieval. */
    last_modified: string,
    /** Used to distinguish a specific revision of an OSCAL document. */
    version: string,
    /** The OSCAL model version the document was authored against. */
    oscal_version: string,
    /** Document identifiers qualified by an identifier scheme. */
    document_ids?: DocumentId[],
    /** An entry in a sequential list of revisions to the containing document, expected to be in reverse chronological order (i.e. latest first). */
    revisions?: Revision[],
    /** Defines a function, which might be assigned to a party in a specific situation. */
    roles?: Role[],
    /** A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document. */
    locations?: Location[],
    /** An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document. */
    parties?: Party[],
    /** An action applied by a role within a given party to the content. */
    actions?: Action[],
}


/**
 * An entry in a sequential list of revisions to the containing document.
 */
export interface Revision extends OscalCommon {
    /** A human-readable name or title. */
    title?: string,
    /** The date and time the document was last made available. */
    published?: string,
    /** The date and time the document was last modified. */
    last_modified?: string,
    /** Used to distinguish a specific revision of an OSCAL document from other previous and future versions. */
    version: string,
    /** The OSCAL model version the document was authored against and will conform to as valid. */
    oscal_version?: string,
}


/**
 * A document identifier qualified by an identifier scheme.
 */
export interface DocumentId {
    /** Qualifies the kind of identifier using a URI. */
    scheme?: string,
    /** A document identifier value. */
    identifier: string,
}


/**
 * Defines a function, which might be assigned to a party in a specific situation.
 */
export interface Role extends OscalCommon {
    /** A unique identifier for the role. */
    id: string,
    /** A human-readable name or title. */
    title: string,
    /** A short common name, abbreviation, or acronym. */
    short_name?: string,
    /** A human-readable description. */
    description?: string,
}


/**
 * A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.
 */
export interface Location extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** Email addresses associated with the containing object. */
    email_addresses?: string[],
    /** Telephone numbers associated with the containing object. */
    telephone_numbers?: TelephoneNumber[],
    /** A postal address for the location. */
    address?: Address,
    /** The uniform resource locator (URL) for a web site or other resource associated with the location. */
    urls?: string[],
}


/**
 * An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.
 */
export interface Party extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A category describing the kind of party the object describes. */
    type: string,
    /** The full name of the party. */
    name?: string,
    /** A short common name, abbreviation, or acronym. */
    short_name?: string,
    /** Email addresses associated with the containing object. */
    email_addresses?: string[],
    /** Telephone numbers associated with the containing object. */
    telephone_numbers?: TelephoneNumber[],
    /** An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID). */
    external_ids?: PartyExternalId[],
    /** Postal addresses associated with the containing object. */
    addresses?: Address[],
    /** Reference to a location by UUID. */
    location_uuids?: string[],
    /** A reference to another party by UUID, typically an organization, that this subject is associated with. */
    member_of_organizations?: string[],
}


/**
 * An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).
 */
export interface PartyExternalId {
    /** Indicates the type of external identifier. */
    scheme: string,
    /** A unique human-oriented identifier within a particular context. */
    id: string,
}


/**
 * A reference to a set of persons and/or organizations that have responsibility for performing the referenced role in the context of the containing object.
 */
export interface ResponsibleParty extends OscalCommon {
    /** A reference to a role performed by a party. */
    role_id: string,
    /** References to party UUIDs. */
    party_uuids: string[],
}


/**
 * A reference to a role with responsibility for performing a function relative to the containing object, optionally associated with a set of persons and/or organizations that perform that role.
 */
export interface ResponsibleRole extends OscalCommon {
    /** A human-oriented identifier reference to a role performed. */
    role_id: string,
    /** References to party UUIDs. */
    party_uuids?: string[],
}


/**
 * An action applied by a role within a given party to the content.
 */
export interface Action extends OscalCommon, HasResponsibleParties {
    /** A unique identifier that can be used to reference this defined action elsewhere in an OSCAL document. */
    uuid: string,
    /** The type of action documented by the assembly, such as an approval. */
    type: string,
    /** The date and time when the action occurred. */
    date?: string,
    /** Specifies the action type system used. */
    system: string,
}


/**
 * A telephone service number as defined by ITU-T E.164.
 */
export interface TelephoneNumber {
    /** Indicates the type of phone number. Typical values: home, office, mobile. Other values are permitted. */
    type?: string,
    /** A telephone number value. */
    number: string,
}


/**
 * A postal address for the location.
 */
export interface Address {
    /** Indicates the type of address. Typical values: home, work. Other values are permitted. */
    type?: string,
    /** A single line of an address. */
    addr_lines?: string[],
    /** City, town or geographical region for the mailing address. */
    city?: string,
    /** State, province or analogous geographical region for a mailing address. */
    state?: string,
    /** Postal or ZIP code for mailing address. */
    postal_code?: string,
    /** The ISO 3166-1 alpha-2 country code for the mailing address. */
    country?: string,
}


/**
 * A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
 */
export interface Hash {
    /** The value associated with the containing object. */
    value: string,
    /** The digest method by which a hash is derived. SHOULD be one of the HashAlgorithmEnum values but other values are permitted (allow-other="yes"). */
    algorithm: string,
}


/**
 * An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value pair.
 */
export interface Property {
    /** A textual label, within a namespace, that identifies a specific attribute, characteristic, or quality of the property's containing object. */
    name: string,
    /** A unique identifier for a property. */
    uuid?: string,
    /** A namespace qualifying the property's name. This allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** Indicates the value of the attribute, characteristic, or quality. */
    value: string,
    /** A textual label that provides a sub-type or characterization of the property's name. */
    _class?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** An identifier for relating distinct sets of properties. */
    group?: string,
}


/**
 * A reference to a local or remote resource, that has a specific relation to the containing object.
 */
export interface Link {
    /** A resolvable URL reference to a resource. */
    href: string,
    /** Describes the type of relationship provided by the link's hypertext reference. This can be an indicator of the link's purpose. */
    rel?: string,
    /** In case where the href points to a back-matter/resource, this value will indicate the URI fragment to append to any rlink associated with the resource. This value MUST be URI encoded. */
    resource_fragment?: string,
    /** A label that indicates the nature of a resource, as a data serialization or format. */
    media_type?: string,
    /** A textual label to associate with the containing object. */
    text?: string,
}


/**
 * A collection of resources that may be referenced from within the OSCAL document instance.
 */
export interface BackMatter {
    /** A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources. */
    resources?: Resource[],
}


/**
 * A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.
 */
export interface Resource {
    /** A unique identifier for a resource. */
    uuid: string,
    /** An optional name given to the resource, which may be used by a tool for display and navigation. */
    title?: string,
    /** An optional short summary of the resource used to indicate the purpose of the resource. */
    description?: string,
    /** A list of properties. */
    props?: Property[],
    /** Document identifiers qualified by an identifier scheme. */
    document_ids?: DocumentId[],
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** An optional citation consisting of end note text using structured markup. */
    citation?: Citation,
    /** A URL-based pointer to an external resource with an optional hash for verification and change detection. */
    rlinks?: ResourceLink[],
    /** A resource encoded using the Base64 alphabet defined by RFC 2045. */
    base64?: Base64Resource,
}


/**
 * An optional citation consisting of end note text using structured markup.
 */
export interface Citation extends HasPropsAndLinks {
    /** A line of citation text. */
    text: string,
}


/**
 * A URL-based pointer to an external resource with an optional hash for verification and change detection.
 */
export interface ResourceLink {
    /** A resolvable URL pointing to the referenced resource. */
    href: string,
    /** A label that indicates the nature of a resource, as a data serialization or format. */
    media_type?: string,
    /** A representation of a cryptographic digest generated over a resource using a specified hash algorithm. */
    hashes?: Hash[],
}


/**
 * A resource encoded using the Base64 alphabet defined by RFC 2045.
 */
export interface Base64Resource {
    /** A label that indicates the nature of a resource, as a data serialization or format. */
    media_type?: string,
    /** The value associated with the containing object. */
    value: string,
    /** Name of the file before it was encoded as Base64 to be embedded in a resource. */
    filename?: string,
}


/**
 * An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
 */
export interface Part extends HasPropsAndLinks {
    /** A unique identifier for the part. */
    id?: string,
    /** A textual label that uniquely identifies the part's semantic type, which exists in a value space qualified by the ns. */
    name: string,
    /** An optional namespace qualifying the part's name. This allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** An optional textual providing a sub-type or characterization of the part's name, or a category to which the part belongs. */
    _class?: string,
    /** An optional name given to the part, which may be used by a tool for display and navigation. */
    title?: string,
    /** Permits multiple paragraphs, lists, tables etc. */
    prose?: string,
    /** A collection of parts. */
    parts?: Part[],
}


/**
 * Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
 */
export interface Parameter extends OscalCommon {
    /** A unique identifier for the parameter. */
    id: string,
    /** A textual label that provides a characterization of the type, purpose, use or scope of the parameter. */
    _class?: string,
    /** (deprecated) Another parameter invoking this one. This construct has been deprecated and should not be used. */
    depends_on?: string,
    /** A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned. */
    label?: string,
    /** Describes the purpose and use of a parameter. */
    usage?: string,
    /** A formal or informal expression of a constraint or test. */
    constraints?: ParameterConstraint[],
    /** A prose statement that provides a recommendation for the use of a parameter. */
    guidelines?: ParameterGuideline[],
    /** A parameter value or set of values. */
    values?: string[],
    /** Presenting a choice among alternatives. */
    select?: ParameterSelection,
}


/**
 * A formal or informal expression of a constraint or test.
 */
export interface ParameterConstraint {
    /** A textual summary of the constraint to be applied. */
    description?: string,
    /** A test expression which is expected to be evaluated by a tool. */
    tests?: ConstraintTest[],
}


/**
 * A test expression which is expected to be evaluated by a tool.
 */
export interface ConstraintTest {
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** A formal (executable) expression of a constraint. */
    expression: string,
}


/**
 * A prose statement that provides a recommendation for the use of a parameter.
 */
export interface ParameterGuideline {
    /** Prose permits multiple paragraphs, lists, tables etc. */
    prose: string,
}


/**
 * Presenting a choice among alternatives.
 */
export interface ParameterSelection {
    /** Describes the number of selections that must occur. Without this setting, only one value should be assumed to be permitted. */
    how_many?: string,
    /** A value selection among several such options. */
    choice?: string[],
}


/**
 * Include all controls from the imported catalog or profile resources.
 */
export interface IncludeAll {
}


/**
 * Selecting a set of controls by matching their IDs with a wildcard pattern.
 */
export interface ControlMatching {
    /** Additional commentary about the containing object. */
    remarks?: string,
    /** A glob expression matching the IDs of one or more controls to be selected. */
    pattern?: string,
}


/**
 * Select a control or controls from an imported control set.
 */
export interface SelectControlById {
    /** When a control is included, whether its child (dependent) controls are also included. */
    with_child_controls?: string,
    /** Selecting a control by its ID given as a literal. */
    with_ids?: string[],
    /** Selecting a set of controls by matching their IDs with a wildcard pattern. */
    matching?: ControlMatching[],
}


/**
 * Root wrapper for an OSCAL Assessment Plan document.
 */
export interface AssessmentPlanDocument extends OscalDocument {
    /** The root assessment plan object. */
    assessment_plan: AssessmentPlan,
}


/**
 * An assessment plan, such as those provided by a FedRAMP assessor.
 */
export interface AssessmentPlan {
    /** Assessment Plan Universally Unique Identifier. */
    uuid: string,
    /** Provides information about the containing document, and defines concepts shared across the document. */
    metadata: Metadata,
    /** Used to import information about the system from an SSP. */
    import_ssp: ImportSSP,
    /** Used to define data objects that do not appear in the referenced SSP. */
    local_definitions?: LocalDefinitions,
    /** Terms and conditions under which an assessment can be performed. */
    terms_and_conditions?: TermsAndConditions,
    /** Identifies system elements being assessed. */
    assessment_subjects?: AssessmentSubject[],
    /** Identifies the assets used to perform this assessment. */
    assessment_assets?: AssessmentAssets,
    /** Identifies the controls being assessed and their control objectives. */
    reviewed_controls: ReviewedControls,
    /** A collection of tasks. */
    tasks?: Task[],
    /** A collection of resources that may be referenced from within the OSCAL document instance. */
    back_matter?: BackMatter,
}


/**
 * Used by the assessment plan and POA&M to import information about the system.
 */
export interface ImportSSP {
    /** A resolvable URL reference to a resource. */
    href: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
 */
export interface LocalDefinitions {
    /** A collection of system components. */
    components?: SystemComponent[],
    /** A collection of inventory items. */
    inventory_items?: InventoryItem[],
    /** A collection of system users. */
    users?: SystemUser[],
    /** A collection of locally-defined control objectives. */
    objectives_and_methods?: LocalObjective[],
    /** A collection of activities. */
    activities?: Activity[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Used to define various terms and conditions under which an assessment can be performed.
 */
export interface TermsAndConditions {
    /** A collection of parts. */
    parts?: AssessmentPart[],
}


/**
 * Identifies the controls being assessed and their control objectives.
 */
export interface ReviewedControls extends OscalCommon {
    /** A human-readable description. */
    description?: string,
    /** Identifies the controls being assessed. */
    control_selections: ControlSelection[],
    /** Identifies the control objectives of the assessment. */
    control_objective_selections?: ControlObjectiveSelection[],
}


/**
 * Identifies the controls being assessed.
 */
export interface ControlSelection extends OscalCommon {
    /** A human-readable description. */
    description?: string,
    /** Include all controls from the imported catalog or profile resources. */
    include_all?: IncludeAll,
    /** Controls to include in the assessment. */
    include_controls?: AssessmentSelectControlById[],
    /** Controls to exclude from the assessment. */
    exclude_controls?: AssessmentSelectControlById[],
}


/**
 * Identifies the control objectives of the assessment.
 */
export interface ControlObjectiveSelection extends OscalCommon {
    /** A human-readable description. */
    description?: string,
    /** Include all controls from the imported catalog or profile resources. */
    include_all?: IncludeAll,
    /** Objectives to include in the assessment. */
    include_objectives?: SelectObjectiveById[],
    /** Objectives to exclude from the assessment. */
    exclude_objectives?: SelectObjectiveById[],
}


/**
 * Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement IDs.
 */
export interface AssessmentSelectControlById {
    /** A reference to a control by its identifier. */
    control_id: string,
    /** Statement IDs for control selection. */
    statement_ids?: string[],
}


/**
 * Used to select a control objective for inclusion/exclusion.
 */
export interface SelectObjectiveById {
    /** Reference to a control objective by its identifier. */
    objective_id: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies system elements being assessed, such as components, inventory items, and locations.
 */
export interface AssessmentSubject extends OscalCommon {
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable description. */
    description?: string,
    /** Include all controls from the imported catalog or profile resources. */
    include_all?: IncludeAll,
    /** Assessment subjects to include. */
    include_subjects?: SelectSubjectById[],
    /** Assessment subjects to exclude. */
    exclude_subjects?: SelectSubjectById[],
}


/**
 * Identifies a set of assessment subjects to include/exclude by UUID.
 */
export interface SelectSubjectById extends OscalCommon {
    /** A UUID reference to the identified subject. */
    subject_uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
}


/**
 * A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
 */
export interface SubjectReference extends OscalCommon {
    /** A UUID reference to the identified subject. */
    subject_uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable name or title. */
    title?: string,
}


/**
 * Used when the assessment subjects will be determined as part of one or more other assessment activities.
 */
export interface AssessmentSubjectPlaceholder extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description?: string,
    /** Activities that will identify assessment subjects. */
    sources: AssessmentSubjectSource[],
}


/**
 * Assessment subjects will be identified while conducting the referenced activity.
 */
export interface AssessmentSubjectSource {
    /** A UUID reference to a task. */
    task_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies the assets used to perform this assessment.
 */
export interface AssessmentAssets {
    /** A collection of system components. */
    components?: SystemComponent[],
    /** A collection of assessment platforms. */
    assessment_platforms: AssessmentPlatform[],
}


/**
 * Used to represent the toolset used to perform aspects of the assessment.
 */
export interface AssessmentPlatform extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** The set of components used by the assessment platform. */
    uses_components?: UsesComponent[],
}


/**
 * The set of components that are used by the assessment platform.
 */
export interface UsesComponent extends OscalCommon, HasResponsibleParties {
    /** A UUID reference to a component. */
    component_uuid: string,
}


/**
 * A local definition of a control objective for this assessment. Uses catalog syntax for control objective and assessment actions.
 */
export interface LocalObjective extends OscalCommon {
    /** A reference to a control by its identifier. */
    control_id: string,
    /** A human-readable description. */
    description?: string,
    /** A collection of parts. */
    parts: ControlPart[],
}


/**
 * A local definition of a control objective.
 */
export interface AssessmentMethod extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description?: string,
    /** An assessment part. */
    part: AssessmentPart,
}


/**
 * Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended activity.
 */
export interface Activity extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description: string,
    /** A collection of steps in an activity. */
    steps?: Step[],
    /** A reference to reviewed controls for this activity or step. */
    related_controls?: ReviewedControls,
}


/**
 * Identifies an individual step in a series of steps related to an activity, such as an assessment test or examination procedure.
 */
export interface Step extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description: string,
    /** Identifies the controls being assessed and their control objectives. */
    reviewed_controls?: ReviewedControls,
}


/**
 * Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
 */
export interface Task extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description?: string,
    /** The timing under which a task is intended to occur. */
    timing?: EventTiming,
    /** Tasks that this task depends on. */
    dependencies?: TaskDependency[],
    /** Activities associated with this task. */
    associated_activities?: AssociatedActivity[],
    /** A collection of tasks. */
    tasks?: Task[],
    /** Assessment subjects or subject references for this object. */
    subjects?: AssessmentSubject[],
}


/**
 * The timing under which the task is intended to occur.
 */
export interface EventTiming {
    /** The task is intended to occur on the specified date. */
    on_date?: OnDateCondition,
    /** The task is intended to occur within the specified date range. */
    within_date_range?: WithinDateRange,
    /** The task is intended to occur at the specified frequency. */
    at_frequency?: AtFrequency,
}


/**
 * The task is intended to occur on the specified date.
 */
export interface OnDateCondition {
    /** The date and time when the action occurred. */
    date: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * The task is intended to occur within the specified date range.
 */
export interface WithinDateRange {
    /** The start date/time. */
    start: string,
    /** The end date/time. */
    end: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * The task is intended to occur at the specified frequency.
 */
export interface AtFrequency {
    /** The task must occur every period (in the given units). */
    period: number,
    /** The unit of time for the period. */
    unit: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Used to indicate that a task is dependent on another task.
 */
export interface TaskDependency {
    /** A UUID reference to a task. */
    task_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies an individual activity to be performed as part of a task.
 */
export interface AssociatedActivity extends OscalCommon, HasResponsibleRoles {
    /** A UUID reference to an activity. */
    activity_uuid: string,
    /** Assessment subjects or subject references for this object. */
    subjects: AssessmentSubject[],
}


/**
 * A partition of an assessment plan or results or a child of another part.
 */
export interface AssessmentPart extends HasPropsAndLinks {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid?: string,
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name: string,
    /** An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** A textual label that provides a sub-type or characterization. */
    _class?: string,
    /** A human-readable name or title. */
    title?: string,
    /** Permits multiple paragraphs, lists, tables etc. */
    prose?: string,
    /** A collection of parts. */
    parts?: AssessmentPart[],
}


/**
 * An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
 */
export interface ControlPart extends HasPropsAndLinks {
    /** A unique human-oriented identifier within a particular context. */
    id?: string,
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name: string,
    /** An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name. */
    ns?: string,
    /** A textual label that provides a sub-type or characterization. */
    _class?: string,
    /** A human-readable name or title. */
    title?: string,
    /** Permits multiple paragraphs, lists, tables etc. */
    prose?: string,
    /** A collection of parts. */
    parts?: ControlPart[],
}


/**
 * Identifies the parameter that will be set by the enclosed value.
 */
export interface SetParameter {
    /** A reference to a parameter by its identifier. */
    param_id: string,
    /** A parameter value or set of values. */
    values: string[],
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A defined component that can be part of an implemented system.
 */
export interface SystemComponent extends OscalCommon, HasResponsibleRoles {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** A summary of the technological or business purpose of the component. */
    purpose?: string,
    /** Information about the protocol used to provide a service. */
    protocols?: Protocol[],
    /** Indicates the status of the containing object. */
    status: ComponentStatus,
}


/**
 * Describes the operational status of the system component.
 */
export interface ComponentStatus {
    /** The operational status. */
    state: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Information about the protocol used to provide a service.
 */
export interface Protocol {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid?: string,
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name: string,
    /** A human-readable name or title. */
    title?: string,
    /** Where applicable, the transport layer protocol port range. */
    port_ranges?: PortRange[],
}


/**
 * Where applicable, the transport layer protocol port range.
 */
export interface PortRange {
    /** The start date/time. */
    start?: number,
    /** The end date/time. */
    end?: number,
    /** Indicates the transport type. */
    transport?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Indicates the degree to which a given control is implemented.
 */
export interface ImplementationStatus {
    /** Identifies the implementation status of the control or control objective. */
    state: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * A type of user that interacts with the system based on an associated role.
 */
export interface SystemUser extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A short common name, abbreviation, or acronym. */
    short_name?: string,
    /** A human-readable description. */
    description?: string,
    /** Role identifiers associated with the user. */
    role_ids?: string[],
    /** A collection of authorized privileges. */
    authorized_privileges?: AuthorizedPrivilege[],
}


/**
 * Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
 */
export interface AuthorizedPrivilege {
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description?: string,
    /** Describes a function performed for a given authorized privilege. */
    functions_performed: string[],
}


/**
 * A single managed inventory item within the system.
 */
export interface InventoryItem extends OscalCommon, HasResponsibleParties {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description: string,
    /** A collection of implemented components. */
    implemented_components?: ImplementedComponent[],
}


/**
 * The set of components that are implemented in a given system inventory item.
 */
export interface ImplementedComponent extends OscalCommon, HasResponsibleParties {
    /** A UUID reference to a component. */
    component_uuid: string,
}


/**
 * A human-oriented, globally unique identifier for a system.
 */
export interface SystemId {
    /** A unique human-oriented identifier within a particular context. */
    id: string,
    /** A human-readable label for a specific identifier scheme. */
    identifier_type?: string,
}


/**
 * Identifies the source of the finding, such as a tool, interviewed person, or activity.
 */
export interface Origin {
    /** The actor that produces an observation, a finding, or a risk. */
    actors: OriginActor[],
    /** Identifies tasks for which the containing object is a consequence. */
    related_tasks?: RelatedTask[],
}


/**
 * The actor that produces an observation, a finding, or a risk.
 */
export interface OriginActor extends HasPropsAndLinks {
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** A machine-oriented identifier reference to the tool or person based on the associated type. */
    actor_uuid: string,
    /** A reference to a role by its identifier. */
    role_id?: string,
}


/**
 * Identifies an individual task for which the containing object is a consequence of.
 */
export interface RelatedTask extends OscalCommon, HasResponsibleParties {
    /** A UUID reference to a task. */
    task_uuid: string,
    /** Assessment subjects or subject references for this object. */
    subjects?: AssessmentSubject[],
    /** Used to detail assessment subjects that were identified by this task. */
    identified_subject?: IdentifiedSubject,
}


/**
 * Used to detail assessment subjects that were identified by this task.
 */
export interface IdentifiedSubject {
    /** A reference to an assessment subject placeholder defined in the assessment plan. */
    subject_placeholder_uuid: string,
    /** Assessment subjects or subject references for this object. */
    subjects: AssessmentSubject[],
}


/**
 * Describes an individual observation.
 */
export interface Observation extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description: string,
    /** Identifies how the observation was made. */
    methods: string,
    /** Identifies the nature of the observation. */
    types?: string,
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** Assessment subjects or subject references for this object. */
    subjects?: SubjectReference[],
    /** Links the observation to relevant evidence. */
    relevant_evidence?: RelevantEvidence[],
    /** Date/time stamp identifying when the finding information was collected. */
    collected: string,
    /** Date/time identifying when the finding information is no longer considered valid. */
    expires?: string,
}


/**
 * Links this observation to relevant evidence.
 */
export interface RelevantEvidence extends OscalCommon {
    /** A resolvable URL reference to a resource. */
    href?: string,
    /** A human-readable description. */
    description: string,
}


/**
 * Describes an individual finding.
 */
export interface Finding extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** Identifies the target of a finding. */
    target: FindingTarget,
    /** A reference to the implementation statement in the SSP to which this finding is related. */
    implementation_statement_uuid?: string,
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** Relates the containing object to a set of referenced observations. */
    related_observations?: RelatedObservation[],
    /** Relates the finding to a set of referenced risks. */
    related_risks?: AssociatedRisk[],
}


/**
 * Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
 */
export interface FindingTarget extends OscalCommon {
    /** Indicates the nature or kind of the containing object. */
    type: string,
    /** Identifies the specific target qualified by the type. */
    target_id: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description?: string,
    /** Identifies the implementation status of the control. */
    implementation_status?: ImplementationStatus,
    /** Indicates the status of the containing object. */
    status: ObjectiveStatus,
}


/**
 * A determination of if the objective is satisfied or not within a given system.
 */
export interface ObjectiveStatus {
    /** An indication as to whether the objective is satisfied or not. */
    state: string,
    /** The reason the objective was given its status. */
    reason?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Relates the identified element to a set of referenced observations.
 */
export interface RelatedObservation {
    /** A machine-oriented identifier reference to an observation defined in the list of observations. */
    observation_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Relates the finding to a set of referenced risks.
 */
export interface AssociatedRisk {
    /** A machine-oriented identifier reference to a risk defined in the list of risks. */
    risk_uuid: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * An identified risk.
 */
export interface Risk extends HasPropsAndLinks {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** An assessor's summary of the risk, in narrative form. */
    statement: string,
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** The referenced threat identifiers. */
    threat_ids?: ThreatId[],
    /** Supporting information about the risk and how it relates to the system. */
    characterizations?: Characterization[],
    /** Describes existing mitigating factors that may affect the overall determination of the risk. */
    mitigating_factors?: MitigatingFactor[],
    /** The date/time by which the risk must be resolved. */
    deadline?: string,
    /** Describes either recommended or actual responses to a risk. */
    remediations?: Response[],
    /** A log of all risk-related tasks taken. */
    risk_log?: RiskLog,
    /** Relates the containing object to a set of referenced observations. */
    related_observations?: RelatedObservation[],
    /** Indicates the status of the containing object. */
    status: string,
}


/**
 * A pointer, by ID, to an externally-defined threat.
 */
export interface ThreatId {
    /** A resolvable URL reference to a resource. */
    href?: string,
    /** Specifies the system or scheme from which the identifier originates. */
    system: string,
    /** A unique human-oriented identifier within a particular context. */
    id: string,
}


/**
 * A collection of descriptive data about the containing object from a specific origin.
 */
export interface Characterization extends HasPropsAndLinks {
    /** The source of the finding. */
    origin: Origin,
    /** An individual characteristic that is part of a larger set produced by the same actor. */
    facets: Facet[],
}


/**
 * An individual characteristic that is part of a larger set produced by the same actor.
 */
export interface Facet extends OscalCommon {
    /** A textual label that uniquely identifies an attribute or semantic type. */
    name: string,
    /** The value associated with the containing object. */
    value: string,
    /** Specifies the system or scheme from which the identifier originates. */
    system: string,
}


/**
 * Describes an existing mitigating factor that may affect the overall determination of the risk.
 */
export interface MitigatingFactor extends HasPropsAndLinks {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable description. */
    description: string,
    /** A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this implementation statement elsewhere in this or other OSCAL instances. */
    implementation_uuid?: string,
    /** Assessment subjects or subject references for this object. */
    subjects?: SubjectReference[],
}


/**
 * Describes either recommended or an actual plan for addressing the risk.
 */
export interface Response extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title: string,
    /** A human-readable description. */
    description: string,
    /** Identifies whether this is a recommendation or an actual plan. */
    lifecycle: string,
    /** Identifies the source of observations, findings, or risks. */
    origins?: Origin[],
    /** Identifies an asset required to achieve remediation. */
    required_assets?: RequiredAsset[],
    /** A collection of tasks. */
    tasks?: Task[],
}


/**
 * Identifies an asset required to achieve remediation.
 */
export interface RequiredAsset extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description: string,
    /** Assessment subjects or subject references for this object. */
    subjects?: SubjectReference[],
}


/**
 * A log of all risk-related tasks taken.
 */
export interface RiskLog {
    /** Identifies an individual risk response that occurred as part of managing an identified risk. */
    entries: RiskLogEntry[],
}


/**
 * Identifies an individual risk response that occurred as part of managing an identified risk.
 */
export interface RiskLogEntry extends OscalCommon {
    /** A machine-oriented, globally unique identifier with a cross-instance scope. */
    uuid: string,
    /** A human-readable name or title. */
    title?: string,
    /** A human-readable description. */
    description?: string,
    /** The start date/time. */
    start: string,
    /** The end date/time. */
    end?: string,
    /** Used to indicate who created a log entry in what role. */
    logged_by?: LoggedBy[],
    /** Identifies the risk change that prompted the log entry. */
    status_change?: string,
    /** Identifies an individual risk response that this log entry is for. */
    related_responses?: RiskResponseReference[],
}


/**
 * Used to indicate who created a log entry in what role.
 */
export interface LoggedBy {
    /** A machine-oriented identifier reference to the party who is making the log entry. */
    party_uuid: string,
    /** A reference to a role by its identifier. */
    role_id?: string,
    /** Additional commentary about the containing object. */
    remarks?: string,
}


/**
 * Identifies an individual risk response that this log entry is for.
 */
export interface RiskResponseReference extends OscalCommon {
    /** A machine-oriented identifier reference to a unique risk response. */
    response_uuid: string,
    /** Identifies tasks for which the containing object is a consequence. */
    related_tasks?: RelatedTask[],
}



