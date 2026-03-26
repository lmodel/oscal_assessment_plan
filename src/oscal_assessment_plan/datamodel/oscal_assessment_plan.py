# Auto generated from oscal_assessment_plan.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-27T16:32:12
# Schema: oscal_assessment_plan
#
# id: https://w3id.org/lmodel/oscal_assessment_plan
# description: OSCAL Assessment Plan Model: LinkML Schema
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = "1.2.1"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OSCAL_ASSESSMENT_PLAN = CurieNamespace('oscal_assessment_plan', 'https://w3id.org/lmodel/oscal_assessment_plan/')
OSCAL_CATALOG = CurieNamespace('oscal_catalog', 'https://w3id.org/lmodel/oscal_catalog/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = OSCAL_ASSESSMENT_PLAN


# Types
class NonNegativeIntegerType(int):
    """ A non-negative integer value (>= 0), as used for port range boundaries. """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NonNegativeIntegerType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.NonNegativeIntegerType


class PositiveIntegerType(int):
    """ A positive integer value (>= 1), as used for task recurrence periods. """
    type_class_uri = XSD["positiveInteger"]
    type_class_curie = "xsd:positiveInteger"
    type_name = "PositiveIntegerType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.PositiveIntegerType


class UUIDType(str):
    """ A type 4 or type 5 UUID per RFC 4122. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UUIDType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.UUIDType


class URIType(str):
    """ A universal resource identifier formatted according to RFC3986. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URIType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.URIType


class URIReferenceType(str):
    """ A URI Reference, either a URI or relative-reference, per RFC3986. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URIReferenceType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.URIReferenceType


class DateTimeWithTimezoneType(str):
    """ A string representing a point in time with a required timezone. """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "DateTimeWithTimezoneType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.DateTimeWithTimezoneType


class MarkupLineType(str):
    """ A single line of Markdown content (no newlines). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "MarkupLineType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.MarkupLineType


class MarkupMultilineType(str):
    """ Multiple lines of Markdown content. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "MarkupMultilineType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.MarkupMultilineType


class TokenType(str):
    """ A non-colonized XML NCName token. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "TokenType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.TokenType


class Base64Type(str):
    """ Binary data encoded using Base64 as defined by RFC4648. """
    type_class_uri = XSD["base64Binary"]
    type_class_curie = "xsd:base64Binary"
    type_name = "Base64Type"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.Base64Type


class EmailAddressType(str):
    """ An email address string formatted according to RFC 6531. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "EmailAddressType"
    type_model_uri = OSCAL_ASSESSMENT_PLAN.EmailAddressType


# Class references



@dataclass(repr=False)
class AssessmentPlan(YAMLRoot):
    """
    An assessment plan, such as those provided by a FedRAMP assessor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentPlan"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentPlan"
    class_name: ClassVar[str] = "AssessmentPlan"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentPlan

    uuid: str = None
    metadata: Union[dict, "Metadata"] = None
    import_ssp: Union[dict, "ImportSSP"] = None
    reviewed_controls: Union[dict, "ReviewedControls"] = None
    local_definitions: Optional[Union[dict, "LocalDefinitions"]] = None
    terms_and_conditions: Optional[Union[dict, "TermsAndConditions"]] = None
    assessment_subjects: Optional[Union[Union[dict, "AssessmentSubject"], list[Union[dict, "AssessmentSubject"]]]] = empty_list()
    assessment_assets: Optional[Union[dict, "AssessmentAssets"]] = None
    tasks: Optional[Union[Union[dict, "Task"], list[Union[dict, "Task"]]]] = empty_list()
    back_matter: Optional[Union[dict, "BackMatter"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self._is_empty(self.import_ssp):
            self.MissingRequiredField("import_ssp")
        if not isinstance(self.import_ssp, ImportSSP):
            self.import_ssp = ImportSSP(**as_dict(self.import_ssp))

        if self._is_empty(self.reviewed_controls):
            self.MissingRequiredField("reviewed_controls")
        if not isinstance(self.reviewed_controls, ReviewedControls):
            self.reviewed_controls = ReviewedControls(**as_dict(self.reviewed_controls))

        if self.local_definitions is not None and not isinstance(self.local_definitions, LocalDefinitions):
            self.local_definitions = LocalDefinitions(**as_dict(self.local_definitions))

        if self.terms_and_conditions is not None and not isinstance(self.terms_and_conditions, TermsAndConditions):
            self.terms_and_conditions = TermsAndConditions(**as_dict(self.terms_and_conditions))

        self._normalize_inlined_as_list(slot_name="assessment_subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        if self.assessment_assets is not None and not isinstance(self.assessment_assets, AssessmentAssets):
            self.assessment_assets = AssessmentAssets(**as_dict(self.assessment_assets))

        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="uuid", keyed=False)

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImportSSP(YAMLRoot):
    """
    Used by the assessment plan and POA&M to import information about the system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImportSSP"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImportSSP"
    class_name: ClassVar[str] = "ImportSSP"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ImportSSP

    href: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocalDefinitions(YAMLRoot):
    """
    Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["LocalDefinitions"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:LocalDefinitions"
    class_name: ClassVar[str] = "LocalDefinitions"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.LocalDefinitions

    components: Optional[Union[Union[dict, "SystemComponent"], list[Union[dict, "SystemComponent"]]]] = empty_list()
    inventory_items: Optional[Union[Union[dict, "InventoryItem"], list[Union[dict, "InventoryItem"]]]] = empty_list()
    users: Optional[Union[Union[dict, "SystemUser"], list[Union[dict, "SystemUser"]]]] = empty_list()
    objectives_and_methods: Optional[Union[Union[dict, "LocalObjective"], list[Union[dict, "LocalObjective"]]]] = empty_list()
    activities: Optional[Union[Union[dict, "Activity"], list[Union[dict, "Activity"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="components", slot_type=SystemComponent, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="inventory_items", slot_type=InventoryItem, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="users", slot_type=SystemUser, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="objectives_and_methods", slot_type=LocalObjective, key_name="control_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="activities", slot_type=Activity, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermsAndConditions(YAMLRoot):
    """
    Used to define various terms and conditions under which an assessment can be performed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["TermsAndConditions"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:TermsAndConditions"
    class_name: ClassVar[str] = "TermsAndConditions"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.TermsAndConditions

    parts: Optional[Union[Union[dict, "AssessmentPart"], list[Union[dict, "AssessmentPart"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="parts", slot_type=AssessmentPart, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReviewedControls(YAMLRoot):
    """
    Identifies the controls being assessed and their control objectives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ReviewedControls"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ReviewedControls"
    class_name: ClassVar[str] = "ReviewedControls"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ReviewedControls

    control_selections: Union[Union[dict, "ControlSelection"], list[Union[dict, "ControlSelection"]]] = None
    description: Optional[str] = None
    control_objective_selections: Optional[Union[Union[dict, "ControlObjectiveSelection"], list[Union[dict, "ControlObjectiveSelection"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_selections):
            self.MissingRequiredField("control_selections")
        if not isinstance(self.control_selections, list):
            self.control_selections = [self.control_selections] if self.control_selections is not None else []
        self.control_selections = [v if isinstance(v, ControlSelection) else ControlSelection(**as_dict(v)) for v in self.control_selections]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.control_objective_selections, list):
            self.control_objective_selections = [self.control_objective_selections] if self.control_objective_selections is not None else []
        self.control_objective_selections = [v if isinstance(v, ControlObjectiveSelection) else ControlObjectiveSelection(**as_dict(v)) for v in self.control_objective_selections]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlSelection(YAMLRoot):
    """
    Identifies the controls being assessed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ControlSelection"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ControlSelection"
    class_name: ClassVar[str] = "ControlSelection"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ControlSelection

    description: Optional[str] = None
    include_all: Optional[Union[dict, "IncludeAll"]] = None
    include_controls: Optional[Union[Union[dict, "AssessmentSelectControlById"], list[Union[dict, "AssessmentSelectControlById"]]]] = empty_list()
    exclude_controls: Optional[Union[Union[dict, "AssessmentSelectControlById"], list[Union[dict, "AssessmentSelectControlById"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.include_all is not None and not isinstance(self.include_all, IncludeAll):
            self.include_all = IncludeAll()

        self._normalize_inlined_as_list(slot_name="include_controls", slot_type=AssessmentSelectControlById, key_name="control_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="exclude_controls", slot_type=AssessmentSelectControlById, key_name="control_id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlObjectiveSelection(YAMLRoot):
    """
    Identifies the control objectives of the assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ControlObjectiveSelection"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ControlObjectiveSelection"
    class_name: ClassVar[str] = "ControlObjectiveSelection"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ControlObjectiveSelection

    description: Optional[str] = None
    include_all: Optional[Union[dict, "IncludeAll"]] = None
    include_objectives: Optional[Union[Union[dict, "SelectObjectiveById"], list[Union[dict, "SelectObjectiveById"]]]] = empty_list()
    exclude_objectives: Optional[Union[Union[dict, "SelectObjectiveById"], list[Union[dict, "SelectObjectiveById"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.include_all is not None and not isinstance(self.include_all, IncludeAll):
            self.include_all = IncludeAll()

        self._normalize_inlined_as_list(slot_name="include_objectives", slot_type=SelectObjectiveById, key_name="objective_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="exclude_objectives", slot_type=SelectObjectiveById, key_name="objective_id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentSelectControlById(YAMLRoot):
    """
    Select a specific control for inclusion/exclusion in the assessment by literal control ID and optional statement
    IDs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentSelectControlById"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentSelectControlById"
    class_name: ClassVar[str] = "AssessmentSelectControlById"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentSelectControlById

    control_id: str = None
    statement_ids: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        if not isinstance(self.statement_ids, list):
            self.statement_ids = [self.statement_ids] if self.statement_ids is not None else []
        self.statement_ids = [v if isinstance(v, str) else str(v) for v in self.statement_ids]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SelectObjectiveById(YAMLRoot):
    """
    Used to select a control objective for inclusion/exclusion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SelectObjectiveById"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SelectObjectiveById"
    class_name: ClassVar[str] = "SelectObjectiveById"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.SelectObjectiveById

    objective_id: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.objective_id):
            self.MissingRequiredField("objective_id")
        if not isinstance(self.objective_id, str):
            self.objective_id = str(self.objective_id)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentSubject(YAMLRoot):
    """
    Identifies system elements being assessed, such as components, inventory items, and locations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentSubject"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentSubject"
    class_name: ClassVar[str] = "AssessmentSubject"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentSubject

    type: Union[str, "AssessmentSubjectTypeEnum"] = None
    description: Optional[str] = None
    include_all: Optional[Union[dict, "IncludeAll"]] = None
    include_subjects: Optional[Union[Union[dict, "SelectSubjectById"], list[Union[dict, "SelectSubjectById"]]]] = empty_list()
    exclude_subjects: Optional[Union[Union[dict, "SelectSubjectById"], list[Union[dict, "SelectSubjectById"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, AssessmentSubjectTypeEnum):
            self.type = AssessmentSubjectTypeEnum(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.include_all is not None and not isinstance(self.include_all, IncludeAll):
            self.include_all = IncludeAll()

        self._normalize_inlined_as_list(slot_name="include_subjects", slot_type=SelectSubjectById, key_name="subject_uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="exclude_subjects", slot_type=SelectSubjectById, key_name="subject_uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SelectSubjectById(YAMLRoot):
    """
    Identifies a set of assessment subjects to include/exclude by UUID.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SelectSubjectById"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SelectSubjectById"
    class_name: ClassVar[str] = "SelectSubjectById"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.SelectSubjectById

    subject_uuid: str = None
    type: Union[str, "SelectSubjectTypeEnum"] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_uuid):
            self.MissingRequiredField("subject_uuid")
        if not isinstance(self.subject_uuid, str):
            self.subject_uuid = str(self.subject_uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SelectSubjectTypeEnum):
            self.type = SelectSubjectTypeEnum(self.type)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubjectReference(YAMLRoot):
    """
    A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a
    component, inventory item, location, user, or something else.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SubjectReference"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SubjectReference"
    class_name: ClassVar[str] = "SubjectReference"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.SubjectReference

    subject_uuid: str = None
    type: Union[str, "SelectSubjectTypeEnum"] = None
    title: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_uuid):
            self.MissingRequiredField("subject_uuid")
        if not isinstance(self.subject_uuid, str):
            self.subject_uuid = str(self.subject_uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SelectSubjectTypeEnum):
            self.type = SelectSubjectTypeEnum(self.type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentSubjectPlaceholder(YAMLRoot):
    """
    Used when the assessment subjects will be determined as part of one or more other assessment activities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentSubjectPlaceholder"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentSubjectPlaceholder"
    class_name: ClassVar[str] = "AssessmentSubjectPlaceholder"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentSubjectPlaceholder

    uuid: str = None
    sources: Union[Union[dict, "AssessmentSubjectSource"], list[Union[dict, "AssessmentSubjectSource"]]] = None
    description: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.sources):
            self.MissingRequiredField("sources")
        self._normalize_inlined_as_list(slot_name="sources", slot_type=AssessmentSubjectSource, key_name="task_uuid", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentSubjectSource(YAMLRoot):
    """
    Assessment subjects will be identified while conducting the referenced activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentSubjectSource"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentSubjectSource"
    class_name: ClassVar[str] = "AssessmentSubjectSource"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentSubjectSource

    task_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.task_uuid):
            self.MissingRequiredField("task_uuid")
        if not isinstance(self.task_uuid, str):
            self.task_uuid = str(self.task_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentAssets(YAMLRoot):
    """
    Identifies the assets used to perform this assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentAssets"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentAssets"
    class_name: ClassVar[str] = "AssessmentAssets"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentAssets

    assessment_platforms: Union[Union[dict, "AssessmentPlatform"], list[Union[dict, "AssessmentPlatform"]]] = None
    components: Optional[Union[Union[dict, "SystemComponent"], list[Union[dict, "SystemComponent"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment_platforms):
            self.MissingRequiredField("assessment_platforms")
        self._normalize_inlined_as_list(slot_name="assessment_platforms", slot_type=AssessmentPlatform, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="components", slot_type=SystemComponent, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentPlatform(YAMLRoot):
    """
    Used to represent the toolset used to perform aspects of the assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentPlatform"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentPlatform"
    class_name: ClassVar[str] = "AssessmentPlatform"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentPlatform

    uuid: str = None
    title: Optional[str] = None
    uses_components: Optional[Union[Union[dict, "UsesComponent"], list[Union[dict, "UsesComponent"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="uses_components", slot_type=UsesComponent, key_name="component_uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UsesComponent(YAMLRoot):
    """
    The set of components that are used by the assessment platform.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["UsesComponent"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:UsesComponent"
    class_name: ClassVar[str] = "UsesComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.UsesComponent

    component_uuid: str = None
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, "ResponsibleParty"], list[Union[dict, "ResponsibleParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_uuid):
            self.MissingRequiredField("component_uuid")
        if not isinstance(self.component_uuid, str):
            self.component_uuid = str(self.component_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocalObjective(YAMLRoot):
    """
    A local definition of a control objective for this assessment. Uses catalog syntax for control objective and
    assessment actions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["LocalObjective"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:LocalObjective"
    class_name: ClassVar[str] = "LocalObjective"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.LocalObjective

    control_id: str = None
    parts: Union[Union[dict, "ControlPart"], list[Union[dict, "ControlPart"]]] = None
    description: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_id):
            self.MissingRequiredField("control_id")
        if not isinstance(self.control_id, str):
            self.control_id = str(self.control_id)

        if self._is_empty(self.parts):
            self.MissingRequiredField("parts")
        self._normalize_inlined_as_list(slot_name="parts", slot_type=ControlPart, key_name="name", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentMethod(YAMLRoot):
    """
    A local definition of a control objective.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentMethod"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentMethod"
    class_name: ClassVar[str] = "AssessmentMethod"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentMethod

    uuid: str = None
    part: Union[dict, "AssessmentPart"] = None
    description: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.part):
            self.MissingRequiredField("part")
        if not isinstance(self.part, AssessmentPart):
            self.part = AssessmentPart(**as_dict(self.part))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Activity(YAMLRoot):
    """
    Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended
    activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Activity"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Activity

    uuid: str = None
    description: str = None
    title: Optional[str] = None
    steps: Optional[Union[Union[dict, "Step"], list[Union[dict, "Step"]]]] = empty_list()
    related_controls: Optional[Union[dict, ReviewedControls]] = None
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, "ResponsibleRole"], list[Union[dict, "ResponsibleRole"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="steps", slot_type=Step, key_name="uuid", keyed=False)

        if self.related_controls is not None and not isinstance(self.related_controls, ReviewedControls):
            self.related_controls = ReviewedControls(**as_dict(self.related_controls))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Step(YAMLRoot):
    """
    Identifies an individual step in a series of steps related to an activity, such as an assessment test or
    examination procedure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Step"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Step"
    class_name: ClassVar[str] = "Step"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Step

    uuid: str = None
    description: str = None
    title: Optional[str] = None
    reviewed_controls: Optional[Union[dict, ReviewedControls]] = None
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, "ResponsibleRole"], list[Union[dict, "ResponsibleRole"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.reviewed_controls is not None and not isinstance(self.reviewed_controls, ReviewedControls):
            self.reviewed_controls = ReviewedControls(**as_dict(self.reviewed_controls))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Task(YAMLRoot):
    """
    Represents a scheduled event or milestone, which may be associated with a series of assessment actions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Task"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Task"
    class_name: ClassVar[str] = "Task"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Task

    uuid: str = None
    type: Union[str, "TaskTypeEnum"] = None
    title: str = None
    description: Optional[str] = None
    timing: Optional[Union[dict, "EventTiming"]] = None
    dependencies: Optional[Union[Union[dict, "TaskDependency"], list[Union[dict, "TaskDependency"]]]] = empty_list()
    associated_activities: Optional[Union[Union[dict, "AssociatedActivity"], list[Union[dict, "AssociatedActivity"]]]] = empty_list()
    tasks: Optional[Union[Union[dict, "Task"], list[Union[dict, "Task"]]]] = empty_list()
    subjects: Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]] = empty_list()
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, "ResponsibleRole"], list[Union[dict, "ResponsibleRole"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, TaskTypeEnum):
            self.type = TaskTypeEnum(self.type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.timing is not None and not isinstance(self.timing, EventTiming):
            self.timing = EventTiming(**as_dict(self.timing))

        self._normalize_inlined_as_list(slot_name="dependencies", slot_type=TaskDependency, key_name="task_uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="associated_activities", slot_type=AssociatedActivity, key_name="activity_uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventTiming(YAMLRoot):
    """
    The timing under which the task is intended to occur.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["EventTiming"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:EventTiming"
    class_name: ClassVar[str] = "EventTiming"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.EventTiming

    on_date: Optional[Union[dict, "OnDateCondition"]] = None
    within_date_range: Optional[Union[dict, "WithinDateRange"]] = None
    at_frequency: Optional[Union[dict, "AtFrequency"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.on_date is not None and not isinstance(self.on_date, OnDateCondition):
            self.on_date = OnDateCondition(**as_dict(self.on_date))

        if self.within_date_range is not None and not isinstance(self.within_date_range, WithinDateRange):
            self.within_date_range = WithinDateRange(**as_dict(self.within_date_range))

        if self.at_frequency is not None and not isinstance(self.at_frequency, AtFrequency):
            self.at_frequency = AtFrequency(**as_dict(self.at_frequency))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OnDateCondition(YAMLRoot):
    """
    The task is intended to occur on the specified date.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["OnDateCondition"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:OnDateCondition"
    class_name: ClassVar[str] = "OnDateCondition"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.OnDateCondition

    date: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.date):
            self.MissingRequiredField("date")
        if not isinstance(self.date, str):
            self.date = str(self.date)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithinDateRange(YAMLRoot):
    """
    The task is intended to occur within the specified date range.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["WithinDateRange"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:WithinDateRange"
    class_name: ClassVar[str] = "WithinDateRange"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.WithinDateRange

    start: str = None
    end: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, str):
            self.start = str(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, str):
            self.end = str(self.end)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtFrequency(YAMLRoot):
    """
    The task is intended to occur at the specified frequency.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AtFrequency"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AtFrequency"
    class_name: ClassVar[str] = "AtFrequency"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AtFrequency

    period: int = None
    unit: Union[str, "TimingUnitEnum"] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.period):
            self.MissingRequiredField("period")
        if not isinstance(self.period, int):
            self.period = int(self.period)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, TimingUnitEnum):
            self.unit = TimingUnitEnum(self.unit)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaskDependency(YAMLRoot):
    """
    Used to indicate that a task is dependent on another task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["TaskDependency"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:TaskDependency"
    class_name: ClassVar[str] = "TaskDependency"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.TaskDependency

    task_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.task_uuid):
            self.MissingRequiredField("task_uuid")
        if not isinstance(self.task_uuid, str):
            self.task_uuid = str(self.task_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociatedActivity(YAMLRoot):
    """
    Identifies an individual activity to be performed as part of a task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssociatedActivity"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssociatedActivity"
    class_name: ClassVar[str] = "AssociatedActivity"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssociatedActivity

    activity_uuid: str = None
    subjects: Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]] = None
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, "ResponsibleRole"], list[Union[dict, "ResponsibleRole"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.activity_uuid):
            self.MissingRequiredField("activity_uuid")
        if not isinstance(self.activity_uuid, str):
            self.activity_uuid = str(self.activity_uuid)

        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        self._normalize_inlined_as_list(slot_name="subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssessmentPart(YAMLRoot):
    """
    A partition of an assessment plan or results or a child of another part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentPart"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentPart"
    class_name: ClassVar[str] = "AssessmentPart"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentPart

    name: Union[str, "AssessmentPartNameEnum"] = None
    uuid: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None
    title: Optional[str] = None
    prose: Optional[str] = None
    parts: Optional[Union[Union[dict, "AssessmentPart"], list[Union[dict, "AssessmentPart"]]]] = empty_list()
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, AssessmentPartNameEnum):
            self.name = AssessmentPartNameEnum(self.name)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=AssessmentPart, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlPart(YAMLRoot):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another
    part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ControlPart"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ControlPart"
    class_name: ClassVar[str] = "ControlPart"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ControlPart

    name: str = None
    id: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None
    title: Optional[str] = None
    prose: Optional[str] = None
    parts: Optional[Union[Union[dict, "ControlPart"], list[Union[dict, "ControlPart"]]]] = empty_list()
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=ControlPart, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SetParameter(YAMLRoot):
    """
    Identifies the parameter that will be set by the enclosed value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SetParameter"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SetParameter"
    class_name: ClassVar[str] = "SetParameter"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.SetParameter

    param_id: str = None
    values: Union[str, list[str]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.param_id):
            self.MissingRequiredField("param_id")
        if not isinstance(self.param_id, str):
            self.param_id = str(self.param_id)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemComponent(YAMLRoot):
    """
    A defined component that can be part of an implemented system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SystemComponent"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SystemComponent"
    class_name: ClassVar[str] = "SystemComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.SystemComponent

    uuid: str = None
    type: Union[str, "ComponentTypeEnum"] = None
    title: str = None
    description: str = None
    status: Union[dict, "ComponentStatus"] = None
    purpose: Optional[str] = None
    protocols: Optional[Union[Union[dict, "Protocol"], list[Union[dict, "Protocol"]]]] = empty_list()
    remarks: Optional[str] = None
    responsible_roles: Optional[Union[Union[dict, "ResponsibleRole"], list[Union[dict, "ResponsibleRole"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, ComponentTypeEnum):
            self.type = ComponentTypeEnum(self.type)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, ComponentStatus):
            self.status = ComponentStatus(**as_dict(self.status))

        if self.purpose is not None and not isinstance(self.purpose, str):
            self.purpose = str(self.purpose)

        self._normalize_inlined_as_list(slot_name="protocols", slot_type=Protocol, key_name="name", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentStatus(YAMLRoot):
    """
    Describes the operational status of the system component.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ComponentStatus"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ComponentStatus"
    class_name: ClassVar[str] = "ComponentStatus"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ComponentStatus

    state: Union[str, "ComponentStateEnum"] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, ComponentStateEnum):
            self.state = ComponentStateEnum(self.state)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Protocol(YAMLRoot):
    """
    Information about the protocol used to provide a service.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Protocol"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Protocol"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Protocol

    name: str = None
    uuid: Optional[str] = None
    title: Optional[str] = None
    port_ranges: Optional[Union[Union[dict, "PortRange"], list[Union[dict, "PortRange"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.port_ranges, list):
            self.port_ranges = [self.port_ranges] if self.port_ranges is not None else []
        self.port_ranges = [v if isinstance(v, PortRange) else PortRange(**as_dict(v)) for v in self.port_ranges]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PortRange(YAMLRoot):
    """
    Where applicable, the transport layer protocol port range.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["PortRange"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:PortRange"
    class_name: ClassVar[str] = "PortRange"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.PortRange

    start: Optional[int] = None
    end: Optional[int] = None
    transport: Optional[Union[str, "TransportEnum"]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.start is not None and not isinstance(self.start, int):
            self.start = int(self.start)

        if self.end is not None and not isinstance(self.end, int):
            self.end = int(self.end)

        if self.transport is not None and not isinstance(self.transport, TransportEnum):
            self.transport = TransportEnum(self.transport)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementationStatus(YAMLRoot):
    """
    Indicates the degree to which a given control is implemented.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImplementationStatus"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImplementationStatus"
    class_name: ClassVar[str] = "ImplementationStatus"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ImplementationStatus

    state: Union[str, "ImplementationStatusStateEnum"] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, ImplementationStatusStateEnum):
            self.state = ImplementationStatusStateEnum(self.state)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemUser(YAMLRoot):
    """
    A type of user that interacts with the system based on an associated role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SystemUser"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SystemUser"
    class_name: ClassVar[str] = "SystemUser"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.SystemUser

    uuid: str = None
    title: Optional[str] = None
    short_name: Optional[str] = None
    description: Optional[str] = None
    role_ids: Optional[Union[str, list[str]]] = empty_list()
    authorized_privileges: Optional[Union[Union[dict, "AuthorizedPrivilege"], list[Union[dict, "AuthorizedPrivilege"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.role_ids, list):
            self.role_ids = [self.role_ids] if self.role_ids is not None else []
        self.role_ids = [v if isinstance(v, str) else str(v) for v in self.role_ids]

        self._normalize_inlined_as_list(slot_name="authorized_privileges", slot_type=AuthorizedPrivilege, key_name="title", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthorizedPrivilege(YAMLRoot):
    """
    Identifies a specific system privilege held by the user, along with an associated description and/or rationale for
    the privilege.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AuthorizedPrivilege"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AuthorizedPrivilege"
    class_name: ClassVar[str] = "AuthorizedPrivilege"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AuthorizedPrivilege

    title: str = None
    functions_performed: Union[str, list[str]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.functions_performed):
            self.MissingRequiredField("functions_performed")
        if not isinstance(self.functions_performed, list):
            self.functions_performed = [self.functions_performed] if self.functions_performed is not None else []
        self.functions_performed = [v if isinstance(v, str) else str(v) for v in self.functions_performed]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InventoryItem(YAMLRoot):
    """
    A single managed inventory item within the system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["InventoryItem"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:InventoryItem"
    class_name: ClassVar[str] = "InventoryItem"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.InventoryItem

    uuid: str = None
    description: str = None
    implemented_components: Optional[Union[Union[dict, "ImplementedComponent"], list[Union[dict, "ImplementedComponent"]]]] = empty_list()
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, "ResponsibleParty"], list[Union[dict, "ResponsibleParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="implemented_components", slot_type=ImplementedComponent, key_name="component_uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementedComponent(YAMLRoot):
    """
    The set of components that are implemented in a given system inventory item.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ImplementedComponent"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ImplementedComponent"
    class_name: ClassVar[str] = "ImplementedComponent"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ImplementedComponent

    component_uuid: str = None
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, "ResponsibleParty"], list[Union[dict, "ResponsibleParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_uuid):
            self.MissingRequiredField("component_uuid")
        if not isinstance(self.component_uuid, str):
            self.component_uuid = str(self.component_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemId(YAMLRoot):
    """
    A human-oriented, globally unique identifier for a system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["SystemId"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:SystemId"
    class_name: ClassVar[str] = "SystemId"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.SystemId

    id: str = None
    identifier_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.identifier_type is not None and not isinstance(self.identifier_type, str):
            self.identifier_type = str(self.identifier_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Origin(YAMLRoot):
    """
    Identifies the source of the finding, such as a tool, interviewed person, or activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Origin"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Origin"
    class_name: ClassVar[str] = "Origin"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Origin

    actors: Union[Union[dict, "OriginActor"], list[Union[dict, "OriginActor"]]] = None
    related_tasks: Optional[Union[Union[dict, "RelatedTask"], list[Union[dict, "RelatedTask"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.actors):
            self.MissingRequiredField("actors")
        self._normalize_inlined_as_list(slot_name="actors", slot_type=OriginActor, key_name="type", keyed=False)

        self._normalize_inlined_as_list(slot_name="related_tasks", slot_type=RelatedTask, key_name="task_uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OriginActor(YAMLRoot):
    """
    The actor that produces an observation, a finding, or a risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["OriginActor"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:OriginActor"
    class_name: ClassVar[str] = "OriginActor"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.OriginActor

    type: Union[str, "OriginActorTypeEnum"] = None
    actor_uuid: str = None
    role_id: Optional[str] = None
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, OriginActorTypeEnum):
            self.type = OriginActorTypeEnum(self.type)

        if self._is_empty(self.actor_uuid):
            self.MissingRequiredField("actor_uuid")
        if not isinstance(self.actor_uuid, str):
            self.actor_uuid = str(self.actor_uuid)

        if self.role_id is not None and not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedTask(YAMLRoot):
    """
    Identifies an individual task for which the containing object is a consequence of.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RelatedTask"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RelatedTask"
    class_name: ClassVar[str] = "RelatedTask"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.RelatedTask

    task_uuid: str = None
    subjects: Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]] = empty_list()
    identified_subject: Optional[Union[dict, "IdentifiedSubject"]] = None
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, "ResponsibleParty"], list[Union[dict, "ResponsibleParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.task_uuid):
            self.MissingRequiredField("task_uuid")
        if not isinstance(self.task_uuid, str):
            self.task_uuid = str(self.task_uuid)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        if self.identified_subject is not None and not isinstance(self.identified_subject, IdentifiedSubject):
            self.identified_subject = IdentifiedSubject(**as_dict(self.identified_subject))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentifiedSubject(YAMLRoot):
    """
    Used to detail assessment subjects that were identified by this task.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["IdentifiedSubject"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:IdentifiedSubject"
    class_name: ClassVar[str] = "IdentifiedSubject"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.IdentifiedSubject

    subject_placeholder_uuid: str = None
    subjects: Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_placeholder_uuid):
            self.MissingRequiredField("subject_placeholder_uuid")
        if not isinstance(self.subject_placeholder_uuid, str):
            self.subject_placeholder_uuid = str(self.subject_placeholder_uuid)

        if self._is_empty(self.subjects):
            self.MissingRequiredField("subjects")
        self._normalize_inlined_as_list(slot_name="subjects", slot_type=AssessmentSubject, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Observation(YAMLRoot):
    """
    Describes an individual observation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Observation"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Observation

    uuid: str = None
    description: str = None
    methods: Union[Union[str, "ObservationMethodEnum"], list[Union[str, "ObservationMethodEnum"]]] = None
    collected: str = None
    title: Optional[str] = None
    types: Optional[Union[Union[str, "ObservationTypeEnum"], list[Union[str, "ObservationTypeEnum"]]]] = empty_list()
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    subjects: Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]] = empty_list()
    relevant_evidence: Optional[Union[Union[dict, "RelevantEvidence"], list[Union[dict, "RelevantEvidence"]]]] = empty_list()
    expires: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.methods):
            self.MissingRequiredField("methods")
        if not isinstance(self.methods, list):
            self.methods = [self.methods] if self.methods is not None else []
        self.methods = [v if isinstance(v, ObservationMethodEnum) else ObservationMethodEnum(v) for v in self.methods]

        if self._is_empty(self.collected):
            self.MissingRequiredField("collected")
        if not isinstance(self.collected, str):
            self.collected = str(self.collected)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.types, list):
            self.types = [self.types] if self.types is not None else []
        self.types = [v if isinstance(v, ObservationTypeEnum) else ObservationTypeEnum(v) for v in self.types]

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=SubjectReference, key_name="subject_uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="relevant_evidence", slot_type=RelevantEvidence, key_name="description", keyed=False)

        if self.expires is not None and not isinstance(self.expires, str):
            self.expires = str(self.expires)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelevantEvidence(YAMLRoot):
    """
    Links this observation to relevant evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RelevantEvidence"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RelevantEvidence"
    class_name: ClassVar[str] = "RelevantEvidence"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.RelevantEvidence

    description: str = None
    href: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Finding(YAMLRoot):
    """
    Describes an individual finding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Finding"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Finding"
    class_name: ClassVar[str] = "Finding"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Finding

    uuid: str = None
    title: str = None
    description: str = None
    target: Union[dict, "FindingTarget"] = None
    implementation_statement_uuid: Optional[str] = None
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    related_observations: Optional[Union[Union[dict, "RelatedObservation"], list[Union[dict, "RelatedObservation"]]]] = empty_list()
    related_risks: Optional[Union[Union[dict, "AssociatedRisk"], list[Union[dict, "AssociatedRisk"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, FindingTarget):
            self.target = FindingTarget(**as_dict(self.target))

        if self.implementation_statement_uuid is not None and not isinstance(self.implementation_statement_uuid, str):
            self.implementation_statement_uuid = str(self.implementation_statement_uuid)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        if self.related_observations is not None:
            self.related_observations = [r if isinstance(r, RelatedObservation) else RelatedObservation(**as_dict(r)) if isinstance(r, (dict, JsonObj)) else RelatedObservation(observation_uuid=str(r)) for r in (self.related_observations if isinstance(self.related_observations, list) else [self.related_observations])]

        self._normalize_inlined_as_list(slot_name="related_risks", slot_type=AssociatedRisk, key_name="risk_uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FindingTarget(YAMLRoot):
    """
    Captures an assessor's conclusions regarding the degree to which an objective is satisfied.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["FindingTarget"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:FindingTarget"
    class_name: ClassVar[str] = "FindingTarget"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.FindingTarget

    type: Union[str, "FindingTargetTypeEnum"] = None
    target_id: str = None
    status: Union[dict, "ObjectiveStatus"] = None
    title: Optional[str] = None
    description: Optional[str] = None
    implementation_status: Optional[Union[dict, ImplementationStatus]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, FindingTargetTypeEnum):
            self.type = FindingTargetTypeEnum(self.type)

        if self._is_empty(self.target_id):
            self.MissingRequiredField("target_id")
        if not isinstance(self.target_id, str):
            self.target_id = str(self.target_id)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, ObjectiveStatus):
            self.status = ObjectiveStatus(**as_dict(self.status))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.implementation_status is not None and not isinstance(self.implementation_status, ImplementationStatus):
            self.implementation_status = ImplementationStatus(**as_dict(self.implementation_status))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObjectiveStatus(YAMLRoot):
    """
    A determination of if the objective is satisfied or not within a given system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ObjectiveStatus"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ObjectiveStatus"
    class_name: ClassVar[str] = "ObjectiveStatus"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ObjectiveStatus

    state: Union[str, "ObjectiveStatusStateEnum"] = None
    reason: Optional[Union[str, "ObjectiveStatusReasonEnum"]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, ObjectiveStatusStateEnum):
            self.state = ObjectiveStatusStateEnum(self.state)

        if self.reason is not None and not isinstance(self.reason, ObjectiveStatusReasonEnum):
            self.reason = ObjectiveStatusReasonEnum(self.reason)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedObservation(YAMLRoot):
    """
    Relates the identified element to a set of referenced observations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RelatedObservation"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RelatedObservation"
    class_name: ClassVar[str] = "RelatedObservation"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.RelatedObservation

    observation_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observation_uuid):
            self.MissingRequiredField("observation_uuid")
        if not isinstance(self.observation_uuid, str):
            self.observation_uuid = str(self.observation_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociatedRisk(YAMLRoot):
    """
    Relates the finding to a set of referenced risks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssociatedRisk"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssociatedRisk"
    class_name: ClassVar[str] = "AssociatedRisk"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssociatedRisk

    risk_uuid: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.risk_uuid):
            self.MissingRequiredField("risk_uuid")
        if not isinstance(self.risk_uuid, str):
            self.risk_uuid = str(self.risk_uuid)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Risk(YAMLRoot):
    """
    An identified risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Risk"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Risk"
    class_name: ClassVar[str] = "Risk"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Risk

    uuid: str = None
    title: str = None
    description: str = None
    statement: str = None
    status: Union[str, "RiskStatusEnum"] = None
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    threat_ids: Optional[Union[Union[dict, "ThreatId"], list[Union[dict, "ThreatId"]]]] = empty_list()
    characterizations: Optional[Union[Union[dict, "Characterization"], list[Union[dict, "Characterization"]]]] = empty_list()
    mitigating_factors: Optional[Union[Union[dict, "MitigatingFactor"], list[Union[dict, "MitigatingFactor"]]]] = empty_list()
    deadline: Optional[str] = None
    remediations: Optional[Union[Union[dict, "Response"], list[Union[dict, "Response"]]]] = empty_list()
    risk_log: Optional[Union[dict, "RiskLog"]] = None
    related_observations: Optional[Union[Union[dict, RelatedObservation], list[Union[dict, RelatedObservation]]]] = empty_list()
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, RiskStatusEnum):
            self.status = RiskStatusEnum(self.status)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        self._normalize_inlined_as_list(slot_name="threat_ids", slot_type=ThreatId, key_name="system", keyed=False)

        if not isinstance(self.characterizations, list):
            self.characterizations = [self.characterizations] if self.characterizations is not None else []
        self.characterizations = [v if isinstance(v, Characterization) else Characterization(**as_dict(v)) for v in self.characterizations]

        self._normalize_inlined_as_list(slot_name="mitigating_factors", slot_type=MitigatingFactor, key_name="uuid", keyed=False)

        if self.deadline is not None and not isinstance(self.deadline, str):
            self.deadline = str(self.deadline)

        self._normalize_inlined_as_list(slot_name="remediations", slot_type=Response, key_name="uuid", keyed=False)

        if self.risk_log is not None and not isinstance(self.risk_log, RiskLog):
            self.risk_log = RiskLog(**as_dict(self.risk_log))

        if self.related_observations is not None:
            self.related_observations = [r if isinstance(r, RelatedObservation) else RelatedObservation(**as_dict(r)) if isinstance(r, (dict, JsonObj)) else RelatedObservation(observation_uuid=str(r)) for r in (self.related_observations if isinstance(self.related_observations, list) else [self.related_observations])]

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThreatId(YAMLRoot):
    """
    A pointer, by ID, to an externally-defined threat.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["ThreatId"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:ThreatId"
    class_name: ClassVar[str] = "ThreatId"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ThreatId

    system: str = None
    id: str = None
    href: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Characterization(YAMLRoot):
    """
    A collection of descriptive data about the containing object from a specific origin.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Characterization"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Characterization"
    class_name: ClassVar[str] = "Characterization"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Characterization

    origin: Union[dict, Origin] = None
    facets: Union[Union[dict, "Facet"], list[Union[dict, "Facet"]]] = None
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.origin):
            self.MissingRequiredField("origin")
        if not isinstance(self.origin, Origin):
            self.origin = Origin(**as_dict(self.origin))

        if self._is_empty(self.facets):
            self.MissingRequiredField("facets")
        self._normalize_inlined_as_list(slot_name="facets", slot_type=Facet, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Facet(YAMLRoot):
    """
    An individual characteristic that is part of a larger set produced by the same actor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Facet"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Facet"
    class_name: ClassVar[str] = "Facet"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Facet

    name: str = None
    value: str = None
    system: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MitigatingFactor(YAMLRoot):
    """
    Describes an existing mitigating factor that may affect the overall determination of the risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["MitigatingFactor"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:MitigatingFactor"
    class_name: ClassVar[str] = "MitigatingFactor"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.MitigatingFactor

    uuid: str = None
    description: str = None
    implementation_uuid: Optional[str] = None
    subjects: Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]] = empty_list()
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.implementation_uuid is not None and not isinstance(self.implementation_uuid, str):
            self.implementation_uuid = str(self.implementation_uuid)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=SubjectReference, key_name="subject_uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Response(YAMLRoot):
    """
    Describes either recommended or an actual plan for addressing the risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["Response"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:Response"
    class_name: ClassVar[str] = "Response"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Response

    uuid: str = None
    title: str = None
    description: str = None
    lifecycle: Union[str, "ResponseLifecycleEnum"] = None
    origins: Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]] = empty_list()
    required_assets: Optional[Union[Union[dict, "RequiredAsset"], list[Union[dict, "RequiredAsset"]]]] = empty_list()
    tasks: Optional[Union[Union[dict, Task], list[Union[dict, Task]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.lifecycle):
            self.MissingRequiredField("lifecycle")
        if not isinstance(self.lifecycle, ResponseLifecycleEnum):
            self.lifecycle = ResponseLifecycleEnum(self.lifecycle)

        if not isinstance(self.origins, list):
            self.origins = [self.origins] if self.origins is not None else []
        self.origins = [v if isinstance(v, Origin) else Origin(**as_dict(v)) for v in self.origins]

        self._normalize_inlined_as_list(slot_name="required_assets", slot_type=RequiredAsset, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="tasks", slot_type=Task, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredAsset(YAMLRoot):
    """
    Identifies an asset required to achieve remediation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RequiredAsset"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RequiredAsset"
    class_name: ClassVar[str] = "RequiredAsset"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.RequiredAsset

    uuid: str = None
    description: str = None
    title: Optional[str] = None
    subjects: Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=SubjectReference, key_name="subject_uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskLog(YAMLRoot):
    """
    A log of all risk-related tasks taken.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RiskLog"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RiskLog"
    class_name: ClassVar[str] = "RiskLog"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.RiskLog

    entries: Union[Union[dict, "RiskLogEntry"], list[Union[dict, "RiskLogEntry"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.entries):
            self.MissingRequiredField("entries")
        self._normalize_inlined_as_list(slot_name="entries", slot_type=RiskLogEntry, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskLogEntry(YAMLRoot):
    """
    Identifies an individual risk response that occurred as part of managing an identified risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RiskLogEntry"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RiskLogEntry"
    class_name: ClassVar[str] = "RiskLogEntry"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.RiskLogEntry

    uuid: str = None
    start: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    end: Optional[str] = None
    logged_by: Optional[Union[Union[dict, "LoggedBy"], list[Union[dict, "LoggedBy"]]]] = empty_list()
    status_change: Optional[Union[str, "RiskStatusEnum"]] = None
    related_responses: Optional[Union[Union[dict, "RiskResponseReference"], list[Union[dict, "RiskResponseReference"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, str):
            self.start = str(self.start)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.end is not None and not isinstance(self.end, str):
            self.end = str(self.end)

        self._normalize_inlined_as_list(slot_name="logged_by", slot_type=LoggedBy, key_name="party_uuid", keyed=False)

        if self.status_change is not None and not isinstance(self.status_change, RiskStatusEnum):
            self.status_change = RiskStatusEnum(self.status_change)

        self._normalize_inlined_as_list(slot_name="related_responses", slot_type=RiskResponseReference, key_name="response_uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LoggedBy(YAMLRoot):
    """
    Used to indicate who created a log entry in what role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["LoggedBy"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:LoggedBy"
    class_name: ClassVar[str] = "LoggedBy"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.LoggedBy

    party_uuid: str = None
    role_id: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.party_uuid):
            self.MissingRequiredField("party_uuid")
        if not isinstance(self.party_uuid, str):
            self.party_uuid = str(self.party_uuid)

        if self.role_id is not None and not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskResponseReference(YAMLRoot):
    """
    Identifies an individual risk response that this log entry is for.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["RiskResponseReference"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:RiskResponseReference"
    class_name: ClassVar[str] = "RiskResponseReference"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.RiskResponseReference

    response_uuid: str = None
    related_tasks: Optional[Union[Union[dict, RelatedTask], list[Union[dict, RelatedTask]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.response_uuid):
            self.MissingRequiredField("response_uuid")
        if not isinstance(self.response_uuid, str):
            self.response_uuid = str(self.response_uuid)

        self._normalize_inlined_as_list(slot_name="related_tasks", slot_type=RelatedTask, key_name="task_uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasPropsAndLinks(YAMLRoot):
    """
    Mixin providing the props and links slots that are common to many OSCAL objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["HasPropsAndLinks"]
    class_class_curie: ClassVar[str] = "oscal_catalog:HasPropsAndLinks"
    class_name: ClassVar[str] = "HasPropsAndLinks"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.HasPropsAndLinks

    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OscalCommon(YAMLRoot):
    """
    Mixin providing props, links, and remarks slots common to most OSCAL objects. Extends HasPropsAndLinks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["OscalCommon"]
    class_class_curie: ClassVar[str] = "oscal_catalog:OscalCommon"
    class_name: ClassVar[str] = "OscalCommon"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.OscalCommon

    remarks: Optional[str] = None
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasResponsibleRoles(YAMLRoot):
    """
    Mixin providing the responsible-roles slot for objects that carry role assignments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["HasResponsibleRoles"]
    class_class_curie: ClassVar[str] = "oscal_catalog:HasResponsibleRoles"
    class_name: ClassVar[str] = "HasResponsibleRoles"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.HasResponsibleRoles

    responsible_roles: Optional[Union[Union[dict, "ResponsibleRole"], list[Union[dict, "ResponsibleRole"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="responsible_roles", slot_type=ResponsibleRole, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HasResponsibleParties(YAMLRoot):
    """
    Mixin providing the responsible-parties slot for objects that carry party assignments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["HasResponsibleParties"]
    class_class_curie: ClassVar[str] = "oscal_catalog:HasResponsibleParties"
    class_name: ClassVar[str] = "HasResponsibleParties"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.HasResponsibleParties

    responsible_parties: Optional[Union[Union[dict, "ResponsibleParty"], list[Union[dict, "ResponsibleParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


class OscalDocument(YAMLRoot):
    """
    A root wrapper for an OSCAL document, which may be of any OSCAL document type (e.g. Catalog, Profile, Assessment
    Plan, SSP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["OscalDocument"]
    class_class_curie: ClassVar[str] = "oscal_catalog:OscalDocument"
    class_name: ClassVar[str] = "OscalDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.OscalDocument


@dataclass(repr=False)
class AssessmentPlanDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Assessment Plan document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN["AssessmentPlanDocument"]
    class_class_curie: ClassVar[str] = "oscal_assessment_plan:AssessmentPlanDocument"
    class_name: ClassVar[str] = "AssessmentPlanDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.AssessmentPlanDocument

    assessment_plan: Union[dict, AssessmentPlan] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment_plan):
            self.MissingRequiredField("assessment_plan")
        if not isinstance(self.assessment_plan, AssessmentPlan):
            self.assessment_plan = AssessmentPlan(**as_dict(self.assessment_plan))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalogDocument(OscalDocument):
    """
    Root wrapper for an OSCAL Catalog document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["CatalogDocument"]
    class_class_curie: ClassVar[str] = "oscal_catalog:CatalogDocument"
    class_name: ClassVar[str] = "CatalogDocument"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.CatalogDocument

    catalog: Union[dict, "Catalog"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.catalog):
            self.MissingRequiredField("catalog")
        if not isinstance(self.catalog, Catalog):
            self.catalog = Catalog(**as_dict(self.catalog))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalog(YAMLRoot):
    """
    A structured, organized collection of control information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Catalog"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Catalog"
    class_name: ClassVar[str] = "Catalog"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Catalog

    uuid: str = None
    metadata: Union[dict, "Metadata"] = None
    back_matter: Optional[Union[dict, "BackMatter"]] = None
    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()
    groups: Optional[Union[Union[dict, "Group"], list[Union[dict, "Group"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, Metadata):
            self.metadata = Metadata(**as_dict(self.metadata))

        if self.back_matter is not None and not isinstance(self.back_matter, BackMatter):
            self.back_matter = BackMatter(**as_dict(self.back_matter))

        self._normalize_inlined_as_list(slot_name="params", slot_type=Parameter, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="controls", slot_type=Control, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="groups", slot_type=Group, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Group(YAMLRoot):
    """
    A group of controls, or of groups of controls.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Group"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Group"
    class_name: ClassVar[str] = "Group"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Group

    title: str = None
    id: Optional[str] = None
    _class: Optional[str] = None
    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    groups: Optional[Union[Union[dict, "Group"], list[Union[dict, "Group"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        self._normalize_inlined_as_list(slot_name="params", slot_type=Parameter, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=Part, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="groups", slot_type=Group, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="controls", slot_type=Control, key_name="id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Control(YAMLRoot):
    """
    A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk
    related to an information system and its information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Control"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Control"
    class_name: ClassVar[str] = "Control"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Control

    id: str = None
    title: str = None
    _class: Optional[str] = None
    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        self._normalize_inlined_as_list(slot_name="params", slot_type=Parameter, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=Part, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="controls", slot_type=Control, key_name="id", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Metadata(YAMLRoot):
    """
    Provides information about the containing document, and defines concepts shared across the document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Metadata"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Metadata"
    class_name: ClassVar[str] = "Metadata"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Metadata

    title: str = None
    last_modified: str = None
    version: str = None
    oscal_version: str = None
    published: Optional[str] = None
    document_ids: Optional[Union[Union[dict, "DocumentId"], list[Union[dict, "DocumentId"]]]] = empty_list()
    revisions: Optional[Union[Union[dict, "Revision"], list[Union[dict, "Revision"]]]] = empty_list()
    roles: Optional[Union[Union[dict, "Role"], list[Union[dict, "Role"]]]] = empty_list()
    locations: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    parties: Optional[Union[Union[dict, "Party"], list[Union[dict, "Party"]]]] = empty_list()
    actions: Optional[Union[Union[dict, "Action"], list[Union[dict, "Action"]]]] = empty_list()
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, "ResponsibleParty"], list[Union[dict, "ResponsibleParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.last_modified):
            self.MissingRequiredField("last_modified")
        if not isinstance(self.last_modified, str):
            self.last_modified = str(self.last_modified)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.oscal_version):
            self.MissingRequiredField("oscal_version")
        if not isinstance(self.oscal_version, str):
            self.oscal_version = str(self.oscal_version)

        if self.published is not None and not isinstance(self.published, str):
            self.published = str(self.published)

        self._normalize_inlined_as_list(slot_name="document_ids", slot_type=DocumentId, key_name="identifier", keyed=False)

        self._normalize_inlined_as_list(slot_name="revisions", slot_type=Revision, key_name="version", keyed=False)

        self._normalize_inlined_as_list(slot_name="roles", slot_type=Role, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="locations", slot_type=Location, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="parties", slot_type=Party, key_name="uuid", keyed=False)

        self._normalize_inlined_as_list(slot_name="actions", slot_type=Action, key_name="uuid", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Revision(YAMLRoot):
    """
    An entry in a sequential list of revisions to the containing document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Revision"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Revision"
    class_name: ClassVar[str] = "Revision"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Revision

    version: str = None
    title: Optional[str] = None
    published: Optional[str] = None
    last_modified: Optional[str] = None
    oscal_version: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.published is not None and not isinstance(self.published, str):
            self.published = str(self.published)

        if self.last_modified is not None and not isinstance(self.last_modified, str):
            self.last_modified = str(self.last_modified)

        if self.oscal_version is not None and not isinstance(self.oscal_version, str):
            self.oscal_version = str(self.oscal_version)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentId(YAMLRoot):
    """
    A document identifier qualified by an identifier scheme.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["DocumentId"]
    class_class_curie: ClassVar[str] = "oscal_catalog:DocumentId"
    class_name: ClassVar[str] = "DocumentId"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.DocumentId

    identifier: str = None
    scheme: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.scheme is not None and not isinstance(self.scheme, str):
            self.scheme = str(self.scheme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Role(YAMLRoot):
    """
    Defines a function, which might be assigned to a party in a specific situation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Role"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Role

    id: str = None
    title: str = None
    short_name: Optional[str] = None
    description: Optional[str] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Location(YAMLRoot):
    """
    A physical point of presence, which may be associated with people, organizations, or other concepts within the
    current or linked OSCAL document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Location"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Location

    uuid: str = None
    title: Optional[str] = None
    email_addresses: Optional[Union[str, list[str]]] = empty_list()
    telephone_numbers: Optional[Union[Union[dict, "TelephoneNumber"], list[Union[dict, "TelephoneNumber"]]]] = empty_list()
    address: Optional[Union[dict, "Address"]] = None
    urls: Optional[Union[str, list[str]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.email_addresses, list):
            self.email_addresses = [self.email_addresses] if self.email_addresses is not None else []
        self.email_addresses = [v if isinstance(v, str) else str(v) for v in self.email_addresses]

        self._normalize_inlined_as_list(slot_name="telephone_numbers", slot_type=TelephoneNumber, key_name="number", keyed=False)

        if self.address is not None and not isinstance(self.address, Address):
            self.address = Address(**as_dict(self.address))

        if not isinstance(self.urls, list):
            self.urls = [self.urls] if self.urls is not None else []
        self.urls = [v if isinstance(v, str) else str(v) for v in self.urls]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Party(YAMLRoot):
    """
    An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL
    document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Party"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Party"
    class_name: ClassVar[str] = "Party"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Party

    uuid: str = None
    type: Union[str, "PartyTypeEnum"] = None
    name: Optional[str] = None
    short_name: Optional[str] = None
    email_addresses: Optional[Union[str, list[str]]] = empty_list()
    telephone_numbers: Optional[Union[Union[dict, "TelephoneNumber"], list[Union[dict, "TelephoneNumber"]]]] = empty_list()
    external_ids: Optional[Union[Union[dict, "PartyExternalId"], list[Union[dict, "PartyExternalId"]]]] = empty_list()
    addresses: Optional[Union[Union[dict, "Address"], list[Union[dict, "Address"]]]] = empty_list()
    location_uuids: Optional[Union[str, list[str]]] = empty_list()
    member_of_organizations: Optional[Union[str, list[str]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, PartyTypeEnum):
            self.type = PartyTypeEnum(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if not isinstance(self.email_addresses, list):
            self.email_addresses = [self.email_addresses] if self.email_addresses is not None else []
        self.email_addresses = [v if isinstance(v, str) else str(v) for v in self.email_addresses]

        self._normalize_inlined_as_list(slot_name="telephone_numbers", slot_type=TelephoneNumber, key_name="number", keyed=False)

        self._normalize_inlined_as_list(slot_name="external_ids", slot_type=PartyExternalId, key_name="scheme", keyed=False)

        if not isinstance(self.addresses, list):
            self.addresses = [self.addresses] if self.addresses is not None else []
        self.addresses = [v if isinstance(v, Address) else Address(**as_dict(v)) for v in self.addresses]

        if not isinstance(self.location_uuids, list):
            self.location_uuids = [self.location_uuids] if self.location_uuids is not None else []
        self.location_uuids = [v if isinstance(v, str) else str(v) for v in self.location_uuids]

        if not isinstance(self.member_of_organizations, list):
            self.member_of_organizations = [self.member_of_organizations] if self.member_of_organizations is not None else []
        self.member_of_organizations = [v if isinstance(v, str) else str(v) for v in self.member_of_organizations]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PartyExternalId(YAMLRoot):
    """
    An identifier for a person or organization using a designated scheme, e.g. an Open Researcher and Contributor ID
    (ORCID).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["PartyExternalId"]
    class_class_curie: ClassVar[str] = "oscal_catalog:PartyExternalId"
    class_name: ClassVar[str] = "PartyExternalId"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.PartyExternalId

    scheme: str = None
    id: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scheme):
            self.MissingRequiredField("scheme")
        if not isinstance(self.scheme, str):
            self.scheme = str(self.scheme)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResponsibleParty(YAMLRoot):
    """
    A reference to a set of persons and/or organizations that have responsibility for performing the referenced role
    in the context of the containing object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ResponsibleParty"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ResponsibleParty"
    class_name: ClassVar[str] = "ResponsibleParty"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ResponsibleParty

    role_id: str = None
    party_uuids: Union[str, list[str]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        if self._is_empty(self.party_uuids):
            self.MissingRequiredField("party_uuids")
        if not isinstance(self.party_uuids, list):
            self.party_uuids = [self.party_uuids] if self.party_uuids is not None else []
        self.party_uuids = [v if isinstance(v, str) else str(v) for v in self.party_uuids]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResponsibleRole(YAMLRoot):
    """
    A reference to a role with responsibility for performing a function relative to the containing object, optionally
    associated with a set of persons and/or organizations that perform that role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ResponsibleRole"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ResponsibleRole"
    class_name: ClassVar[str] = "ResponsibleRole"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ResponsibleRole

    role_id: str = None
    party_uuids: Optional[Union[str, list[str]]] = empty_list()
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.role_id):
            self.MissingRequiredField("role_id")
        if not isinstance(self.role_id, str):
            self.role_id = str(self.role_id)

        if not isinstance(self.party_uuids, list):
            self.party_uuids = [self.party_uuids] if self.party_uuids is not None else []
        self.party_uuids = [v if isinstance(v, str) else str(v) for v in self.party_uuids]

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Action(YAMLRoot):
    """
    An action applied by a role within a given party to the content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Action"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Action

    uuid: str = None
    type: str = None
    system: str = None
    date: Optional[str] = None
    remarks: Optional[str] = None
    responsible_parties: Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        self._normalize_inlined_as_list(slot_name="responsible_parties", slot_type=ResponsibleParty, key_name="role_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TelephoneNumber(YAMLRoot):
    """
    A telephone service number as defined by ITU-T E.164.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["TelephoneNumber"]
    class_class_curie: ClassVar[str] = "oscal_catalog:TelephoneNumber"
    class_name: ClassVar[str] = "TelephoneNumber"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.TelephoneNumber

    number: str = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.number):
            self.MissingRequiredField("number")
        if not isinstance(self.number, str):
            self.number = str(self.number)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Address(YAMLRoot):
    """
    A postal address for the location.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Address"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Address

    type: Optional[str] = None
    addr_lines: Optional[Union[str, list[str]]] = empty_list()
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.addr_lines, list):
            self.addr_lines = [self.addr_lines] if self.addr_lines is not None else []
        self.addr_lines = [v if isinstance(v, str) else str(v) for v in self.addr_lines]

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        if self.postal_code is not None and not isinstance(self.postal_code, str):
            self.postal_code = str(self.postal_code)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hash(YAMLRoot):
    """
    A representation of a cryptographic digest generated over a resource using a specified hash algorithm.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Hash"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Hash"
    class_name: ClassVar[str] = "Hash"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Hash

    value: str = None
    algorithm: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, str):
            self.algorithm = str(self.algorithm)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Property(YAMLRoot):
    """
    An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value
    pair.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Property"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Property

    name: str = None
    value: str = None
    uuid: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None
    remarks: Optional[str] = None
    group: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        if self.group is not None and not isinstance(self.group, str):
            self.group = str(self.group)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Link(YAMLRoot):
    """
    A reference to a local or remote resource, that has a specific relation to the containing object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Link"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Link"
    class_name: ClassVar[str] = "Link"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Link

    href: str = None
    rel: Optional[str] = None
    resource_fragment: Optional[str] = None
    media_type: Optional[str] = None
    text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        if self.resource_fragment is not None and not isinstance(self.resource_fragment, str):
            self.resource_fragment = str(self.resource_fragment)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BackMatter(YAMLRoot):
    """
    A collection of resources that may be referenced from within the OSCAL document instance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["BackMatter"]
    class_class_curie: ClassVar[str] = "oscal_catalog:BackMatter"
    class_name: ClassVar[str] = "BackMatter"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.BackMatter

    resources: Optional[Union[Union[dict, "Resource"], list[Union[dict, "Resource"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="resources", slot_type=Resource, key_name="uuid", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(YAMLRoot):
    """
    A resource associated with content in the containing document instance. A resource may be directly included in the
    document using base64 encoding or may point to one or more equivalent internet resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Resource"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Resource

    uuid: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    document_ids: Optional[Union[Union[dict, DocumentId], list[Union[dict, DocumentId]]]] = empty_list()
    remarks: Optional[str] = None
    citation: Optional[Union[dict, "Citation"]] = None
    rlinks: Optional[Union[Union[dict, "ResourceLink"], list[Union[dict, "ResourceLink"]]]] = empty_list()
    base64: Optional[Union[dict, "Base64Resource"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uuid):
            self.MissingRequiredField("uuid")
        if not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="document_ids", slot_type=DocumentId, key_name="identifier", keyed=False)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        if self.citation is not None and not isinstance(self.citation, Citation):
            self.citation = Citation(**as_dict(self.citation))

        if self.rlinks is not None:
            self.rlinks = [r if isinstance(r, ResourceLink) else ResourceLink(**as_dict(r)) if isinstance(r, (dict, JsonObj)) else ResourceLink(href=str(r)) for r in (self.rlinks if isinstance(self.rlinks, list) else [self.rlinks])]

        if self.base64 is not None and not isinstance(self.base64, Base64Resource):
            self.base64 = Base64Resource(**as_dict(self.base64))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Citation(YAMLRoot):
    """
    An optional citation consisting of end note text using structured markup.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Citation"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Citation"
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Citation

    text: str = None
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.text):
            self.MissingRequiredField("text")
        if not isinstance(self.text, str):
            self.text = str(self.text)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResourceLink(YAMLRoot):
    """
    A URL-based pointer to an external resource with an optional hash for verification and change detection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ResourceLink"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ResourceLink"
    class_name: ClassVar[str] = "ResourceLink"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ResourceLink

    href: str = None
    media_type: Optional[str] = None
    hashes: Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.href):
            self.MissingRequiredField("href")
        if not isinstance(self.href, str):
            self.href = str(self.href)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        self._normalize_inlined_as_list(slot_name="hashes", slot_type=Hash, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Base64Resource(YAMLRoot):
    """
    A resource encoded using the Base64 alphabet defined by RFC 2045.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Base64Resource"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Base64Resource"
    class_name: ClassVar[str] = "Base64Resource"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Base64Resource

    value: str = None
    media_type: Optional[str] = None
    filename: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.media_type is not None and not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self.filename is not None and not isinstance(self.filename, str):
            self.filename = str(self.filename)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Part(YAMLRoot):
    """
    An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another
    part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Part"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Part

    name: str = None
    id: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None
    title: Optional[str] = None
    prose: Optional[str] = None
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()
    props: Optional[Union[Union[dict, Property], list[Union[dict, Property]]]] = empty_list()
    links: Optional[Union[Union[dict, Link], list[Union[dict, Link]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        self._normalize_inlined_as_list(slot_name="parts", slot_type=Part, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="props", slot_type=Property, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="links", slot_type=Link, key_name="href", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Parameter(YAMLRoot):
    """
    Parameters provide a mechanism for the dynamic assignment of value(s) in a control.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["Parameter"]
    class_class_curie: ClassVar[str] = "oscal_catalog:Parameter"
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.Parameter

    id: str = None
    _class: Optional[str] = None
    depends_on: Optional[str] = None
    label: Optional[str] = None
    usage: Optional[str] = None
    constraints: Optional[Union[Union[dict, "ParameterConstraint"], list[Union[dict, "ParameterConstraint"]]]] = empty_list()
    guidelines: Optional[Union[Union[dict, "ParameterGuideline"], list[Union[dict, "ParameterGuideline"]]]] = empty_list()
    values: Optional[Union[str, list[str]]] = empty_list()
    select: Optional[Union[dict, "ParameterSelection"]] = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        if self.depends_on is not None and not isinstance(self.depends_on, str):
            self.depends_on = str(self.depends_on)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.usage is not None and not isinstance(self.usage, str):
            self.usage = str(self.usage)

        if not isinstance(self.constraints, list):
            self.constraints = [self.constraints] if self.constraints is not None else []
        self.constraints = [v if isinstance(v, ParameterConstraint) else ParameterConstraint(**as_dict(v)) for v in self.constraints]

        if self.guidelines is not None:
            self.guidelines = [g if isinstance(g, ParameterGuideline) else ParameterGuideline(**as_dict(g)) if isinstance(g, (dict, JsonObj)) else ParameterGuideline(prose=str(g)) for g in (self.guidelines if isinstance(self.guidelines, list) else [self.guidelines])]

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.select is not None and not isinstance(self.select, ParameterSelection):
            self.select = ParameterSelection(**as_dict(self.select))

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParameterConstraint(YAMLRoot):
    """
    A formal or informal expression of a constraint or test.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ParameterConstraint"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ParameterConstraint"
    class_name: ClassVar[str] = "ParameterConstraint"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ParameterConstraint

    description: Optional[str] = None
    tests: Optional[Union[Union[dict, "ConstraintTest"], list[Union[dict, "ConstraintTest"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="tests", slot_type=ConstraintTest, key_name="expression", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConstraintTest(YAMLRoot):
    """
    A test expression which is expected to be evaluated by a tool.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ConstraintTest"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ConstraintTest"
    class_name: ClassVar[str] = "ConstraintTest"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ConstraintTest

    expression: str = None
    remarks: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.expression):
            self.MissingRequiredField("expression")
        if not isinstance(self.expression, str):
            self.expression = str(self.expression)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParameterGuideline(YAMLRoot):
    """
    A prose statement that provides a recommendation for the use of a parameter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ParameterGuideline"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ParameterGuideline"
    class_name: ClassVar[str] = "ParameterGuideline"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ParameterGuideline

    prose: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.prose):
            self.MissingRequiredField("prose")
        if not isinstance(self.prose, str):
            self.prose = str(self.prose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParameterSelection(YAMLRoot):
    """
    Presenting a choice among alternatives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ParameterSelection"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ParameterSelection"
    class_name: ClassVar[str] = "ParameterSelection"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ParameterSelection

    how_many: Optional[Union[str, "ParameterCardinalityEnum"]] = None
    choice: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.how_many is not None and not isinstance(self.how_many, ParameterCardinalityEnum):
            self.how_many = ParameterCardinalityEnum(self.how_many)

        if not isinstance(self.choice, list):
            self.choice = [self.choice] if self.choice is not None else []
        self.choice = [v if isinstance(v, str) else str(v) for v in self.choice]

        super().__post_init__(**kwargs)


class IncludeAll(YAMLRoot):
    """
    Include all controls from the imported catalog or profile resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["IncludeAll"]
    class_class_curie: ClassVar[str] = "oscal_catalog:IncludeAll"
    class_name: ClassVar[str] = "IncludeAll"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.IncludeAll


@dataclass(repr=False)
class ControlMatching(YAMLRoot):
    """
    Selecting a set of controls by matching their IDs with a wildcard pattern.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["ControlMatching"]
    class_class_curie: ClassVar[str] = "oscal_catalog:ControlMatching"
    class_name: ClassVar[str] = "ControlMatching"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.ControlMatching

    remarks: Optional[str] = None
    pattern: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        if self.pattern is not None and not isinstance(self.pattern, str):
            self.pattern = str(self.pattern)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SelectControlById(YAMLRoot):
    """
    Select a control or controls from an imported control set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OSCAL_CATALOG["SelectControlById"]
    class_class_curie: ClassVar[str] = "oscal_catalog:SelectControlById"
    class_name: ClassVar[str] = "SelectControlById"
    class_model_uri: ClassVar[URIRef] = OSCAL_ASSESSMENT_PLAN.SelectControlById

    with_child_controls: Optional[Union[str, "WithChildControlsEnum"]] = None
    with_ids: Optional[Union[str, list[str]]] = empty_list()
    matching: Optional[Union[Union[dict, ControlMatching], list[Union[dict, ControlMatching]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.with_child_controls is not None and not isinstance(self.with_child_controls, WithChildControlsEnum):
            self.with_child_controls = WithChildControlsEnum(self.with_child_controls)

        if not isinstance(self.with_ids, list):
            self.with_ids = [self.with_ids] if self.with_ids is not None else []
        self.with_ids = [v if isinstance(v, str) else str(v) for v in self.with_ids]

        if not isinstance(self.matching, list):
            self.matching = [self.matching] if self.matching is not None else []
        self.matching = [v if isinstance(v, ControlMatching) else ControlMatching(**as_dict(v)) for v in self.matching]

        super().__post_init__(**kwargs)


# Enumerations
class TaskTypeEnum(EnumDefinitionImpl):

    milestone = PermissibleValue(text="milestone")
    action = PermissibleValue(text="action")

    _defn = EnumDefinition(
        name="TaskTypeEnum",
    )

class TimingUnitEnum(EnumDefinitionImpl):

    seconds = PermissibleValue(text="seconds")
    minutes = PermissibleValue(text="minutes")
    hours = PermissibleValue(text="hours")
    days = PermissibleValue(text="days")
    months = PermissibleValue(text="months")
    years = PermissibleValue(text="years")

    _defn = EnumDefinition(
        name="TimingUnitEnum",
    )

class AssessmentSubjectTypeEnum(EnumDefinitionImpl):

    component = PermissibleValue(text="component")
    location = PermissibleValue(text="location")
    party = PermissibleValue(text="party")
    user = PermissibleValue(text="user")

    _defn = EnumDefinition(
        name="AssessmentSubjectTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "inventory-item",
            PermissibleValue(text="inventory-item"))

class SelectSubjectTypeEnum(EnumDefinitionImpl):

    component = PermissibleValue(text="component")
    location = PermissibleValue(text="location")
    party = PermissibleValue(text="party")
    user = PermissibleValue(text="user")
    resource = PermissibleValue(text="resource")

    _defn = EnumDefinition(
        name="SelectSubjectTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "inventory-item",
            PermissibleValue(text="inventory-item"))

class OriginActorTypeEnum(EnumDefinitionImpl):

    tool = PermissibleValue(text="tool")
    party = PermissibleValue(text="party")

    _defn = EnumDefinition(
        name="OriginActorTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "assessment-platform",
            PermissibleValue(text="assessment-platform"))

class ObservationMethodEnum(EnumDefinitionImpl):

    EXAMINE = PermissibleValue(text="EXAMINE")
    INTERVIEW = PermissibleValue(text="INTERVIEW")
    TEST = PermissibleValue(text="TEST")
    UNKNOWN = PermissibleValue(text="UNKNOWN")

    _defn = EnumDefinition(
        name="ObservationMethodEnum",
    )

class ObservationTypeEnum(EnumDefinitionImpl):

    mitigation = PermissibleValue(text="mitigation")
    finding = PermissibleValue(text="finding")
    discovery = PermissibleValue(text="discovery")
    historic = PermissibleValue(text="historic")

    _defn = EnumDefinition(
        name="ObservationTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ssp-statement-issue",
            PermissibleValue(text="ssp-statement-issue"))
        setattr(cls, "control-objective",
            PermissibleValue(text="control-objective"))

class RiskStatusEnum(EnumDefinitionImpl):

    open = PermissibleValue(text="open")
    investigating = PermissibleValue(text="investigating")
    remediating = PermissibleValue(text="remediating")
    closed = PermissibleValue(text="closed")

    _defn = EnumDefinition(
        name="RiskStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "deviation-requested",
            PermissibleValue(text="deviation-requested"))
        setattr(cls, "deviation-approved",
            PermissibleValue(text="deviation-approved"))

class FindingTargetTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="FindingTargetTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "statement-id",
            PermissibleValue(text="statement-id"))
        setattr(cls, "objective-id",
            PermissibleValue(text="objective-id"))

class ObjectiveStatusStateEnum(EnumDefinitionImpl):

    satisfied = PermissibleValue(text="satisfied")

    _defn = EnumDefinition(
        name="ObjectiveStatusStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-satisfied",
            PermissibleValue(text="not-satisfied"))

class ObjectiveStatusReasonEnum(EnumDefinitionImpl):

    fail = PermissibleValue(text="fail")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ObjectiveStatusReasonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "pass",
            PermissibleValue(text="pass"))

class ImplementationStatusStateEnum(EnumDefinitionImpl):

    implemented = PermissibleValue(text="implemented")
    partial = PermissibleValue(text="partial")
    planned = PermissibleValue(text="planned")
    alternative = PermissibleValue(text="alternative")

    _defn = EnumDefinition(
        name="ImplementationStatusStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not-applicable",
            PermissibleValue(text="not-applicable"))

class ComponentTypeEnum(EnumDefinitionImpl):

    system = PermissibleValue(text="system")
    interconnection = PermissibleValue(text="interconnection")
    software = PermissibleValue(text="software")
    hardware = PermissibleValue(text="hardware")
    service = PermissibleValue(text="service")
    policy = PermissibleValue(text="policy")
    physical = PermissibleValue(text="physical")
    plan = PermissibleValue(text="plan")
    guidance = PermissibleValue(text="guidance")
    standard = PermissibleValue(text="standard")
    validation = PermissibleValue(text="validation")
    network = PermissibleValue(text="network")

    _defn = EnumDefinition(
        name="ComponentTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "this-system",
            PermissibleValue(text="this-system"))
        setattr(cls, "process-procedure",
            PermissibleValue(text="process-procedure"))

class ComponentStateEnum(EnumDefinitionImpl):

    operational = PermissibleValue(text="operational")
    disposition = PermissibleValue(text="disposition")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="ComponentStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "under-development",
            PermissibleValue(text="under-development"))

class TransportEnum(EnumDefinitionImpl):

    TCP = PermissibleValue(text="TCP")
    UDP = PermissibleValue(text="UDP")

    _defn = EnumDefinition(
        name="TransportEnum",
    )

class AssessmentPartNameEnum(EnumDefinitionImpl):

    asset = PermissibleValue(text="asset")
    method = PermissibleValue(text="method")
    objective = PermissibleValue(text="objective")

    _defn = EnumDefinition(
        name="AssessmentPartNameEnum",
    )

class ResponseLifecycleEnum(EnumDefinitionImpl):

    recommendation = PermissibleValue(text="recommendation")
    planned = PermissibleValue(text="planned")
    completed = PermissibleValue(text="completed")

    _defn = EnumDefinition(
        name="ResponseLifecycleEnum",
    )

class PartyTypeEnum(EnumDefinitionImpl):

    person = PermissibleValue(text="person")
    organization = PermissibleValue(text="organization")

    _defn = EnumDefinition(
        name="PartyTypeEnum",
    )

class HashAlgorithmEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="HashAlgorithmEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SHA-224",
            PermissibleValue(text="SHA-224"))
        setattr(cls, "SHA-256",
            PermissibleValue(text="SHA-256"))
        setattr(cls, "SHA-384",
            PermissibleValue(text="SHA-384"))
        setattr(cls, "SHA-512",
            PermissibleValue(text="SHA-512"))
        setattr(cls, "SHA3-224",
            PermissibleValue(text="SHA3-224"))
        setattr(cls, "SHA3-256",
            PermissibleValue(text="SHA3-256"))
        setattr(cls, "SHA3-384",
            PermissibleValue(text="SHA3-384"))
        setattr(cls, "SHA3-512",
            PermissibleValue(text="SHA3-512"))

class PhoneTypeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    office = PermissibleValue(text="office")
    mobile = PermissibleValue(text="mobile")

    _defn = EnumDefinition(
        name="PhoneTypeEnum",
    )

class AddressTypeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")

    _defn = EnumDefinition(
        name="AddressTypeEnum",
    )

class ParameterCardinalityEnum(EnumDefinitionImpl):

    one = PermissibleValue(text="one")

    _defn = EnumDefinition(
        name="ParameterCardinalityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "one-or-more",
            PermissibleValue(text="one-or-more"))

class WithChildControlsEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="WithChildControlsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "True",
            PermissibleValue(text="True"))
        setattr(cls, "False",
            PermissibleValue(text="False"))

# Slots
class slots:
    pass

slots.subject_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_uuid, name="subject-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.subject_uuid, domain=None, range=Optional[str])

slots.task_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.task_uuid, name="task-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('task_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.task_uuid, domain=None, range=Optional[str])

slots.activity_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.activity_uuid, name="activity-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('activity_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.activity_uuid, domain=None, range=Optional[str])

slots.component_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.component_uuid, name="component-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('component_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.component_uuid, domain=None, range=Optional[str])

slots.control_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_id, name="control-id", curie=OSCAL_ASSESSMENT_PLAN.curie('control_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.control_id, domain=None, range=Optional[str])

slots.include_all = Slot(uri=OSCAL_ASSESSMENT_PLAN.include_all, name="include-all", curie=OSCAL_ASSESSMENT_PLAN.curie('include_all'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.include_all, domain=None, range=Optional[Union[dict, IncludeAll]])

slots.subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.subjects, domain=None, range=Optional[Union[str, list[str]]])

slots.origins = Slot(uri=OSCAL_ASSESSMENT_PLAN.origins, name="origins", curie=OSCAL_ASSESSMENT_PLAN.curie('origins'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.origins, domain=None, range=Optional[Union[Union[dict, Origin], list[Union[dict, Origin]]]])

slots.reviewed_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.reviewed_controls, name="reviewed-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('reviewed_controls'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.reviewed_controls, domain=None, range=Optional[Union[dict, ReviewedControls]])

slots.tasks = Slot(uri=OSCAL_ASSESSMENT_PLAN.tasks, name="tasks", curie=OSCAL_ASSESSMENT_PLAN.curie('tasks'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.tasks, domain=None, range=Optional[Union[Union[dict, Task], list[Union[dict, Task]]]])

slots.components = Slot(uri=OSCAL_ASSESSMENT_PLAN.components, name="components", curie=OSCAL_ASSESSMENT_PLAN.curie('components'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.components, domain=None, range=Optional[Union[Union[dict, SystemComponent], list[Union[dict, SystemComponent]]]])

slots.status = Slot(uri=OSCAL_ASSESSMENT_PLAN.status, name="status", curie=OSCAL_ASSESSMENT_PLAN.curie('status'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.status, domain=None, range=Optional[str])

slots.related_observations = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_observations, name="related-observations", curie=OSCAL_ASSESSMENT_PLAN.curie('related_observations'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.related_observations, domain=None, range=Optional[Union[Union[dict, RelatedObservation], list[Union[dict, RelatedObservation]]]])

slots.related_tasks = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_tasks, name="related-tasks", curie=OSCAL_ASSESSMENT_PLAN.curie('related_tasks'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.related_tasks, domain=None, range=Optional[Union[Union[dict, RelatedTask], list[Union[dict, RelatedTask]]]])

slots.start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.start, domain=None, range=Optional[str])

slots.end = Slot(uri=OSCAL_ASSESSMENT_PLAN.end, name="end", curie=OSCAL_ASSESSMENT_PLAN.curie('end'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.end, domain=None, range=Optional[str])

slots.assessment_plan = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_plan, name="assessment-plan", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_plan'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.assessment_plan, domain=None, range=Optional[Union[dict, AssessmentPlan]])

slots.import_ssp = Slot(uri=OSCAL_ASSESSMENT_PLAN.import_ssp, name="import-ssp", curie=OSCAL_ASSESSMENT_PLAN.curie('import_ssp'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.import_ssp, domain=None, range=Optional[Union[dict, ImportSSP]])

slots.local_definitions = Slot(uri=OSCAL_ASSESSMENT_PLAN.local_definitions, name="local-definitions", curie=OSCAL_ASSESSMENT_PLAN.curie('local_definitions'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.local_definitions, domain=None, range=Optional[Union[dict, LocalDefinitions]])

slots.terms_and_conditions = Slot(uri=OSCAL_ASSESSMENT_PLAN.terms_and_conditions, name="terms-and-conditions", curie=OSCAL_ASSESSMENT_PLAN.curie('terms_and_conditions'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.terms_and_conditions, domain=None, range=Optional[Union[dict, TermsAndConditions]])

slots.assessment_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_subjects, name="assessment-subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.assessment_subjects, domain=None, range=Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]])

slots.assessment_assets = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_assets, name="assessment-assets", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_assets'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.assessment_assets, domain=None, range=Optional[Union[dict, AssessmentAssets]])

slots.inventory_items = Slot(uri=OSCAL_ASSESSMENT_PLAN.inventory_items, name="inventory-items", curie=OSCAL_ASSESSMENT_PLAN.curie('inventory_items'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.inventory_items, domain=None, range=Optional[Union[Union[dict, InventoryItem], list[Union[dict, InventoryItem]]]])

slots.users = Slot(uri=OSCAL_ASSESSMENT_PLAN.users, name="users", curie=OSCAL_ASSESSMENT_PLAN.curie('users'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.users, domain=None, range=Optional[Union[Union[dict, SystemUser], list[Union[dict, SystemUser]]]])

slots.objectives_and_methods = Slot(uri=OSCAL_ASSESSMENT_PLAN.objectives_and_methods, name="objectives-and-methods", curie=OSCAL_ASSESSMENT_PLAN.curie('objectives_and_methods'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.objectives_and_methods, domain=None, range=Optional[Union[Union[dict, LocalObjective], list[Union[dict, LocalObjective]]]])

slots.activities = Slot(uri=OSCAL_ASSESSMENT_PLAN.activities, name="activities", curie=OSCAL_ASSESSMENT_PLAN.curie('activities'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.activities, domain=None, range=Optional[Union[Union[dict, Activity], list[Union[dict, Activity]]]])

slots.control_selections = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_selections, name="control-selections", curie=OSCAL_ASSESSMENT_PLAN.curie('control_selections'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.control_selections, domain=None, range=Optional[Union[Union[dict, ControlSelection], list[Union[dict, ControlSelection]]]])

slots.control_objective_selections = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_objective_selections, name="control-objective-selections", curie=OSCAL_ASSESSMENT_PLAN.curie('control_objective_selections'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.control_objective_selections, domain=None, range=Optional[Union[Union[dict, ControlObjectiveSelection], list[Union[dict, ControlObjectiveSelection]]]])

slots.include_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.include_controls, name="include-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('include_controls'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.include_controls, domain=None, range=Optional[Union[Union[dict, AssessmentSelectControlById], list[Union[dict, AssessmentSelectControlById]]]])

slots.exclude_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.exclude_controls, name="exclude-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('exclude_controls'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.exclude_controls, domain=None, range=Optional[Union[Union[dict, AssessmentSelectControlById], list[Union[dict, AssessmentSelectControlById]]]])

slots.include_objectives = Slot(uri=OSCAL_ASSESSMENT_PLAN.include_objectives, name="include-objectives", curie=OSCAL_ASSESSMENT_PLAN.curie('include_objectives'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.include_objectives, domain=None, range=Optional[Union[Union[dict, SelectObjectiveById], list[Union[dict, SelectObjectiveById]]]])

slots.exclude_objectives = Slot(uri=OSCAL_ASSESSMENT_PLAN.exclude_objectives, name="exclude-objectives", curie=OSCAL_ASSESSMENT_PLAN.curie('exclude_objectives'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.exclude_objectives, domain=None, range=Optional[Union[Union[dict, SelectObjectiveById], list[Union[dict, SelectObjectiveById]]]])

slots.statement_ids = Slot(uri=OSCAL_ASSESSMENT_PLAN.statement_ids, name="statement-ids", curie=OSCAL_ASSESSMENT_PLAN.curie('statement_ids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.statement_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.objective_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.objective_id, name="objective-id", curie=OSCAL_ASSESSMENT_PLAN.curie('objective_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.objective_id, domain=None, range=Optional[str])

slots.include_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.include_subjects, name="include-subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('include_subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.include_subjects, domain=None, range=Optional[Union[Union[dict, SelectSubjectById], list[Union[dict, SelectSubjectById]]]])

slots.exclude_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.exclude_subjects, name="exclude-subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('exclude_subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.exclude_subjects, domain=None, range=Optional[Union[Union[dict, SelectSubjectById], list[Union[dict, SelectSubjectById]]]])

slots.sources = Slot(uri=OSCAL_ASSESSMENT_PLAN.sources, name="sources", curie=OSCAL_ASSESSMENT_PLAN.curie('sources'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.sources, domain=None, range=Optional[Union[Union[dict, AssessmentSubjectSource], list[Union[dict, AssessmentSubjectSource]]]])

slots.assessment_platforms = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_platforms, name="assessment-platforms", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_platforms'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.assessment_platforms, domain=None, range=Optional[Union[Union[dict, AssessmentPlatform], list[Union[dict, AssessmentPlatform]]]])

slots.uses_components = Slot(uri=OSCAL_ASSESSMENT_PLAN.uses_components, name="uses-components", curie=OSCAL_ASSESSMENT_PLAN.curie('uses_components'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.uses_components, domain=None, range=Optional[Union[Union[dict, UsesComponent], list[Union[dict, UsesComponent]]]])

slots.part = Slot(uri=OSCAL_ASSESSMENT_PLAN.part, name="part", curie=OSCAL_ASSESSMENT_PLAN.curie('part'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.part, domain=None, range=Optional[Union[dict, AssessmentPart]])

slots.steps = Slot(uri=OSCAL_ASSESSMENT_PLAN.steps, name="steps", curie=OSCAL_ASSESSMENT_PLAN.curie('steps'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.steps, domain=None, range=Optional[Union[Union[dict, Step], list[Union[dict, Step]]]])

slots.related_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_controls, name="related-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('related_controls'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.related_controls, domain=None, range=Optional[Union[dict, ReviewedControls]])

slots.timing = Slot(uri=OSCAL_ASSESSMENT_PLAN.timing, name="timing", curie=OSCAL_ASSESSMENT_PLAN.curie('timing'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.timing, domain=None, range=Optional[Union[dict, EventTiming]])

slots.dependencies = Slot(uri=OSCAL_ASSESSMENT_PLAN.dependencies, name="dependencies", curie=OSCAL_ASSESSMENT_PLAN.curie('dependencies'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.dependencies, domain=None, range=Optional[Union[Union[dict, TaskDependency], list[Union[dict, TaskDependency]]]])

slots.associated_activities = Slot(uri=OSCAL_ASSESSMENT_PLAN.associated_activities, name="associated-activities", curie=OSCAL_ASSESSMENT_PLAN.curie('associated_activities'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.associated_activities, domain=None, range=Optional[Union[Union[dict, AssociatedActivity], list[Union[dict, AssociatedActivity]]]])

slots.on_date = Slot(uri=OSCAL_ASSESSMENT_PLAN.on_date, name="on-date", curie=OSCAL_ASSESSMENT_PLAN.curie('on_date'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.on_date, domain=None, range=Optional[Union[dict, OnDateCondition]])

slots.within_date_range = Slot(uri=OSCAL_ASSESSMENT_PLAN.within_date_range, name="within-date-range", curie=OSCAL_ASSESSMENT_PLAN.curie('within_date_range'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.within_date_range, domain=None, range=Optional[Union[dict, WithinDateRange]])

slots.at_frequency = Slot(uri=OSCAL_ASSESSMENT_PLAN.at_frequency, name="at-frequency", curie=OSCAL_ASSESSMENT_PLAN.curie('at_frequency'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.at_frequency, domain=None, range=Optional[Union[dict, AtFrequency]])

slots.period = Slot(uri=OSCAL_ASSESSMENT_PLAN.period, name="period", curie=OSCAL_ASSESSMENT_PLAN.curie('period'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.period, domain=None, range=Optional[int])

slots.unit = Slot(uri=OSCAL_ASSESSMENT_PLAN.unit, name="unit", curie=OSCAL_ASSESSMENT_PLAN.curie('unit'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.unit, domain=None, range=Optional[Union[str, "TimingUnitEnum"]])

slots.param_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.param_id, name="param-id", curie=OSCAL_ASSESSMENT_PLAN.curie('param_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.param_id, domain=None, range=Optional[str])

slots.purpose = Slot(uri=OSCAL_ASSESSMENT_PLAN.purpose, name="purpose", curie=OSCAL_ASSESSMENT_PLAN.curie('purpose'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.purpose, domain=None, range=Optional[str])

slots.protocols = Slot(uri=OSCAL_ASSESSMENT_PLAN.protocols, name="protocols", curie=OSCAL_ASSESSMENT_PLAN.curie('protocols'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.protocols, domain=None, range=Optional[Union[Union[dict, Protocol], list[Union[dict, Protocol]]]])

slots.port_ranges = Slot(uri=OSCAL_ASSESSMENT_PLAN.port_ranges, name="port-ranges", curie=OSCAL_ASSESSMENT_PLAN.curie('port_ranges'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.port_ranges, domain=None, range=Optional[Union[Union[dict, PortRange], list[Union[dict, PortRange]]]])

slots.transport = Slot(uri=OSCAL_ASSESSMENT_PLAN.transport, name="transport", curie=OSCAL_ASSESSMENT_PLAN.curie('transport'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.transport, domain=None, range=Optional[Union[str, "TransportEnum"]])

slots.role_ids = Slot(uri=OSCAL_ASSESSMENT_PLAN.role_ids, name="role-ids", curie=OSCAL_ASSESSMENT_PLAN.curie('role_ids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.role_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.authorized_privileges = Slot(uri=OSCAL_ASSESSMENT_PLAN.authorized_privileges, name="authorized-privileges", curie=OSCAL_ASSESSMENT_PLAN.curie('authorized_privileges'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.authorized_privileges, domain=None, range=Optional[Union[Union[dict, AuthorizedPrivilege], list[Union[dict, AuthorizedPrivilege]]]])

slots.functions_performed = Slot(uri=OSCAL_ASSESSMENT_PLAN.functions_performed, name="functions-performed", curie=OSCAL_ASSESSMENT_PLAN.curie('functions_performed'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.functions_performed, domain=None, range=Optional[Union[str, list[str]]])

slots.implemented_components = Slot(uri=OSCAL_ASSESSMENT_PLAN.implemented_components, name="implemented-components", curie=OSCAL_ASSESSMENT_PLAN.curie('implemented_components'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.implemented_components, domain=None, range=Optional[Union[Union[dict, ImplementedComponent], list[Union[dict, ImplementedComponent]]]])

slots.identifier_type = Slot(uri=OSCAL_ASSESSMENT_PLAN.identifier_type, name="identifier-type", curie=OSCAL_ASSESSMENT_PLAN.curie('identifier_type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.identifier_type, domain=None, range=Optional[str])

slots.actors = Slot(uri=OSCAL_ASSESSMENT_PLAN.actors, name="actors", curie=OSCAL_ASSESSMENT_PLAN.curie('actors'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.actors, domain=None, range=Optional[Union[Union[dict, OriginActor], list[Union[dict, OriginActor]]]])

slots.actor_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.actor_uuid, name="actor-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('actor_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.actor_uuid, domain=None, range=Optional[str])

slots.identified_subject = Slot(uri=OSCAL_ASSESSMENT_PLAN.identified_subject, name="identified-subject", curie=OSCAL_ASSESSMENT_PLAN.curie('identified_subject'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.identified_subject, domain=None, range=Optional[Union[dict, IdentifiedSubject]])

slots.subject_placeholder_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_placeholder_uuid, name="subject-placeholder-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_placeholder_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.subject_placeholder_uuid, domain=None, range=Optional[str])

slots.methods = Slot(uri=OSCAL_ASSESSMENT_PLAN.methods, name="methods", curie=OSCAL_ASSESSMENT_PLAN.curie('methods'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.methods, domain=None, range=Optional[Union[Union[str, "ObservationMethodEnum"], list[Union[str, "ObservationMethodEnum"]]]])

slots.types = Slot(uri=OSCAL_ASSESSMENT_PLAN.types, name="types", curie=OSCAL_ASSESSMENT_PLAN.curie('types'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.types, domain=None, range=Optional[Union[Union[str, "ObservationTypeEnum"], list[Union[str, "ObservationTypeEnum"]]]])

slots.relevant_evidence = Slot(uri=OSCAL_ASSESSMENT_PLAN.relevant_evidence, name="relevant-evidence", curie=OSCAL_ASSESSMENT_PLAN.curie('relevant_evidence'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.relevant_evidence, domain=None, range=Optional[Union[Union[dict, RelevantEvidence], list[Union[dict, RelevantEvidence]]]])

slots.collected = Slot(uri=OSCAL_ASSESSMENT_PLAN.collected, name="collected", curie=OSCAL_ASSESSMENT_PLAN.curie('collected'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.collected, domain=None, range=Optional[str])

slots.expires = Slot(uri=OSCAL_ASSESSMENT_PLAN.expires, name="expires", curie=OSCAL_ASSESSMENT_PLAN.curie('expires'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.expires, domain=None, range=Optional[str])

slots.target = Slot(uri=OSCAL_ASSESSMENT_PLAN.target, name="target", curie=OSCAL_ASSESSMENT_PLAN.curie('target'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.target, domain=None, range=Optional[Union[dict, FindingTarget]])

slots.implementation_statement_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.implementation_statement_uuid, name="implementation-statement-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('implementation_statement_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.implementation_statement_uuid, domain=None, range=Optional[str])

slots.related_risks = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_risks, name="related-risks", curie=OSCAL_ASSESSMENT_PLAN.curie('related_risks'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.related_risks, domain=None, range=Optional[Union[Union[dict, AssociatedRisk], list[Union[dict, AssociatedRisk]]]])

slots.target_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.target_id, name="target-id", curie=OSCAL_ASSESSMENT_PLAN.curie('target_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.target_id, domain=None, range=Optional[str])

slots.implementation_status = Slot(uri=OSCAL_ASSESSMENT_PLAN.implementation_status, name="implementation-status", curie=OSCAL_ASSESSMENT_PLAN.curie('implementation_status'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.implementation_status, domain=None, range=Optional[Union[dict, ImplementationStatus]])

slots.reason = Slot(uri=OSCAL_ASSESSMENT_PLAN.reason, name="reason", curie=OSCAL_ASSESSMENT_PLAN.curie('reason'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.reason, domain=None, range=Optional[Union[str, "ObjectiveStatusReasonEnum"]])

slots.observation_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.observation_uuid, name="observation-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('observation_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.observation_uuid, domain=None, range=Optional[str])

slots.risk_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.risk_uuid, name="risk-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('risk_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.risk_uuid, domain=None, range=Optional[str])

slots.statement = Slot(uri=OSCAL_ASSESSMENT_PLAN.statement, name="statement", curie=OSCAL_ASSESSMENT_PLAN.curie('statement'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.statement, domain=None, range=Optional[str])

slots.threat_ids = Slot(uri=OSCAL_ASSESSMENT_PLAN.threat_ids, name="threat-ids", curie=OSCAL_ASSESSMENT_PLAN.curie('threat_ids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.threat_ids, domain=None, range=Optional[Union[Union[dict, ThreatId], list[Union[dict, ThreatId]]]])

slots.characterizations = Slot(uri=OSCAL_ASSESSMENT_PLAN.characterizations, name="characterizations", curie=OSCAL_ASSESSMENT_PLAN.curie('characterizations'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.characterizations, domain=None, range=Optional[Union[Union[dict, Characterization], list[Union[dict, Characterization]]]])

slots.mitigating_factors = Slot(uri=OSCAL_ASSESSMENT_PLAN.mitigating_factors, name="mitigating-factors", curie=OSCAL_ASSESSMENT_PLAN.curie('mitigating_factors'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.mitigating_factors, domain=None, range=Optional[Union[Union[dict, MitigatingFactor], list[Union[dict, MitigatingFactor]]]])

slots.deadline = Slot(uri=OSCAL_ASSESSMENT_PLAN.deadline, name="deadline", curie=OSCAL_ASSESSMENT_PLAN.curie('deadline'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.deadline, domain=None, range=Optional[str])

slots.remediations = Slot(uri=OSCAL_ASSESSMENT_PLAN.remediations, name="remediations", curie=OSCAL_ASSESSMENT_PLAN.curie('remediations'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.remediations, domain=None, range=Optional[Union[Union[dict, Response], list[Union[dict, Response]]]])

slots.risk_log = Slot(uri=OSCAL_ASSESSMENT_PLAN.risk_log, name="risk-log", curie=OSCAL_ASSESSMENT_PLAN.curie('risk_log'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.risk_log, domain=None, range=Optional[Union[dict, RiskLog]])

slots.origin = Slot(uri=OSCAL_ASSESSMENT_PLAN.origin, name="origin", curie=OSCAL_ASSESSMENT_PLAN.curie('origin'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.origin, domain=None, range=Optional[Union[dict, Origin]])

slots.facets = Slot(uri=OSCAL_ASSESSMENT_PLAN.facets, name="facets", curie=OSCAL_ASSESSMENT_PLAN.curie('facets'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.facets, domain=None, range=Optional[Union[Union[dict, Facet], list[Union[dict, Facet]]]])

slots.implementation_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.implementation_uuid, name="implementation-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('implementation_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.implementation_uuid, domain=None, range=Optional[str])

slots.lifecycle = Slot(uri=OSCAL_ASSESSMENT_PLAN.lifecycle, name="lifecycle", curie=OSCAL_ASSESSMENT_PLAN.curie('lifecycle'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.lifecycle, domain=None, range=Optional[Union[str, "ResponseLifecycleEnum"]])

slots.required_assets = Slot(uri=OSCAL_ASSESSMENT_PLAN.required_assets, name="required-assets", curie=OSCAL_ASSESSMENT_PLAN.curie('required_assets'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.required_assets, domain=None, range=Optional[Union[Union[dict, RequiredAsset], list[Union[dict, RequiredAsset]]]])

slots.entries = Slot(uri=OSCAL_ASSESSMENT_PLAN.entries, name="entries", curie=OSCAL_ASSESSMENT_PLAN.curie('entries'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.entries, domain=None, range=Optional[Union[Union[dict, RiskLogEntry], list[Union[dict, RiskLogEntry]]]])

slots.logged_by = Slot(uri=OSCAL_ASSESSMENT_PLAN.logged_by, name="logged-by", curie=OSCAL_ASSESSMENT_PLAN.curie('logged_by'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.logged_by, domain=None, range=Optional[Union[Union[dict, LoggedBy], list[Union[dict, LoggedBy]]]])

slots.status_change = Slot(uri=OSCAL_ASSESSMENT_PLAN.status_change, name="status-change", curie=OSCAL_ASSESSMENT_PLAN.curie('status_change'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.status_change, domain=None, range=Optional[Union[str, "RiskStatusEnum"]])

slots.related_responses = Slot(uri=OSCAL_ASSESSMENT_PLAN.related_responses, name="related-responses", curie=OSCAL_ASSESSMENT_PLAN.curie('related_responses'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.related_responses, domain=None, range=Optional[Union[Union[dict, RiskResponseReference], list[Union[dict, RiskResponseReference]]]])

slots.party_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.party_uuid, name="party-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('party_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.party_uuid, domain=None, range=Optional[str])

slots.response_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.response_uuid, name="response-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('response_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.response_uuid, domain=None, range=Optional[str])

slots.uuid = Slot(uri=OSCAL_CATALOG.uuid, name="uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.uuid, domain=None, range=Optional[str])

slots.title = Slot(uri=OSCAL_CATALOG.title, name="title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.title, domain=None, range=Optional[str])

slots.description = Slot(uri=OSCAL_CATALOG.description, name="description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.description, domain=None, range=Optional[str])

slots.remarks = Slot(uri=OSCAL_CATALOG.remarks, name="remarks", curie=OSCAL_CATALOG.curie('remarks'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.remarks, domain=None, range=Optional[str])

slots.href = Slot(uri=OSCAL_CATALOG.href, name="href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.href, domain=None, range=Optional[str])

slots.props = Slot(uri=OSCAL_CATALOG.props, name="props", curie=OSCAL_CATALOG.curie('props'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.props, domain=None, range=Optional[Union[Union[dict, Property], list[Union[dict, Property]]]])

slots.links = Slot(uri=OSCAL_CATALOG.links, name="links", curie=OSCAL_CATALOG.curie('links'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.links, domain=None, range=Optional[Union[Union[dict, Link], list[Union[dict, Link]]]])

slots.responsible_roles = Slot(uri=OSCAL_CATALOG.responsible_roles, name="responsible-roles", curie=OSCAL_CATALOG.curie('responsible_roles'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.responsible_roles, domain=None, range=Optional[Union[Union[dict, ResponsibleRole], list[Union[dict, ResponsibleRole]]]])

slots.responsible_parties = Slot(uri=OSCAL_CATALOG.responsible_parties, name="responsible-parties", curie=OSCAL_CATALOG.curie('responsible_parties'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.responsible_parties, domain=None, range=Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]])

slots.id = Slot(uri=OSCAL_CATALOG.id, name="id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.id, domain=None, range=Optional[str])

slots._class = Slot(uri=OSCAL_CATALOG._class, name="_class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL_ASSESSMENT_PLAN._class, domain=None, range=Optional[str])

slots.name = Slot(uri=OSCAL_CATALOG.name, name="name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.name, domain=None, range=Optional[str])

slots.ns = Slot(uri=OSCAL_CATALOG.ns, name="ns", curie=OSCAL_CATALOG.curie('ns'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ns, domain=None, range=Optional[str])

slots.type = Slot(uri=OSCAL_CATALOG.type, name="type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.type, domain=None, range=Optional[str])

slots.value = Slot(uri=OSCAL_CATALOG.value, name="value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.value, domain=None, range=Optional[str])

slots.scheme = Slot(uri=OSCAL_CATALOG.scheme, name="scheme", curie=OSCAL_CATALOG.curie('scheme'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.scheme, domain=None, range=Optional[str])

slots.role_id = Slot(uri=OSCAL_CATALOG.role_id, name="role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.role_id, domain=None, range=Optional[str])

slots.party_uuids = Slot(uri=OSCAL_CATALOG.party_uuids, name="party-uuids", curie=OSCAL_CATALOG.curie('party_uuids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.party_uuids, domain=None, range=Optional[Union[str, list[str]]])

slots.email_addresses = Slot(uri=OSCAL_CATALOG.email_addresses, name="email-addresses", curie=OSCAL_CATALOG.curie('email_addresses'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.email_addresses, domain=None, range=Optional[Union[str, list[str]]])

slots.telephone_numbers = Slot(uri=OSCAL_CATALOG.telephone_numbers, name="telephone-numbers", curie=OSCAL_CATALOG.curie('telephone_numbers'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.telephone_numbers, domain=None, range=Optional[Union[Union[dict, TelephoneNumber], list[Union[dict, TelephoneNumber]]]])

slots.short_name = Slot(uri=OSCAL_CATALOG.short_name, name="short-name", curie=OSCAL_CATALOG.curie('short_name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.short_name, domain=None, range=Optional[str])

slots.published = Slot(uri=OSCAL_CATALOG.published, name="published", curie=OSCAL_CATALOG.curie('published'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.published, domain=None, range=Optional[str])

slots.last_modified = Slot(uri=OSCAL_CATALOG.last_modified, name="last-modified", curie=OSCAL_CATALOG.curie('last_modified'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.last_modified, domain=None, range=Optional[str])

slots.version = Slot(uri=OSCAL_CATALOG.version, name="version", curie=OSCAL_CATALOG.curie('version'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.version, domain=None, range=Optional[str])

slots.oscal_version = Slot(uri=OSCAL_CATALOG.oscal_version, name="oscal-version", curie=OSCAL_CATALOG.curie('oscal_version'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.oscal_version, domain=None, range=Optional[str])

slots.document_ids = Slot(uri=OSCAL_CATALOG.document_ids, name="document-ids", curie=OSCAL_CATALOG.curie('document_ids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.document_ids, domain=None, range=Optional[Union[Union[dict, DocumentId], list[Union[dict, DocumentId]]]])

slots.prose = Slot(uri=OSCAL_CATALOG.prose, name="prose", curie=OSCAL_CATALOG.curie('prose'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.prose, domain=None, range=Optional[str])

slots.params = Slot(uri=OSCAL_CATALOG.params, name="params", curie=OSCAL_CATALOG.curie('params'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.params, domain=None, range=Optional[Union[Union[dict, Parameter], list[Union[dict, Parameter]]]])

slots.controls = Slot(uri=OSCAL_CATALOG.controls, name="controls", curie=OSCAL_CATALOG.curie('controls'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.controls, domain=None, range=Optional[Union[Union[dict, Control], list[Union[dict, Control]]]])

slots.groups = Slot(uri=OSCAL_CATALOG.groups, name="groups", curie=OSCAL_CATALOG.curie('groups'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.groups, domain=None, range=Optional[Union[Union[dict, Group], list[Union[dict, Group]]]])

slots.parts = Slot(uri=OSCAL_CATALOG.parts, name="parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.parts, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.media_type = Slot(uri=OSCAL_CATALOG.media_type, name="media-type", curie=OSCAL_CATALOG.curie('media_type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.media_type, domain=None, range=Optional[str])

slots.text = Slot(uri=OSCAL_CATALOG.text, name="text", curie=OSCAL_CATALOG.curie('text'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.text, domain=None, range=Optional[str])

slots.how_many = Slot(uri=OSCAL_CATALOG.how_many, name="how-many", curie=OSCAL_CATALOG.curie('how_many'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.how_many, domain=None, range=Optional[Union[str, "ParameterCardinalityEnum"]])

slots.choice = Slot(uri=OSCAL_CATALOG.choice, name="choice", curie=OSCAL_CATALOG.curie('choice'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.choice, domain=None, range=Optional[Union[str, list[str]]])

slots.catalog = Slot(uri=OSCAL_CATALOG.catalog, name="catalog", curie=OSCAL_CATALOG.curie('catalog'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.catalog, domain=None, range=Optional[Union[dict, Catalog]])

slots.metadata = Slot(uri=OSCAL_CATALOG.metadata, name="metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.metadata, domain=None, range=Optional[Union[dict, Metadata]])

slots.back_matter = Slot(uri=OSCAL_CATALOG.back_matter, name="back-matter", curie=OSCAL_CATALOG.curie('back_matter'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.back_matter, domain=None, range=Optional[Union[dict, BackMatter]])

slots.revisions = Slot(uri=OSCAL_CATALOG.revisions, name="revisions", curie=OSCAL_CATALOG.curie('revisions'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.revisions, domain=None, range=Optional[Union[Union[dict, Revision], list[Union[dict, Revision]]]])

slots.roles = Slot(uri=OSCAL_CATALOG.roles, name="roles", curie=OSCAL_CATALOG.curie('roles'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.roles, domain=None, range=Optional[Union[Union[dict, Role], list[Union[dict, Role]]]])

slots.locations = Slot(uri=OSCAL_CATALOG.locations, name="locations", curie=OSCAL_CATALOG.curie('locations'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.locations, domain=None, range=Optional[Union[Union[dict, Location], list[Union[dict, Location]]]])

slots.parties = Slot(uri=OSCAL_CATALOG.parties, name="parties", curie=OSCAL_CATALOG.curie('parties'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.parties, domain=None, range=Optional[Union[Union[dict, Party], list[Union[dict, Party]]]])

slots.actions = Slot(uri=OSCAL_CATALOG.actions, name="actions", curie=OSCAL_CATALOG.curie('actions'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.actions, domain=None, range=Optional[Union[Union[dict, Action], list[Union[dict, Action]]]])

slots.identifier = Slot(uri=OSCAL_CATALOG.identifier, name="identifier", curie=OSCAL_CATALOG.curie('identifier'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.identifier, domain=None, range=Optional[str])

slots.address = Slot(uri=OSCAL_CATALOG.address, name="address", curie=OSCAL_CATALOG.curie('address'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.address, domain=None, range=Optional[Union[dict, Address]])

slots.urls = Slot(uri=OSCAL_CATALOG.urls, name="urls", curie=OSCAL_CATALOG.curie('urls'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.urls, domain=None, range=Optional[Union[str, list[str]]])

slots.external_ids = Slot(uri=OSCAL_CATALOG.external_ids, name="external-ids", curie=OSCAL_CATALOG.curie('external_ids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.external_ids, domain=None, range=Optional[Union[Union[dict, PartyExternalId], list[Union[dict, PartyExternalId]]]])

slots.addresses = Slot(uri=OSCAL_CATALOG.addresses, name="addresses", curie=OSCAL_CATALOG.curie('addresses'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.addresses, domain=None, range=Optional[Union[Union[dict, Address], list[Union[dict, Address]]]])

slots.location_uuids = Slot(uri=OSCAL_CATALOG.location_uuids, name="location-uuids", curie=OSCAL_CATALOG.curie('location_uuids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.location_uuids, domain=None, range=Optional[Union[str, list[str]]])

slots.member_of_organizations = Slot(uri=OSCAL_CATALOG.member_of_organizations, name="member-of-organizations", curie=OSCAL_CATALOG.curie('member_of_organizations'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.member_of_organizations, domain=None, range=Optional[Union[str, list[str]]])

slots.date = Slot(uri=OSCAL_CATALOG.date, name="date", curie=OSCAL_CATALOG.curie('date'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.date, domain=None, range=Optional[str])

slots.system = Slot(uri=OSCAL_CATALOG.system, name="system", curie=OSCAL_CATALOG.curie('system'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.system, domain=None, range=Optional[str])

slots.number = Slot(uri=OSCAL_CATALOG.number, name="number", curie=OSCAL_CATALOG.curie('number'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.number, domain=None, range=Optional[str])

slots.addr_lines = Slot(uri=OSCAL_CATALOG.addr_lines, name="addr-lines", curie=OSCAL_CATALOG.curie('addr_lines'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.addr_lines, domain=None, range=Optional[Union[str, list[str]]])

slots.city = Slot(uri=OSCAL_CATALOG.city, name="city", curie=OSCAL_CATALOG.curie('city'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.city, domain=None, range=Optional[str])

slots.state = Slot(uri=OSCAL_CATALOG.state, name="state", curie=OSCAL_CATALOG.curie('state'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.state, domain=None, range=Optional[str])

slots.postal_code = Slot(uri=OSCAL_CATALOG.postal_code, name="postal-code", curie=OSCAL_CATALOG.curie('postal_code'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.postal_code, domain=None, range=Optional[str])

slots.country = Slot(uri=OSCAL_CATALOG.country, name="country", curie=OSCAL_CATALOG.curie('country'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.country, domain=None, range=Optional[str])

slots.algorithm = Slot(uri=OSCAL_CATALOG.algorithm, name="algorithm", curie=OSCAL_CATALOG.curie('algorithm'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.algorithm, domain=None, range=Optional[str])

slots.group = Slot(uri=OSCAL_CATALOG.group, name="group", curie=OSCAL_CATALOG.curie('group'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.group, domain=None, range=Optional[str])

slots.rel = Slot(uri=OSCAL_CATALOG.rel, name="rel", curie=OSCAL_CATALOG.curie('rel'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.rel, domain=None, range=Optional[str])

slots.resource_fragment = Slot(uri=OSCAL_CATALOG.resource_fragment, name="resource-fragment", curie=OSCAL_CATALOG.curie('resource_fragment'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.resource_fragment, domain=None, range=Optional[str])

slots.resources = Slot(uri=OSCAL_CATALOG.resources, name="resources", curie=OSCAL_CATALOG.curie('resources'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.citation = Slot(uri=OSCAL_CATALOG.citation, name="citation", curie=OSCAL_CATALOG.curie('citation'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.citation, domain=None, range=Optional[Union[dict, Citation]])

slots.rlinks = Slot(uri=OSCAL_CATALOG.rlinks, name="rlinks", curie=OSCAL_CATALOG.curie('rlinks'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.rlinks, domain=None, range=Optional[Union[Union[dict, ResourceLink], list[Union[dict, ResourceLink]]]])

slots.base64 = Slot(uri=OSCAL_CATALOG.base64, name="base64", curie=OSCAL_CATALOG.curie('base64'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.base64, domain=None, range=Optional[Union[dict, Base64Resource]])

slots.hashes = Slot(uri=OSCAL_CATALOG.hashes, name="hashes", curie=OSCAL_CATALOG.curie('hashes'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.hashes, domain=None, range=Optional[Union[Union[dict, Hash], list[Union[dict, Hash]]]])

slots.filename = Slot(uri=OSCAL_CATALOG.filename, name="filename", curie=OSCAL_CATALOG.curie('filename'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.filename, domain=None, range=Optional[str])

slots.depends_on = Slot(uri=OSCAL_CATALOG.depends_on, name="depends-on", curie=OSCAL_CATALOG.curie('depends_on'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.depends_on, domain=None, range=Optional[str])

slots.label = Slot(uri=OSCAL_CATALOG.label, name="label", curie=OSCAL_CATALOG.curie('label'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.label, domain=None, range=Optional[str])

slots.usage = Slot(uri=OSCAL_CATALOG.usage, name="usage", curie=OSCAL_CATALOG.curie('usage'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.usage, domain=None, range=Optional[str])

slots.constraints = Slot(uri=OSCAL_CATALOG.constraints, name="constraints", curie=OSCAL_CATALOG.curie('constraints'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.constraints, domain=None, range=Optional[Union[Union[dict, ParameterConstraint], list[Union[dict, ParameterConstraint]]]])

slots.guidelines = Slot(uri=OSCAL_CATALOG.guidelines, name="guidelines", curie=OSCAL_CATALOG.curie('guidelines'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.guidelines, domain=None, range=Optional[Union[Union[dict, ParameterGuideline], list[Union[dict, ParameterGuideline]]]])

slots.values = Slot(uri=OSCAL_CATALOG.values, name="values", curie=OSCAL_CATALOG.curie('values'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.values, domain=None, range=Optional[Union[str, list[str]]])

slots.select = Slot(uri=OSCAL_CATALOG.select, name="select", curie=OSCAL_CATALOG.curie('select'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.select, domain=None, range=Optional[Union[dict, ParameterSelection]])

slots.tests = Slot(uri=OSCAL_CATALOG.tests, name="tests", curie=OSCAL_CATALOG.curie('tests'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.tests, domain=None, range=Optional[Union[Union[dict, ConstraintTest], list[Union[dict, ConstraintTest]]]])

slots.expression = Slot(uri=OSCAL_CATALOG.expression, name="expression", curie=OSCAL_CATALOG.curie('expression'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.expression, domain=None, range=Optional[str])

slots.with_child_controls = Slot(uri=OSCAL_CATALOG.with_child_controls, name="with-child-controls", curie=OSCAL_CATALOG.curie('with_child_controls'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.with_child_controls, domain=None, range=Optional[Union[str, "WithChildControlsEnum"]])

slots.with_ids = Slot(uri=OSCAL_CATALOG.with_ids, name="with-ids", curie=OSCAL_CATALOG.curie('with_ids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.with_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.matching = Slot(uri=OSCAL_CATALOG.matching, name="matching", curie=OSCAL_CATALOG.curie('matching'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.matching, domain=None, range=Optional[Union[Union[dict, ControlMatching], list[Union[dict, ControlMatching]]]])

slots.pattern = Slot(uri=OSCAL_CATALOG.pattern, name="pattern", curie=OSCAL_CATALOG.curie('pattern'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.pattern, domain=None, range=Optional[str])

slots.AssessmentPlanDocument_assessment_plan = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_plan, name="AssessmentPlanDocument_assessment-plan", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_plan'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentPlanDocument_assessment_plan, domain=AssessmentPlanDocument, range=Union[dict, AssessmentPlan])

slots.AssessmentPlan_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentPlan_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentPlan_uuid, domain=AssessmentPlan, range=str)

slots.AssessmentPlan_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="AssessmentPlan_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentPlan_metadata, domain=AssessmentPlan, range=Union[dict, "Metadata"])

slots.AssessmentPlan_import_ssp = Slot(uri=OSCAL_ASSESSMENT_PLAN.import_ssp, name="AssessmentPlan_import-ssp", curie=OSCAL_ASSESSMENT_PLAN.curie('import_ssp'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentPlan_import_ssp, domain=AssessmentPlan, range=Union[dict, "ImportSSP"])

slots.AssessmentPlan_reviewed_controls = Slot(uri=OSCAL_ASSESSMENT_PLAN.reviewed_controls, name="AssessmentPlan_reviewed-controls", curie=OSCAL_ASSESSMENT_PLAN.curie('reviewed_controls'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentPlan_reviewed_controls, domain=AssessmentPlan, range=Union[dict, "ReviewedControls"])

slots.ImportSSP_href = Slot(uri=OSCAL_CATALOG.href, name="ImportSSP_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ImportSSP_href, domain=ImportSSP, range=str)

slots.TermsAndConditions_parts = Slot(uri=OSCAL_CATALOG.parts, name="TermsAndConditions_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.TermsAndConditions_parts, domain=TermsAndConditions, range=Optional[Union[Union[dict, "AssessmentPart"], list[Union[dict, "AssessmentPart"]]]])

slots.ReviewedControls_control_selections = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_selections, name="ReviewedControls_control-selections", curie=OSCAL_ASSESSMENT_PLAN.curie('control_selections'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ReviewedControls_control_selections, domain=ReviewedControls, range=Union[Union[dict, "ControlSelection"], list[Union[dict, "ControlSelection"]]])

slots.AssessmentSelectControlById_control_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_id, name="AssessmentSelectControlById_control-id", curie=OSCAL_ASSESSMENT_PLAN.curie('control_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentSelectControlById_control_id, domain=AssessmentSelectControlById, range=str)

slots.SelectObjectiveById_objective_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.objective_id, name="SelectObjectiveById_objective-id", curie=OSCAL_ASSESSMENT_PLAN.curie('objective_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SelectObjectiveById_objective_id, domain=SelectObjectiveById, range=str)

slots.AssessmentSubject_type = Slot(uri=OSCAL_CATALOG.type, name="AssessmentSubject_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentSubject_type, domain=AssessmentSubject, range=Union[str, "AssessmentSubjectTypeEnum"])

slots.SelectSubjectById_subject_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_uuid, name="SelectSubjectById_subject-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SelectSubjectById_subject_uuid, domain=SelectSubjectById, range=str)

slots.SelectSubjectById_type = Slot(uri=OSCAL_CATALOG.type, name="SelectSubjectById_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SelectSubjectById_type, domain=SelectSubjectById, range=Union[str, "SelectSubjectTypeEnum"])

slots.SubjectReference_subject_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_uuid, name="SubjectReference_subject-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SubjectReference_subject_uuid, domain=SubjectReference, range=str)

slots.SubjectReference_type = Slot(uri=OSCAL_CATALOG.type, name="SubjectReference_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SubjectReference_type, domain=SubjectReference, range=Union[str, "SelectSubjectTypeEnum"])

slots.AssessmentSubjectPlaceholder_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentSubjectPlaceholder_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentSubjectPlaceholder_uuid, domain=AssessmentSubjectPlaceholder, range=str)

slots.AssessmentSubjectPlaceholder_sources = Slot(uri=OSCAL_ASSESSMENT_PLAN.sources, name="AssessmentSubjectPlaceholder_sources", curie=OSCAL_ASSESSMENT_PLAN.curie('sources'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentSubjectPlaceholder_sources, domain=AssessmentSubjectPlaceholder, range=Union[Union[dict, "AssessmentSubjectSource"], list[Union[dict, "AssessmentSubjectSource"]]])

slots.AssessmentSubjectSource_task_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.task_uuid, name="AssessmentSubjectSource_task-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('task_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentSubjectSource_task_uuid, domain=AssessmentSubjectSource, range=str)

slots.AssessmentAssets_assessment_platforms = Slot(uri=OSCAL_ASSESSMENT_PLAN.assessment_platforms, name="AssessmentAssets_assessment-platforms", curie=OSCAL_ASSESSMENT_PLAN.curie('assessment_platforms'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentAssets_assessment_platforms, domain=AssessmentAssets, range=Union[Union[dict, "AssessmentPlatform"], list[Union[dict, "AssessmentPlatform"]]])

slots.AssessmentPlatform_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentPlatform_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentPlatform_uuid, domain=AssessmentPlatform, range=str)

slots.UsesComponent_component_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.component_uuid, name="UsesComponent_component-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('component_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.UsesComponent_component_uuid, domain=UsesComponent, range=str)

slots.LocalObjective_control_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.control_id, name="LocalObjective_control-id", curie=OSCAL_ASSESSMENT_PLAN.curie('control_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.LocalObjective_control_id, domain=LocalObjective, range=str)

slots.LocalObjective_parts = Slot(uri=OSCAL_CATALOG.parts, name="LocalObjective_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.LocalObjective_parts, domain=LocalObjective, range=Union[Union[dict, "ControlPart"], list[Union[dict, "ControlPart"]]])

slots.AssessmentMethod_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="AssessmentMethod_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentMethod_uuid, domain=AssessmentMethod, range=str)

slots.AssessmentMethod_part = Slot(uri=OSCAL_ASSESSMENT_PLAN.part, name="AssessmentMethod_part", curie=OSCAL_ASSESSMENT_PLAN.curie('part'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentMethod_part, domain=AssessmentMethod, range=Union[dict, "AssessmentPart"])

slots.Activity_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Activity_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Activity_uuid, domain=Activity, range=str)

slots.Activity_description = Slot(uri=OSCAL_CATALOG.description, name="Activity_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Activity_description, domain=Activity, range=str)

slots.Step_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Step_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Step_uuid, domain=Step, range=str)

slots.Step_description = Slot(uri=OSCAL_CATALOG.description, name="Step_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Step_description, domain=Step, range=str)

slots.Task_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Task_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Task_uuid, domain=Task, range=str)

slots.Task_type = Slot(uri=OSCAL_CATALOG.type, name="Task_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Task_type, domain=Task, range=Union[str, "TaskTypeEnum"])

slots.Task_title = Slot(uri=OSCAL_CATALOG.title, name="Task_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Task_title, domain=Task, range=str)

slots.Task_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="Task_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Task_subjects, domain=Task, range=Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]])

slots.OnDateCondition_date = Slot(uri=OSCAL_CATALOG.date, name="OnDateCondition_date", curie=OSCAL_CATALOG.curie('date'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.OnDateCondition_date, domain=OnDateCondition, range=str)

slots.WithinDateRange_start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="WithinDateRange_start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.WithinDateRange_start, domain=WithinDateRange, range=str)

slots.WithinDateRange_end = Slot(uri=OSCAL_ASSESSMENT_PLAN.end, name="WithinDateRange_end", curie=OSCAL_ASSESSMENT_PLAN.curie('end'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.WithinDateRange_end, domain=WithinDateRange, range=str)

slots.AtFrequency_period = Slot(uri=OSCAL_ASSESSMENT_PLAN.period, name="AtFrequency_period", curie=OSCAL_ASSESSMENT_PLAN.curie('period'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AtFrequency_period, domain=AtFrequency, range=int)

slots.AtFrequency_unit = Slot(uri=OSCAL_ASSESSMENT_PLAN.unit, name="AtFrequency_unit", curie=OSCAL_ASSESSMENT_PLAN.curie('unit'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AtFrequency_unit, domain=AtFrequency, range=Union[str, "TimingUnitEnum"])

slots.TaskDependency_task_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.task_uuid, name="TaskDependency_task-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('task_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.TaskDependency_task_uuid, domain=TaskDependency, range=str)

slots.AssociatedActivity_activity_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.activity_uuid, name="AssociatedActivity_activity-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('activity_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssociatedActivity_activity_uuid, domain=AssociatedActivity, range=str)

slots.AssociatedActivity_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="AssociatedActivity_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssociatedActivity_subjects, domain=AssociatedActivity, range=Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]])

slots.AssessmentPart_name = Slot(uri=OSCAL_CATALOG.name, name="AssessmentPart_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentPart_name, domain=AssessmentPart, range=Union[str, "AssessmentPartNameEnum"])

slots.AssessmentPart_parts = Slot(uri=OSCAL_CATALOG.parts, name="AssessmentPart_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssessmentPart_parts, domain=AssessmentPart, range=Optional[Union[Union[dict, "AssessmentPart"], list[Union[dict, "AssessmentPart"]]]])

slots.ControlPart_name = Slot(uri=OSCAL_CATALOG.name, name="ControlPart_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ControlPart_name, domain=ControlPart, range=str)

slots.ControlPart_parts = Slot(uri=OSCAL_CATALOG.parts, name="ControlPart_parts", curie=OSCAL_CATALOG.curie('parts'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ControlPart_parts, domain=ControlPart, range=Optional[Union[Union[dict, "ControlPart"], list[Union[dict, "ControlPart"]]]])

slots.SetParameter_param_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.param_id, name="SetParameter_param-id", curie=OSCAL_ASSESSMENT_PLAN.curie('param_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SetParameter_param_id, domain=SetParameter, range=str)

slots.SetParameter_values = Slot(uri=OSCAL_CATALOG.values, name="SetParameter_values", curie=OSCAL_CATALOG.curie('values'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SetParameter_values, domain=SetParameter, range=Union[str, list[str]])

slots.SystemComponent_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="SystemComponent_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SystemComponent_uuid, domain=SystemComponent, range=str)

slots.SystemComponent_type = Slot(uri=OSCAL_CATALOG.type, name="SystemComponent_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SystemComponent_type, domain=SystemComponent, range=Union[str, "ComponentTypeEnum"])

slots.SystemComponent_title = Slot(uri=OSCAL_CATALOG.title, name="SystemComponent_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SystemComponent_title, domain=SystemComponent, range=str)

slots.SystemComponent_description = Slot(uri=OSCAL_CATALOG.description, name="SystemComponent_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SystemComponent_description, domain=SystemComponent, range=str)

slots.SystemComponent_status = Slot(uri=OSCAL_ASSESSMENT_PLAN.status, name="SystemComponent_status", curie=OSCAL_ASSESSMENT_PLAN.curie('status'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SystemComponent_status, domain=SystemComponent, range=Union[dict, "ComponentStatus"])

slots.ComponentStatus_state = Slot(uri=OSCAL_CATALOG.state, name="ComponentStatus_state", curie=OSCAL_CATALOG.curie('state'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ComponentStatus_state, domain=ComponentStatus, range=Union[str, "ComponentStateEnum"])

slots.Protocol_name = Slot(uri=OSCAL_CATALOG.name, name="Protocol_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Protocol_name, domain=Protocol, range=str)

slots.PortRange_start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="PortRange_start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.PortRange_start, domain=PortRange, range=Optional[int])

slots.PortRange_end = Slot(uri=OSCAL_ASSESSMENT_PLAN.end, name="PortRange_end", curie=OSCAL_ASSESSMENT_PLAN.curie('end'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.PortRange_end, domain=PortRange, range=Optional[int])

slots.ImplementationStatus_state = Slot(uri=OSCAL_CATALOG.state, name="ImplementationStatus_state", curie=OSCAL_CATALOG.curie('state'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ImplementationStatus_state, domain=ImplementationStatus, range=Union[str, "ImplementationStatusStateEnum"])

slots.SystemUser_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="SystemUser_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SystemUser_uuid, domain=SystemUser, range=str)

slots.AuthorizedPrivilege_title = Slot(uri=OSCAL_CATALOG.title, name="AuthorizedPrivilege_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AuthorizedPrivilege_title, domain=AuthorizedPrivilege, range=str)

slots.AuthorizedPrivilege_functions_performed = Slot(uri=OSCAL_ASSESSMENT_PLAN.functions_performed, name="AuthorizedPrivilege_functions-performed", curie=OSCAL_ASSESSMENT_PLAN.curie('functions_performed'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AuthorizedPrivilege_functions_performed, domain=AuthorizedPrivilege, range=Union[str, list[str]])

slots.InventoryItem_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="InventoryItem_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.InventoryItem_uuid, domain=InventoryItem, range=str)

slots.InventoryItem_description = Slot(uri=OSCAL_CATALOG.description, name="InventoryItem_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.InventoryItem_description, domain=InventoryItem, range=str)

slots.ImplementedComponent_component_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.component_uuid, name="ImplementedComponent_component-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('component_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ImplementedComponent_component_uuid, domain=ImplementedComponent, range=str)

slots.SystemId_id = Slot(uri=OSCAL_CATALOG.id, name="SystemId_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.SystemId_id, domain=SystemId, range=str)

slots.Origin_actors = Slot(uri=OSCAL_ASSESSMENT_PLAN.actors, name="Origin_actors", curie=OSCAL_ASSESSMENT_PLAN.curie('actors'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Origin_actors, domain=Origin, range=Union[Union[dict, "OriginActor"], list[Union[dict, "OriginActor"]]])

slots.OriginActor_type = Slot(uri=OSCAL_CATALOG.type, name="OriginActor_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.OriginActor_type, domain=OriginActor, range=Union[str, "OriginActorTypeEnum"])

slots.OriginActor_actor_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.actor_uuid, name="OriginActor_actor-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('actor_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.OriginActor_actor_uuid, domain=OriginActor, range=str)

slots.RelatedTask_task_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.task_uuid, name="RelatedTask_task-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('task_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RelatedTask_task_uuid, domain=RelatedTask, range=str)

slots.RelatedTask_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="RelatedTask_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RelatedTask_subjects, domain=RelatedTask, range=Optional[Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]]])

slots.IdentifiedSubject_subject_placeholder_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.subject_placeholder_uuid, name="IdentifiedSubject_subject-placeholder-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('subject_placeholder_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.IdentifiedSubject_subject_placeholder_uuid, domain=IdentifiedSubject, range=str)

slots.IdentifiedSubject_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="IdentifiedSubject_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.IdentifiedSubject_subjects, domain=IdentifiedSubject, range=Union[Union[dict, AssessmentSubject], list[Union[dict, AssessmentSubject]]])

slots.Observation_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Observation_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Observation_uuid, domain=Observation, range=str)

slots.Observation_description = Slot(uri=OSCAL_CATALOG.description, name="Observation_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Observation_description, domain=Observation, range=str)

slots.Observation_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="Observation_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Observation_subjects, domain=Observation, range=Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]])

slots.Observation_methods = Slot(uri=OSCAL_ASSESSMENT_PLAN.methods, name="Observation_methods", curie=OSCAL_ASSESSMENT_PLAN.curie('methods'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Observation_methods, domain=Observation, range=Union[Union[str, "ObservationMethodEnum"], list[Union[str, "ObservationMethodEnum"]]])

slots.Observation_collected = Slot(uri=OSCAL_ASSESSMENT_PLAN.collected, name="Observation_collected", curie=OSCAL_ASSESSMENT_PLAN.curie('collected'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Observation_collected, domain=Observation, range=str)

slots.RelevantEvidence_description = Slot(uri=OSCAL_CATALOG.description, name="RelevantEvidence_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RelevantEvidence_description, domain=RelevantEvidence, range=str)

slots.Finding_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Finding_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Finding_uuid, domain=Finding, range=str)

slots.Finding_title = Slot(uri=OSCAL_CATALOG.title, name="Finding_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Finding_title, domain=Finding, range=str)

slots.Finding_description = Slot(uri=OSCAL_CATALOG.description, name="Finding_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Finding_description, domain=Finding, range=str)

slots.Finding_target = Slot(uri=OSCAL_ASSESSMENT_PLAN.target, name="Finding_target", curie=OSCAL_ASSESSMENT_PLAN.curie('target'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Finding_target, domain=Finding, range=Union[dict, "FindingTarget"])

slots.FindingTarget_type = Slot(uri=OSCAL_CATALOG.type, name="FindingTarget_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.FindingTarget_type, domain=FindingTarget, range=Union[str, "FindingTargetTypeEnum"])

slots.FindingTarget_target_id = Slot(uri=OSCAL_ASSESSMENT_PLAN.target_id, name="FindingTarget_target-id", curie=OSCAL_ASSESSMENT_PLAN.curie('target_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.FindingTarget_target_id, domain=FindingTarget, range=str)

slots.FindingTarget_status = Slot(uri=OSCAL_ASSESSMENT_PLAN.status, name="FindingTarget_status", curie=OSCAL_ASSESSMENT_PLAN.curie('status'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.FindingTarget_status, domain=FindingTarget, range=Union[dict, "ObjectiveStatus"])

slots.ObjectiveStatus_state = Slot(uri=OSCAL_CATALOG.state, name="ObjectiveStatus_state", curie=OSCAL_CATALOG.curie('state'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ObjectiveStatus_state, domain=ObjectiveStatus, range=Union[str, "ObjectiveStatusStateEnum"])

slots.RelatedObservation_observation_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.observation_uuid, name="RelatedObservation_observation-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('observation_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RelatedObservation_observation_uuid, domain=RelatedObservation, range=str)

slots.AssociatedRisk_risk_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.risk_uuid, name="AssociatedRisk_risk-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('risk_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.AssociatedRisk_risk_uuid, domain=AssociatedRisk, range=str)

slots.Risk_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Risk_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Risk_uuid, domain=Risk, range=str)

slots.Risk_title = Slot(uri=OSCAL_CATALOG.title, name="Risk_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Risk_title, domain=Risk, range=str)

slots.Risk_description = Slot(uri=OSCAL_CATALOG.description, name="Risk_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Risk_description, domain=Risk, range=str)

slots.Risk_statement = Slot(uri=OSCAL_ASSESSMENT_PLAN.statement, name="Risk_statement", curie=OSCAL_ASSESSMENT_PLAN.curie('statement'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Risk_statement, domain=Risk, range=str)

slots.Risk_status = Slot(uri=OSCAL_ASSESSMENT_PLAN.status, name="Risk_status", curie=OSCAL_ASSESSMENT_PLAN.curie('status'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Risk_status, domain=Risk, range=Union[str, "RiskStatusEnum"])

slots.ThreatId_system = Slot(uri=OSCAL_CATALOG.system, name="ThreatId_system", curie=OSCAL_CATALOG.curie('system'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ThreatId_system, domain=ThreatId, range=str)

slots.ThreatId_id = Slot(uri=OSCAL_CATALOG.id, name="ThreatId_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ThreatId_id, domain=ThreatId, range=str)

slots.Characterization_origin = Slot(uri=OSCAL_ASSESSMENT_PLAN.origin, name="Characterization_origin", curie=OSCAL_ASSESSMENT_PLAN.curie('origin'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Characterization_origin, domain=Characterization, range=Union[dict, Origin])

slots.Characterization_facets = Slot(uri=OSCAL_ASSESSMENT_PLAN.facets, name="Characterization_facets", curie=OSCAL_ASSESSMENT_PLAN.curie('facets'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Characterization_facets, domain=Characterization, range=Union[Union[dict, "Facet"], list[Union[dict, "Facet"]]])

slots.Facet_name = Slot(uri=OSCAL_CATALOG.name, name="Facet_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Facet_name, domain=Facet, range=str)

slots.Facet_value = Slot(uri=OSCAL_CATALOG.value, name="Facet_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Facet_value, domain=Facet, range=str)

slots.Facet_system = Slot(uri=OSCAL_CATALOG.system, name="Facet_system", curie=OSCAL_CATALOG.curie('system'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Facet_system, domain=Facet, range=str)

slots.MitigatingFactor_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="MitigatingFactor_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.MitigatingFactor_uuid, domain=MitigatingFactor, range=str)

slots.MitigatingFactor_description = Slot(uri=OSCAL_CATALOG.description, name="MitigatingFactor_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.MitigatingFactor_description, domain=MitigatingFactor, range=str)

slots.MitigatingFactor_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="MitigatingFactor_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.MitigatingFactor_subjects, domain=MitigatingFactor, range=Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]])

slots.Response_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Response_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Response_uuid, domain=Response, range=str)

slots.Response_title = Slot(uri=OSCAL_CATALOG.title, name="Response_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Response_title, domain=Response, range=str)

slots.Response_description = Slot(uri=OSCAL_CATALOG.description, name="Response_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Response_description, domain=Response, range=str)

slots.Response_lifecycle = Slot(uri=OSCAL_ASSESSMENT_PLAN.lifecycle, name="Response_lifecycle", curie=OSCAL_ASSESSMENT_PLAN.curie('lifecycle'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Response_lifecycle, domain=Response, range=Union[str, "ResponseLifecycleEnum"])

slots.RequiredAsset_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="RequiredAsset_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RequiredAsset_uuid, domain=RequiredAsset, range=str)

slots.RequiredAsset_description = Slot(uri=OSCAL_CATALOG.description, name="RequiredAsset_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RequiredAsset_description, domain=RequiredAsset, range=str)

slots.RequiredAsset_subjects = Slot(uri=OSCAL_ASSESSMENT_PLAN.subjects, name="RequiredAsset_subjects", curie=OSCAL_ASSESSMENT_PLAN.curie('subjects'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RequiredAsset_subjects, domain=RequiredAsset, range=Optional[Union[Union[dict, SubjectReference], list[Union[dict, SubjectReference]]]])

slots.RiskLog_entries = Slot(uri=OSCAL_ASSESSMENT_PLAN.entries, name="RiskLog_entries", curie=OSCAL_ASSESSMENT_PLAN.curie('entries'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RiskLog_entries, domain=RiskLog, range=Union[Union[dict, "RiskLogEntry"], list[Union[dict, "RiskLogEntry"]]])

slots.RiskLogEntry_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="RiskLogEntry_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RiskLogEntry_uuid, domain=RiskLogEntry, range=str)

slots.RiskLogEntry_start = Slot(uri=OSCAL_ASSESSMENT_PLAN.start, name="RiskLogEntry_start", curie=OSCAL_ASSESSMENT_PLAN.curie('start'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RiskLogEntry_start, domain=RiskLogEntry, range=str)

slots.LoggedBy_party_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.party_uuid, name="LoggedBy_party-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('party_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.LoggedBy_party_uuid, domain=LoggedBy, range=str)

slots.RiskResponseReference_response_uuid = Slot(uri=OSCAL_ASSESSMENT_PLAN.response_uuid, name="RiskResponseReference_response-uuid", curie=OSCAL_ASSESSMENT_PLAN.curie('response_uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.RiskResponseReference_response_uuid, domain=RiskResponseReference, range=str)

slots.CatalogDocument_catalog = Slot(uri=OSCAL_CATALOG.catalog, name="CatalogDocument_catalog", curie=OSCAL_CATALOG.curie('catalog'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.CatalogDocument_catalog, domain=CatalogDocument, range=Union[dict, "Catalog"])

slots.Catalog_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Catalog_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Catalog_uuid, domain=Catalog, range=str)

slots.Catalog_metadata = Slot(uri=OSCAL_CATALOG.metadata, name="Catalog_metadata", curie=OSCAL_CATALOG.curie('metadata'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Catalog_metadata, domain=Catalog, range=Union[dict, "Metadata"])

slots.Group_id = Slot(uri=OSCAL_CATALOG.id, name="Group_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Group_id, domain=Group, range=Optional[str])

slots.Group__class = Slot(uri=OSCAL_CATALOG._class, name="Group__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Group__class, domain=Group, range=Optional[str])

slots.Group_title = Slot(uri=OSCAL_CATALOG.title, name="Group_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Group_title, domain=Group, range=str)

slots.Control_id = Slot(uri=OSCAL_CATALOG.id, name="Control_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Control_id, domain=Control, range=str)

slots.Control__class = Slot(uri=OSCAL_CATALOG._class, name="Control__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Control__class, domain=Control, range=Optional[str])

slots.Control_title = Slot(uri=OSCAL_CATALOG.title, name="Control_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Control_title, domain=Control, range=str)

slots.Metadata_title = Slot(uri=OSCAL_CATALOG.title, name="Metadata_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Metadata_title, domain=Metadata, range=str)

slots.Metadata_last_modified = Slot(uri=OSCAL_CATALOG.last_modified, name="Metadata_last-modified", curie=OSCAL_CATALOG.curie('last_modified'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Metadata_last_modified, domain=Metadata, range=str)

slots.Metadata_version = Slot(uri=OSCAL_CATALOG.version, name="Metadata_version", curie=OSCAL_CATALOG.curie('version'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Metadata_version, domain=Metadata, range=str)

slots.Metadata_oscal_version = Slot(uri=OSCAL_CATALOG.oscal_version, name="Metadata_oscal-version", curie=OSCAL_CATALOG.curie('oscal_version'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Metadata_oscal_version, domain=Metadata, range=str)

slots.Revision_version = Slot(uri=OSCAL_CATALOG.version, name="Revision_version", curie=OSCAL_CATALOG.curie('version'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Revision_version, domain=Revision, range=str)

slots.DocumentId_identifier = Slot(uri=OSCAL_CATALOG.identifier, name="DocumentId_identifier", curie=OSCAL_CATALOG.curie('identifier'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.DocumentId_identifier, domain=DocumentId, range=str)

slots.Role_id = Slot(uri=OSCAL_CATALOG.id, name="Role_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Role_id, domain=Role, range=str)

slots.Role_title = Slot(uri=OSCAL_CATALOG.title, name="Role_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Role_title, domain=Role, range=str)

slots.Location_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Location_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Location_uuid, domain=Location, range=str)

slots.Party_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Party_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Party_uuid, domain=Party, range=str)

slots.Party_type = Slot(uri=OSCAL_CATALOG.type, name="Party_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Party_type, domain=Party, range=Union[str, "PartyTypeEnum"])

slots.Party_name = Slot(uri=OSCAL_CATALOG.name, name="Party_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Party_name, domain=Party, range=Optional[str])

slots.PartyExternalId_scheme = Slot(uri=OSCAL_CATALOG.scheme, name="PartyExternalId_scheme", curie=OSCAL_CATALOG.curie('scheme'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.PartyExternalId_scheme, domain=PartyExternalId, range=str)

slots.PartyExternalId_id = Slot(uri=OSCAL_CATALOG.id, name="PartyExternalId_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.PartyExternalId_id, domain=PartyExternalId, range=str)

slots.ResponsibleParty_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="ResponsibleParty_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ResponsibleParty_role_id, domain=ResponsibleParty, range=str)

slots.ResponsibleParty_party_uuids = Slot(uri=OSCAL_CATALOG.party_uuids, name="ResponsibleParty_party-uuids", curie=OSCAL_CATALOG.curie('party_uuids'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ResponsibleParty_party_uuids, domain=ResponsibleParty, range=Union[str, list[str]])

slots.ResponsibleRole_role_id = Slot(uri=OSCAL_CATALOG.role_id, name="ResponsibleRole_role-id", curie=OSCAL_CATALOG.curie('role_id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ResponsibleRole_role_id, domain=ResponsibleRole, range=str)

slots.Action_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Action_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Action_uuid, domain=Action, range=str)

slots.Action_type = Slot(uri=OSCAL_CATALOG.type, name="Action_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Action_type, domain=Action, range=str)

slots.Action_system = Slot(uri=OSCAL_CATALOG.system, name="Action_system", curie=OSCAL_CATALOG.curie('system'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Action_system, domain=Action, range=str)

slots.TelephoneNumber_type = Slot(uri=OSCAL_CATALOG.type, name="TelephoneNumber_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.TelephoneNumber_type, domain=TelephoneNumber, range=Optional[str])

slots.TelephoneNumber_number = Slot(uri=OSCAL_CATALOG.number, name="TelephoneNumber_number", curie=OSCAL_CATALOG.curie('number'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.TelephoneNumber_number, domain=TelephoneNumber, range=str)

slots.Address_type = Slot(uri=OSCAL_CATALOG.type, name="Address_type", curie=OSCAL_CATALOG.curie('type'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Address_type, domain=Address, range=Optional[str])

slots.Hash_value = Slot(uri=OSCAL_CATALOG.value, name="Hash_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Hash_value, domain=Hash, range=str)

slots.Hash_algorithm = Slot(uri=OSCAL_CATALOG.algorithm, name="Hash_algorithm", curie=OSCAL_CATALOG.curie('algorithm'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Hash_algorithm, domain=Hash, range=str)

slots.Property_name = Slot(uri=OSCAL_CATALOG.name, name="Property_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Property_name, domain=Property, range=str)

slots.Property_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Property_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Property_uuid, domain=Property, range=Optional[str])

slots.Property_ns = Slot(uri=OSCAL_CATALOG.ns, name="Property_ns", curie=OSCAL_CATALOG.curie('ns'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Property_ns, domain=Property, range=Optional[str])

slots.Property_value = Slot(uri=OSCAL_CATALOG.value, name="Property_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Property_value, domain=Property, range=str)

slots.Property__class = Slot(uri=OSCAL_CATALOG._class, name="Property__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Property__class, domain=Property, range=Optional[str])

slots.Link_href = Slot(uri=OSCAL_CATALOG.href, name="Link_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Link_href, domain=Link, range=str)

slots.Resource_uuid = Slot(uri=OSCAL_CATALOG.uuid, name="Resource_uuid", curie=OSCAL_CATALOG.curie('uuid'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Resource_uuid, domain=Resource, range=str)

slots.Resource_title = Slot(uri=OSCAL_CATALOG.title, name="Resource_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Resource_title, domain=Resource, range=Optional[str])

slots.Resource_description = Slot(uri=OSCAL_CATALOG.description, name="Resource_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Resource_description, domain=Resource, range=Optional[str])

slots.Citation_text = Slot(uri=OSCAL_CATALOG.text, name="Citation_text", curie=OSCAL_CATALOG.curie('text'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Citation_text, domain=Citation, range=str)

slots.ResourceLink_href = Slot(uri=OSCAL_CATALOG.href, name="ResourceLink_href", curie=OSCAL_CATALOG.curie('href'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ResourceLink_href, domain=ResourceLink, range=str)

slots.Base64Resource_value = Slot(uri=OSCAL_CATALOG.value, name="Base64Resource_value", curie=OSCAL_CATALOG.curie('value'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Base64Resource_value, domain=Base64Resource, range=str)

slots.Part_id = Slot(uri=OSCAL_CATALOG.id, name="Part_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Part_id, domain=Part, range=Optional[str])

slots.Part_name = Slot(uri=OSCAL_CATALOG.name, name="Part_name", curie=OSCAL_CATALOG.curie('name'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Part_name, domain=Part, range=str)

slots.Part_ns = Slot(uri=OSCAL_CATALOG.ns, name="Part_ns", curie=OSCAL_CATALOG.curie('ns'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Part_ns, domain=Part, range=Optional[str])

slots.Part__class = Slot(uri=OSCAL_CATALOG._class, name="Part__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Part__class, domain=Part, range=Optional[str])

slots.Part_title = Slot(uri=OSCAL_CATALOG.title, name="Part_title", curie=OSCAL_CATALOG.curie('title'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Part_title, domain=Part, range=Optional[str])

slots.Part_prose = Slot(uri=OSCAL_CATALOG.prose, name="Part_prose", curie=OSCAL_CATALOG.curie('prose'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Part_prose, domain=Part, range=Optional[str])

slots.Parameter_id = Slot(uri=OSCAL_CATALOG.id, name="Parameter_id", curie=OSCAL_CATALOG.curie('id'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Parameter_id, domain=Parameter, range=str)

slots.Parameter__class = Slot(uri=OSCAL_CATALOG._class, name="Parameter__class", curie=OSCAL_CATALOG.curie('_class'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.Parameter__class, domain=Parameter, range=Optional[str])

slots.ParameterConstraint_description = Slot(uri=OSCAL_CATALOG.description, name="ParameterConstraint_description", curie=OSCAL_CATALOG.curie('description'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ParameterConstraint_description, domain=ParameterConstraint, range=Optional[str])

slots.ConstraintTest_expression = Slot(uri=OSCAL_CATALOG.expression, name="ConstraintTest_expression", curie=OSCAL_CATALOG.curie('expression'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ConstraintTest_expression, domain=ConstraintTest, range=str)

slots.ParameterGuideline_prose = Slot(uri=OSCAL_CATALOG.prose, name="ParameterGuideline_prose", curie=OSCAL_CATALOG.curie('prose'),
                   model_uri=OSCAL_ASSESSMENT_PLAN.ParameterGuideline_prose, domain=ParameterGuideline, range=str)
