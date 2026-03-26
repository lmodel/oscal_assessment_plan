from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "1.2.1"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'oscal_assessment_plan',
     'default_range': 'string',
     'description': 'OSCAL Assessment Plan Model: LinkML Schema',
     'id': 'https://w3id.org/lmodel/oscal_assessment_plan',
     'imports': ['linkml:types', './oscal_catalog'],
     'license': 'Apache-2.0',
     'name': 'oscal_assessment_plan',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'oscal_assessment_plan': {'prefix_prefix': 'oscal_assessment_plan',
                                            'prefix_reference': 'https://w3id.org/lmodel/oscal_assessment_plan/'},
                  'oscal_catalog': {'prefix_prefix': 'oscal_catalog',
                                    'prefix_reference': 'https://w3id.org/lmodel/oscal_catalog/'}},
     'see_also': ['https://lmodel.github.io/oscal_assessment_plan',
                  'https://pages.nist.gov/OSCAL/learn/concepts/layer/assessment/assessment-plan/',
                  'https://medium.com/@gregelin/an-orientation-to-oscal-in-the-devsecops-pipeline-b51e45f8503b'],
     'source': 'http://csrc.nist.gov/ns/oscal/1.2.1/oscal-ap-schema.json',
     'source_file': 'src/oscal_assessment_plan/schema/oscal_assessment_plan.yaml',
     'subsets': {'assessment_common': {'description': 'Classes originating from '
                                                      'the oscal-assessment-common '
                                                      'namespace: subjects, '
                                                      'assets, activities, tasks, '
                                                      'findings, observations, '
                                                      'risks, and related helper '
                                                      'types.',
                                       'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
                                       'name': 'assessment_common'},
                 'assessment_plan': {'description': 'Classes that form the root '
                                                    'Assessment Plan document and '
                                                    'its direct structural '
                                                    'containers '
                                                    '(local-definitions, '
                                                    'terms-and-conditions).',
                                     'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
                                     'name': 'assessment_plan'},
                 'implementation_common': {'description': 'Classes originating '
                                                          'from the '
                                                          'oscal-implementation-common '
                                                          'namespace: system '
                                                          'components, protocols, '
                                                          'inventory items, users, '
                                                          'and set-parameter.',
                                           'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
                                           'name': 'implementation_common'}},
     'title': 'oscal_assessment_plan',
     'types': {'NonNegativeIntegerType': {'base': 'int',
                                          'description': 'A non-negative integer '
                                                         'value (>= 0), as used '
                                                         'for port range '
                                                         'boundaries.',
                                          'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
                                          'name': 'NonNegativeIntegerType',
                                          'uri': 'xsd:nonNegativeInteger'},
               'PositiveIntegerType': {'base': 'int',
                                       'description': 'A positive integer value '
                                                      '(>= 1), as used for task '
                                                      'recurrence periods.',
                                       'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
                                       'name': 'PositiveIntegerType',
                                       'uri': 'xsd:positiveInteger'}}} )

class PartyTypeEnum(str, Enum):
    person = "person"
    organization = "organization"


class HashAlgorithmEnum(str, Enum):
    SHA_224 = "SHA-224"
    SHA_256 = "SHA-256"
    SHA_384 = "SHA-384"
    SHA_512 = "SHA-512"
    SHA3_224 = "SHA3-224"
    SHA3_256 = "SHA3-256"
    SHA3_384 = "SHA3-384"
    SHA3_512 = "SHA3-512"


class PhoneTypeEnum(str, Enum):
    home = "home"
    office = "office"
    mobile = "mobile"


class AddressTypeEnum(str, Enum):
    home = "home"
    work = "work"


class ParameterCardinalityEnum(str, Enum):
    one = "one"
    one_or_more = "one-or-more"


class WithChildControlsEnum(str, Enum):
    True_ = "True"
    False_ = "False"


class TaskTypeEnum(str, Enum):
    milestone = "milestone"
    action = "action"


class TimingUnitEnum(str, Enum):
    seconds = "seconds"
    minutes = "minutes"
    hours = "hours"
    days = "days"
    months = "months"
    years = "years"


class AssessmentSubjectTypeEnum(str, Enum):
    component = "component"
    inventory_item = "inventory-item"
    location = "location"
    party = "party"
    user = "user"


class SelectSubjectTypeEnum(str, Enum):
    component = "component"
    inventory_item = "inventory-item"
    location = "location"
    party = "party"
    user = "user"
    resource = "resource"


class OriginActorTypeEnum(str, Enum):
    tool = "tool"
    assessment_platform = "assessment-platform"
    party = "party"


class ObservationMethodEnum(str, Enum):
    EXAMINE = "EXAMINE"
    INTERVIEW = "INTERVIEW"
    TEST = "TEST"
    UNKNOWN = "UNKNOWN"


class ObservationTypeEnum(str, Enum):
    ssp_statement_issue = "ssp-statement-issue"
    control_objective = "control-objective"
    mitigation = "mitigation"
    finding = "finding"
    discovery = "discovery"
    historic = "historic"


class RiskStatusEnum(str, Enum):
    open = "open"
    investigating = "investigating"
    remediating = "remediating"
    deviation_requested = "deviation-requested"
    deviation_approved = "deviation-approved"
    closed = "closed"


class FindingTargetTypeEnum(str, Enum):
    statement_id = "statement-id"
    objective_id = "objective-id"


class ObjectiveStatusStateEnum(str, Enum):
    satisfied = "satisfied"
    not_satisfied = "not-satisfied"


class ObjectiveStatusReasonEnum(str, Enum):
    pass_ = "pass"
    fail = "fail"
    other = "other"


class ImplementationStatusStateEnum(str, Enum):
    implemented = "implemented"
    partial = "partial"
    planned = "planned"
    alternative = "alternative"
    not_applicable = "not-applicable"


class ComponentTypeEnum(str, Enum):
    this_system = "this-system"
    system = "system"
    interconnection = "interconnection"
    software = "software"
    hardware = "hardware"
    service = "service"
    policy = "policy"
    physical = "physical"
    process_procedure = "process-procedure"
    plan = "plan"
    guidance = "guidance"
    standard = "standard"
    validation = "validation"
    network = "network"


class ComponentStateEnum(str, Enum):
    under_development = "under-development"
    operational = "operational"
    disposition = "disposition"
    other = "other"


class TransportEnum(str, Enum):
    TCP = "TCP"
    UDP = "UDP"


class AssessmentPartNameEnum(str, Enum):
    asset = "asset"
    method = "method"
    objective = "objective"


class ResponseLifecycleEnum(str, Enum):
    recommendation = "recommendation"
    planned = "planned"
    completed = "completed"



class HasPropsAndLinks(ConfiguredBaseModel):
    """
    Mixin providing the props and links slots that are common to many OSCAL objects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog', 'mixin': True})

    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class OscalCommon(HasPropsAndLinks):
    """
    Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'mixin': True,
         'mixins': ['HasPropsAndLinks']})

    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class HasResponsibleRoles(ConfiguredBaseModel):
    """
    Mixin providing the responsible-roles slot for objects that carry role assignments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog', 'mixin': True})

    responsible_roles: Optional[list[ResponsibleRole]] = Field(default=None, description="""Responsible role assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleRoles']} })


class HasResponsibleParties(ConfiguredBaseModel):
    """
    Mixin providing the responsible-parties slot for objects that carry party assignments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog', 'mixin': True})

    responsible_parties: Optional[list[ResponsibleParty]] = Field(default=None, description="""Responsible party assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleParties']} })


class OscalDocument(ConfiguredBaseModel):
    """
    A root wrapper for an OSCAL document, which may be of any OSCAL document type (e.g. Catalog, Profile, Assessment Plan, SSP).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog', 'tree_root': True})

    pass


class CatalogDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Catalog document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_catalog'],
         'slot_usage': {'catalog': {'name': 'catalog', 'required': True}}})

    catalog: Catalog = Field(default=..., description="""Root catalog document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogDocument']} })


class Catalog(ConfiguredBaseModel):
    """
    A structured, organized collection of control information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_catalog'],
         'slot_usage': {'metadata': {'name': 'metadata', 'required': True},
                        'uuid': {'description': 'Provides a globally unique means to '
                                                'identify a given catalog instance.',
                                 'name': 'uuid',
                                 'required': True}}})

    uuid: str = Field(default=..., description="""Provides a globally unique means to identify a given catalog instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    metadata: Metadata = Field(default=..., description="""Provides information about the containing document, and defines concepts shared across the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'AssessmentPlan']} })
    back_matter: Optional[BackMatter] = Field(default=None, description="""A collection of resources that may be referenced from within the OSCAL document instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'AssessmentPlan']} })
    params: Optional[list[Parameter]] = Field(default=None, description="""Parameters providing a mechanism for the dynamic assignment of value(s) in a control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'Group', 'Control']} })
    controls: Optional[list[Control]] = Field(default=None, description="""A collection of controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'Group', 'Control']} })
    groups: Optional[list[Group]] = Field(default=None, description="""A collection of control groups.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'Group']} })


class Group(OscalCommon):
    """
    A group of controls, or of groups of controls.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_catalog'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'_class': {'description': 'A textual label that provides a '
                                                  'sub-type or characterization of the '
                                                  'group.',
                                   'name': '_class'},
                        'id': {'description': 'Identifies the group for the purpose of '
                                              'cross-linking within the defining '
                                              'instance or from other instances that '
                                              'reference the catalog.',
                               'name': 'id'},
                        'title': {'description': 'A name given to the group, which may '
                                                 'be used by a tool for display and '
                                                 'navigation.',
                                  'name': 'title',
                                  'required': True}}})

    id: Optional[str] = Field(default=None, description="""Identifies the group for the purpose of cross-linking within the defining instance or from other instances that reference the catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })
    class_: Optional[str] = Field(default=None, alias="_class", description="""A textual label that provides a sub-type or characterization of the group.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Property',
                       'Part',
                       'Parameter',
                       'AssessmentPart',
                       'ControlPart']} })
    title: str = Field(default=..., description="""A name given to the group, which may be used by a tool for display and navigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    params: Optional[list[Parameter]] = Field(default=None, description="""Parameters providing a mechanism for the dynamic assignment of value(s) in a control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'Group', 'Control']} })
    parts: Optional[list[Part]] = Field(default=None, description="""A collection of parts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Part',
                       'TermsAndConditions',
                       'LocalObjective',
                       'AssessmentPart',
                       'ControlPart']} })
    groups: Optional[list[Group]] = Field(default=None, description="""A collection of control groups.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'Group']} })
    controls: Optional[list[Control]] = Field(default=None, description="""A collection of controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'Group', 'Control']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Control(OscalCommon):
    """
    A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk related to an information system and its information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_catalog'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'_class': {'description': 'A textual label that provides a '
                                                  'sub-type or characterization of the '
                                                  'control.',
                                   'name': '_class'},
                        'id': {'description': 'Identifies a control such that it can '
                                              'be referenced in the defining catalog '
                                              'and other OSCAL instances (e.g., '
                                              'profiles).',
                               'name': 'id',
                               'required': True},
                        'title': {'description': 'A name given to the control, which '
                                                 'may be used by a tool for display '
                                                 'and navigation.',
                                  'name': 'title',
                                  'required': True}}})

    id: str = Field(default=..., description="""Identifies a control such that it can be referenced in the defining catalog and other OSCAL instances (e.g., profiles).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })
    class_: Optional[str] = Field(default=None, alias="_class", description="""A textual label that provides a sub-type or characterization of the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Property',
                       'Part',
                       'Parameter',
                       'AssessmentPart',
                       'ControlPart']} })
    title: str = Field(default=..., description="""A name given to the control, which may be used by a tool for display and navigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    params: Optional[list[Parameter]] = Field(default=None, description="""Parameters providing a mechanism for the dynamic assignment of value(s) in a control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'Group', 'Control']} })
    parts: Optional[list[Part]] = Field(default=None, description="""A collection of parts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Part',
                       'TermsAndConditions',
                       'LocalObjective',
                       'AssessmentPart',
                       'ControlPart']} })
    controls: Optional[list[Control]] = Field(default=None, description="""A collection of controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'Group', 'Control']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Metadata(HasResponsibleParties, OscalCommon):
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'mixins': ['OscalCommon', 'HasResponsibleParties'],
         'slot_usage': {'last-modified': {'description': 'The date and time the '
                                                         'document was last stored for '
                                                         'later retrieval.',
                                          'name': 'last-modified',
                                          'required': True},
                        'oscal-version': {'description': 'The OSCAL model version the '
                                                         'document was authored '
                                                         'against.',
                                          'name': 'oscal-version',
                                          'required': True},
                        'title': {'description': 'A name given to the document.',
                                  'name': 'title',
                                  'required': True},
                        'version': {'description': 'Used to distinguish a specific '
                                                   'revision of an OSCAL document.',
                                    'name': 'version',
                                    'required': True}}})

    title: str = Field(default=..., description="""A name given to the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    published: Optional[str] = Field(default=None, description="""The date and time the document was last made available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision']} })
    last_modified: str = Field(default=..., description="""The date and time the document was last stored for later retrieval.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision']} })
    version: str = Field(default=..., description="""Used to distinguish a specific revision of an OSCAL document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision']} })
    oscal_version: str = Field(default=..., description="""The OSCAL model version the document was authored against.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision']} })
    document_ids: Optional[list[DocumentId]] = Field(default=None, description="""Document identifiers qualified by an identifier scheme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Resource']} })
    revisions: Optional[list[Revision]] = Field(default=None, description="""An entry in a sequential list of revisions to the containing document, expected to be in reverse chronological order (i.e. latest first).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata']} })
    roles: Optional[list[Role]] = Field(default=None, description="""Defines a function, which might be assigned to a party in a specific situation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata']} })
    locations: Optional[list[Location]] = Field(default=None, description="""A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata']} })
    parties: Optional[list[Party]] = Field(default=None, description="""An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata']} })
    actions: Optional[list[Action]] = Field(default=None, description="""An action applied by a role within a given party to the content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_parties: Optional[list[ResponsibleParty]] = Field(default=None, description="""Responsible party assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleParties']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Revision(OscalCommon):
    """
    An entry in a sequential list of revisions to the containing document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'version': {'name': 'version', 'required': True}}})

    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    published: Optional[str] = Field(default=None, description="""The date and time the document was last made available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision']} })
    last_modified: Optional[str] = Field(default=None, description="""The date and time the document was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision']} })
    version: str = Field(default=..., description="""Used to distinguish a specific revision of an OSCAL document from other previous and future versions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision']} })
    oscal_version: Optional[str] = Field(default=None, description="""The OSCAL model version the document was authored against and will conform to as valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class DocumentId(ConfiguredBaseModel):
    """
    A document identifier qualified by an identifier scheme.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'slot_usage': {'identifier': {'name': 'identifier', 'required': True}}})

    scheme: Optional[str] = Field(default=None, description="""Qualifies the kind of identifier using a URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentId', 'PartyExternalId']} })
    identifier: str = Field(default=..., description="""A document identifier value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentId']} })


class Role(OscalCommon):
    """
    Defines a function, which might be assigned to a party in a specific situation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'id': {'description': 'A unique identifier for the role.',
                               'name': 'id',
                               'required': True},
                        'title': {'name': 'title', 'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })
    title: str = Field(default=..., description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    short_name: Optional[str] = Field(default=None, description="""A short common name, abbreviation, or acronym.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'Party', 'SystemUser']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Location(OscalCommon):
    """
    A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    email_addresses: Optional[list[str]] = Field(default=None, description="""Email addresses associated with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location', 'Party']} })
    telephone_numbers: Optional[list[TelephoneNumber]] = Field(default=None, description="""Telephone numbers associated with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location', 'Party']} })
    address: Optional[Address] = Field(default=None, description="""A postal address for the location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    urls: Optional[list[str]] = Field(default=None, description="""The uniform resource locator (URL) for a web site or other resource associated with the location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Party(OscalCommon):
    """
    An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'mixins': ['OscalCommon'],
         'rules': [{'description': 'A party may have inline addresses or location UUID '
                                   'references, but not both (metaschema <choice> '
                                   'constraint).',
                    'postconditions': {'slot_conditions': {'location-uuids': {'name': 'location-uuids',
                                                                              'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'addresses': {'name': 'addresses',
                                                                        'value_presence': 'PRESENT'}}},
                    'title': 'addresses-xor-location-uuids'},
                   {'postconditions': {'slot_conditions': {'addresses': {'name': 'addresses',
                                                                         'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'location-uuids': {'name': 'location-uuids',
                                                                             'value_presence': 'PRESENT'}}},
                    'title': 'location-uuids-xor-addresses'}],
         'slot_usage': {'name': {'description': 'The full name of the party.',
                                 'name': 'name',
                                 'range': 'string'},
                        'type': {'description': 'A category describing the kind of '
                                                'party the object describes.',
                                 'name': 'type',
                                 'range': 'PartyTypeEnum',
                                 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    type: PartyTypeEnum = Field(default=..., description="""A category describing the kind of party the object describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    name: Optional[str] = Field(default=None, description="""The full name of the party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Property',
                       'Part',
                       'AssessmentPart',
                       'ControlPart',
                       'Protocol',
                       'Facet']} })
    short_name: Optional[str] = Field(default=None, description="""A short common name, abbreviation, or acronym.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'Party', 'SystemUser']} })
    email_addresses: Optional[list[str]] = Field(default=None, description="""Email addresses associated with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location', 'Party']} })
    telephone_numbers: Optional[list[TelephoneNumber]] = Field(default=None, description="""Telephone numbers associated with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Location', 'Party']} })
    external_ids: Optional[list[PartyExternalId]] = Field(default=None, description="""An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party']} })
    addresses: Optional[list[Address]] = Field(default=None, description="""Postal addresses associated with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party']} })
    location_uuids: Optional[list[str]] = Field(default=None, description="""Reference to a location by UUID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party']} })
    member_of_organizations: Optional[list[str]] = Field(default=None, description="""A reference to another party by UUID, typically an organization, that this subject is associated with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class PartyExternalId(ConfiguredBaseModel):
    """
    An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID (ORCID).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'slot_usage': {'id': {'name': 'id', 'range': 'string', 'required': True},
                        'scheme': {'description': 'Indicates the type of external '
                                                  'identifier.',
                                   'name': 'scheme',
                                   'required': True}}})

    scheme: str = Field(default=..., description="""Indicates the type of external identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DocumentId', 'PartyExternalId']} })
    id: str = Field(default=..., description="""A unique human-oriented identifier within a particular context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })


class ResponsibleParty(OscalCommon):
    """
    A reference to a set of persons and/or organizations that have responsibility for performing the referenced role in the context of the containing object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'party-uuids': {'name': 'party-uuids', 'required': True},
                        'role-id': {'description': 'A reference to a role performed by '
                                                   'a party.',
                                    'name': 'role-id',
                                    'required': True}}})

    role_id: str = Field(default=..., description="""A reference to a role performed by a party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResponsibleParty',
                       'ResponsibleRole',
                       'OriginActor',
                       'LoggedBy']} })
    party_uuids: list[str] = Field(default=..., description="""References to party UUIDs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResponsibleParty', 'ResponsibleRole']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ResponsibleRole(OscalCommon):
    """
    A reference to a role with responsibility for performing a function relative to the containing object, optionally associated with a set of persons and/or organizations that perform that role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'role-id': {'description': 'A human-oriented identifier '
                                                   'reference to a role performed.',
                                    'name': 'role-id',
                                    'required': True}}})

    role_id: str = Field(default=..., description="""A human-oriented identifier reference to a role performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResponsibleParty',
                       'ResponsibleRole',
                       'OriginActor',
                       'LoggedBy']} })
    party_uuids: Optional[list[str]] = Field(default=None, description="""References to party UUIDs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResponsibleParty', 'ResponsibleRole']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Action(HasResponsibleParties, OscalCommon):
    """
    An action applied by a role within a given party to the content.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'mixins': ['OscalCommon', 'HasResponsibleParties'],
         'slot_usage': {'system': {'name': 'system', 'required': True},
                        'type': {'description': 'The type of action documented by the '
                                                'assembly, such as an approval.',
                                 'name': 'type',
                                 'range': 'TokenType',
                                 'required': True},
                        'uuid': {'description': 'A unique identifier that can be used '
                                                'to reference this defined action '
                                                'elsewhere in an OSCAL document.',
                                 'name': 'uuid',
                                 'required': True}}})

    uuid: str = Field(default=..., description="""A unique identifier that can be used to reference this defined action elsewhere in an OSCAL document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    type: str = Field(default=..., description="""The type of action documented by the assembly, such as an approval.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    date: Optional[str] = Field(default=None, description="""The date and time when the action occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action', 'OnDateCondition']} })
    system: str = Field(default=..., description="""Specifies the action type system used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action', 'ThreatId', 'Facet']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_parties: Optional[list[ResponsibleParty]] = Field(default=None, description="""Responsible party assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleParties']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class TelephoneNumber(ConfiguredBaseModel):
    """
    A telephone service number as defined by ITU-T E.164.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'slot_usage': {'number': {'name': 'number', 'required': True},
                        'type': {'description': 'Indicates the type of phone number. '
                                                'Typical values: home, office, mobile. '
                                                'Other values are permitted.',
                                 'name': 'type'}}})

    type: Optional[str] = Field(default=None, description="""Indicates the type of phone number. Typical values: home, office, mobile. Other values are permitted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    number: str = Field(default=..., description="""A telephone number value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TelephoneNumber']} })


class Address(ConfiguredBaseModel):
    """
    A postal address for the location.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'slot_usage': {'type': {'description': 'Indicates the type of address. '
                                                'Typical values: home, work. Other '
                                                'values are permitted.',
                                 'name': 'type'}}})

    type: Optional[str] = Field(default=None, description="""Indicates the type of address. Typical values: home, work. Other values are permitted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    addr_lines: Optional[list[str]] = Field(default=None, description="""A single line of an address.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Address']} })
    city: Optional[str] = Field(default=None, description="""City, town or geographical region for the mailing address.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Address']} })
    state: Optional[str] = Field(default=None, description="""State, province or analogous geographical region for a mailing address.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Address',
                       'ComponentStatus',
                       'ImplementationStatus',
                       'ObjectiveStatus']} })
    postal_code: Optional[str] = Field(default=None, description="""Postal or ZIP code for mailing address.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Address']} })
    country: Optional[str] = Field(default=None, description="""The ISO 3166-1 alpha-2 country code for the mailing address.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Address']} })


class Hash(ConfiguredBaseModel):
    """
    A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'slot_usage': {'algorithm': {'name': 'algorithm', 'required': True},
                        'value': {'name': 'value', 'required': True}}})

    value: str = Field(default=..., description="""The value associated with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'Property', 'Base64Resource', 'Facet']} })
    algorithm: str = Field(default=..., description="""The digest method by which a hash is derived. SHOULD be one of the HashAlgorithmEnum values but other values are permitted (allow-other=\"yes\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash']} })


class Property(ConfiguredBaseModel):
    """
    An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value pair.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'slot_usage': {'_class': {'description': 'A textual label that provides a '
                                                  'sub-type or characterization of the '
                                                  "property's name.",
                                   'name': '_class'},
                        'name': {'description': 'A textual label, within a namespace, '
                                                'that identifies a specific attribute, '
                                                'characteristic, or quality of the '
                                                "property's containing object.",
                                 'name': 'name',
                                 'required': True},
                        'ns': {'description': "A namespace qualifying the property's "
                                              'name. This allows different '
                                              'organizations to associate distinct '
                                              'semantics with the same name.',
                               'name': 'ns'},
                        'uuid': {'description': 'A unique identifier for a property.',
                                 'name': 'uuid'},
                        'value': {'description': 'Indicates the value of the '
                                                 'attribute, characteristic, or '
                                                 'quality.',
                                  'name': 'value',
                                  'required': True}}})

    name: str = Field(default=..., description="""A textual label, within a namespace, that identifies a specific attribute, characteristic, or quality of the property's containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Property',
                       'Part',
                       'AssessmentPart',
                       'ControlPart',
                       'Protocol',
                       'Facet']} })
    uuid: Optional[str] = Field(default=None, description="""A unique identifier for a property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    ns: Optional[str] = Field(default=None, description="""A namespace qualifying the property's name. This allows different organizations to associate distinct semantics with the same name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property', 'Part', 'AssessmentPart', 'ControlPart']} })
    value: str = Field(default=..., description="""Indicates the value of the attribute, characteristic, or quality.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'Property', 'Base64Resource', 'Facet']} })
    class_: Optional[str] = Field(default=None, alias="_class", description="""A textual label that provides a sub-type or characterization of the property's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Property',
                       'Part',
                       'Parameter',
                       'AssessmentPart',
                       'ControlPart']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    group: Optional[str] = Field(default=None, description="""An identifier for relating distinct sets of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property']} })


class Link(ConfiguredBaseModel):
    """
    A reference to a local or remote resource, that has a specific relation to the containing object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_metadata'],
         'slot_usage': {'href': {'description': 'A resolvable URL reference to a '
                                                'resource.',
                                 'name': 'href',
                                 'required': True}}})

    href: str = Field(default=..., description="""A resolvable URL reference to a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link',
                       'ResourceLink',
                       'ImportSSP',
                       'RelevantEvidence',
                       'ThreatId']} })
    rel: Optional[str] = Field(default=None, description="""Describes the type of relationship provided by the link's hypertext reference. This can be an indicator of the link's purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link']} })
    resource_fragment: Optional[str] = Field(default=None, description="""In case where the href points to a back-matter/resource, this value will indicate the URI fragment to append to any rlink associated with the resource. This value MUST be URI encoded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link']} })
    media_type: Optional[str] = Field(default=None, description="""A label that indicates the nature of a resource, as a data serialization or format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link', 'ResourceLink', 'Base64Resource']} })
    text: Optional[str] = Field(default=None, description="""A textual label to associate with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link', 'Citation']} })


class BackMatter(ConfiguredBaseModel):
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_back_matter']})

    resources: Optional[list[Resource]] = Field(default=None, description="""A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BackMatter']} })


class Resource(ConfiguredBaseModel):
    """
    A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_back_matter'],
         'slot_usage': {'description': {'description': 'An optional short summary of '
                                                       'the resource used to indicate '
                                                       'the purpose of the resource.',
                                        'name': 'description'},
                        'title': {'description': 'An optional name given to the '
                                                 'resource, which may be used by a '
                                                 'tool for display and navigation.',
                                  'name': 'title'},
                        'uuid': {'description': 'A unique identifier for a resource.',
                                 'name': 'uuid',
                                 'required': True}}})

    uuid: str = Field(default=..., description="""A unique identifier for a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""An optional name given to the resource, which may be used by a tool for display and navigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: Optional[str] = Field(default=None, description="""An optional short summary of the resource used to indicate the purpose of the resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    document_ids: Optional[list[DocumentId]] = Field(default=None, description="""Document identifiers qualified by an identifier scheme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Resource']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    citation: Optional[Citation] = Field(default=None, description="""An optional citation consisting of end note text using structured markup.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    rlinks: Optional[list[ResourceLink]] = Field(default=None, description="""A URL-based pointer to an external resource with an optional hash for verification and change detection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })
    base64: Optional[Base64Resource] = Field(default=None, description="""A resource encoded using the Base64 alphabet defined by RFC 2045.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Resource']} })


class Citation(HasPropsAndLinks):
    """
    An optional citation consisting of end note text using structured markup.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_back_matter'],
         'mixins': ['HasPropsAndLinks'],
         'slot_usage': {'text': {'description': 'A line of citation text.',
                                 'name': 'text',
                                 'required': True}}})

    text: str = Field(default=..., description="""A line of citation text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link', 'Citation']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ResourceLink(ConfiguredBaseModel):
    """
    A URL-based pointer to an external resource with an optional hash for verification and change detection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_back_matter'],
         'slot_usage': {'href': {'description': 'A resolvable URL pointing to the '
                                                'referenced resource.',
                                 'name': 'href',
                                 'required': True}}})

    href: str = Field(default=..., description="""A resolvable URL pointing to the referenced resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link',
                       'ResourceLink',
                       'ImportSSP',
                       'RelevantEvidence',
                       'ThreatId']} })
    media_type: Optional[str] = Field(default=None, description="""A label that indicates the nature of a resource, as a data serialization or format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link', 'ResourceLink', 'Base64Resource']} })
    hashes: Optional[list[Hash]] = Field(default=None, description="""A representation of a cryptographic digest generated over a resource using a specified hash algorithm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink']} })


class Base64Resource(ConfiguredBaseModel):
    """
    A resource encoded using the Base64 alphabet defined by RFC 2045.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_back_matter'],
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'Base64Type',
                                  'required': True}}})

    media_type: Optional[str] = Field(default=None, description="""A label that indicates the nature of a resource, as a data serialization or format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link', 'ResourceLink', 'Base64Resource']} })
    value: str = Field(default=..., description="""The value associated with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'Property', 'Base64Resource', 'Facet']} })
    filename: Optional[str] = Field(default=None, description="""Name of the file before it was encoded as Base64 to be embedded in a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Base64Resource']} })


class Part(HasPropsAndLinks):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common'],
         'mixins': ['HasPropsAndLinks'],
         'slot_usage': {'_class': {'description': 'An optional textual providing a '
                                                  'sub-type or characterization of the '
                                                  "part's name, or a category to which "
                                                  'the part belongs.',
                                   'name': '_class'},
                        'id': {'description': 'A unique identifier for the part.',
                               'name': 'id'},
                        'name': {'description': 'A textual label that uniquely '
                                                "identifies the part's semantic type, "
                                                'which exists in a value space '
                                                'qualified by the ns.',
                                 'name': 'name',
                                 'required': True},
                        'ns': {'description': 'An optional namespace qualifying the '
                                              "part's name. This allows different "
                                              'organizations to associate distinct '
                                              'semantics with the same name.',
                               'name': 'ns'},
                        'prose': {'description': 'Permits multiple paragraphs, lists, '
                                                 'tables etc.',
                                  'name': 'prose'},
                        'title': {'description': 'An optional name given to the part, '
                                                 'which may be used by a tool for '
                                                 'display and navigation.',
                                  'name': 'title'}}})

    id: Optional[str] = Field(default=None, description="""A unique identifier for the part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })
    name: str = Field(default=..., description="""A textual label that uniquely identifies the part's semantic type, which exists in a value space qualified by the ns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Property',
                       'Part',
                       'AssessmentPart',
                       'ControlPart',
                       'Protocol',
                       'Facet']} })
    ns: Optional[str] = Field(default=None, description="""An optional namespace qualifying the part's name. This allows different organizations to associate distinct semantics with the same name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property', 'Part', 'AssessmentPart', 'ControlPart']} })
    class_: Optional[str] = Field(default=None, alias="_class", description="""An optional textual providing a sub-type or characterization of the part's name, or a category to which the part belongs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Property',
                       'Part',
                       'Parameter',
                       'AssessmentPart',
                       'ControlPart']} })
    title: Optional[str] = Field(default=None, description="""An optional name given to the part, which may be used by a tool for display and navigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    prose: Optional[str] = Field(default=None, description="""Permits multiple paragraphs, lists, tables etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Part', 'ParameterGuideline', 'AssessmentPart', 'ControlPart']} })
    parts: Optional[list[Part]] = Field(default=None, description="""A collection of parts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Part',
                       'TermsAndConditions',
                       'LocalObjective',
                       'AssessmentPart',
                       'ControlPart']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Parameter(OscalCommon):
    """
    Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common'],
         'mixins': ['OscalCommon'],
         'rules': [{'description': 'A parameter may have prescribed values or a '
                                   'selection construct, but not both (metaschema '
                                   '<choice> constraint).',
                    'postconditions': {'slot_conditions': {'select': {'name': 'select',
                                                                      'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'values': {'name': 'values',
                                                                     'value_presence': 'PRESENT'}}},
                    'title': 'values-xor-select'},
                   {'postconditions': {'slot_conditions': {'values': {'name': 'values',
                                                                      'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'select': {'name': 'select',
                                                                     'value_presence': 'PRESENT'}}},
                    'title': 'select-xor-values'}],
         'slot_usage': {'_class': {'description': 'A textual label that provides a '
                                                  'characterization of the type, '
                                                  'purpose, use or scope of the '
                                                  'parameter.',
                                   'name': '_class'},
                        'id': {'description': 'A unique identifier for the parameter.',
                               'name': 'id',
                               'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for the parameter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })
    class_: Optional[str] = Field(default=None, alias="_class", description="""A textual label that provides a characterization of the type, purpose, use or scope of the parameter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Property',
                       'Part',
                       'Parameter',
                       'AssessmentPart',
                       'ControlPart']} })
    depends_on: Optional[str] = Field(default=None, description="""(deprecated) Another parameter invoking this one. This construct has been deprecated and should not be used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter']} })
    label: Optional[str] = Field(default=None, description="""A short, placeholder name for the parameter, which can be used as a substitute for a value if no value is assigned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter']} })
    usage: Optional[str] = Field(default=None, description="""Describes the purpose and use of a parameter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter']} })
    constraints: Optional[list[ParameterConstraint]] = Field(default=None, description="""A formal or informal expression of a constraint or test.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter']} })
    guidelines: Optional[list[ParameterGuideline]] = Field(default=None, description="""A prose statement that provides a recommendation for the use of a parameter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter']} })
    values: Optional[list[str]] = Field(default=None, description="""A parameter value or set of values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter', 'SetParameter']} })
    select: Optional[ParameterSelection] = Field(default=None, description="""Presenting a choice among alternatives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ParameterConstraint(ConfiguredBaseModel):
    """
    A formal or informal expression of a constraint or test.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common'],
         'slot_usage': {'description': {'description': 'A textual summary of the '
                                                       'constraint to be applied.',
                                        'name': 'description'}}})

    description: Optional[str] = Field(default=None, description="""A textual summary of the constraint to be applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    tests: Optional[list[ConstraintTest]] = Field(default=None, description="""A test expression which is expected to be evaluated by a tool.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParameterConstraint']} })


class ConstraintTest(ConfiguredBaseModel):
    """
    A test expression which is expected to be evaluated by a tool.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common'],
         'slot_usage': {'expression': {'name': 'expression', 'required': True}}})

    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    expression: str = Field(default=..., description="""A formal (executable) expression of a constraint.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConstraintTest']} })


class ParameterGuideline(ConfiguredBaseModel):
    """
    A prose statement that provides a recommendation for the use of a parameter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common'],
         'slot_usage': {'prose': {'description': 'Prose permits multiple paragraphs, '
                                                 'lists, tables etc.',
                                  'name': 'prose',
                                  'required': True}}})

    prose: str = Field(default=..., description="""Prose permits multiple paragraphs, lists, tables etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Part', 'ParameterGuideline', 'AssessmentPart', 'ControlPart']} })


class ParameterSelection(ConfiguredBaseModel):
    """
    Presenting a choice among alternatives.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common']})

    how_many: Optional[ParameterCardinalityEnum] = Field(default=None, description="""Describes the number of selections that must occur. Without this setting, only one value should be assumed to be permitted.""", json_schema_extra = { "linkml_meta": {'aliases': ['how_many'], 'domain_of': ['ParameterSelection']} })
    choice: Optional[list[str]] = Field(default=None, description="""A value selection among several such options.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParameterSelection']} })


class IncludeAll(ConfiguredBaseModel):
    """
    Include all controls from the imported catalog or profile resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common']})

    pass


class ControlMatching(ConfiguredBaseModel):
    """
    Selecting a set of controls by matching their IDs with a wildcard pattern.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common']})

    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    pattern: Optional[str] = Field(default=None, description="""A glob expression matching the IDs of one or more controls to be selected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlMatching']} })


class SelectControlById(ConfiguredBaseModel):
    """
    Select a control or controls from an imported control set.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_catalog',
         'in_subset': ['oscal_control_common']})

    with_child_controls: Optional[WithChildControlsEnum] = Field(default=None, description="""When a control is included, whether its child (dependent) controls are also included.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SelectControlById']} })
    with_ids: Optional[list[str]] = Field(default=None, description="""Selecting a control by its ID given as a literal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SelectControlById']} })
    matching: Optional[list[ControlMatching]] = Field(default=None, description="""Selecting a set of controls by matching their IDs with a wildcard pattern.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SelectControlById']} })


class AssessmentPlanDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Assessment Plan document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_plan'],
         'slot_usage': {'assessment-plan': {'name': 'assessment-plan',
                                            'required': True}}})

    assessment_plan: AssessmentPlan = Field(default=..., description="""The root assessment plan object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlanDocument']} })


class AssessmentPlan(ConfiguredBaseModel):
    """
    An assessment plan, such as those provided by a FedRAMP assessor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_plan'],
         'slot_usage': {'import-ssp': {'name': 'import-ssp', 'required': True},
                        'metadata': {'name': 'metadata', 'required': True},
                        'reviewed-controls': {'name': 'reviewed-controls',
                                              'required': True},
                        'uuid': {'description': 'Assessment Plan Universally Unique '
                                                'Identifier.',
                                 'name': 'uuid',
                                 'required': True}}})

    uuid: str = Field(default=..., description="""Assessment Plan Universally Unique Identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    metadata: Metadata = Field(default=..., description="""Provides information about the containing document, and defines concepts shared across the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'AssessmentPlan']} })
    import_ssp: ImportSSP = Field(default=..., description="""Used to import information about the system from an SSP.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan']} })
    local_definitions: Optional[LocalDefinitions] = Field(default=None, description="""Used to define data objects that do not appear in the referenced SSP.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan']} })
    terms_and_conditions: Optional[TermsAndConditions] = Field(default=None, description="""Terms and conditions under which an assessment can be performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan']} })
    assessment_subjects: Optional[list[AssessmentSubject]] = Field(default=None, description="""Identifies system elements being assessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan']} })
    assessment_assets: Optional[AssessmentAssets] = Field(default=None, description="""Identifies the assets used to perform this assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan']} })
    reviewed_controls: ReviewedControls = Field(default=..., description="""Identifies the controls being assessed and their control objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan', 'Step']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""A collection of tasks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan', 'Task', 'Response']} })
    back_matter: Optional[BackMatter] = Field(default=None, description="""A collection of resources that may be referenced from within the OSCAL document instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog', 'AssessmentPlan']} })


class ImportSSP(ConfiguredBaseModel):
    """
    Used by the assessment plan and POA&M to import information about the system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'href': {'name': 'href', 'required': True}}})

    href: str = Field(default=..., description="""A resolvable URL reference to a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link',
                       'ResourceLink',
                       'ImportSSP',
                       'RelevantEvidence',
                       'ThreatId']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class LocalDefinitions(ConfiguredBaseModel):
    """
    Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_plan']})

    components: Optional[list[SystemComponent]] = Field(default=None, description="""A collection of system components.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalDefinitions', 'AssessmentAssets']} })
    inventory_items: Optional[list[InventoryItem]] = Field(default=None, description="""A collection of inventory items.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalDefinitions']} })
    users: Optional[list[SystemUser]] = Field(default=None, description="""A collection of system users.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalDefinitions']} })
    objectives_and_methods: Optional[list[LocalObjective]] = Field(default=None, description="""A collection of locally-defined control objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalDefinitions']} })
    activities: Optional[list[Activity]] = Field(default=None, description="""A collection of activities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalDefinitions']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class TermsAndConditions(ConfiguredBaseModel):
    """
    Used to define various terms and conditions under which an assessment can be performed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_plan'],
         'slot_usage': {'parts': {'name': 'parts', 'range': 'AssessmentPart'}}})

    parts: Optional[list[AssessmentPart]] = Field(default=None, description="""A collection of parts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Part',
                       'TermsAndConditions',
                       'LocalObjective',
                       'AssessmentPart',
                       'ControlPart']} })


class ReviewedControls(OscalCommon):
    """
    Identifies the controls being assessed and their control objectives.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'control-selections': {'name': 'control-selections',
                                               'required': True}}})

    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    control_selections: list[ControlSelection] = Field(default=..., description="""Identifies the controls being assessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReviewedControls']} })
    control_objective_selections: Optional[list[ControlObjectiveSelection]] = Field(default=None, description="""Identifies the control objectives of the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ReviewedControls']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ControlSelection(OscalCommon):
    """
    Identifies the controls being assessed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon']})

    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    include_all: Optional[IncludeAll] = Field(default=None, description="""Include all controls from the imported catalog or profile resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject']} })
    include_controls: Optional[list[AssessmentSelectControlById]] = Field(default=None, description="""Controls to include in the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlSelection']} })
    exclude_controls: Optional[list[AssessmentSelectControlById]] = Field(default=None, description="""Controls to exclude from the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlSelection']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ControlObjectiveSelection(OscalCommon):
    """
    Identifies the control objectives of the assessment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon']})

    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    include_all: Optional[IncludeAll] = Field(default=None, description="""Include all controls from the imported catalog or profile resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject']} })
    include_objectives: Optional[list[SelectObjectiveById]] = Field(default=None, description="""Objectives to include in the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlObjectiveSelection']} })
    exclude_objectives: Optional[list[SelectObjectiveById]] = Field(default=None, description="""Objectives to exclude from the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlObjectiveSelection']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class AssessmentSelectControlById(ConfiguredBaseModel):
    """
    Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement IDs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'control-id': {'name': 'control-id', 'required': True}}})

    control_id: str = Field(default=..., description="""A reference to a control by its identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSelectControlById', 'LocalObjective']} })
    statement_ids: Optional[list[str]] = Field(default=None, description="""Statement IDs for control selection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSelectControlById']} })


class SelectObjectiveById(ConfiguredBaseModel):
    """
    Used to select a control objective for inclusion/exclusion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'objective-id': {'name': 'objective-id', 'required': True}}})

    objective_id: str = Field(default=..., description="""Reference to a control objective by its identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SelectObjectiveById']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class AssessmentSubject(OscalCommon):
    """
    Identifies system elements being assessed, such as components, inventory items, and locations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'type': {'name': 'type',
                                 'range': 'AssessmentSubjectTypeEnum',
                                 'required': True}}})

    type: AssessmentSubjectTypeEnum = Field(default=..., description="""Indicates the nature or kind of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    include_all: Optional[IncludeAll] = Field(default=None, description="""Include all controls from the imported catalog or profile resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject']} })
    include_subjects: Optional[list[SelectSubjectById]] = Field(default=None, description="""Assessment subjects to include.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSubject']} })
    exclude_subjects: Optional[list[SelectSubjectById]] = Field(default=None, description="""Assessment subjects to exclude.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSubject']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class SelectSubjectById(OscalCommon):
    """
    Identifies a set of assessment subjects to include/exclude by UUID.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'subject-uuid': {'name': 'subject-uuid', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'SelectSubjectTypeEnum',
                                 'required': True}}})

    subject_uuid: str = Field(default=..., description="""A UUID reference to the identified subject.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SelectSubjectById', 'SubjectReference']} })
    type: SelectSubjectTypeEnum = Field(default=..., description="""Indicates the nature or kind of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class SubjectReference(OscalCommon):
    """
    A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'subject-uuid': {'name': 'subject-uuid', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'SelectSubjectTypeEnum',
                                 'required': True}}})

    subject_uuid: str = Field(default=..., description="""A UUID reference to the identified subject.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SelectSubjectById', 'SubjectReference']} })
    type: SelectSubjectTypeEnum = Field(default=..., description="""Indicates the nature or kind of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class AssessmentSubjectPlaceholder(OscalCommon):
    """
    Used when the assessment subjects will be determined as part of one or more other assessment activities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'sources': {'name': 'sources', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    sources: list[AssessmentSubjectSource] = Field(default=..., description="""Activities that will identify assessment subjects.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSubjectPlaceholder']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class AssessmentSubjectSource(ConfiguredBaseModel):
    """
    Assessment subjects will be identified while conducting the referenced activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'task-uuid': {'name': 'task-uuid', 'required': True}}})

    task_uuid: str = Field(default=..., description="""A UUID reference to a task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSubjectSource', 'TaskDependency', 'RelatedTask']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class AssessmentAssets(ConfiguredBaseModel):
    """
    Identifies the assets used to perform this assessment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'assessment-platforms': {'name': 'assessment-platforms',
                                                 'required': True}}})

    components: Optional[list[SystemComponent]] = Field(default=None, description="""A collection of system components.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LocalDefinitions', 'AssessmentAssets']} })
    assessment_platforms: list[AssessmentPlatform] = Field(default=..., description="""A collection of assessment platforms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentAssets']} })


class AssessmentPlatform(OscalCommon):
    """
    Used to represent the toolset used to perform aspects of the assessment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    uses_components: Optional[list[UsesComponent]] = Field(default=None, description="""The set of components used by the assessment platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlatform']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class UsesComponent(HasResponsibleParties, OscalCommon):
    """
    The set of components that are used by the assessment platform.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon', 'HasResponsibleParties'],
         'slot_usage': {'component-uuid': {'name': 'component-uuid', 'required': True}}})

    component_uuid: str = Field(default=..., description="""A UUID reference to a component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UsesComponent', 'ImplementedComponent']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_parties: Optional[list[ResponsibleParty]] = Field(default=None, description="""Responsible party assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleParties']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class LocalObjective(OscalCommon):
    """
    A local definition of a control objective for this assessment. Uses catalog syntax for control objective and assessment actions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'control-id': {'name': 'control-id', 'required': True},
                        'parts': {'name': 'parts',
                                  'range': 'ControlPart',
                                  'required': True}}})

    control_id: str = Field(default=..., description="""A reference to a control by its identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSelectControlById', 'LocalObjective']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    parts: list[ControlPart] = Field(default=..., description="""A collection of parts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Part',
                       'TermsAndConditions',
                       'LocalObjective',
                       'AssessmentPart',
                       'ControlPart']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class AssessmentMethod(OscalCommon):
    """
    A local definition of a control objective.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'part': {'name': 'part', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    part: AssessmentPart = Field(default=..., description="""An assessment part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentMethod']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Activity(HasResponsibleRoles, OscalCommon):
    """
    Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon', 'HasResponsibleRoles'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    steps: Optional[list[Step]] = Field(default=None, description="""A collection of steps in an activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    related_controls: Optional[ReviewedControls] = Field(default=None, description="""A reference to reviewed controls for this activity or step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_roles: Optional[list[ResponsibleRole]] = Field(default=None, description="""Responsible role assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleRoles']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Step(HasResponsibleRoles, OscalCommon):
    """
    Identifies an individual step in a series of steps related to an activity, such as an assessment test or examination procedure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon', 'HasResponsibleRoles'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    reviewed_controls: Optional[ReviewedControls] = Field(default=None, description="""Identifies the controls being assessed and their control objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan', 'Step']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_roles: Optional[list[ResponsibleRole]] = Field(default=None, description="""Responsible role assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleRoles']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Task(HasResponsibleRoles, OscalCommon):
    """
    Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon', 'HasResponsibleRoles'],
         'slot_usage': {'subjects': {'name': 'subjects', 'range': 'AssessmentSubject'},
                        'title': {'name': 'title', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'TaskTypeEnum',
                                 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    type: TaskTypeEnum = Field(default=..., description="""Indicates the nature or kind of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    title: str = Field(default=..., description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    timing: Optional[EventTiming] = Field(default=None, description="""The timing under which a task is intended to occur.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task']} })
    dependencies: Optional[list[TaskDependency]] = Field(default=None, description="""Tasks that this task depends on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task']} })
    associated_activities: Optional[list[AssociatedActivity]] = Field(default=None, description="""Activities associated with this task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""A collection of tasks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan', 'Task', 'Response']} })
    subjects: Optional[list[AssessmentSubject]] = Field(default=None, description="""Assessment subjects or subject references for this object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'AssociatedActivity',
                       'RelatedTask',
                       'IdentifiedSubject',
                       'Observation',
                       'MitigatingFactor',
                       'RequiredAsset']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_roles: Optional[list[ResponsibleRole]] = Field(default=None, description="""Responsible role assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleRoles']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class EventTiming(ConfiguredBaseModel):
    """
    The timing under which the task is intended to occur.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common']})

    on_date: Optional[OnDateCondition] = Field(default=None, description="""The task is intended to occur on the specified date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EventTiming']} })
    within_date_range: Optional[WithinDateRange] = Field(default=None, description="""The task is intended to occur within the specified date range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EventTiming']} })
    at_frequency: Optional[AtFrequency] = Field(default=None, description="""The task is intended to occur at the specified frequency.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EventTiming']} })


class OnDateCondition(ConfiguredBaseModel):
    """
    The task is intended to occur on the specified date.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'date': {'name': 'date', 'required': True}}})

    date: str = Field(default=..., description="""The date and time when the action occurred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action', 'OnDateCondition']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class WithinDateRange(ConfiguredBaseModel):
    """
    The task is intended to occur within the specified date range.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'end': {'name': 'end', 'required': True},
                        'start': {'name': 'start', 'required': True}}})

    start: str = Field(default=..., description="""The start date/time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithinDateRange', 'PortRange', 'RiskLogEntry']} })
    end: str = Field(default=..., description="""The end date/time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithinDateRange', 'PortRange', 'RiskLogEntry']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class AtFrequency(ConfiguredBaseModel):
    """
    The task is intended to occur at the specified frequency.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'period': {'name': 'period', 'required': True},
                        'unit': {'name': 'unit', 'required': True}}})

    period: int = Field(default=..., description="""The task must occur every period (in the given units).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtFrequency']} })
    unit: TimingUnitEnum = Field(default=..., description="""The unit of time for the period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtFrequency']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class TaskDependency(ConfiguredBaseModel):
    """
    Used to indicate that a task is dependent on another task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'task-uuid': {'name': 'task-uuid', 'required': True}}})

    task_uuid: str = Field(default=..., description="""A UUID reference to a task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSubjectSource', 'TaskDependency', 'RelatedTask']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class AssociatedActivity(HasResponsibleRoles, OscalCommon):
    """
    Identifies an individual activity to be performed as part of a task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon', 'HasResponsibleRoles'],
         'slot_usage': {'activity-uuid': {'name': 'activity-uuid', 'required': True},
                        'subjects': {'name': 'subjects',
                                     'range': 'AssessmentSubject',
                                     'required': True}}})

    activity_uuid: str = Field(default=..., description="""A UUID reference to an activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedActivity']} })
    subjects: list[AssessmentSubject] = Field(default=..., description="""Assessment subjects or subject references for this object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'AssociatedActivity',
                       'RelatedTask',
                       'IdentifiedSubject',
                       'Observation',
                       'MitigatingFactor',
                       'RequiredAsset']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_roles: Optional[list[ResponsibleRole]] = Field(default=None, description="""Responsible role assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleRoles']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class AssessmentPart(HasPropsAndLinks):
    """
    A partition of an assessment plan or results or a child of another part.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['HasPropsAndLinks'],
         'slot_usage': {'name': {'name': 'name',
                                 'range': 'AssessmentPartNameEnum',
                                 'required': True},
                        'parts': {'name': 'parts', 'range': 'AssessmentPart'}}})

    uuid: Optional[str] = Field(default=None, description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    name: AssessmentPartNameEnum = Field(default=..., description="""A textual label that uniquely identifies an attribute or semantic type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Property',
                       'Part',
                       'AssessmentPart',
                       'ControlPart',
                       'Protocol',
                       'Facet']} })
    ns: Optional[str] = Field(default=None, description="""An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property', 'Part', 'AssessmentPart', 'ControlPart']} })
    class_: Optional[str] = Field(default=None, alias="_class", description="""A textual label that provides a sub-type or characterization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Property',
                       'Part',
                       'Parameter',
                       'AssessmentPart',
                       'ControlPart']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    prose: Optional[str] = Field(default=None, description="""Permits multiple paragraphs, lists, tables etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Part', 'ParameterGuideline', 'AssessmentPart', 'ControlPart']} })
    parts: Optional[list[AssessmentPart]] = Field(default=None, description="""A collection of parts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Part',
                       'TermsAndConditions',
                       'LocalObjective',
                       'AssessmentPart',
                       'ControlPart']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ControlPart(HasPropsAndLinks):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['oscal_control_common'],
         'mixins': ['HasPropsAndLinks'],
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'parts': {'name': 'parts', 'range': 'ControlPart'}}})

    id: Optional[str] = Field(default=None, description="""A unique human-oriented identifier within a particular context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })
    name: str = Field(default=..., description="""A textual label that uniquely identifies an attribute or semantic type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Property',
                       'Part',
                       'AssessmentPart',
                       'ControlPart',
                       'Protocol',
                       'Facet']} })
    ns: Optional[str] = Field(default=None, description="""An optional namespace qualifying a name. Allows different organizations to associate distinct semantics with the same name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property', 'Part', 'AssessmentPart', 'ControlPart']} })
    class_: Optional[str] = Field(default=None, alias="_class", description="""A textual label that provides a sub-type or characterization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Property',
                       'Part',
                       'Parameter',
                       'AssessmentPart',
                       'ControlPart']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    prose: Optional[str] = Field(default=None, description="""Permits multiple paragraphs, lists, tables etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Part', 'ParameterGuideline', 'AssessmentPart', 'ControlPart']} })
    parts: Optional[list[ControlPart]] = Field(default=None, description="""A collection of parts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Part',
                       'TermsAndConditions',
                       'LocalObjective',
                       'AssessmentPart',
                       'ControlPart']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class SetParameter(ConfiguredBaseModel):
    """
    Identifies the parameter that will be set by the enclosed value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'slot_usage': {'param-id': {'name': 'param-id', 'required': True},
                        'values': {'name': 'values', 'required': True}}})

    param_id: str = Field(default=..., description="""A reference to a parameter by its identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SetParameter']} })
    values: list[str] = Field(default=..., description="""A parameter value or set of values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter', 'SetParameter']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class SystemComponent(HasResponsibleRoles, OscalCommon):
    """
    A defined component that can be part of an implemented system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'mixins': ['OscalCommon', 'HasResponsibleRoles'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'status': {'inlined': True,
                                   'name': 'status',
                                   'range': 'ComponentStatus',
                                   'required': True},
                        'title': {'name': 'title', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'ComponentTypeEnum',
                                 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    type: ComponentTypeEnum = Field(default=..., description="""Indicates the nature or kind of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    title: str = Field(default=..., description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    purpose: Optional[str] = Field(default=None, description="""A summary of the technological or business purpose of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemComponent']} })
    protocols: Optional[list[Protocol]] = Field(default=None, description="""Information about the protocol used to provide a service.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemComponent']} })
    status: ComponentStatus = Field(default=..., description="""Indicates the status of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemComponent', 'FindingTarget', 'Risk']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_roles: Optional[list[ResponsibleRole]] = Field(default=None, description="""Responsible role assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleRoles']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ComponentStatus(ConfiguredBaseModel):
    """
    Describes the operational status of the system component.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'slot_usage': {'state': {'description': 'The operational status.',
                                  'name': 'state',
                                  'range': 'ComponentStateEnum',
                                  'required': True}}})

    state: ComponentStateEnum = Field(default=..., description="""The operational status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Address',
                       'ComponentStatus',
                       'ImplementationStatus',
                       'ObjectiveStatus']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class Protocol(ConfiguredBaseModel):
    """
    Information about the protocol used to provide a service.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'slot_usage': {'name': {'name': 'name', 'range': 'string', 'required': True}}})

    uuid: Optional[str] = Field(default=None, description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    name: str = Field(default=..., description="""A textual label that uniquely identifies an attribute or semantic type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Property',
                       'Part',
                       'AssessmentPart',
                       'ControlPart',
                       'Protocol',
                       'Facet']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    port_ranges: Optional[list[PortRange]] = Field(default=None, description="""Where applicable, the transport layer protocol port range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Protocol']} })


class PortRange(ConfiguredBaseModel):
    """
    Where applicable, the transport layer protocol port range.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'slot_usage': {'end': {'name': 'end', 'range': 'NonNegativeIntegerType'},
                        'start': {'name': 'start', 'range': 'NonNegativeIntegerType'}}})

    start: Optional[int] = Field(default=None, description="""The start date/time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithinDateRange', 'PortRange', 'RiskLogEntry']} })
    end: Optional[int] = Field(default=None, description="""The end date/time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithinDateRange', 'PortRange', 'RiskLogEntry']} })
    transport: Optional[TransportEnum] = Field(default=None, description="""Indicates the transport type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PortRange']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class ImplementationStatus(ConfiguredBaseModel):
    """
    Indicates the degree to which a given control is implemented.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'slot_usage': {'state': {'description': 'Identifies the implementation status '
                                                 'of the control or control objective.',
                                  'name': 'state',
                                  'range': 'ImplementationStatusStateEnum',
                                  'required': True}}})

    state: ImplementationStatusStateEnum = Field(default=..., description="""Identifies the implementation status of the control or control objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Address',
                       'ComponentStatus',
                       'ImplementationStatus',
                       'ObjectiveStatus']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class SystemUser(OscalCommon):
    """
    A type of user that interacts with the system based on an associated role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    short_name: Optional[str] = Field(default=None, description="""A short common name, abbreviation, or acronym.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'Party', 'SystemUser']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    role_ids: Optional[list[str]] = Field(default=None, description="""Role identifiers associated with the user.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemUser']} })
    authorized_privileges: Optional[list[AuthorizedPrivilege]] = Field(default=None, description="""A collection of authorized privileges.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemUser']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class AuthorizedPrivilege(ConfiguredBaseModel):
    """
    Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'slot_usage': {'functions-performed': {'name': 'functions-performed',
                                                'required': True},
                        'title': {'name': 'title', 'required': True}}})

    title: str = Field(default=..., description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    functions_performed: list[str] = Field(default=..., description="""Describes a function performed for a given authorized privilege.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AuthorizedPrivilege']} })


class InventoryItem(HasResponsibleParties, OscalCommon):
    """
    A single managed inventory item within the system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'mixins': ['OscalCommon', 'HasResponsibleParties'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    implemented_components: Optional[list[ImplementedComponent]] = Field(default=None, description="""A collection of implemented components.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InventoryItem']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_parties: Optional[list[ResponsibleParty]] = Field(default=None, description="""Responsible party assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleParties']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ImplementedComponent(HasResponsibleParties, OscalCommon):
    """
    The set of components that are implemented in a given system inventory item.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'mixins': ['OscalCommon', 'HasResponsibleParties'],
         'slot_usage': {'component-uuid': {'name': 'component-uuid', 'required': True}}})

    component_uuid: str = Field(default=..., description="""A UUID reference to a component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UsesComponent', 'ImplementedComponent']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_parties: Optional[list[ResponsibleParty]] = Field(default=None, description="""Responsible party assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleParties']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class SystemId(ConfiguredBaseModel):
    """
    A human-oriented, globally unique identifier for a system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['implementation_common'],
         'slot_usage': {'id': {'name': 'id', 'range': 'string', 'required': True}}})

    id: str = Field(default=..., description="""A unique human-oriented identifier within a particular context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })
    identifier_type: Optional[str] = Field(default=None, description="""A human-readable label for a specific identifier scheme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemId']} })


class Origin(ConfiguredBaseModel):
    """
    Identifies the source of the finding, such as a tool, interviewed person, or activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'actors': {'name': 'actors', 'required': True}}})

    actors: list[OriginActor] = Field(default=..., description="""The actor that produces an observation, a finding, or a risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Origin']} })
    related_tasks: Optional[list[RelatedTask]] = Field(default=None, description="""Identifies tasks for which the containing object is a consequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Origin', 'RiskResponseReference']} })


class OriginActor(HasPropsAndLinks):
    """
    The actor that produces an observation, a finding, or a risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['HasPropsAndLinks'],
         'slot_usage': {'actor-uuid': {'name': 'actor-uuid', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'OriginActorTypeEnum',
                                 'required': True}}})

    type: OriginActorTypeEnum = Field(default=..., description="""Indicates the nature or kind of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    actor_uuid: str = Field(default=..., description="""A machine-oriented identifier reference to the tool or person based on the associated type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OriginActor']} })
    role_id: Optional[str] = Field(default=None, description="""A reference to a role by its identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResponsibleParty',
                       'ResponsibleRole',
                       'OriginActor',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class RelatedTask(HasResponsibleParties, OscalCommon):
    """
    Identifies an individual task for which the containing object is a consequence of.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon', 'HasResponsibleParties'],
         'slot_usage': {'subjects': {'name': 'subjects', 'range': 'AssessmentSubject'},
                        'task-uuid': {'name': 'task-uuid', 'required': True}}})

    task_uuid: str = Field(default=..., description="""A UUID reference to a task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentSubjectSource', 'TaskDependency', 'RelatedTask']} })
    subjects: Optional[list[AssessmentSubject]] = Field(default=None, description="""Assessment subjects or subject references for this object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'AssociatedActivity',
                       'RelatedTask',
                       'IdentifiedSubject',
                       'Observation',
                       'MitigatingFactor',
                       'RequiredAsset']} })
    identified_subject: Optional[IdentifiedSubject] = Field(default=None, description="""Used to detail assessment subjects that were identified by this task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedTask']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    responsible_parties: Optional[list[ResponsibleParty]] = Field(default=None, description="""Responsible party assignments.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasResponsibleParties']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class IdentifiedSubject(ConfiguredBaseModel):
    """
    Used to detail assessment subjects that were identified by this task.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'subject-placeholder-uuid': {'name': 'subject-placeholder-uuid',
                                                     'required': True},
                        'subjects': {'name': 'subjects',
                                     'range': 'AssessmentSubject',
                                     'required': True}}})

    subject_placeholder_uuid: str = Field(default=..., description="""A reference to an assessment subject placeholder defined in the assessment plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedSubject']} })
    subjects: list[AssessmentSubject] = Field(default=..., description="""Assessment subjects or subject references for this object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'AssociatedActivity',
                       'RelatedTask',
                       'IdentifiedSubject',
                       'Observation',
                       'MitigatingFactor',
                       'RequiredAsset']} })


class Observation(OscalCommon):
    """
    Describes an individual observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'collected': {'name': 'collected', 'required': True},
                        'description': {'name': 'description', 'required': True},
                        'methods': {'name': 'methods', 'required': True},
                        'subjects': {'name': 'subjects', 'range': 'SubjectReference'},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    methods: list[ObservationMethodEnum] = Field(default=..., description="""Identifies how the observation was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation']} })
    types: Optional[list[ObservationTypeEnum]] = Field(default=None, description="""Identifies the nature of the observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation']} })
    origins: Optional[list[Origin]] = Field(default=None, description="""Identifies the source of observations, findings, or risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation', 'Finding', 'Risk', 'Response']} })
    subjects: Optional[list[SubjectReference]] = Field(default=None, description="""Assessment subjects or subject references for this object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'AssociatedActivity',
                       'RelatedTask',
                       'IdentifiedSubject',
                       'Observation',
                       'MitigatingFactor',
                       'RequiredAsset']} })
    relevant_evidence: Optional[list[RelevantEvidence]] = Field(default=None, description="""Links the observation to relevant evidence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation']} })
    collected: str = Field(default=..., description="""Date/time stamp identifying when the finding information was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation']} })
    expires: Optional[str] = Field(default=None, description="""Date/time identifying when the finding information is no longer considered valid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class RelevantEvidence(OscalCommon):
    """
    Links this observation to relevant evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'description': {'name': 'description', 'required': True}}})

    href: Optional[str] = Field(default=None, description="""A resolvable URL reference to a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link',
                       'ResourceLink',
                       'ImportSSP',
                       'RelevantEvidence',
                       'ThreatId']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Finding(OscalCommon):
    """
    Describes an individual finding.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'target': {'name': 'target', 'required': True},
                        'title': {'name': 'title', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: str = Field(default=..., description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    target: FindingTarget = Field(default=..., description="""Identifies the target of a finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding']} })
    implementation_statement_uuid: Optional[str] = Field(default=None, description="""A reference to the implementation statement in the SSP to which this finding is related.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding']} })
    origins: Optional[list[Origin]] = Field(default=None, description="""Identifies the source of observations, findings, or risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation', 'Finding', 'Risk', 'Response']} })
    related_observations: Optional[list[RelatedObservation]] = Field(default=None, description="""Relates the containing object to a set of referenced observations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding', 'Risk']} })
    related_risks: Optional[list[AssociatedRisk]] = Field(default=None, description="""Relates the finding to a set of referenced risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class FindingTarget(OscalCommon):
    """
    Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'status': {'inlined': True,
                                   'name': 'status',
                                   'range': 'ObjectiveStatus',
                                   'required': True},
                        'target-id': {'name': 'target-id', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'FindingTargetTypeEnum',
                                 'required': True}}})

    type: FindingTargetTypeEnum = Field(default=..., description="""Indicates the nature or kind of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Action',
                       'TelephoneNumber',
                       'Address',
                       'AssessmentSubject',
                       'SelectSubjectById',
                       'SubjectReference',
                       'Task',
                       'SystemComponent',
                       'OriginActor',
                       'FindingTarget']} })
    target_id: str = Field(default=..., description="""Identifies the specific target qualified by the type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FindingTarget']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    implementation_status: Optional[ImplementationStatus] = Field(default=None, description="""Identifies the implementation status of the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FindingTarget']} })
    status: ObjectiveStatus = Field(default=..., description="""Indicates the status of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemComponent', 'FindingTarget', 'Risk']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ObjectiveStatus(ConfiguredBaseModel):
    """
    A determination of if the objective is satisfied or not within a given system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'state': {'description': 'An indication as to whether the '
                                                 'objective is satisfied or not.',
                                  'name': 'state',
                                  'range': 'ObjectiveStatusStateEnum',
                                  'required': True}}})

    state: ObjectiveStatusStateEnum = Field(default=..., description="""An indication as to whether the objective is satisfied or not.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Address',
                       'ComponentStatus',
                       'ImplementationStatus',
                       'ObjectiveStatus']} })
    reason: Optional[ObjectiveStatusReasonEnum] = Field(default=None, description="""The reason the objective was given its status.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ObjectiveStatus']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class RelatedObservation(ConfiguredBaseModel):
    """
    Relates the identified element to a set of referenced observations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'observation-uuid': {'name': 'observation-uuid',
                                             'required': True}}})

    observation_uuid: str = Field(default=..., description="""A machine-oriented identifier reference to an observation defined in the list of observations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelatedObservation']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class AssociatedRisk(ConfiguredBaseModel):
    """
    Relates the finding to a set of referenced risks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'risk-uuid': {'name': 'risk-uuid', 'required': True}}})

    risk_uuid: str = Field(default=..., description="""A machine-oriented identifier reference to a risk defined in the list of risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedRisk']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class Risk(HasPropsAndLinks):
    """
    An identified risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['HasPropsAndLinks'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'statement': {'name': 'statement', 'required': True},
                        'status': {'name': 'status',
                                   'range': 'RiskStatusEnum',
                                   'required': True},
                        'title': {'name': 'title', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: str = Field(default=..., description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    statement: str = Field(default=..., description="""An assessor's summary of the risk, in narrative form.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    origins: Optional[list[Origin]] = Field(default=None, description="""Identifies the source of observations, findings, or risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation', 'Finding', 'Risk', 'Response']} })
    threat_ids: Optional[list[ThreatId]] = Field(default=None, description="""The referenced threat identifiers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    characterizations: Optional[list[Characterization]] = Field(default=None, description="""Supporting information about the risk and how it relates to the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    mitigating_factors: Optional[list[MitigatingFactor]] = Field(default=None, description="""Describes existing mitigating factors that may affect the overall determination of the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    deadline: Optional[str] = Field(default=None, description="""The date/time by which the risk must be resolved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    remediations: Optional[list[Response]] = Field(default=None, description="""Describes either recommended or actual responses to a risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    risk_log: Optional[RiskLog] = Field(default=None, description="""A log of all risk-related tasks taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    related_observations: Optional[list[RelatedObservation]] = Field(default=None, description="""Relates the containing object to a set of referenced observations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Finding', 'Risk']} })
    status: RiskStatusEnum = Field(default=..., description="""Indicates the status of the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemComponent', 'FindingTarget', 'Risk']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class ThreatId(ConfiguredBaseModel):
    """
    A pointer, by ID, to an externally-defined threat.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'id': {'name': 'id', 'range': 'URIType', 'required': True},
                        'system': {'description': 'Specifies the system or scheme from '
                                                  'which the identifier originates.',
                                   'name': 'system',
                                   'required': True}}})

    href: Optional[str] = Field(default=None, description="""A resolvable URL reference to a resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link',
                       'ResourceLink',
                       'ImportSSP',
                       'RelevantEvidence',
                       'ThreatId']} })
    system: str = Field(default=..., description="""Specifies the system or scheme from which the identifier originates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action', 'ThreatId', 'Facet']} })
    id: str = Field(default=..., description="""A unique human-oriented identifier within a particular context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Role',
                       'PartyExternalId',
                       'Part',
                       'Parameter',
                       'ControlPart',
                       'SystemId',
                       'ThreatId']} })


class Characterization(HasPropsAndLinks):
    """
    A collection of descriptive data about the containing object from a specific origin.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['HasPropsAndLinks'],
         'slot_usage': {'facets': {'name': 'facets', 'required': True},
                        'origin': {'name': 'origin', 'required': True}}})

    origin: Origin = Field(default=..., description="""The source of the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Characterization']} })
    facets: list[Facet] = Field(default=..., description="""An individual characteristic that is part of a larger set produced by the same actor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Characterization']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Facet(OscalCommon):
    """
    An individual characteristic that is part of a larger set produced by the same actor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'name': {'name': 'name', 'required': True},
                        'system': {'description': 'Specifies the system or scheme from '
                                                  'which the identifier originates.',
                                   'name': 'system',
                                   'required': True},
                        'value': {'name': 'value', 'required': True}}})

    name: str = Field(default=..., description="""A textual label that uniquely identifies an attribute or semantic type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party',
                       'Property',
                       'Part',
                       'AssessmentPart',
                       'ControlPart',
                       'Protocol',
                       'Facet']} })
    value: str = Field(default=..., description="""The value associated with the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Hash', 'Property', 'Base64Resource', 'Facet']} })
    system: str = Field(default=..., description="""Specifies the system or scheme from which the identifier originates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action', 'ThreatId', 'Facet']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class MitigatingFactor(HasPropsAndLinks):
    """
    Describes an existing mitigating factor that may affect the overall determination of the risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['HasPropsAndLinks'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'subjects': {'name': 'subjects', 'range': 'SubjectReference'},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    implementation_uuid: Optional[str] = Field(default=None, description="""A machine-oriented, globally unique identifier with cross-instance scope that can be used to reference this implementation statement elsewhere in this or other OSCAL instances.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MitigatingFactor']} })
    subjects: Optional[list[SubjectReference]] = Field(default=None, description="""Assessment subjects or subject references for this object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'AssociatedActivity',
                       'RelatedTask',
                       'IdentifiedSubject',
                       'Observation',
                       'MitigatingFactor',
                       'RequiredAsset']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class Response(OscalCommon):
    """
    Describes either recommended or an actual plan for addressing the risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'lifecycle': {'name': 'lifecycle', 'required': True},
                        'title': {'name': 'title', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: str = Field(default=..., description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    lifecycle: ResponseLifecycleEnum = Field(default=..., description="""Identifies whether this is a recommendation or an actual plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Response']} })
    origins: Optional[list[Origin]] = Field(default=None, description="""Identifies the source of observations, findings, or risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Observation', 'Finding', 'Risk', 'Response']} })
    required_assets: Optional[list[RequiredAsset]] = Field(default=None, description="""Identifies an asset required to achieve remediation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Response']} })
    tasks: Optional[list[Task]] = Field(default=None, description="""A collection of tasks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssessmentPlan', 'Task', 'Response']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class RequiredAsset(OscalCommon):
    """
    Identifies an asset required to achieve remediation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'description': {'name': 'description', 'required': True},
                        'subjects': {'name': 'subjects', 'range': 'SubjectReference'},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: str = Field(default=..., description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    subjects: Optional[list[SubjectReference]] = Field(default=None, description="""Assessment subjects or subject references for this object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Task',
                       'AssociatedActivity',
                       'RelatedTask',
                       'IdentifiedSubject',
                       'Observation',
                       'MitigatingFactor',
                       'RequiredAsset']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class RiskLog(ConfiguredBaseModel):
    """
    A log of all risk-related tasks taken.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'entries': {'name': 'entries', 'required': True}}})

    entries: list[RiskLogEntry] = Field(default=..., description="""Identifies an individual risk response that occurred as part of managing an identified risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskLog']} })


class RiskLogEntry(OscalCommon):
    """
    Identifies an individual risk response that occurred as part of managing an identified risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'start': {'name': 'start', 'required': True},
                        'uuid': {'name': 'uuid', 'required': True}}})

    uuid: str = Field(default=..., description="""A machine-oriented, globally unique identifier with a cross-instance scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Catalog',
                       'Location',
                       'Party',
                       'Action',
                       'Property',
                       'Resource',
                       'AssessmentPlan',
                       'AssessmentSubjectPlaceholder',
                       'AssessmentPlatform',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'InventoryItem',
                       'Observation',
                       'Finding',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group',
                       'Control',
                       'Metadata',
                       'Revision',
                       'Role',
                       'Location',
                       'Resource',
                       'Part',
                       'SubjectReference',
                       'AssessmentPlatform',
                       'Activity',
                       'Step',
                       'Task',
                       'AssessmentPart',
                       'ControlPart',
                       'SystemComponent',
                       'Protocol',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'Observation',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role',
                       'Resource',
                       'ParameterConstraint',
                       'ReviewedControls',
                       'ControlSelection',
                       'ControlObjectiveSelection',
                       'AssessmentSubject',
                       'AssessmentSubjectPlaceholder',
                       'LocalObjective',
                       'AssessmentMethod',
                       'Activity',
                       'Step',
                       'Task',
                       'SystemComponent',
                       'SystemUser',
                       'AuthorizedPrivilege',
                       'InventoryItem',
                       'Observation',
                       'RelevantEvidence',
                       'Finding',
                       'FindingTarget',
                       'Risk',
                       'MitigatingFactor',
                       'Response',
                       'RequiredAsset',
                       'RiskLogEntry']} })
    start: str = Field(default=..., description="""The start date/time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithinDateRange', 'PortRange', 'RiskLogEntry']} })
    end: Optional[str] = Field(default=None, description="""The end date/time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WithinDateRange', 'PortRange', 'RiskLogEntry']} })
    logged_by: Optional[list[LoggedBy]] = Field(default=None, description="""Used to indicate who created a log entry in what role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskLogEntry']} })
    status_change: Optional[RiskStatusEnum] = Field(default=None, description="""Identifies the risk change that prompted the log entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskLogEntry']} })
    related_responses: Optional[list[RiskResponseReference]] = Field(default=None, description="""Identifies an individual risk response that this log entry is for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskLogEntry']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


class LoggedBy(ConfiguredBaseModel):
    """
    Used to indicate who created a log entry in what role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'slot_usage': {'party-uuid': {'name': 'party-uuid', 'required': True}}})

    party_uuid: str = Field(default=..., description="""A machine-oriented identifier reference to the party who is making the log entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LoggedBy']} })
    role_id: Optional[str] = Field(default=None, description="""A reference to a role by its identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResponsibleParty',
                       'ResponsibleRole',
                       'OriginActor',
                       'LoggedBy']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })


class RiskResponseReference(OscalCommon):
    """
    Identifies an individual risk response that this log entry is for.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/oscal_assessment_plan',
         'in_subset': ['assessment_common'],
         'mixins': ['OscalCommon'],
         'slot_usage': {'response-uuid': {'name': 'response-uuid', 'required': True}}})

    response_uuid: str = Field(default=..., description="""A machine-oriented identifier reference to a unique risk response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskResponseReference']} })
    related_tasks: Optional[list[RelatedTask]] = Field(default=None, description="""Identifies tasks for which the containing object is a consequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Origin', 'RiskResponseReference']} })
    remarks: Optional[str] = Field(default=None, description="""Additional commentary about the containing object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['OscalCommon',
                       'Property',
                       'Resource',
                       'ConstraintTest',
                       'ControlMatching',
                       'ImportSSP',
                       'LocalDefinitions',
                       'SelectObjectiveById',
                       'AssessmentSubjectSource',
                       'OnDateCondition',
                       'WithinDateRange',
                       'AtFrequency',
                       'TaskDependency',
                       'SetParameter',
                       'ComponentStatus',
                       'PortRange',
                       'ImplementationStatus',
                       'ObjectiveStatus',
                       'RelatedObservation',
                       'AssociatedRisk',
                       'LoggedBy']} })
    props: Optional[list[Property]] = Field(default=None, description="""A list of properties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks', 'Resource']} })
    links: Optional[list[Link]] = Field(default=None, description="""A list of links.""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasPropsAndLinks']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
HasPropsAndLinks.model_rebuild()
OscalCommon.model_rebuild()
HasResponsibleRoles.model_rebuild()
HasResponsibleParties.model_rebuild()
OscalDocument.model_rebuild()
CatalogDocument.model_rebuild()
Catalog.model_rebuild()
Group.model_rebuild()
Control.model_rebuild()
Metadata.model_rebuild()
Revision.model_rebuild()
DocumentId.model_rebuild()
Role.model_rebuild()
Location.model_rebuild()
Party.model_rebuild()
PartyExternalId.model_rebuild()
ResponsibleParty.model_rebuild()
ResponsibleRole.model_rebuild()
Action.model_rebuild()
TelephoneNumber.model_rebuild()
Address.model_rebuild()
Hash.model_rebuild()
Property.model_rebuild()
Link.model_rebuild()
BackMatter.model_rebuild()
Resource.model_rebuild()
Citation.model_rebuild()
ResourceLink.model_rebuild()
Base64Resource.model_rebuild()
Part.model_rebuild()
Parameter.model_rebuild()
ParameterConstraint.model_rebuild()
ConstraintTest.model_rebuild()
ParameterGuideline.model_rebuild()
ParameterSelection.model_rebuild()
IncludeAll.model_rebuild()
ControlMatching.model_rebuild()
SelectControlById.model_rebuild()
AssessmentPlanDocument.model_rebuild()
AssessmentPlan.model_rebuild()
ImportSSP.model_rebuild()
LocalDefinitions.model_rebuild()
TermsAndConditions.model_rebuild()
ReviewedControls.model_rebuild()
ControlSelection.model_rebuild()
ControlObjectiveSelection.model_rebuild()
AssessmentSelectControlById.model_rebuild()
SelectObjectiveById.model_rebuild()
AssessmentSubject.model_rebuild()
SelectSubjectById.model_rebuild()
SubjectReference.model_rebuild()
AssessmentSubjectPlaceholder.model_rebuild()
AssessmentSubjectSource.model_rebuild()
AssessmentAssets.model_rebuild()
AssessmentPlatform.model_rebuild()
UsesComponent.model_rebuild()
LocalObjective.model_rebuild()
AssessmentMethod.model_rebuild()
Activity.model_rebuild()
Step.model_rebuild()
Task.model_rebuild()
EventTiming.model_rebuild()
OnDateCondition.model_rebuild()
WithinDateRange.model_rebuild()
AtFrequency.model_rebuild()
TaskDependency.model_rebuild()
AssociatedActivity.model_rebuild()
AssessmentPart.model_rebuild()
ControlPart.model_rebuild()
SetParameter.model_rebuild()
SystemComponent.model_rebuild()
ComponentStatus.model_rebuild()
Protocol.model_rebuild()
PortRange.model_rebuild()
ImplementationStatus.model_rebuild()
SystemUser.model_rebuild()
AuthorizedPrivilege.model_rebuild()
InventoryItem.model_rebuild()
ImplementedComponent.model_rebuild()
SystemId.model_rebuild()
Origin.model_rebuild()
OriginActor.model_rebuild()
RelatedTask.model_rebuild()
IdentifiedSubject.model_rebuild()
Observation.model_rebuild()
RelevantEvidence.model_rebuild()
Finding.model_rebuild()
FindingTarget.model_rebuild()
ObjectiveStatus.model_rebuild()
RelatedObservation.model_rebuild()
AssociatedRisk.model_rebuild()
Risk.model_rebuild()
ThreatId.model_rebuild()
Characterization.model_rebuild()
Facet.model_rebuild()
MitigatingFactor.model_rebuild()
Response.model_rebuild()
RequiredAsset.model_rebuild()
RiskLog.model_rebuild()
RiskLogEntry.model_rebuild()
LoggedBy.model_rebuild()
RiskResponseReference.model_rebuild()
