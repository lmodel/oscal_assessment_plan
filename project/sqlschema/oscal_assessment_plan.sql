-- # Class: AssessmentPlanDocument Description: Root wrapper for an OSCAL Assessment Plan document.
--     * Slot: id
--     * Slot: assessment_plan_id Description: The root assessment plan object.
-- # Class: AssessmentPlan Description: An assessment plan, such as those provided by a FedRAMP assessor.
--     * Slot: id
--     * Slot: uuid Description: Assessment Plan Universally Unique Identifier.
--     * Slot: metadata_id Description: Provides information about the containing document, and defines concepts shared across the document.
--     * Slot: import_ssp_id Description: Used to import information about the system from an SSP.
--     * Slot: local_definitions_id Description: Used to define data objects that do not appear in the referenced SSP.
--     * Slot: terms_and_conditions_id Description: Terms and conditions under which an assessment can be performed.
--     * Slot: assessment_assets_id Description: Identifies the assets used to perform this assessment.
--     * Slot: reviewed_controls_id Description: Identifies the controls being assessed and their control objectives.
--     * Slot: back_matter_id Description: A collection of resources that may be referenced from within the OSCAL document instance.
-- # Class: ImportSSP Description: Used by the assessment plan and POA&M to import information about the system.
--     * Slot: id
--     * Slot: href Description: A resolvable URL reference to a resource.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: LocalDefinitions Description: Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
--     * Slot: id
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: TermsAndConditions Description: Used to define various terms and conditions under which an assessment can be performed.
--     * Slot: id
-- # Class: ReviewedControls Description: Identifies the controls being assessed and their control objectives.
--     * Slot: id
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: ControlSelection Description: Identifies the controls being assessed.
--     * Slot: id
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: ReviewedControls_id Description: Autocreated FK slot
--     * Slot: include_all_id Description: Include all controls from the imported catalog or profile resources.
-- # Class: ControlObjectiveSelection Description: Identifies the control objectives of the assessment.
--     * Slot: id
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: ReviewedControls_id Description: Autocreated FK slot
--     * Slot: include_all_id Description: Include all controls from the imported catalog or profile resources.
-- # Class: AssessmentSelectControlById Description: Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement IDs.
--     * Slot: id
--     * Slot: control_id Description: A reference to a control by its identifier.
--     * Slot: ControlSelection_id Description: Autocreated FK slot
-- # Class: SelectObjectiveById Description: Used to select a control objective for inclusion/exclusion.
--     * Slot: id
--     * Slot: objective_id Description: Reference to a control objective by its identifier.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: ControlObjectiveSelection_id Description: Autocreated FK slot
-- # Class: AssessmentSubject Description: Identifies system elements being assessed, such as components, inventory items, and locations.
--     * Slot: id
--     * Slot: type Description: Indicates the nature or kind of the containing object.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: AssessmentPlan_id Description: Autocreated FK slot
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: AssociatedActivity_id Description: Autocreated FK slot
--     * Slot: RelatedTask_id Description: Autocreated FK slot
--     * Slot: IdentifiedSubject_id Description: Autocreated FK slot
--     * Slot: include_all_id Description: Include all controls from the imported catalog or profile resources.
-- # Class: SelectSubjectById Description: Identifies a set of assessment subjects to include/exclude by UUID.
--     * Slot: id
--     * Slot: subject_uuid Description: A UUID reference to the identified subject.
--     * Slot: type Description: Indicates the nature or kind of the containing object.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: AssessmentSubject_id Description: Autocreated FK slot
-- # Class: SubjectReference Description: A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
--     * Slot: id
--     * Slot: subject_uuid Description: A UUID reference to the identified subject.
--     * Slot: type Description: Indicates the nature or kind of the containing object.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: MitigatingFactor_id Description: Autocreated FK slot
--     * Slot: RequiredAsset_id Description: Autocreated FK slot
-- # Class: AssessmentSubjectPlaceholder Description: Used when the assessment subjects will be determined as part of one or more other assessment activities.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: AssessmentSubjectSource Description: Assessment subjects will be identified while conducting the referenced activity.
--     * Slot: id
--     * Slot: task_uuid Description: A UUID reference to a task.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: AssessmentSubjectPlaceholder_id Description: Autocreated FK slot
-- # Class: AssessmentAssets Description: Identifies the assets used to perform this assessment.
--     * Slot: id
-- # Class: AssessmentPlatform Description: Used to represent the toolset used to perform aspects of the assessment.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: AssessmentAssets_id Description: Autocreated FK slot
-- # Class: UsesComponent Description: The set of components that are used by the assessment platform.
--     * Slot: id
--     * Slot: component_uuid Description: A UUID reference to a component.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: AssessmentPlatform_id Description: Autocreated FK slot
-- # Class: LocalObjective Description: A local definition of a control objective for this assessment. Uses catalog syntax for control objective and assessment actions.
--     * Slot: id
--     * Slot: control_id Description: A reference to a control by its identifier.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: LocalDefinitions_id Description: Autocreated FK slot
-- # Class: AssessmentMethod Description: A local definition of a control objective.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: part_id Description: An assessment part.
-- # Class: Activity Description: Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended activity.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: LocalDefinitions_id Description: Autocreated FK slot
--     * Slot: related_controls_id Description: A reference to reviewed controls for this activity or step.
-- # Class: Step Description: Identifies an individual step in a series of steps related to an activity, such as an assessment test or examination procedure.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: reviewed_controls_id Description: Identifies the controls being assessed and their control objectives.
-- # Class: Task Description: Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: type Description: Indicates the nature or kind of the containing object.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: AssessmentPlan_id Description: Autocreated FK slot
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: Response_id Description: Autocreated FK slot
--     * Slot: timing_id Description: The timing under which a task is intended to occur.
-- # Class: EventTiming Description: The timing under which the task is intended to occur.
--     * Slot: id
--     * Slot: on_date_id Description: The task is intended to occur on the specified date.
--     * Slot: within_date_range_id Description: The task is intended to occur within the specified date range.
--     * Slot: at_frequency_id Description: The task is intended to occur at the specified frequency.
-- # Class: OnDateCondition Description: The task is intended to occur on the specified date.
--     * Slot: id
--     * Slot: date Description: The date and time when the action occurred.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: WithinDateRange Description: The task is intended to occur within the specified date range.
--     * Slot: id
--     * Slot: start Description: The start date/time.
--     * Slot: end Description: The end date/time.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: AtFrequency Description: The task is intended to occur at the specified frequency.
--     * Slot: id
--     * Slot: period Description: The task must occur every period (in the given units).
--     * Slot: unit Description: The unit of time for the period.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: TaskDependency Description: Used to indicate that a task is dependent on another task.
--     * Slot: id
--     * Slot: task_uuid Description: A UUID reference to a task.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Task_id Description: Autocreated FK slot
-- # Class: AssociatedActivity Description: Identifies an individual activity to be performed as part of a task.
--     * Slot: id
--     * Slot: activity_uuid Description: A UUID reference to an activity.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Task_id Description: Autocreated FK slot
-- # Class: AssessmentPart Description: A partition of an assessment plan or results or a child of another part.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: name Description: A textual label that uniquely identifies an attribute or semantic type.
--     * Slot: ns Description: An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name.
--     * Slot: _class Description: A textual label that provides a sub-type or characterization.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: prose Description: Permits multiple paragraphs, lists, tables etc.
--     * Slot: TermsAndConditions_id Description: Autocreated FK slot
--     * Slot: AssessmentPart_id Description: Autocreated FK slot
-- # Class: ControlPart Description: An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
--     * Slot: uid
--     * Slot: id Description: A unique human-oriented identifier within a particular context.
--     * Slot: name Description: A textual label that uniquely identifies an attribute or semantic type.
--     * Slot: ns Description: An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name.
--     * Slot: _class Description: A textual label that provides a sub-type or characterization.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: prose Description: Permits multiple paragraphs, lists, tables etc.
--     * Slot: LocalObjective_id Description: Autocreated FK slot
--     * Slot: ControlPart_uid Description: Autocreated FK slot
-- # Class: SetParameter Description: Identifies the parameter that will be set by the enclosed value.
--     * Slot: id
--     * Slot: param_id Description: A reference to a parameter by its identifier.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: SystemComponent Description: A defined component that can be part of an implemented system.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: type Description: Indicates the nature or kind of the containing object.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: purpose Description: A summary of the technological or business purpose of the component.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: LocalDefinitions_id Description: Autocreated FK slot
--     * Slot: AssessmentAssets_id Description: Autocreated FK slot
--     * Slot: status_id Description: Indicates the status of the containing object.
-- # Class: ComponentStatus Description: Describes the operational status of the system component.
--     * Slot: id
--     * Slot: state Description: The operational status.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: Protocol Description: Information about the protocol used to provide a service.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: name Description: A textual label that uniquely identifies an attribute or semantic type.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: SystemComponent_id Description: Autocreated FK slot
-- # Class: PortRange Description: Where applicable, the transport layer protocol port range.
--     * Slot: id
--     * Slot: start Description: The start date/time.
--     * Slot: end Description: The end date/time.
--     * Slot: transport Description: Indicates the transport type.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Protocol_id Description: Autocreated FK slot
-- # Class: ImplementationStatus Description: Indicates the degree to which a given control is implemented.
--     * Slot: id
--     * Slot: state Description: Identifies the implementation status of the control or control objective.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: SystemUser Description: A type of user that interacts with the system based on an associated role.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: short_name Description: A short common name, abbreviation, or acronym.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: LocalDefinitions_id Description: Autocreated FK slot
-- # Class: AuthorizedPrivilege Description: Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
--     * Slot: id
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: SystemUser_id Description: Autocreated FK slot
-- # Class: InventoryItem Description: A single managed inventory item within the system.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: LocalDefinitions_id Description: Autocreated FK slot
-- # Class: ImplementedComponent Description: The set of components that are implemented in a given system inventory item.
--     * Slot: id
--     * Slot: component_uuid Description: A UUID reference to a component.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: InventoryItem_id Description: Autocreated FK slot
-- # Class: SystemId Description: A human-oriented, globally unique identifier for a system.
--     * Slot: uid
--     * Slot: id Description: A unique human-oriented identifier within a particular context.
--     * Slot: identifier_type Description: A human-readable label for a specific identifier scheme.
-- # Class: Origin Description: Identifies the source of the finding, such as a tool, interviewed person, or activity.
--     * Slot: id
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: Finding_id Description: Autocreated FK slot
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: Response_id Description: Autocreated FK slot
-- # Class: OriginActor Description: The actor that produces an observation, a finding, or a risk.
--     * Slot: id
--     * Slot: type Description: Indicates the nature or kind of the containing object.
--     * Slot: actor_uuid Description: A machine-oriented identifier reference to the tool or person based on the associated type.
--     * Slot: role_id Description: A reference to a role by its identifier.
--     * Slot: Origin_id Description: Autocreated FK slot
-- # Class: RelatedTask Description: Identifies an individual task for which the containing object is a consequence of.
--     * Slot: id
--     * Slot: task_uuid Description: A UUID reference to a task.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Origin_id Description: Autocreated FK slot
--     * Slot: RiskResponseReference_id Description: Autocreated FK slot
--     * Slot: identified_subject_id Description: Used to detail assessment subjects that were identified by this task.
-- # Class: IdentifiedSubject Description: Used to detail assessment subjects that were identified by this task.
--     * Slot: id
--     * Slot: subject_placeholder_uuid Description: A reference to an assessment subject placeholder defined in the assessment plan.
-- # Class: Observation Description: Describes an individual observation.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: collected Description: Date/time stamp identifying when the finding information was collected.
--     * Slot: expires Description: Date/time identifying when the finding information is no longer considered valid.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: RelevantEvidence Description: Links this observation to relevant evidence.
--     * Slot: id
--     * Slot: href Description: A resolvable URL reference to a resource.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Observation_id Description: Autocreated FK slot
-- # Class: Finding Description: Describes an individual finding.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: implementation_statement_uuid Description: A reference to the implementation statement in the SSP to which this finding is related.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: target_id Description: Identifies the target of a finding.
-- # Class: FindingTarget Description: Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
--     * Slot: id
--     * Slot: type Description: Indicates the nature or kind of the containing object.
--     * Slot: target_id Description: Identifies the specific target qualified by the type.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: implementation_status_id Description: Identifies the implementation status of the control.
--     * Slot: status_id Description: Indicates the status of the containing object.
-- # Class: ObjectiveStatus Description: A determination of if the objective is satisfied or not within a given system.
--     * Slot: id
--     * Slot: state Description: An indication as to whether the objective is satisfied or not.
--     * Slot: reason Description: The reason the objective was given its status.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: RelatedObservation Description: Relates the identified element to a set of referenced observations.
--     * Slot: id
--     * Slot: observation_uuid Description: A machine-oriented identifier reference to an observation defined in the list of observations.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Finding_id Description: Autocreated FK slot
--     * Slot: Risk_id Description: Autocreated FK slot
-- # Class: AssociatedRisk Description: Relates the finding to a set of referenced risks.
--     * Slot: id
--     * Slot: risk_uuid Description: A machine-oriented identifier reference to a risk defined in the list of risks.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Finding_id Description: Autocreated FK slot
-- # Class: Risk Description: An identified risk.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: statement Description: An assessor's summary of the risk, in narrative form.
--     * Slot: deadline Description: The date/time by which the risk must be resolved.
--     * Slot: status Description: Indicates the status of the containing object.
--     * Slot: risk_log_id Description: A log of all risk-related tasks taken.
-- # Class: ThreatId Description: A pointer, by ID, to an externally-defined threat.
--     * Slot: uid
--     * Slot: href Description: A resolvable URL reference to a resource.
--     * Slot: system Description: Specifies the system or scheme from which the identifier originates.
--     * Slot: id Description: A unique human-oriented identifier within a particular context.
--     * Slot: Risk_id Description: Autocreated FK slot
-- # Class: Characterization Description: A collection of descriptive data about the containing object from a specific origin.
--     * Slot: id
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: origin_id Description: The source of the finding.
-- # Class: Facet Description: An individual characteristic that is part of a larger set produced by the same actor.
--     * Slot: id
--     * Slot: name Description: A textual label that uniquely identifies an attribute or semantic type.
--     * Slot: value Description: The value associated with the containing object.
--     * Slot: system Description: Specifies the system or scheme from which the identifier originates.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Characterization_id Description: Autocreated FK slot
-- # Class: MitigatingFactor Description: Describes an existing mitigating factor that may affect the overall determination of the risk.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: description Description: A human-readable description.
--     * Slot: implementation_uuid Description: A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this implementation statement elsewhere in this or other OSCAL instances.
--     * Slot: Risk_id Description: Autocreated FK slot
-- # Class: Response Description: Describes either recommended or an actual plan for addressing the risk.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: lifecycle Description: Identifies whether this is a recommendation or an actual plan.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Risk_id Description: Autocreated FK slot
-- # Class: RequiredAsset Description: Identifies an asset required to achieve remediation.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Response_id Description: Autocreated FK slot
-- # Class: RiskLog Description: A log of all risk-related tasks taken.
--     * Slot: id
-- # Class: RiskLogEntry Description: Identifies an individual risk response that occurred as part of managing an identified risk.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: description Description: A human-readable description.
--     * Slot: start Description: The start date/time.
--     * Slot: end Description: The end date/time.
--     * Slot: status_change Description: Identifies the risk change that prompted the log entry.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: RiskLog_id Description: Autocreated FK slot
-- # Class: LoggedBy Description: Used to indicate who created a log entry in what role.
--     * Slot: id
--     * Slot: party_uuid Description: A machine-oriented identifier reference to the party who is making the log entry.
--     * Slot: role_id Description: A reference to a role by its identifier.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: RiskLogEntry_id Description: Autocreated FK slot
-- # Class: RiskResponseReference Description: Identifies an individual risk response that this log entry is for.
--     * Slot: id
--     * Slot: response_uuid Description: A machine-oriented identifier reference to a unique risk response.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: RiskLogEntry_id Description: Autocreated FK slot
-- # Class: HasPropsAndLinks Description: Mixin providing the props and links slots that are common to many OSCAL objects.
--     * Slot: id
-- # Class: OscalCommon Description: Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
--     * Slot: id
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: HasResponsibleRoles Description: Mixin providing the responsible-roles slot for objects that carry role assignments.
--     * Slot: id
-- # Class: HasResponsibleParties Description: Mixin providing the responsible-parties slot for objects that carry party assignments.
--     * Slot: id
-- # Class: OscalDocument Description: A root wrapper for an OSCAL document, which may be of any OSCAL document type (e.g. Catalog, Profile, Assessment Plan, SSP).
--     * Slot: id
-- # Class: CatalogDocument Description: Root wrapper for an OSCAL Catalog document.
--     * Slot: id
--     * Slot: catalog_id Description: Root catalog document.
-- # Class: Catalog Description: A structured, organized collection of control information.
--     * Slot: id
--     * Slot: uuid Description: Provides a globally unique means to identify a given catalog instance.
--     * Slot: metadata_id Description: Provides information about the containing document, and defines concepts shared across the document.
--     * Slot: back_matter_id Description: A collection of resources that may be referenced from within the OSCAL document instance.
-- # Class: Group Description: A group of controls, or of groups of controls.
--     * Slot: uid
--     * Slot: id Description: Identifies the group for the purpose of cross-linking within the defining instance or from other instances that reference the catalog.
--     * Slot: _class Description: A textual label that provides a sub-type or characterization of the group.
--     * Slot: title Description: A name given to the group, which may be used by a tool for display and navigation.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Catalog_id Description: Autocreated FK slot
--     * Slot: Group_uid Description: Autocreated FK slot
-- # Class: Control Description: A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk related to an information system and its information.
--     * Slot: uid
--     * Slot: id Description: Identifies a control such that it can be referenced in the defining catalog and other OSCAL instances (e.g., profiles).
--     * Slot: _class Description: A textual label that provides a sub-type or characterization of the control.
--     * Slot: title Description: A name given to the control, which may be used by a tool for display and navigation.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Catalog_id Description: Autocreated FK slot
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: Control_uid Description: Autocreated FK slot
-- # Class: Metadata Description: Provides information about the containing document, and defines concepts shared across the document.
--     * Slot: id
--     * Slot: title Description: A name given to the document.
--     * Slot: published Description: The date and time the document was last made available.
--     * Slot: last_modified Description: The date and time the document was last stored for later retrieval.
--     * Slot: version Description: Used to distinguish a specific revision of an OSCAL document.
--     * Slot: oscal_version Description: The OSCAL model version the document was authored against.
--     * Slot: remarks Description: Additional commentary about the containing object.
-- # Class: Revision Description: An entry in a sequential list of revisions to the containing document.
--     * Slot: id
--     * Slot: title Description: A human-readable name or title.
--     * Slot: published Description: The date and time the document was last made available.
--     * Slot: last_modified Description: The date and time the document was last modified.
--     * Slot: version Description: Used to distinguish a specific revision of an OSCAL document from other previous and future versions.
--     * Slot: oscal_version Description: The OSCAL model version the document was authored against and will conform to as valid.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Metadata_id Description: Autocreated FK slot
-- # Class: DocumentId Description: A document identifier qualified by an identifier scheme.
--     * Slot: id
--     * Slot: scheme Description: Qualifies the kind of identifier using a URI.
--     * Slot: identifier Description: A document identifier value.
--     * Slot: Metadata_id Description: Autocreated FK slot
--     * Slot: Resource_id Description: Autocreated FK slot
-- # Class: Role Description: Defines a function, which might be assigned to a party in a specific situation.
--     * Slot: uid
--     * Slot: id Description: A unique identifier for the role.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: short_name Description: A short common name, abbreviation, or acronym.
--     * Slot: description Description: A human-readable description.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Metadata_id Description: Autocreated FK slot
-- # Class: Location Description: A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: title Description: A human-readable name or title.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Metadata_id Description: Autocreated FK slot
--     * Slot: address_id Description: A postal address for the location.
-- # Class: Party Description: An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.
--     * Slot: id
--     * Slot: uuid Description: A machine-oriented, globally unique identifier with a cross-instance scope.
--     * Slot: type Description: A category describing the kind of party the object describes.
--     * Slot: name Description: The full name of the party.
--     * Slot: short_name Description: A short common name, abbreviation, or acronym.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Metadata_id Description: Autocreated FK slot
-- # Class: PartyExternalId Description: An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).
--     * Slot: uid
--     * Slot: scheme Description: Indicates the type of external identifier.
--     * Slot: id Description: A unique human-oriented identifier within a particular context.
--     * Slot: Party_id Description: Autocreated FK slot
-- # Class: ResponsibleParty Description: A reference to a set of persons and/or organizations that have responsibility for performing the referenced role in the context of the containing object.
--     * Slot: id
--     * Slot: role_id Description: A reference to a role performed by a party.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: UsesComponent_id Description: Autocreated FK slot
--     * Slot: InventoryItem_id Description: Autocreated FK slot
--     * Slot: ImplementedComponent_id Description: Autocreated FK slot
--     * Slot: RelatedTask_id Description: Autocreated FK slot
--     * Slot: HasResponsibleParties_id Description: Autocreated FK slot
--     * Slot: Metadata_id Description: Autocreated FK slot
--     * Slot: Action_id Description: Autocreated FK slot
-- # Class: ResponsibleRole Description: A reference to a role with responsibility for performing a function relative to the containing object, optionally associated with a set of persons and/or organizations that perform that role.
--     * Slot: id
--     * Slot: role_id Description: A human-oriented identifier reference to a role performed.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: Step_id Description: Autocreated FK slot
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: AssociatedActivity_id Description: Autocreated FK slot
--     * Slot: SystemComponent_id Description: Autocreated FK slot
--     * Slot: HasResponsibleRoles_id Description: Autocreated FK slot
-- # Class: Action Description: An action applied by a role within a given party to the content.
--     * Slot: id
--     * Slot: uuid Description: A unique identifier that can be used to reference this defined action elsewhere in an OSCAL document.
--     * Slot: type Description: The type of action documented by the assembly, such as an approval.
--     * Slot: date Description: The date and time when the action occurred.
--     * Slot: system Description: Specifies the action type system used.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Metadata_id Description: Autocreated FK slot
-- # Class: TelephoneNumber Description: A telephone service number as defined by ITU-T E.164.
--     * Slot: id
--     * Slot: type Description: Indicates the type of phone number.
--     * Slot: number Description: A telephone number value.
--     * Slot: Location_id Description: Autocreated FK slot
--     * Slot: Party_id Description: Autocreated FK slot
-- # Class: Address Description: A postal address for the location.
--     * Slot: id
--     * Slot: type Description: Indicates the type of address.
--     * Slot: city Description: City, town or geographical region for the mailing address.
--     * Slot: state Description: State, province or analogous geographical region for a mailing address.
--     * Slot: postal_code Description: Postal or ZIP code for mailing address.
--     * Slot: country Description: The ISO 3166-1 alpha-2 country code for the mailing address.
--     * Slot: Party_id Description: Autocreated FK slot
-- # Class: Hash Description: A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
--     * Slot: id
--     * Slot: value Description: The value associated with the containing object.
--     * Slot: algorithm Description: The digest method by which a hash is derived.
--     * Slot: ResourceLink_id Description: Autocreated FK slot
-- # Class: Property Description: An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value pair.
--     * Slot: id
--     * Slot: name Description: A textual label, within a namespace, that identifies a specific attribute, characteristic, or quality of the property's containing object.
--     * Slot: uuid Description: A unique identifier for a property.
--     * Slot: ns Description: A namespace qualifying the property's name. This allows different organizations to associate distinct semantics with the same name.
--     * Slot: value Description: Indicates the value of the attribute, characteristic, or quality.
--     * Slot: _class Description: A textual label that provides a sub-type or characterization of the property's name.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: group Description: An identifier for relating distinct sets of properties.
--     * Slot: ReviewedControls_id Description: Autocreated FK slot
--     * Slot: ControlSelection_id Description: Autocreated FK slot
--     * Slot: ControlObjectiveSelection_id Description: Autocreated FK slot
--     * Slot: AssessmentSubject_id Description: Autocreated FK slot
--     * Slot: SelectSubjectById_id Description: Autocreated FK slot
--     * Slot: SubjectReference_id Description: Autocreated FK slot
--     * Slot: AssessmentSubjectPlaceholder_id Description: Autocreated FK slot
--     * Slot: AssessmentPlatform_id Description: Autocreated FK slot
--     * Slot: UsesComponent_id Description: Autocreated FK slot
--     * Slot: LocalObjective_id Description: Autocreated FK slot
--     * Slot: AssessmentMethod_id Description: Autocreated FK slot
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: Step_id Description: Autocreated FK slot
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: AssociatedActivity_id Description: Autocreated FK slot
--     * Slot: AssessmentPart_id Description: Autocreated FK slot
--     * Slot: ControlPart_uid Description: Autocreated FK slot
--     * Slot: SystemComponent_id Description: Autocreated FK slot
--     * Slot: SystemUser_id Description: Autocreated FK slot
--     * Slot: InventoryItem_id Description: Autocreated FK slot
--     * Slot: ImplementedComponent_id Description: Autocreated FK slot
--     * Slot: OriginActor_id Description: Autocreated FK slot
--     * Slot: RelatedTask_id Description: Autocreated FK slot
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: RelevantEvidence_id Description: Autocreated FK slot
--     * Slot: Finding_id Description: Autocreated FK slot
--     * Slot: FindingTarget_id Description: Autocreated FK slot
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: Characterization_id Description: Autocreated FK slot
--     * Slot: Facet_id Description: Autocreated FK slot
--     * Slot: MitigatingFactor_id Description: Autocreated FK slot
--     * Slot: Response_id Description: Autocreated FK slot
--     * Slot: RequiredAsset_id Description: Autocreated FK slot
--     * Slot: RiskLogEntry_id Description: Autocreated FK slot
--     * Slot: RiskResponseReference_id Description: Autocreated FK slot
--     * Slot: HasPropsAndLinks_id Description: Autocreated FK slot
--     * Slot: OscalCommon_id Description: Autocreated FK slot
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: Control_uid Description: Autocreated FK slot
--     * Slot: Metadata_id Description: Autocreated FK slot
--     * Slot: Revision_id Description: Autocreated FK slot
--     * Slot: Role_uid Description: Autocreated FK slot
--     * Slot: Location_id Description: Autocreated FK slot
--     * Slot: Party_id Description: Autocreated FK slot
--     * Slot: ResponsibleParty_id Description: Autocreated FK slot
--     * Slot: ResponsibleRole_id Description: Autocreated FK slot
--     * Slot: Action_id Description: Autocreated FK slot
--     * Slot: Resource_id Description: Autocreated FK slot
--     * Slot: Citation_id Description: Autocreated FK slot
--     * Slot: Part_uid Description: Autocreated FK slot
--     * Slot: Parameter_uid Description: Autocreated FK slot
-- # Class: Link Description: A reference to a local or remote resource, that has a specific relation to the containing object.
--     * Slot: id
--     * Slot: href Description: A resolvable URL reference to a resource.
--     * Slot: rel Description: Describes the type of relationship provided by the link's hypertext reference. This can be an indicator of the link's purpose.
--     * Slot: resource_fragment Description: In case where the href points to a back-matter/resource, this value will indicate the URI fragment to append to any rlink associated with the resource. This value MUST be URI encoded.
--     * Slot: media_type Description: A label that indicates the nature of a resource, as a data serialization or format.
--     * Slot: text Description: A textual label to associate with the containing object.
--     * Slot: ReviewedControls_id Description: Autocreated FK slot
--     * Slot: ControlSelection_id Description: Autocreated FK slot
--     * Slot: ControlObjectiveSelection_id Description: Autocreated FK slot
--     * Slot: AssessmentSubject_id Description: Autocreated FK slot
--     * Slot: SelectSubjectById_id Description: Autocreated FK slot
--     * Slot: SubjectReference_id Description: Autocreated FK slot
--     * Slot: AssessmentSubjectPlaceholder_id Description: Autocreated FK slot
--     * Slot: AssessmentPlatform_id Description: Autocreated FK slot
--     * Slot: UsesComponent_id Description: Autocreated FK slot
--     * Slot: LocalObjective_id Description: Autocreated FK slot
--     * Slot: AssessmentMethod_id Description: Autocreated FK slot
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: Step_id Description: Autocreated FK slot
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: AssociatedActivity_id Description: Autocreated FK slot
--     * Slot: AssessmentPart_id Description: Autocreated FK slot
--     * Slot: ControlPart_uid Description: Autocreated FK slot
--     * Slot: SystemComponent_id Description: Autocreated FK slot
--     * Slot: SystemUser_id Description: Autocreated FK slot
--     * Slot: InventoryItem_id Description: Autocreated FK slot
--     * Slot: ImplementedComponent_id Description: Autocreated FK slot
--     * Slot: OriginActor_id Description: Autocreated FK slot
--     * Slot: RelatedTask_id Description: Autocreated FK slot
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: RelevantEvidence_id Description: Autocreated FK slot
--     * Slot: Finding_id Description: Autocreated FK slot
--     * Slot: FindingTarget_id Description: Autocreated FK slot
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: Characterization_id Description: Autocreated FK slot
--     * Slot: Facet_id Description: Autocreated FK slot
--     * Slot: MitigatingFactor_id Description: Autocreated FK slot
--     * Slot: Response_id Description: Autocreated FK slot
--     * Slot: RequiredAsset_id Description: Autocreated FK slot
--     * Slot: RiskLogEntry_id Description: Autocreated FK slot
--     * Slot: RiskResponseReference_id Description: Autocreated FK slot
--     * Slot: HasPropsAndLinks_id Description: Autocreated FK slot
--     * Slot: OscalCommon_id Description: Autocreated FK slot
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: Control_uid Description: Autocreated FK slot
--     * Slot: Metadata_id Description: Autocreated FK slot
--     * Slot: Revision_id Description: Autocreated FK slot
--     * Slot: Role_uid Description: Autocreated FK slot
--     * Slot: Location_id Description: Autocreated FK slot
--     * Slot: Party_id Description: Autocreated FK slot
--     * Slot: ResponsibleParty_id Description: Autocreated FK slot
--     * Slot: ResponsibleRole_id Description: Autocreated FK slot
--     * Slot: Action_id Description: Autocreated FK slot
--     * Slot: Citation_id Description: Autocreated FK slot
--     * Slot: Part_uid Description: Autocreated FK slot
--     * Slot: Parameter_uid Description: Autocreated FK slot
-- # Class: BackMatter Description: A collection of resources that may be referenced from within the OSCAL document instance.
--     * Slot: id
-- # Class: Resource Description: A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.
--     * Slot: id
--     * Slot: uuid Description: A unique identifier for a resource.
--     * Slot: title Description: An optional name given to the resource, which may be used by a tool for display and navigation.
--     * Slot: description Description: An optional short summary of the resource used to indicate the purpose of the resource.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: BackMatter_id Description: Autocreated FK slot
--     * Slot: citation_id Description: An optional citation consisting of end note text using structured markup.
--     * Slot: base64_id Description: A resource encoded using the Base64 alphabet defined by RFC 2045.
-- # Class: Citation Description: An optional citation consisting of end note text using structured markup.
--     * Slot: id
--     * Slot: text Description: A line of citation text.
-- # Class: ResourceLink Description: A URL-based pointer to an external resource with an optional hash for verification and change detection.
--     * Slot: id
--     * Slot: href Description: A resolvable URL pointing to the referenced resource.
--     * Slot: media_type Description: A label that indicates the nature of a resource, as a data serialization or format.
--     * Slot: Resource_id Description: Autocreated FK slot
-- # Class: Base64Resource Description: A resource encoded using the Base64 alphabet defined by RFC 2045.
--     * Slot: id
--     * Slot: media_type Description: A label that indicates the nature of a resource, as a data serialization or format.
--     * Slot: value Description: The value associated with the containing object.
--     * Slot: filename Description: Name of the file before it was encoded as Base64 to be embedded in a resource.
-- # Class: Part Description: An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
--     * Slot: uid
--     * Slot: id Description: A unique identifier for the part.
--     * Slot: name Description: A textual label that uniquely identifies the part's semantic type, which exists in a value space qualified by the ns.
--     * Slot: ns Description: An optional namespace qualifying the part's name. This allows different organizations to associate distinct semantics with the same name.
--     * Slot: _class Description: An optional textual providing a sub-type or characterization of the part's name, or a category to which the part belongs.
--     * Slot: title Description: An optional name given to the part, which may be used by a tool for display and navigation.
--     * Slot: prose Description: Permits multiple paragraphs, lists, tables etc.
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: Control_uid Description: Autocreated FK slot
--     * Slot: Part_uid Description: Autocreated FK slot
-- # Class: Parameter Description: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
--     * Slot: uid
--     * Slot: id Description: A unique identifier for the parameter.
--     * Slot: _class Description: A textual label that provides a characterization of the type, purpose, use or scope of the parameter.
--     * Slot: depends_on Description: (deprecated) Another parameter invoking this one. This construct has been deprecated and should not be used.
--     * Slot: label Description: A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned.
--     * Slot: usage Description: Describes the purpose and use of a parameter.
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: Catalog_id Description: Autocreated FK slot
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: Control_uid Description: Autocreated FK slot
--     * Slot: select_id Description: Presenting a choice among alternatives.
-- # Class: ParameterConstraint Description: A formal or informal expression of a constraint or test.
--     * Slot: id
--     * Slot: description Description: A textual summary of the constraint to be applied.
--     * Slot: Parameter_uid Description: Autocreated FK slot
-- # Class: ConstraintTest Description: A test expression which is expected to be evaluated by a tool.
--     * Slot: id
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: expression Description: A formal (executable) expression of a constraint.
--     * Slot: ParameterConstraint_id Description: Autocreated FK slot
-- # Class: ParameterGuideline Description: A prose statement that provides a recommendation for the use of a parameter.
--     * Slot: id
--     * Slot: prose Description: Prose permits multiple paragraphs, lists, tables etc.
--     * Slot: Parameter_uid Description: Autocreated FK slot
-- # Class: ParameterSelection Description: Presenting a choice among alternatives.
--     * Slot: id
--     * Slot: how_many Description: Describes the number of selections that must occur. Without this setting, only one value should be assumed to be permitted.
-- # Class: IncludeAll Description: Include all controls from the imported catalog or profile resources.
--     * Slot: id
-- # Class: ControlMatching Description: Selecting a set of controls by matching their IDs with a wildcard pattern.
--     * Slot: id
--     * Slot: remarks Description: Additional commentary about the containing object.
--     * Slot: pattern Description: A glob expression matching the IDs of one or more controls to be selected.
--     * Slot: SelectControlById_id Description: Autocreated FK slot
-- # Class: SelectControlById Description: Select a control or controls from an imported control set.
--     * Slot: id
--     * Slot: with_child_controls Description: When a control is included, whether its child (dependent) controls are also included.
-- # Class: AssessmentSelectControlById_statement_ids
--     * Slot: AssessmentSelectControlById_id Description: Autocreated FK slot
--     * Slot: statement_ids Description: Statement IDs for control selection.
-- # Class: SetParameter_values
--     * Slot: SetParameter_id Description: Autocreated FK slot
--     * Slot: values Description: A parameter value or set of values.
-- # Class: SystemUser_role_ids
--     * Slot: SystemUser_id Description: Autocreated FK slot
--     * Slot: role_ids Description: Role identifiers associated with the user.
-- # Class: AuthorizedPrivilege_functions_performed
--     * Slot: AuthorizedPrivilege_id Description: Autocreated FK slot
--     * Slot: functions_performed Description: Describes a function performed for a given authorized privilege.
-- # Class: Observation_methods
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: methods Description: Identifies how the observation was made.
-- # Class: Observation_types
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: types Description: Identifies the nature of the observation.
-- # Class: Location_email_addresses
--     * Slot: Location_id Description: Autocreated FK slot
--     * Slot: email_addresses Description: Email addresses associated with the containing object.
-- # Class: Location_urls
--     * Slot: Location_id Description: Autocreated FK slot
--     * Slot: urls Description: The uniform resource locator (URL) for a web site or other resource associated with the location.
-- # Class: Party_email_addresses
--     * Slot: Party_id Description: Autocreated FK slot
--     * Slot: email_addresses Description: Email addresses associated with the containing object.
-- # Class: Party_location_uuids
--     * Slot: Party_id Description: Autocreated FK slot
--     * Slot: location_uuids Description: Reference to a location by UUID.
-- # Class: Party_member_of_organizations
--     * Slot: Party_id Description: Autocreated FK slot
--     * Slot: member_of_organizations Description: A reference to another party by UUID, typically an organization, that this subject is associated with.
-- # Class: ResponsibleParty_party_uuids
--     * Slot: ResponsibleParty_id Description: Autocreated FK slot
--     * Slot: party_uuids Description: References to party UUIDs.
-- # Class: ResponsibleRole_party_uuids
--     * Slot: ResponsibleRole_id Description: Autocreated FK slot
--     * Slot: party_uuids Description: References to party UUIDs.
-- # Class: Address_addr_lines
--     * Slot: Address_id Description: Autocreated FK slot
--     * Slot: addr_lines Description: A single line of an address.
-- # Class: Parameter_values
--     * Slot: Parameter_uid Description: Autocreated FK slot
--     * Slot: values Description: A parameter value or set of values.
-- # Class: ParameterSelection_choice
--     * Slot: ParameterSelection_id Description: Autocreated FK slot
--     * Slot: choice Description: A value selection among several such options.
-- # Class: SelectControlById_with_ids
--     * Slot: SelectControlById_id Description: Autocreated FK slot
--     * Slot: with_ids Description: Selecting a control by its ID given as a literal.

CREATE TABLE "ImportSSP" (
	id INTEGER NOT NULL,
	href TEXT NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ImportSSP_id" ON "ImportSSP" (id);

CREATE TABLE "LocalDefinitions" (
	id INTEGER NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LocalDefinitions_id" ON "LocalDefinitions" (id);

CREATE TABLE "TermsAndConditions" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TermsAndConditions_id" ON "TermsAndConditions" (id);

CREATE TABLE "ReviewedControls" (
	id INTEGER NOT NULL,
	description TEXT,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ReviewedControls_id" ON "ReviewedControls" (id);

CREATE TABLE "AssessmentSubjectPlaceholder" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	description TEXT,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AssessmentSubjectPlaceholder_id" ON "AssessmentSubjectPlaceholder" (id);

CREATE TABLE "AssessmentAssets" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AssessmentAssets_id" ON "AssessmentAssets" (id);

CREATE TABLE "OnDateCondition" (
	id INTEGER NOT NULL,
	date TEXT NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OnDateCondition_id" ON "OnDateCondition" (id);

CREATE TABLE "WithinDateRange" (
	id INTEGER NOT NULL,
	start TEXT NOT NULL,
	"end" TEXT NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_WithinDateRange_id" ON "WithinDateRange" (id);

CREATE TABLE "AtFrequency" (
	id INTEGER NOT NULL,
	period INTEGER NOT NULL,
	unit VARCHAR(7) NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AtFrequency_id" ON "AtFrequency" (id);

CREATE TABLE "SetParameter" (
	id INTEGER NOT NULL,
	param_id TEXT NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SetParameter_id" ON "SetParameter" (id);

CREATE TABLE "ComponentStatus" (
	id INTEGER NOT NULL,
	state VARCHAR(17) NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ComponentStatus_id" ON "ComponentStatus" (id);

CREATE TABLE "ImplementationStatus" (
	id INTEGER NOT NULL,
	state VARCHAR(14) NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ImplementationStatus_id" ON "ImplementationStatus" (id);

CREATE TABLE "SystemId" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	identifier_type TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_SystemId_uid" ON "SystemId" (uid);

CREATE TABLE "IdentifiedSubject" (
	id INTEGER NOT NULL,
	subject_placeholder_uuid TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IdentifiedSubject_id" ON "IdentifiedSubject" (id);

CREATE TABLE "Observation" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	description TEXT NOT NULL,
	collected TEXT NOT NULL,
	expires TEXT,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Observation_id" ON "Observation" (id);

CREATE TABLE "ObjectiveStatus" (
	id INTEGER NOT NULL,
	state VARCHAR(13) NOT NULL,
	reason VARCHAR(5),
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ObjectiveStatus_id" ON "ObjectiveStatus" (id);

CREATE TABLE "RiskLog" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RiskLog_id" ON "RiskLog" (id);

CREATE TABLE "HasPropsAndLinks" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HasPropsAndLinks_id" ON "HasPropsAndLinks" (id);

CREATE TABLE "OscalCommon" (
	id INTEGER NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OscalCommon_id" ON "OscalCommon" (id);

CREATE TABLE "HasResponsibleRoles" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HasResponsibleRoles_id" ON "HasResponsibleRoles" (id);

CREATE TABLE "HasResponsibleParties" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HasResponsibleParties_id" ON "HasResponsibleParties" (id);

CREATE TABLE "OscalDocument" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_OscalDocument_id" ON "OscalDocument" (id);

CREATE TABLE "Metadata" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	published TEXT,
	last_modified TEXT NOT NULL,
	version TEXT NOT NULL,
	oscal_version TEXT NOT NULL,
	remarks TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Metadata_id" ON "Metadata" (id);

CREATE TABLE "BackMatter" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BackMatter_id" ON "BackMatter" (id);

CREATE TABLE "Citation" (
	id INTEGER NOT NULL,
	text TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Citation_id" ON "Citation" (id);

CREATE TABLE "Base64Resource" (
	id INTEGER NOT NULL,
	media_type TEXT,
	value TEXT NOT NULL,
	filename TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Base64Resource_id" ON "Base64Resource" (id);

CREATE TABLE "ParameterSelection" (
	id INTEGER NOT NULL,
	how_many VARCHAR(11),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ParameterSelection_id" ON "ParameterSelection" (id);

CREATE TABLE "IncludeAll" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_IncludeAll_id" ON "IncludeAll" (id);

CREATE TABLE "SelectControlById" (
	id INTEGER NOT NULL,
	with_child_controls VARCHAR(5),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SelectControlById_id" ON "SelectControlById" (id);

CREATE TABLE "AssessmentPlan" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	metadata_id INTEGER NOT NULL,
	import_ssp_id INTEGER NOT NULL,
	local_definitions_id INTEGER,
	terms_and_conditions_id INTEGER,
	assessment_assets_id INTEGER,
	reviewed_controls_id INTEGER NOT NULL,
	back_matter_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "Metadata" (id),
	FOREIGN KEY(import_ssp_id) REFERENCES "ImportSSP" (id),
	FOREIGN KEY(local_definitions_id) REFERENCES "LocalDefinitions" (id),
	FOREIGN KEY(terms_and_conditions_id) REFERENCES "TermsAndConditions" (id),
	FOREIGN KEY(assessment_assets_id) REFERENCES "AssessmentAssets" (id),
	FOREIGN KEY(reviewed_controls_id) REFERENCES "ReviewedControls" (id),
	FOREIGN KEY(back_matter_id) REFERENCES "BackMatter" (id)
);
CREATE INDEX "ix_AssessmentPlan_id" ON "AssessmentPlan" (id);

CREATE TABLE "ControlSelection" (
	id INTEGER NOT NULL,
	description TEXT,
	remarks TEXT,
	"ReviewedControls_id" INTEGER,
	include_all_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReviewedControls_id") REFERENCES "ReviewedControls" (id),
	FOREIGN KEY(include_all_id) REFERENCES "IncludeAll" (id)
);
CREATE INDEX "ix_ControlSelection_id" ON "ControlSelection" (id);

CREATE TABLE "ControlObjectiveSelection" (
	id INTEGER NOT NULL,
	description TEXT,
	remarks TEXT,
	"ReviewedControls_id" INTEGER,
	include_all_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReviewedControls_id") REFERENCES "ReviewedControls" (id),
	FOREIGN KEY(include_all_id) REFERENCES "IncludeAll" (id)
);
CREATE INDEX "ix_ControlObjectiveSelection_id" ON "ControlObjectiveSelection" (id);

CREATE TABLE "AssessmentSubjectSource" (
	id INTEGER NOT NULL,
	task_uuid TEXT NOT NULL,
	remarks TEXT,
	"AssessmentSubjectPlaceholder_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AssessmentSubjectPlaceholder_id") REFERENCES "AssessmentSubjectPlaceholder" (id)
);
CREATE INDEX "ix_AssessmentSubjectSource_id" ON "AssessmentSubjectSource" (id);

CREATE TABLE "AssessmentPlatform" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	remarks TEXT,
	"AssessmentAssets_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AssessmentAssets_id") REFERENCES "AssessmentAssets" (id)
);
CREATE INDEX "ix_AssessmentPlatform_id" ON "AssessmentPlatform" (id);

CREATE TABLE "LocalObjective" (
	id INTEGER NOT NULL,
	control_id TEXT NOT NULL,
	description TEXT,
	remarks TEXT,
	"LocalDefinitions_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("LocalDefinitions_id") REFERENCES "LocalDefinitions" (id)
);
CREATE INDEX "ix_LocalObjective_id" ON "LocalObjective" (id);

CREATE TABLE "Activity" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	description TEXT NOT NULL,
	remarks TEXT,
	"LocalDefinitions_id" INTEGER,
	related_controls_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("LocalDefinitions_id") REFERENCES "LocalDefinitions" (id),
	FOREIGN KEY(related_controls_id) REFERENCES "ReviewedControls" (id)
);
CREATE INDEX "ix_Activity_id" ON "Activity" (id);

CREATE TABLE "EventTiming" (
	id INTEGER NOT NULL,
	on_date_id INTEGER,
	within_date_range_id INTEGER,
	at_frequency_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(on_date_id) REFERENCES "OnDateCondition" (id),
	FOREIGN KEY(within_date_range_id) REFERENCES "WithinDateRange" (id),
	FOREIGN KEY(at_frequency_id) REFERENCES "AtFrequency" (id)
);
CREATE INDEX "ix_EventTiming_id" ON "EventTiming" (id);

CREATE TABLE "AssessmentPart" (
	id INTEGER NOT NULL,
	uuid TEXT,
	name VARCHAR(9) NOT NULL,
	ns TEXT,
	_class TEXT,
	title TEXT,
	prose TEXT,
	"TermsAndConditions_id" INTEGER,
	"AssessmentPart_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("TermsAndConditions_id") REFERENCES "TermsAndConditions" (id),
	FOREIGN KEY("AssessmentPart_id") REFERENCES "AssessmentPart" (id)
);
CREATE INDEX "ix_AssessmentPart_id" ON "AssessmentPart" (id);

CREATE TABLE "SystemComponent" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	type VARCHAR(17) NOT NULL,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	purpose TEXT,
	remarks TEXT,
	"LocalDefinitions_id" INTEGER,
	"AssessmentAssets_id" INTEGER,
	status_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("LocalDefinitions_id") REFERENCES "LocalDefinitions" (id),
	FOREIGN KEY("AssessmentAssets_id") REFERENCES "AssessmentAssets" (id),
	FOREIGN KEY(status_id) REFERENCES "ComponentStatus" (id)
);
CREATE INDEX "ix_SystemComponent_id" ON "SystemComponent" (id);

CREATE TABLE "SystemUser" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	short_name TEXT,
	description TEXT,
	remarks TEXT,
	"LocalDefinitions_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("LocalDefinitions_id") REFERENCES "LocalDefinitions" (id)
);
CREATE INDEX "ix_SystemUser_id" ON "SystemUser" (id);

CREATE TABLE "InventoryItem" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	description TEXT NOT NULL,
	remarks TEXT,
	"LocalDefinitions_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("LocalDefinitions_id") REFERENCES "LocalDefinitions" (id)
);
CREATE INDEX "ix_InventoryItem_id" ON "InventoryItem" (id);

CREATE TABLE "RelevantEvidence" (
	id INTEGER NOT NULL,
	href TEXT,
	description TEXT NOT NULL,
	remarks TEXT,
	"Observation_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id)
);
CREATE INDEX "ix_RelevantEvidence_id" ON "RelevantEvidence" (id);

CREATE TABLE "FindingTarget" (
	id INTEGER NOT NULL,
	type VARCHAR(12) NOT NULL,
	target_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	remarks TEXT,
	implementation_status_id INTEGER,
	status_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(implementation_status_id) REFERENCES "ImplementationStatus" (id),
	FOREIGN KEY(status_id) REFERENCES "ObjectiveStatus" (id)
);
CREATE INDEX "ix_FindingTarget_id" ON "FindingTarget" (id);

CREATE TABLE "Risk" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	statement TEXT NOT NULL,
	deadline TEXT,
	status VARCHAR(19) NOT NULL,
	risk_log_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(risk_log_id) REFERENCES "RiskLog" (id)
);
CREATE INDEX "ix_Risk_id" ON "Risk" (id);

CREATE TABLE "RiskLogEntry" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	description TEXT,
	start TEXT NOT NULL,
	"end" TEXT,
	status_change VARCHAR(19),
	remarks TEXT,
	"RiskLog_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RiskLog_id") REFERENCES "RiskLog" (id)
);
CREATE INDEX "ix_RiskLogEntry_id" ON "RiskLogEntry" (id);

CREATE TABLE "Catalog" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	metadata_id INTEGER NOT NULL,
	back_matter_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "Metadata" (id),
	FOREIGN KEY(back_matter_id) REFERENCES "BackMatter" (id)
);
CREATE INDEX "ix_Catalog_id" ON "Catalog" (id);

CREATE TABLE "Revision" (
	id INTEGER NOT NULL,
	title TEXT,
	published TEXT,
	last_modified TEXT,
	version TEXT NOT NULL,
	oscal_version TEXT,
	remarks TEXT,
	"Metadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id)
);
CREATE INDEX "ix_Revision_id" ON "Revision" (id);

CREATE TABLE "Role" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	title TEXT NOT NULL,
	short_name TEXT,
	description TEXT,
	remarks TEXT,
	"Metadata_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id)
);
CREATE INDEX "ix_Role_uid" ON "Role" (uid);

CREATE TABLE "Party" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	type VARCHAR(12) NOT NULL,
	name TEXT,
	short_name TEXT,
	remarks TEXT,
	"Metadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id)
);
CREATE INDEX "ix_Party_id" ON "Party" (id);

CREATE TABLE "Action" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	type TEXT NOT NULL,
	date TEXT,
	system TEXT NOT NULL,
	remarks TEXT,
	"Metadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id)
);
CREATE INDEX "ix_Action_id" ON "Action" (id);

CREATE TABLE "Resource" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	description TEXT,
	remarks TEXT,
	"BackMatter_id" INTEGER,
	citation_id INTEGER,
	base64_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BackMatter_id") REFERENCES "BackMatter" (id),
	FOREIGN KEY(citation_id) REFERENCES "Citation" (id),
	FOREIGN KEY(base64_id) REFERENCES "Base64Resource" (id)
);
CREATE INDEX "ix_Resource_id" ON "Resource" (id);

CREATE TABLE "ControlMatching" (
	id INTEGER NOT NULL,
	remarks TEXT,
	pattern TEXT,
	"SelectControlById_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SelectControlById_id") REFERENCES "SelectControlById" (id)
);
CREATE INDEX "ix_ControlMatching_id" ON "ControlMatching" (id);

CREATE TABLE "SetParameter_values" (
	"SetParameter_id" INTEGER,
	"values" TEXT NOT NULL,
	PRIMARY KEY ("SetParameter_id", "values"),
	FOREIGN KEY("SetParameter_id") REFERENCES "SetParameter" (id)
);
CREATE INDEX "ix_SetParameter_values_SetParameter_id" ON "SetParameter_values" ("SetParameter_id");
CREATE INDEX "ix_SetParameter_values_values" ON "SetParameter_values" ("values");

CREATE TABLE "Observation_methods" (
	"Observation_id" INTEGER,
	methods VARCHAR(9) NOT NULL,
	PRIMARY KEY ("Observation_id", methods),
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id)
);
CREATE INDEX "ix_Observation_methods_methods" ON "Observation_methods" (methods);
CREATE INDEX "ix_Observation_methods_Observation_id" ON "Observation_methods" ("Observation_id");

CREATE TABLE "Observation_types" (
	"Observation_id" INTEGER,
	types VARCHAR(19),
	PRIMARY KEY ("Observation_id", types),
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id)
);
CREATE INDEX "ix_Observation_types_types" ON "Observation_types" (types);
CREATE INDEX "ix_Observation_types_Observation_id" ON "Observation_types" ("Observation_id");

CREATE TABLE "ParameterSelection_choice" (
	"ParameterSelection_id" INTEGER,
	choice TEXT,
	PRIMARY KEY ("ParameterSelection_id", choice),
	FOREIGN KEY("ParameterSelection_id") REFERENCES "ParameterSelection" (id)
);
CREATE INDEX "ix_ParameterSelection_choice_ParameterSelection_id" ON "ParameterSelection_choice" ("ParameterSelection_id");
CREATE INDEX "ix_ParameterSelection_choice_choice" ON "ParameterSelection_choice" (choice);

CREATE TABLE "SelectControlById_with_ids" (
	"SelectControlById_id" INTEGER,
	with_ids TEXT,
	PRIMARY KEY ("SelectControlById_id", with_ids),
	FOREIGN KEY("SelectControlById_id") REFERENCES "SelectControlById" (id)
);
CREATE INDEX "ix_SelectControlById_with_ids_SelectControlById_id" ON "SelectControlById_with_ids" ("SelectControlById_id");
CREATE INDEX "ix_SelectControlById_with_ids_with_ids" ON "SelectControlById_with_ids" (with_ids);

CREATE TABLE "AssessmentPlanDocument" (
	id INTEGER NOT NULL,
	assessment_plan_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(assessment_plan_id) REFERENCES "AssessmentPlan" (id)
);
CREATE INDEX "ix_AssessmentPlanDocument_id" ON "AssessmentPlanDocument" (id);

CREATE TABLE "AssessmentSelectControlById" (
	id INTEGER NOT NULL,
	control_id TEXT NOT NULL,
	"ControlSelection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ControlSelection_id") REFERENCES "ControlSelection" (id)
);
CREATE INDEX "ix_AssessmentSelectControlById_id" ON "AssessmentSelectControlById" (id);

CREATE TABLE "SelectObjectiveById" (
	id INTEGER NOT NULL,
	objective_id TEXT NOT NULL,
	remarks TEXT,
	"ControlObjectiveSelection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ControlObjectiveSelection_id") REFERENCES "ControlObjectiveSelection" (id)
);
CREATE INDEX "ix_SelectObjectiveById_id" ON "SelectObjectiveById" (id);

CREATE TABLE "UsesComponent" (
	id INTEGER NOT NULL,
	component_uuid TEXT NOT NULL,
	remarks TEXT,
	"AssessmentPlatform_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AssessmentPlatform_id") REFERENCES "AssessmentPlatform" (id)
);
CREATE INDEX "ix_UsesComponent_id" ON "UsesComponent" (id);

CREATE TABLE "AssessmentMethod" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	description TEXT,
	remarks TEXT,
	part_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(part_id) REFERENCES "AssessmentPart" (id)
);
CREATE INDEX "ix_AssessmentMethod_id" ON "AssessmentMethod" (id);

CREATE TABLE "Step" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	description TEXT NOT NULL,
	remarks TEXT,
	"Activity_id" INTEGER,
	reviewed_controls_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY(reviewed_controls_id) REFERENCES "ReviewedControls" (id)
);
CREATE INDEX "ix_Step_id" ON "Step" (id);

CREATE TABLE "ControlPart" (
	uid INTEGER NOT NULL,
	id TEXT,
	name TEXT NOT NULL,
	ns TEXT,
	_class TEXT,
	title TEXT,
	prose TEXT,
	"LocalObjective_id" INTEGER,
	"ControlPart_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("LocalObjective_id") REFERENCES "LocalObjective" (id),
	FOREIGN KEY("ControlPart_uid") REFERENCES "ControlPart" (uid)
);
CREATE INDEX "ix_ControlPart_uid" ON "ControlPart" (uid);

CREATE TABLE "Protocol" (
	id INTEGER NOT NULL,
	uuid TEXT,
	name TEXT NOT NULL,
	title TEXT,
	"SystemComponent_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SystemComponent_id") REFERENCES "SystemComponent" (id)
);
CREATE INDEX "ix_Protocol_id" ON "Protocol" (id);

CREATE TABLE "AuthorizedPrivilege" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"SystemUser_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SystemUser_id") REFERENCES "SystemUser" (id)
);
CREATE INDEX "ix_AuthorizedPrivilege_id" ON "AuthorizedPrivilege" (id);

CREATE TABLE "ImplementedComponent" (
	id INTEGER NOT NULL,
	component_uuid TEXT NOT NULL,
	remarks TEXT,
	"InventoryItem_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InventoryItem_id") REFERENCES "InventoryItem" (id)
);
CREATE INDEX "ix_ImplementedComponent_id" ON "ImplementedComponent" (id);

CREATE TABLE "Finding" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	implementation_statement_uuid TEXT,
	remarks TEXT,
	target_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(target_id) REFERENCES "FindingTarget" (id)
);
CREATE INDEX "ix_Finding_id" ON "Finding" (id);

CREATE TABLE "ThreatId" (
	uid INTEGER NOT NULL,
	href TEXT,
	system TEXT NOT NULL,
	id TEXT NOT NULL,
	"Risk_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id)
);
CREATE INDEX "ix_ThreatId_uid" ON "ThreatId" (uid);

CREATE TABLE "MitigatingFactor" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	description TEXT NOT NULL,
	implementation_uuid TEXT,
	"Risk_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id)
);
CREATE INDEX "ix_MitigatingFactor_id" ON "MitigatingFactor" (id);

CREATE TABLE "Response" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT NOT NULL,
	lifecycle VARCHAR(14) NOT NULL,
	remarks TEXT,
	"Risk_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id)
);
CREATE INDEX "ix_Response_id" ON "Response" (id);

CREATE TABLE "LoggedBy" (
	id INTEGER NOT NULL,
	party_uuid TEXT NOT NULL,
	role_id TEXT,
	remarks TEXT,
	"RiskLogEntry_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RiskLogEntry_id") REFERENCES "RiskLogEntry" (id)
);
CREATE INDEX "ix_LoggedBy_id" ON "LoggedBy" (id);

CREATE TABLE "RiskResponseReference" (
	id INTEGER NOT NULL,
	response_uuid TEXT NOT NULL,
	remarks TEXT,
	"RiskLogEntry_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("RiskLogEntry_id") REFERENCES "RiskLogEntry" (id)
);
CREATE INDEX "ix_RiskResponseReference_id" ON "RiskResponseReference" (id);

CREATE TABLE "CatalogDocument" (
	id INTEGER NOT NULL,
	catalog_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(catalog_id) REFERENCES "Catalog" (id)
);
CREATE INDEX "ix_CatalogDocument_id" ON "CatalogDocument" (id);

CREATE TABLE "Group" (
	uid INTEGER NOT NULL,
	id TEXT,
	_class TEXT,
	title TEXT NOT NULL,
	remarks TEXT,
	"Catalog_id" INTEGER,
	"Group_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Catalog_id") REFERENCES "Catalog" (id),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid)
);
CREATE INDEX "ix_Group_uid" ON "Group" (uid);

CREATE TABLE "DocumentId" (
	id INTEGER NOT NULL,
	scheme TEXT,
	identifier TEXT NOT NULL,
	"Metadata_id" INTEGER,
	"Resource_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id),
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_DocumentId_id" ON "DocumentId" (id);

CREATE TABLE "PartyExternalId" (
	uid INTEGER NOT NULL,
	scheme TEXT NOT NULL,
	id TEXT NOT NULL,
	"Party_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_PartyExternalId_uid" ON "PartyExternalId" (uid);

CREATE TABLE "Address" (
	id INTEGER NOT NULL,
	type VARCHAR(4),
	city TEXT,
	state TEXT,
	postal_code TEXT,
	country TEXT,
	"Party_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_Address_id" ON "Address" (id);

CREATE TABLE "ResourceLink" (
	id INTEGER NOT NULL,
	href TEXT NOT NULL,
	media_type TEXT,
	"Resource_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_ResourceLink_id" ON "ResourceLink" (id);

CREATE TABLE "SystemUser_role_ids" (
	"SystemUser_id" INTEGER,
	role_ids TEXT,
	PRIMARY KEY ("SystemUser_id", role_ids),
	FOREIGN KEY("SystemUser_id") REFERENCES "SystemUser" (id)
);
CREATE INDEX "ix_SystemUser_role_ids_SystemUser_id" ON "SystemUser_role_ids" ("SystemUser_id");
CREATE INDEX "ix_SystemUser_role_ids_role_ids" ON "SystemUser_role_ids" (role_ids);

CREATE TABLE "Party_email_addresses" (
	"Party_id" INTEGER,
	email_addresses TEXT,
	PRIMARY KEY ("Party_id", email_addresses),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_Party_email_addresses_Party_id" ON "Party_email_addresses" ("Party_id");
CREATE INDEX "ix_Party_email_addresses_email_addresses" ON "Party_email_addresses" (email_addresses);

CREATE TABLE "Party_location_uuids" (
	"Party_id" INTEGER,
	location_uuids TEXT,
	PRIMARY KEY ("Party_id", location_uuids),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_Party_location_uuids_Party_id" ON "Party_location_uuids" ("Party_id");
CREATE INDEX "ix_Party_location_uuids_location_uuids" ON "Party_location_uuids" (location_uuids);

CREATE TABLE "Party_member_of_organizations" (
	"Party_id" INTEGER,
	member_of_organizations TEXT,
	PRIMARY KEY ("Party_id", member_of_organizations),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_Party_member_of_organizations_member_of_organizations" ON "Party_member_of_organizations" (member_of_organizations);
CREATE INDEX "ix_Party_member_of_organizations_Party_id" ON "Party_member_of_organizations" ("Party_id");

CREATE TABLE "Task" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	type VARCHAR(9) NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	remarks TEXT,
	"AssessmentPlan_id" INTEGER,
	"Task_id" INTEGER,
	"Response_id" INTEGER,
	timing_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AssessmentPlan_id") REFERENCES "AssessmentPlan" (id),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id),
	FOREIGN KEY("Response_id") REFERENCES "Response" (id),
	FOREIGN KEY(timing_id) REFERENCES "EventTiming" (id)
);
CREATE INDEX "ix_Task_id" ON "Task" (id);

CREATE TABLE "PortRange" (
	id INTEGER NOT NULL,
	start INTEGER,
	"end" INTEGER,
	transport VARCHAR(3),
	remarks TEXT,
	"Protocol_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Protocol_id") REFERENCES "Protocol" (id)
);
CREATE INDEX "ix_PortRange_id" ON "PortRange" (id);

CREATE TABLE "Origin" (
	id INTEGER NOT NULL,
	"Observation_id" INTEGER,
	"Finding_id" INTEGER,
	"Risk_id" INTEGER,
	"Response_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id),
	FOREIGN KEY("Finding_id") REFERENCES "Finding" (id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id),
	FOREIGN KEY("Response_id") REFERENCES "Response" (id)
);
CREATE INDEX "ix_Origin_id" ON "Origin" (id);

CREATE TABLE "RelatedObservation" (
	id INTEGER NOT NULL,
	observation_uuid TEXT NOT NULL,
	remarks TEXT,
	"Finding_id" INTEGER,
	"Risk_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Finding_id") REFERENCES "Finding" (id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id)
);
CREATE INDEX "ix_RelatedObservation_id" ON "RelatedObservation" (id);

CREATE TABLE "AssociatedRisk" (
	id INTEGER NOT NULL,
	risk_uuid TEXT NOT NULL,
	remarks TEXT,
	"Finding_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Finding_id") REFERENCES "Finding" (id)
);
CREATE INDEX "ix_AssociatedRisk_id" ON "AssociatedRisk" (id);

CREATE TABLE "RequiredAsset" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	description TEXT NOT NULL,
	remarks TEXT,
	"Response_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Response_id") REFERENCES "Response" (id)
);
CREATE INDEX "ix_RequiredAsset_id" ON "RequiredAsset" (id);

CREATE TABLE "Control" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	_class TEXT,
	title TEXT NOT NULL,
	remarks TEXT,
	"Catalog_id" INTEGER,
	"Group_uid" INTEGER,
	"Control_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Catalog_id") REFERENCES "Catalog" (id),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid)
);
CREATE INDEX "ix_Control_uid" ON "Control" (uid);

CREATE TABLE "Location" (
	id INTEGER NOT NULL,
	uuid TEXT NOT NULL,
	title TEXT,
	remarks TEXT,
	"Metadata_id" INTEGER,
	address_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id),
	FOREIGN KEY(address_id) REFERENCES "Address" (id)
);
CREATE INDEX "ix_Location_id" ON "Location" (id);

CREATE TABLE "Hash" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	algorithm VARCHAR(8) NOT NULL,
	"ResourceLink_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ResourceLink_id") REFERENCES "ResourceLink" (id)
);
CREATE INDEX "ix_Hash_id" ON "Hash" (id);

CREATE TABLE "AssessmentSelectControlById_statement_ids" (
	"AssessmentSelectControlById_id" INTEGER,
	statement_ids TEXT,
	PRIMARY KEY ("AssessmentSelectControlById_id", statement_ids),
	FOREIGN KEY("AssessmentSelectControlById_id") REFERENCES "AssessmentSelectControlById" (id)
);
CREATE INDEX "ix_AssessmentSelectControlById_statement_ids_statement_ids" ON "AssessmentSelectControlById_statement_ids" (statement_ids);
CREATE INDEX "ix_AssessmentSelectControlById_statement_ids_AssessmentSelectControlById_id" ON "AssessmentSelectControlById_statement_ids" ("AssessmentSelectControlById_id");

CREATE TABLE "AuthorizedPrivilege_functions_performed" (
	"AuthorizedPrivilege_id" INTEGER,
	functions_performed TEXT NOT NULL,
	PRIMARY KEY ("AuthorizedPrivilege_id", functions_performed),
	FOREIGN KEY("AuthorizedPrivilege_id") REFERENCES "AuthorizedPrivilege" (id)
);
CREATE INDEX "ix_AuthorizedPrivilege_functions_performed_AuthorizedPrivilege_id" ON "AuthorizedPrivilege_functions_performed" ("AuthorizedPrivilege_id");
CREATE INDEX "ix_AuthorizedPrivilege_functions_performed_functions_performed" ON "AuthorizedPrivilege_functions_performed" (functions_performed);

CREATE TABLE "Address_addr_lines" (
	"Address_id" INTEGER,
	addr_lines TEXT,
	PRIMARY KEY ("Address_id", addr_lines),
	FOREIGN KEY("Address_id") REFERENCES "Address" (id)
);
CREATE INDEX "ix_Address_addr_lines_Address_id" ON "Address_addr_lines" ("Address_id");
CREATE INDEX "ix_Address_addr_lines_addr_lines" ON "Address_addr_lines" (addr_lines);

CREATE TABLE "SubjectReference" (
	id INTEGER NOT NULL,
	subject_uuid TEXT NOT NULL,
	type VARCHAR(14) NOT NULL,
	title TEXT,
	remarks TEXT,
	"Observation_id" INTEGER,
	"MitigatingFactor_id" INTEGER,
	"RequiredAsset_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id),
	FOREIGN KEY("MitigatingFactor_id") REFERENCES "MitigatingFactor" (id),
	FOREIGN KEY("RequiredAsset_id") REFERENCES "RequiredAsset" (id)
);
CREATE INDEX "ix_SubjectReference_id" ON "SubjectReference" (id);

CREATE TABLE "TaskDependency" (
	id INTEGER NOT NULL,
	task_uuid TEXT NOT NULL,
	remarks TEXT,
	"Task_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id)
);
CREATE INDEX "ix_TaskDependency_id" ON "TaskDependency" (id);

CREATE TABLE "AssociatedActivity" (
	id INTEGER NOT NULL,
	activity_uuid TEXT NOT NULL,
	remarks TEXT,
	"Task_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id)
);
CREATE INDEX "ix_AssociatedActivity_id" ON "AssociatedActivity" (id);

CREATE TABLE "OriginActor" (
	id INTEGER NOT NULL,
	type VARCHAR(19) NOT NULL,
	actor_uuid TEXT NOT NULL,
	role_id TEXT,
	"Origin_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Origin_id") REFERENCES "Origin" (id)
);
CREATE INDEX "ix_OriginActor_id" ON "OriginActor" (id);

CREATE TABLE "RelatedTask" (
	id INTEGER NOT NULL,
	task_uuid TEXT NOT NULL,
	remarks TEXT,
	"Origin_id" INTEGER,
	"RiskResponseReference_id" INTEGER,
	identified_subject_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Origin_id") REFERENCES "Origin" (id),
	FOREIGN KEY("RiskResponseReference_id") REFERENCES "RiskResponseReference" (id),
	FOREIGN KEY(identified_subject_id) REFERENCES "IdentifiedSubject" (id)
);
CREATE INDEX "ix_RelatedTask_id" ON "RelatedTask" (id);

CREATE TABLE "Characterization" (
	id INTEGER NOT NULL,
	"Risk_id" INTEGER,
	origin_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id),
	FOREIGN KEY(origin_id) REFERENCES "Origin" (id)
);
CREATE INDEX "ix_Characterization_id" ON "Characterization" (id);

CREATE TABLE "TelephoneNumber" (
	id INTEGER NOT NULL,
	type VARCHAR(6),
	number TEXT NOT NULL,
	"Location_id" INTEGER,
	"Party_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Location_id") REFERENCES "Location" (id),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_TelephoneNumber_id" ON "TelephoneNumber" (id);

CREATE TABLE "Part" (
	uid INTEGER NOT NULL,
	id TEXT,
	name TEXT NOT NULL,
	ns TEXT,
	_class TEXT,
	title TEXT,
	prose TEXT,
	"Group_uid" INTEGER,
	"Control_uid" INTEGER,
	"Part_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid),
	FOREIGN KEY("Part_uid") REFERENCES "Part" (uid)
);
CREATE INDEX "ix_Part_uid" ON "Part" (uid);

CREATE TABLE "Parameter" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	_class TEXT,
	depends_on TEXT,
	label TEXT,
	usage TEXT,
	remarks TEXT,
	"Catalog_id" INTEGER,
	"Group_uid" INTEGER,
	"Control_uid" INTEGER,
	select_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Catalog_id") REFERENCES "Catalog" (id),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid),
	FOREIGN KEY(select_id) REFERENCES "ParameterSelection" (id)
);
CREATE INDEX "ix_Parameter_uid" ON "Parameter" (uid);

CREATE TABLE "Location_email_addresses" (
	"Location_id" INTEGER,
	email_addresses TEXT,
	PRIMARY KEY ("Location_id", email_addresses),
	FOREIGN KEY("Location_id") REFERENCES "Location" (id)
);
CREATE INDEX "ix_Location_email_addresses_email_addresses" ON "Location_email_addresses" (email_addresses);
CREATE INDEX "ix_Location_email_addresses_Location_id" ON "Location_email_addresses" ("Location_id");

CREATE TABLE "Location_urls" (
	"Location_id" INTEGER,
	urls TEXT,
	PRIMARY KEY ("Location_id", urls),
	FOREIGN KEY("Location_id") REFERENCES "Location" (id)
);
CREATE INDEX "ix_Location_urls_urls" ON "Location_urls" (urls);
CREATE INDEX "ix_Location_urls_Location_id" ON "Location_urls" ("Location_id");

CREATE TABLE "AssessmentSubject" (
	id INTEGER NOT NULL,
	type VARCHAR(14) NOT NULL,
	description TEXT,
	remarks TEXT,
	"AssessmentPlan_id" INTEGER,
	"Task_id" INTEGER,
	"AssociatedActivity_id" INTEGER,
	"RelatedTask_id" INTEGER,
	"IdentifiedSubject_id" INTEGER,
	include_all_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AssessmentPlan_id") REFERENCES "AssessmentPlan" (id),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id),
	FOREIGN KEY("AssociatedActivity_id") REFERENCES "AssociatedActivity" (id),
	FOREIGN KEY("RelatedTask_id") REFERENCES "RelatedTask" (id),
	FOREIGN KEY("IdentifiedSubject_id") REFERENCES "IdentifiedSubject" (id),
	FOREIGN KEY(include_all_id) REFERENCES "IncludeAll" (id)
);
CREATE INDEX "ix_AssessmentSubject_id" ON "AssessmentSubject" (id);

CREATE TABLE "Facet" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	value TEXT NOT NULL,
	system TEXT NOT NULL,
	remarks TEXT,
	"Characterization_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Characterization_id") REFERENCES "Characterization" (id)
);
CREATE INDEX "ix_Facet_id" ON "Facet" (id);

CREATE TABLE "ResponsibleParty" (
	id INTEGER NOT NULL,
	role_id TEXT NOT NULL,
	remarks TEXT,
	"UsesComponent_id" INTEGER,
	"InventoryItem_id" INTEGER,
	"ImplementedComponent_id" INTEGER,
	"RelatedTask_id" INTEGER,
	"HasResponsibleParties_id" INTEGER,
	"Metadata_id" INTEGER,
	"Action_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("UsesComponent_id") REFERENCES "UsesComponent" (id),
	FOREIGN KEY("InventoryItem_id") REFERENCES "InventoryItem" (id),
	FOREIGN KEY("ImplementedComponent_id") REFERENCES "ImplementedComponent" (id),
	FOREIGN KEY("RelatedTask_id") REFERENCES "RelatedTask" (id),
	FOREIGN KEY("HasResponsibleParties_id") REFERENCES "HasResponsibleParties" (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id),
	FOREIGN KEY("Action_id") REFERENCES "Action" (id)
);
CREATE INDEX "ix_ResponsibleParty_id" ON "ResponsibleParty" (id);

CREATE TABLE "ResponsibleRole" (
	id INTEGER NOT NULL,
	role_id TEXT NOT NULL,
	remarks TEXT,
	"Activity_id" INTEGER,
	"Step_id" INTEGER,
	"Task_id" INTEGER,
	"AssociatedActivity_id" INTEGER,
	"SystemComponent_id" INTEGER,
	"HasResponsibleRoles_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("Step_id") REFERENCES "Step" (id),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id),
	FOREIGN KEY("AssociatedActivity_id") REFERENCES "AssociatedActivity" (id),
	FOREIGN KEY("SystemComponent_id") REFERENCES "SystemComponent" (id),
	FOREIGN KEY("HasResponsibleRoles_id") REFERENCES "HasResponsibleRoles" (id)
);
CREATE INDEX "ix_ResponsibleRole_id" ON "ResponsibleRole" (id);

CREATE TABLE "ParameterConstraint" (
	id INTEGER NOT NULL,
	description TEXT,
	"Parameter_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid)
);
CREATE INDEX "ix_ParameterConstraint_id" ON "ParameterConstraint" (id);

CREATE TABLE "ParameterGuideline" (
	id INTEGER NOT NULL,
	prose TEXT NOT NULL,
	"Parameter_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid)
);
CREATE INDEX "ix_ParameterGuideline_id" ON "ParameterGuideline" (id);

CREATE TABLE "Parameter_values" (
	"Parameter_uid" INTEGER,
	"values" TEXT,
	PRIMARY KEY ("Parameter_uid", "values"),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid)
);
CREATE INDEX "ix_Parameter_values_Parameter_uid" ON "Parameter_values" ("Parameter_uid");
CREATE INDEX "ix_Parameter_values_values" ON "Parameter_values" ("values");

CREATE TABLE "SelectSubjectById" (
	id INTEGER NOT NULL,
	subject_uuid TEXT NOT NULL,
	type VARCHAR(14) NOT NULL,
	remarks TEXT,
	"AssessmentSubject_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AssessmentSubject_id") REFERENCES "AssessmentSubject" (id)
);
CREATE INDEX "ix_SelectSubjectById_id" ON "SelectSubjectById" (id);

CREATE TABLE "ConstraintTest" (
	id INTEGER NOT NULL,
	remarks TEXT,
	expression TEXT NOT NULL,
	"ParameterConstraint_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ParameterConstraint_id") REFERENCES "ParameterConstraint" (id)
);
CREATE INDEX "ix_ConstraintTest_id" ON "ConstraintTest" (id);

CREATE TABLE "ResponsibleParty_party_uuids" (
	"ResponsibleParty_id" INTEGER,
	party_uuids TEXT NOT NULL,
	PRIMARY KEY ("ResponsibleParty_id", party_uuids),
	FOREIGN KEY("ResponsibleParty_id") REFERENCES "ResponsibleParty" (id)
);
CREATE INDEX "ix_ResponsibleParty_party_uuids_ResponsibleParty_id" ON "ResponsibleParty_party_uuids" ("ResponsibleParty_id");
CREATE INDEX "ix_ResponsibleParty_party_uuids_party_uuids" ON "ResponsibleParty_party_uuids" (party_uuids);

CREATE TABLE "ResponsibleRole_party_uuids" (
	"ResponsibleRole_id" INTEGER,
	party_uuids TEXT,
	PRIMARY KEY ("ResponsibleRole_id", party_uuids),
	FOREIGN KEY("ResponsibleRole_id") REFERENCES "ResponsibleRole" (id)
);
CREATE INDEX "ix_ResponsibleRole_party_uuids_ResponsibleRole_id" ON "ResponsibleRole_party_uuids" ("ResponsibleRole_id");
CREATE INDEX "ix_ResponsibleRole_party_uuids_party_uuids" ON "ResponsibleRole_party_uuids" (party_uuids);

CREATE TABLE "Property" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	uuid TEXT,
	ns TEXT,
	value TEXT NOT NULL,
	_class TEXT,
	remarks TEXT,
	"group" TEXT,
	"ReviewedControls_id" INTEGER,
	"ControlSelection_id" INTEGER,
	"ControlObjectiveSelection_id" INTEGER,
	"AssessmentSubject_id" INTEGER,
	"SelectSubjectById_id" INTEGER,
	"SubjectReference_id" INTEGER,
	"AssessmentSubjectPlaceholder_id" INTEGER,
	"AssessmentPlatform_id" INTEGER,
	"UsesComponent_id" INTEGER,
	"LocalObjective_id" INTEGER,
	"AssessmentMethod_id" INTEGER,
	"Activity_id" INTEGER,
	"Step_id" INTEGER,
	"Task_id" INTEGER,
	"AssociatedActivity_id" INTEGER,
	"AssessmentPart_id" INTEGER,
	"ControlPart_uid" INTEGER,
	"SystemComponent_id" INTEGER,
	"SystemUser_id" INTEGER,
	"InventoryItem_id" INTEGER,
	"ImplementedComponent_id" INTEGER,
	"OriginActor_id" INTEGER,
	"RelatedTask_id" INTEGER,
	"Observation_id" INTEGER,
	"RelevantEvidence_id" INTEGER,
	"Finding_id" INTEGER,
	"FindingTarget_id" INTEGER,
	"Risk_id" INTEGER,
	"Characterization_id" INTEGER,
	"Facet_id" INTEGER,
	"MitigatingFactor_id" INTEGER,
	"Response_id" INTEGER,
	"RequiredAsset_id" INTEGER,
	"RiskLogEntry_id" INTEGER,
	"RiskResponseReference_id" INTEGER,
	"HasPropsAndLinks_id" INTEGER,
	"OscalCommon_id" INTEGER,
	"Group_uid" INTEGER,
	"Control_uid" INTEGER,
	"Metadata_id" INTEGER,
	"Revision_id" INTEGER,
	"Role_uid" INTEGER,
	"Location_id" INTEGER,
	"Party_id" INTEGER,
	"ResponsibleParty_id" INTEGER,
	"ResponsibleRole_id" INTEGER,
	"Action_id" INTEGER,
	"Resource_id" INTEGER,
	"Citation_id" INTEGER,
	"Part_uid" INTEGER,
	"Parameter_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReviewedControls_id") REFERENCES "ReviewedControls" (id),
	FOREIGN KEY("ControlSelection_id") REFERENCES "ControlSelection" (id),
	FOREIGN KEY("ControlObjectiveSelection_id") REFERENCES "ControlObjectiveSelection" (id),
	FOREIGN KEY("AssessmentSubject_id") REFERENCES "AssessmentSubject" (id),
	FOREIGN KEY("SelectSubjectById_id") REFERENCES "SelectSubjectById" (id),
	FOREIGN KEY("SubjectReference_id") REFERENCES "SubjectReference" (id),
	FOREIGN KEY("AssessmentSubjectPlaceholder_id") REFERENCES "AssessmentSubjectPlaceholder" (id),
	FOREIGN KEY("AssessmentPlatform_id") REFERENCES "AssessmentPlatform" (id),
	FOREIGN KEY("UsesComponent_id") REFERENCES "UsesComponent" (id),
	FOREIGN KEY("LocalObjective_id") REFERENCES "LocalObjective" (id),
	FOREIGN KEY("AssessmentMethod_id") REFERENCES "AssessmentMethod" (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("Step_id") REFERENCES "Step" (id),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id),
	FOREIGN KEY("AssociatedActivity_id") REFERENCES "AssociatedActivity" (id),
	FOREIGN KEY("AssessmentPart_id") REFERENCES "AssessmentPart" (id),
	FOREIGN KEY("ControlPart_uid") REFERENCES "ControlPart" (uid),
	FOREIGN KEY("SystemComponent_id") REFERENCES "SystemComponent" (id),
	FOREIGN KEY("SystemUser_id") REFERENCES "SystemUser" (id),
	FOREIGN KEY("InventoryItem_id") REFERENCES "InventoryItem" (id),
	FOREIGN KEY("ImplementedComponent_id") REFERENCES "ImplementedComponent" (id),
	FOREIGN KEY("OriginActor_id") REFERENCES "OriginActor" (id),
	FOREIGN KEY("RelatedTask_id") REFERENCES "RelatedTask" (id),
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id),
	FOREIGN KEY("RelevantEvidence_id") REFERENCES "RelevantEvidence" (id),
	FOREIGN KEY("Finding_id") REFERENCES "Finding" (id),
	FOREIGN KEY("FindingTarget_id") REFERENCES "FindingTarget" (id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id),
	FOREIGN KEY("Characterization_id") REFERENCES "Characterization" (id),
	FOREIGN KEY("Facet_id") REFERENCES "Facet" (id),
	FOREIGN KEY("MitigatingFactor_id") REFERENCES "MitigatingFactor" (id),
	FOREIGN KEY("Response_id") REFERENCES "Response" (id),
	FOREIGN KEY("RequiredAsset_id") REFERENCES "RequiredAsset" (id),
	FOREIGN KEY("RiskLogEntry_id") REFERENCES "RiskLogEntry" (id),
	FOREIGN KEY("RiskResponseReference_id") REFERENCES "RiskResponseReference" (id),
	FOREIGN KEY("HasPropsAndLinks_id") REFERENCES "HasPropsAndLinks" (id),
	FOREIGN KEY("OscalCommon_id") REFERENCES "OscalCommon" (id),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id),
	FOREIGN KEY("Revision_id") REFERENCES "Revision" (id),
	FOREIGN KEY("Role_uid") REFERENCES "Role" (uid),
	FOREIGN KEY("Location_id") REFERENCES "Location" (id),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id),
	FOREIGN KEY("ResponsibleParty_id") REFERENCES "ResponsibleParty" (id),
	FOREIGN KEY("ResponsibleRole_id") REFERENCES "ResponsibleRole" (id),
	FOREIGN KEY("Action_id") REFERENCES "Action" (id),
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id),
	FOREIGN KEY("Citation_id") REFERENCES "Citation" (id),
	FOREIGN KEY("Part_uid") REFERENCES "Part" (uid),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid)
);
CREATE INDEX "ix_Property_id" ON "Property" (id);

CREATE TABLE "Link" (
	id INTEGER NOT NULL,
	href TEXT NOT NULL,
	rel TEXT,
	resource_fragment TEXT,
	media_type TEXT,
	text TEXT,
	"ReviewedControls_id" INTEGER,
	"ControlSelection_id" INTEGER,
	"ControlObjectiveSelection_id" INTEGER,
	"AssessmentSubject_id" INTEGER,
	"SelectSubjectById_id" INTEGER,
	"SubjectReference_id" INTEGER,
	"AssessmentSubjectPlaceholder_id" INTEGER,
	"AssessmentPlatform_id" INTEGER,
	"UsesComponent_id" INTEGER,
	"LocalObjective_id" INTEGER,
	"AssessmentMethod_id" INTEGER,
	"Activity_id" INTEGER,
	"Step_id" INTEGER,
	"Task_id" INTEGER,
	"AssociatedActivity_id" INTEGER,
	"AssessmentPart_id" INTEGER,
	"ControlPart_uid" INTEGER,
	"SystemComponent_id" INTEGER,
	"SystemUser_id" INTEGER,
	"InventoryItem_id" INTEGER,
	"ImplementedComponent_id" INTEGER,
	"OriginActor_id" INTEGER,
	"RelatedTask_id" INTEGER,
	"Observation_id" INTEGER,
	"RelevantEvidence_id" INTEGER,
	"Finding_id" INTEGER,
	"FindingTarget_id" INTEGER,
	"Risk_id" INTEGER,
	"Characterization_id" INTEGER,
	"Facet_id" INTEGER,
	"MitigatingFactor_id" INTEGER,
	"Response_id" INTEGER,
	"RequiredAsset_id" INTEGER,
	"RiskLogEntry_id" INTEGER,
	"RiskResponseReference_id" INTEGER,
	"HasPropsAndLinks_id" INTEGER,
	"OscalCommon_id" INTEGER,
	"Group_uid" INTEGER,
	"Control_uid" INTEGER,
	"Metadata_id" INTEGER,
	"Revision_id" INTEGER,
	"Role_uid" INTEGER,
	"Location_id" INTEGER,
	"Party_id" INTEGER,
	"ResponsibleParty_id" INTEGER,
	"ResponsibleRole_id" INTEGER,
	"Action_id" INTEGER,
	"Citation_id" INTEGER,
	"Part_uid" INTEGER,
	"Parameter_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ReviewedControls_id") REFERENCES "ReviewedControls" (id),
	FOREIGN KEY("ControlSelection_id") REFERENCES "ControlSelection" (id),
	FOREIGN KEY("ControlObjectiveSelection_id") REFERENCES "ControlObjectiveSelection" (id),
	FOREIGN KEY("AssessmentSubject_id") REFERENCES "AssessmentSubject" (id),
	FOREIGN KEY("SelectSubjectById_id") REFERENCES "SelectSubjectById" (id),
	FOREIGN KEY("SubjectReference_id") REFERENCES "SubjectReference" (id),
	FOREIGN KEY("AssessmentSubjectPlaceholder_id") REFERENCES "AssessmentSubjectPlaceholder" (id),
	FOREIGN KEY("AssessmentPlatform_id") REFERENCES "AssessmentPlatform" (id),
	FOREIGN KEY("UsesComponent_id") REFERENCES "UsesComponent" (id),
	FOREIGN KEY("LocalObjective_id") REFERENCES "LocalObjective" (id),
	FOREIGN KEY("AssessmentMethod_id") REFERENCES "AssessmentMethod" (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("Step_id") REFERENCES "Step" (id),
	FOREIGN KEY("Task_id") REFERENCES "Task" (id),
	FOREIGN KEY("AssociatedActivity_id") REFERENCES "AssociatedActivity" (id),
	FOREIGN KEY("AssessmentPart_id") REFERENCES "AssessmentPart" (id),
	FOREIGN KEY("ControlPart_uid") REFERENCES "ControlPart" (uid),
	FOREIGN KEY("SystemComponent_id") REFERENCES "SystemComponent" (id),
	FOREIGN KEY("SystemUser_id") REFERENCES "SystemUser" (id),
	FOREIGN KEY("InventoryItem_id") REFERENCES "InventoryItem" (id),
	FOREIGN KEY("ImplementedComponent_id") REFERENCES "ImplementedComponent" (id),
	FOREIGN KEY("OriginActor_id") REFERENCES "OriginActor" (id),
	FOREIGN KEY("RelatedTask_id") REFERENCES "RelatedTask" (id),
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id),
	FOREIGN KEY("RelevantEvidence_id") REFERENCES "RelevantEvidence" (id),
	FOREIGN KEY("Finding_id") REFERENCES "Finding" (id),
	FOREIGN KEY("FindingTarget_id") REFERENCES "FindingTarget" (id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id),
	FOREIGN KEY("Characterization_id") REFERENCES "Characterization" (id),
	FOREIGN KEY("Facet_id") REFERENCES "Facet" (id),
	FOREIGN KEY("MitigatingFactor_id") REFERENCES "MitigatingFactor" (id),
	FOREIGN KEY("Response_id") REFERENCES "Response" (id),
	FOREIGN KEY("RequiredAsset_id") REFERENCES "RequiredAsset" (id),
	FOREIGN KEY("RiskLogEntry_id") REFERENCES "RiskLogEntry" (id),
	FOREIGN KEY("RiskResponseReference_id") REFERENCES "RiskResponseReference" (id),
	FOREIGN KEY("HasPropsAndLinks_id") REFERENCES "HasPropsAndLinks" (id),
	FOREIGN KEY("OscalCommon_id") REFERENCES "OscalCommon" (id),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id),
	FOREIGN KEY("Revision_id") REFERENCES "Revision" (id),
	FOREIGN KEY("Role_uid") REFERENCES "Role" (uid),
	FOREIGN KEY("Location_id") REFERENCES "Location" (id),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id),
	FOREIGN KEY("ResponsibleParty_id") REFERENCES "ResponsibleParty" (id),
	FOREIGN KEY("ResponsibleRole_id") REFERENCES "ResponsibleRole" (id),
	FOREIGN KEY("Action_id") REFERENCES "Action" (id),
	FOREIGN KEY("Citation_id") REFERENCES "Citation" (id),
	FOREIGN KEY("Part_uid") REFERENCES "Part" (uid),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid)
);
CREATE INDEX "ix_Link_id" ON "Link" (id);
