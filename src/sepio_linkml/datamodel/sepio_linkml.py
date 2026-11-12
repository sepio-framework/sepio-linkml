# Auto generated from sepio_linkml.yaml by pythongen.py version: 0.0.1
# Schema: sepio-linkml
#
# id: https://w3id.org/sepio-framework/sepio-linkml
# description: LinkML-based specification of the SEPIO information model.
# license: Apache Software License 2.0

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

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.12.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SEPIO_MODEL = CurieNamespace('sepio-model', 'https://example.org/sepio-model/')
SEPIO_LINKML = CurieNamespace('sepio_linkml', 'https://w3id.org/sepio-framework/sepio-linkml/')
DEFAULT_ = SEPIO_LINKML


# Types

# Class references



@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    Anything that exists, has existed, or will exist.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Entity"]
    class_class_curie: ClassVar[str] = "sepio-model:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Entity

    id: str = None
    type: str = None
    identifiers: Optional[Union[str, list[str]]] = empty_list()
    label: Optional[str] = None
    alternative_labels: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    extensions: Optional[Union[Union[dict, "Extension"], list[Union[dict, "Extension"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.identifiers, list):
            self.identifiers = [self.identifiers] if self.identifiers is not None else []
        self.identifiers = [v if isinstance(v, str) else str(v) for v in self.identifiers]

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.alternative_labels, list):
            self.alternative_labels = [self.alternative_labels] if self.alternative_labels is not None else []
        self.alternative_labels = [v if isinstance(v, str) else str(v) for v in self.alternative_labels]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="extensions", slot_type=Extension, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationEntity(Entity):
    """
    An abstract (non-physical) entity that is about something - representing the underlying 'information content'
    conveyed by physical or digital information artifacts like books, web pages, data tables, or photographs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["InformationEntity"]
    class_class_curie: ClassVar[str] = "sepio-model:InformationEntity"
    class_name: ClassVar[str] = "InformationEntity"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.InformationEntity

    id: str = None
    type: str = None
    is_about: Optional[Union[str, list[str]]] = empty_list()
    contributions: Optional[Union[Union[dict, "Contribution"], list[Union[dict, "Contribution"]]]] = empty_list()
    date_authored: Optional[str] = None
    specified_by: Optional[Union[str, list[str]]] = empty_list()
    supporting_methods: Optional[Union[str, list[str]]] = empty_list()
    supporting_method_types: Optional[Union[Union[dict, "Coding"], list[Union[dict, "Coding"]]]] = empty_list()
    derived_from: Optional[Union[Union[dict, "InformationEntity"], list[Union[dict, "InformationEntity"]]]] = empty_list()
    reported_in: Optional[Union[str, list[str]]] = empty_list()
    sources: Optional[Union[str, list[str]]] = empty_list()
    information_quality: Optional[Union[dict, "Coding"]] = None
    record_metadata: Optional[Union[dict, "RecordMetadata"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.is_about, list):
            self.is_about = [self.is_about] if self.is_about is not None else []
        self.is_about = [v if isinstance(v, str) else str(v) for v in self.is_about]

        self._normalize_inlined_as_list(slot_name="contributions", slot_type=Contribution, key_name="id", keyed=False)

        if self.date_authored is not None and not isinstance(self.date_authored, str):
            self.date_authored = str(self.date_authored)

        if not isinstance(self.specified_by, list):
            self.specified_by = [self.specified_by] if self.specified_by is not None else []
        self.specified_by = [v if isinstance(v, str) else str(v) for v in self.specified_by]

        if not isinstance(self.supporting_methods, list):
            self.supporting_methods = [self.supporting_methods] if self.supporting_methods is not None else []
        self.supporting_methods = [v if isinstance(v, str) else str(v) for v in self.supporting_methods]

        if not isinstance(self.supporting_method_types, list):
            self.supporting_method_types = [self.supporting_method_types] if self.supporting_method_types is not None else []
        self.supporting_method_types = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.supporting_method_types]

        self._normalize_inlined_as_list(slot_name="derived_from", slot_type=InformationEntity, key_name="id", keyed=False)

        if not isinstance(self.reported_in, list):
            self.reported_in = [self.reported_in] if self.reported_in is not None else []
        self.reported_in = [v if isinstance(v, str) else str(v) for v in self.reported_in]

        if not isinstance(self.sources, list):
            self.sources = [self.sources] if self.sources is not None else []
        self.sources = [v if isinstance(v, str) else str(v) for v in self.sources]

        if self.information_quality is not None and not isinstance(self.information_quality, Coding):
            self.information_quality = Coding(**as_dict(self.information_quality))

        if self.record_metadata is not None and not isinstance(self.record_metadata, RecordMetadata):
            self.record_metadata = RecordMetadata(**as_dict(self.record_metadata))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Method(InformationEntity):
    """
    A set of instructions that specify how to achieve some objective.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Method"]
    class_class_curie: ClassVar[str] = "sepio-model:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Method

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    urls: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if not isinstance(self.urls, list):
            self.urls = [self.urls] if self.urls is not None else []
        self.urls = [v if isinstance(v, str) else str(v) for v in self.urls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Document(InformationEntity):
    """
    A collection of information, usually in a text-based or graphic human-readable form, intended to be read and
    understood together as a whole.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Document"]
    class_class_curie: ClassVar[str] = "sepio-model:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Document

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    title: Optional[str] = None
    urls: Optional[Union[str, list[str]]] = empty_list()
    pmid: Optional[str] = None
    doi: Optional[str] = None
    license: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.urls, list):
            self.urls = [self.urls] if self.urls is not None else []
        self.urls = [v if isinstance(v, str) else str(v) for v in self.urls]

        if self.pmid is not None and not isinstance(self.pmid, str):
            self.pmid = str(self.pmid)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataItem(InformationEntity):
    """
    An Information Entity representing an individual piece of data, generated or acquired through methods which
    reliably produce truthful information about something.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["DataItem"]
    class_class_curie: ClassVar[str] = "sepio-model:DataItem"
    class_name: ClassVar[str] = "DataItem"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.DataItem

    id: str = None
    type: str = None
    value: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    unit: Optional[Union[dict, "Coding"]] = None
    variability_measures: Optional[Union[Union[dict, "DataItem"], list[Union[dict, "DataItem"]]]] = empty_list()
    confidence_interval: Optional[Union[dict, "DataItem"]] = None
    component_data_item: Optional[Union[Union[dict, "DataItem"], list[Union[dict, "DataItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.unit is not None and not isinstance(self.unit, Coding):
            self.unit = Coding(**as_dict(self.unit))

        self._normalize_inlined_as_list(slot_name="variability_measures", slot_type=DataItem, key_name="id", keyed=False)

        if self.confidence_interval is not None and not isinstance(self.confidence_interval, DataItem):
            self.confidence_interval = DataItem(**as_dict(self.confidence_interval))

        self._normalize_inlined_as_list(slot_name="component_data_item", slot_type=DataItem, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSet(InformationEntity):
    """
    A collection of related data items or records that are organized together in a common format or structure, to
    enable their computational manipulation as a unit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["DataSet"]
    class_class_curie: ClassVar[str] = "sepio-model:DataSet"
    class_name: ClassVar[str] = "DataSet"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.DataSet

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    release_date: Optional[str] = None
    version: Optional[str] = None
    license: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Activity(Entity):
    """
    An action or set of actions performed by an agent, that occurs over a period of time. Activities may use,
    generate, modify, move, or destroy one or more entities.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Activity"]
    class_class_curie: ClassVar[str] = "sepio-model:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Activity

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    date: Optional[Union[str, XSDDate]] = None
    performed_by: Optional[Union[Union[dict, "Agent"], list[Union[dict, "Agent"]]]] = empty_list()
    specified_by: Optional[Union[Union[dict, Method], list[Union[dict, Method]]]] = empty_list()
    input: Optional[Union[Union[dict, Entity], list[Union[dict, Entity]]]] = empty_list()
    output: Optional[Union[Union[dict, Entity], list[Union[dict, Entity]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.date is not None and not isinstance(self.date, XSDDate):
            self.date = XSDDate(self.date)

        self._normalize_inlined_as_list(slot_name="performed_by", slot_type=Agent, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="specified_by", slot_type=Method, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="input", slot_type=Entity, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="output", slot_type=Entity, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Contribution(Activity):
    """
    An action or actions taken by a particular agent in the creation, modification, assessment, or deprecation of some
    entity (e.g. a Statement, Evidence Line, DataSet, Publication, etc.).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Contribution"]
    class_class_curie: ClassVar[str] = "sepio-model:Contribution"
    class_name: ClassVar[str] = "Contribution"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Contribution

    id: str = None
    type: str = None
    contributor: Optional[Union[dict, "Agent"]] = None
    activity_type: Optional[Union[Union[dict, "Coding"], list[Union[dict, "Coding"]]]] = empty_list()
    contribution_made_to: Optional[Union[dict, InformationEntity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.contributor is not None and not isinstance(self.contributor, Agent):
            self.contributor = Agent(**as_dict(self.contributor))

        if not isinstance(self.activity_type, list):
            self.activity_type = [self.activity_type] if self.activity_type is not None else []
        self.activity_type = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.activity_type]

        if self.contribution_made_to is not None and not isinstance(self.contribution_made_to, InformationEntity):
            self.contribution_made_to = InformationEntity(**as_dict(self.contribution_made_to))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agent(Entity):
    """
    An autonomous actor (person, organization, or software agent) that bears some form of responsibility for an
    activity taking place, for the existence of an entity, or for another agent's activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Agent"]
    class_class_curie: ClassVar[str] = "sepio-model:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Agent

    id: str = None
    type: str = None
    subtype: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, str):
            self.subtype = str(self.subtype)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Statement(InformationEntity):
    """
    A claim of purported truth as made by a particular agent, on a particular occasion. Statements may be used to
    simply put forth a possible fact (i.e. a 'proposition') as true, or to provide a more nuanced assessment of the
    level of confidence or evidence supporting a particular proposition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Statement"]
    class_class_curie: ClassVar[str] = "sepio-model:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Statement

    id: str = None
    type: str = None
    statement_text: Optional[str] = None
    proposition: Optional[Union[dict, "Proposition"]] = None
    subject: Optional[str] = None
    predicate: Optional[Union[dict, "Coding"]] = None
    object: Optional[str] = None
    qualifier: Optional[Union[Union[dict, "Qualifier"], list[Union[dict, "Qualifier"]]]] = empty_list()
    direction: Optional[str] = None
    strength: Optional[str] = None
    score: Optional[float] = None
    subject_classification: Optional[Union[dict, "Coding"]] = None
    has_evidence_of_types: Optional[Union[str, list[str]]] = empty_list()
    has_evidence_lines: Optional[Union[Union[dict, "EvidenceLine"], list[Union[dict, "EvidenceLine"]]]] = empty_list()
    has_evidence: Optional[Union[Union[dict, InformationEntity], list[Union[dict, InformationEntity]]]] = empty_list()
    has_evidence_from_sources: Optional[Union[Union[dict, InformationEntity], list[Union[dict, InformationEntity]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.statement_text is not None and not isinstance(self.statement_text, str):
            self.statement_text = str(self.statement_text)

        if self.proposition is not None and not isinstance(self.proposition, Proposition):
            self.proposition = Proposition(**as_dict(self.proposition))

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, Coding):
            self.predicate = Coding(**as_dict(self.predicate))

        if self.object is not None and not isinstance(self.object, str):
            self.object = str(self.object)

        self._normalize_inlined_as_list(slot_name="qualifier", slot_type=Qualifier, key_name="name", keyed=False)

        if self.direction is not None and not isinstance(self.direction, str):
            self.direction = str(self.direction)

        if self.strength is not None and not isinstance(self.strength, str):
            self.strength = str(self.strength)

        if self.score is not None and not isinstance(self.score, float):
            self.score = float(self.score)

        if self.subject_classification is not None and not isinstance(self.subject_classification, Coding):
            self.subject_classification = Coding(**as_dict(self.subject_classification))

        if not isinstance(self.has_evidence_of_types, list):
            self.has_evidence_of_types = [self.has_evidence_of_types] if self.has_evidence_of_types is not None else []
        self.has_evidence_of_types = [v if isinstance(v, str) else str(v) for v in self.has_evidence_of_types]

        self._normalize_inlined_as_list(slot_name="has_evidence_lines", slot_type=EvidenceLine, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_evidence", slot_type=InformationEntity, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_evidence_from_sources", slot_type=InformationEntity, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyResult(InformationEntity):
    """
    A collection of data items from a single study that pertain to a particular subject or experimental unit in the
    study, along with optional provenance information describing how these data items were generated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["StudyResult"]
    class_class_curie: ClassVar[str] = "sepio-model:StudyResult"
    class_name: ClassVar[str] = "StudyResult"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.StudyResult

    id: str = None
    type: str = None
    focus: Optional[str] = None
    data_items: Optional[Union[Union[dict, DataItem], list[Union[dict, DataItem]]]] = empty_list()
    interpretation: Optional[Union[dict, "Coding"]] = None
    source_data_set: Optional[Union[Union[dict, DataSet], list[Union[dict, DataSet]]]] = empty_list()
    component_result: Optional[Union[Union[dict, "StudyResult"], list[Union[dict, "StudyResult"]]]] = empty_list()
    study_group: Optional[Union[dict, "StudyGroup"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.focus is not None and not isinstance(self.focus, str):
            self.focus = str(self.focus)

        self._normalize_inlined_as_list(slot_name="data_items", slot_type=DataItem, key_name="id", keyed=False)

        if self.interpretation is not None and not isinstance(self.interpretation, Coding):
            self.interpretation = Coding(**as_dict(self.interpretation))

        self._normalize_inlined_as_list(slot_name="source_data_set", slot_type=DataSet, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="component_result", slot_type=StudyResult, key_name="id", keyed=False)

        if self.study_group is not None and not isinstance(self.study_group, StudyGroup):
            self.study_group = StudyGroup(**as_dict(self.study_group))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceLine(InformationEntity):
    """
    An independent, evidence-based argument that may support or refute the validity of a specific proposition. The
    strength and direction of this argument is based on an interpretation of one or more pieces of information as
    evidence for or against the target proposition.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["EvidenceLine"]
    class_class_curie: ClassVar[str] = "sepio-model:EvidenceLine"
    class_name: ClassVar[str] = "EvidenceLine"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.EvidenceLine

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    target_proposition: Optional[Union[dict, "Proposition"]] = None
    has_evidence_items: Optional[Union[Union[dict, InformationEntity], list[Union[dict, InformationEntity]]]] = empty_list()
    direction_of_evidence_provided: Optional[str] = None
    strength_of_evidence_provided: Optional[str] = None
    score_of_evidence_provided: Optional[float] = None
    evidence_item_sources: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.target_proposition is not None and not isinstance(self.target_proposition, Proposition):
            self.target_proposition = Proposition(**as_dict(self.target_proposition))

        self._normalize_inlined_as_list(slot_name="has_evidence_items", slot_type=InformationEntity, key_name="id", keyed=False)

        if self.direction_of_evidence_provided is not None and not isinstance(self.direction_of_evidence_provided, str):
            self.direction_of_evidence_provided = str(self.direction_of_evidence_provided)

        if self.strength_of_evidence_provided is not None and not isinstance(self.strength_of_evidence_provided, str):
            self.strength_of_evidence_provided = str(self.strength_of_evidence_provided)

        if self.score_of_evidence_provided is not None and not isinstance(self.score_of_evidence_provided, float):
            self.score_of_evidence_provided = float(self.score_of_evidence_provided)

        if not isinstance(self.evidence_item_sources, list):
            self.evidence_item_sources = [self.evidence_item_sources] if self.evidence_item_sources is not None else []
        self.evidence_item_sources = [v if isinstance(v, str) else str(v) for v in self.evidence_item_sources]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Proposition(Entity):
    """
    An abstract entity representing a possible fact that is either true or false.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Proposition"]
    class_class_curie: ClassVar[str] = "sepio-model:Proposition"
    class_name: ClassVar[str] = "Proposition"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Proposition

    id: str = None
    type: str = None
    subject: str = None
    predicate: Union[dict, "Coding"] = None
    object: str = None
    proposition_text: Optional[str] = None
    qualifier: Optional[Union[Union[dict, "Qualifier"], list[Union[dict, "Qualifier"]]]] = empty_list()
    negated: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, Coding):
            self.predicate = Coding(**as_dict(self.predicate))

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        if self.proposition_text is not None and not isinstance(self.proposition_text, str):
            self.proposition_text = str(self.proposition_text)

        self._normalize_inlined_as_list(slot_name="qualifier", slot_type=Qualifier, key_name="name", keyed=False)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyGroup(Entity):
    """
    A collection of individuals or specimens from the same taxonomic class, selected for analysis in a scientific
    study based on their exhibiting one or more common characteristics (e.g. species, race, age, gender, disease
    state, income). May be referred to as a 'cohort' or 'population' in specific research settings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["StudyGroup"]
    class_class_curie: ClassVar[str] = "sepio-model:StudyGroup"
    class_name: ClassVar[str] = "StudyGroup"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.StudyGroup

    id: str = None
    type: str = None
    member_count: Optional[int] = None
    is_subset_of: Optional[Union[Union[dict, "StudyGroup"], list[Union[dict, "StudyGroup"]]]] = empty_list()
    characteristics: Optional[Union[Union[dict, "Characteristic"], list[Union[dict, "Characteristic"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.member_count is not None and not isinstance(self.member_count, int):
            self.member_count = int(self.member_count)

        self._normalize_inlined_as_list(slot_name="is_subset_of", slot_type=StudyGroup, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="characteristics", slot_type=Characteristic, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


class Utility(YAMLRoot):
    """
    An abstract organizational class that groups classes acting as complex datatypes in the model - providing reusable
    collections of fields that can be plugged into other objects to capture sets of related information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Utility"]
    class_class_curie: ClassVar[str] = "sepio-model:Utility"
    class_name: ClassVar[str] = "Utility"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Utility


@dataclass(repr=False)
class Coding(Utility):
    """
    A structured representation of a code for a defined concept in a terminology or code system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Coding"]
    class_class_curie: ClassVar[str] = "sepio-model:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Coding

    code: Optional[str] = None
    label: Optional[str] = None
    system: Optional[str] = None
    system_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.system is not None and not isinstance(self.system, str):
            self.system = str(self.system)

        if self.system_version is not None and not isinstance(self.system_version, str):
            self.system_version = str(self.system_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Qualifier(Utility):
    """
    A key-value object used to capture additional piece of information that extends or refines the meaning of a
    Statement's core subject - predicate - object 'triple' - by providing additional detail, or constraining the
    statement to apply in a particular context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Qualifier"]
    class_class_curie: ClassVar[str] = "sepio-model:Qualifier"
    class_name: ClassVar[str] = "Qualifier"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Qualifier

    name: str = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Expression(Utility):
    """
    A structure for labels representing systematic expressions that describe an entity, as generated by formal
    nomenclatures (e.g. HGVS for genetic variants, ISCN for karyotypes, HLA nomenclature for HLA genes/alleles).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Expression"]
    class_class_curie: ClassVar[str] = "sepio-model:Expression"
    class_name: ClassVar[str] = "Expression"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Expression

    value: str = None
    system_url: Optional[Union[str, URIorCURIE]] = None
    system_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.system_url is not None and not isinstance(self.system_url, URIorCURIE):
            self.system_url = URIorCURIE(self.system_url)

        if self.system_version is not None and not isinstance(self.system_version, str):
            self.system_version = str(self.system_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Extension(Utility):
    """
    A data structure that allows custom attributes to be defined for an Entity, to capture information unique to a
    given content provider, or not currently supported by the core specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Extension"]
    class_class_curie: ClassVar[str] = "sepio-model:Extension"
    class_name: ClassVar[str] = "Extension"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Extension

    name: str = None
    value: str = None
    extension_description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.extension_description is not None and not isinstance(self.extension_description, str):
            self.extension_description = str(self.extension_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecordMetadata(Utility):
    """
    A reusable structure that encapsulates provenance metadata about a serialized data record or object in a
    particular dataset (as opposed to provenance of the real world entity this record or object represents).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["RecordMetadata"]
    class_class_curie: ClassVar[str] = "sepio-model:RecordMetadata"
    class_name: ClassVar[str] = "RecordMetadata"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.RecordMetadata

    record_identifier: Optional[str] = None
    record_version: Optional[str] = None
    derived_from_record: Optional[Union[str, list[str]]] = empty_list()
    date_record_created: Optional[str] = None
    contributions: Optional[Union[Union[dict, Contribution], list[Union[dict, Contribution]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.record_identifier is not None and not isinstance(self.record_identifier, str):
            self.record_identifier = str(self.record_identifier)

        if self.record_version is not None and not isinstance(self.record_version, str):
            self.record_version = str(self.record_version)

        if not isinstance(self.derived_from_record, list):
            self.derived_from_record = [self.derived_from_record] if self.derived_from_record is not None else []
        self.derived_from_record = [v if isinstance(v, str) else str(v) for v in self.derived_from_record]

        if self.date_record_created is not None and not isinstance(self.date_record_created, str):
            self.date_record_created = str(self.date_record_created)

        self._normalize_inlined_as_list(slot_name="contributions", slot_type=Contribution, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Characteristic(Utility):
    """
    An object holding a name-value pair used to describe a trait or role of an individual member of a StudyGroup.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO_MODEL["Characteristic"]
    class_class_curie: ClassVar[str] = "sepio-model:Characteristic"
    class_name: ClassVar[str] = "Characteristic"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Characteristic

    name: str = None
    values: Union[str, list[str]] = None
    value_operator: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.value_operator is not None and not isinstance(self.value_operator, str):
            self.value_operator = str(self.value_operator)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.entity__id = Slot(uri=SEPIO_MODEL.id, name="entity__id", curie=SEPIO_MODEL.curie('id'),
                   model_uri=SEPIO_LINKML.entity__id, domain=None, range=str)

slots.entity__identifiers = Slot(uri=SEPIO_MODEL.identifiers, name="entity__identifiers", curie=SEPIO_MODEL.curie('identifiers'),
                   model_uri=SEPIO_LINKML.entity__identifiers, domain=None, range=Optional[Union[str, list[str]]])

slots.entity__type = Slot(uri=SEPIO_MODEL.type, name="entity__type", curie=SEPIO_MODEL.curie('type'),
                   model_uri=SEPIO_LINKML.entity__type, domain=None, range=str)

slots.entity__label = Slot(uri=SEPIO_MODEL.label, name="entity__label", curie=SEPIO_MODEL.curie('label'),
                   model_uri=SEPIO_LINKML.entity__label, domain=None, range=Optional[str])

slots.entity__alternative_labels = Slot(uri=SEPIO_MODEL.alternative_labels, name="entity__alternative_labels", curie=SEPIO_MODEL.curie('alternative_labels'),
                   model_uri=SEPIO_LINKML.entity__alternative_labels, domain=None, range=Optional[Union[str, list[str]]])

slots.entity__description = Slot(uri=SEPIO_MODEL.description, name="entity__description", curie=SEPIO_MODEL.curie('description'),
                   model_uri=SEPIO_LINKML.entity__description, domain=None, range=Optional[str])

slots.entity__extensions = Slot(uri=SEPIO_MODEL.extensions, name="entity__extensions", curie=SEPIO_MODEL.curie('extensions'),
                   model_uri=SEPIO_LINKML.entity__extensions, domain=None, range=Optional[Union[Union[dict, Extension], list[Union[dict, Extension]]]])

slots.informationEntity__is_about = Slot(uri=SEPIO_MODEL.is_about, name="informationEntity__is_about", curie=SEPIO_MODEL.curie('is_about'),
                   model_uri=SEPIO_LINKML.informationEntity__is_about, domain=None, range=Optional[Union[str, list[str]]])

slots.informationEntity__contributions = Slot(uri=SEPIO_MODEL.contributions, name="informationEntity__contributions", curie=SEPIO_MODEL.curie('contributions'),
                   model_uri=SEPIO_LINKML.informationEntity__contributions, domain=None, range=Optional[Union[Union[dict, Contribution], list[Union[dict, Contribution]]]])

slots.informationEntity__date_authored = Slot(uri=SEPIO_MODEL.date_authored, name="informationEntity__date_authored", curie=SEPIO_MODEL.curie('date_authored'),
                   model_uri=SEPIO_LINKML.informationEntity__date_authored, domain=None, range=Optional[str])

slots.informationEntity__specified_by = Slot(uri=SEPIO_MODEL.specified_by, name="informationEntity__specified_by", curie=SEPIO_MODEL.curie('specified_by'),
                   model_uri=SEPIO_LINKML.informationEntity__specified_by, domain=None, range=Optional[Union[str, list[str]]])

slots.informationEntity__supporting_methods = Slot(uri=SEPIO_MODEL.supporting_methods, name="informationEntity__supporting_methods", curie=SEPIO_MODEL.curie('supporting_methods'),
                   model_uri=SEPIO_LINKML.informationEntity__supporting_methods, domain=None, range=Optional[Union[str, list[str]]])

slots.informationEntity__supporting_method_types = Slot(uri=SEPIO_MODEL.supporting_method_types, name="informationEntity__supporting_method_types", curie=SEPIO_MODEL.curie('supporting_method_types'),
                   model_uri=SEPIO_LINKML.informationEntity__supporting_method_types, domain=None, range=Optional[Union[Union[dict, Coding], list[Union[dict, Coding]]]])

slots.informationEntity__derived_from = Slot(uri=SEPIO_MODEL.derived_from, name="informationEntity__derived_from", curie=SEPIO_MODEL.curie('derived_from'),
                   model_uri=SEPIO_LINKML.informationEntity__derived_from, domain=None, range=Optional[Union[Union[dict, InformationEntity], list[Union[dict, InformationEntity]]]])

slots.informationEntity__reported_in = Slot(uri=SEPIO_MODEL.reported_in, name="informationEntity__reported_in", curie=SEPIO_MODEL.curie('reported_in'),
                   model_uri=SEPIO_LINKML.informationEntity__reported_in, domain=None, range=Optional[Union[str, list[str]]])

slots.informationEntity__sources = Slot(uri=SEPIO_MODEL.sources, name="informationEntity__sources", curie=SEPIO_MODEL.curie('sources'),
                   model_uri=SEPIO_LINKML.informationEntity__sources, domain=None, range=Optional[Union[str, list[str]]])

slots.informationEntity__information_quality = Slot(uri=SEPIO_MODEL.information_quality, name="informationEntity__information_quality", curie=SEPIO_MODEL.curie('information_quality'),
                   model_uri=SEPIO_LINKML.informationEntity__information_quality, domain=None, range=Optional[Union[dict, Coding]])

slots.informationEntity__record_metadata = Slot(uri=SEPIO_MODEL.record_metadata, name="informationEntity__record_metadata", curie=SEPIO_MODEL.curie('record_metadata'),
                   model_uri=SEPIO_LINKML.informationEntity__record_metadata, domain=None, range=Optional[Union[dict, RecordMetadata]])

slots.method__subtype = Slot(uri=SEPIO_MODEL.subtype, name="method__subtype", curie=SEPIO_MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.method__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.method__urls = Slot(uri=SEPIO_MODEL.urls, name="method__urls", curie=SEPIO_MODEL.curie('urls'),
                   model_uri=SEPIO_LINKML.method__urls, domain=None, range=Optional[Union[str, list[str]]])

slots.document__subtype = Slot(uri=SEPIO_MODEL.subtype, name="document__subtype", curie=SEPIO_MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.document__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.document__title = Slot(uri=SEPIO_MODEL.title, name="document__title", curie=SEPIO_MODEL.curie('title'),
                   model_uri=SEPIO_LINKML.document__title, domain=None, range=Optional[str])

slots.document__urls = Slot(uri=SEPIO_MODEL.urls, name="document__urls", curie=SEPIO_MODEL.curie('urls'),
                   model_uri=SEPIO_LINKML.document__urls, domain=None, range=Optional[Union[str, list[str]]])

slots.document__pmid = Slot(uri=SEPIO_MODEL.pmid, name="document__pmid", curie=SEPIO_MODEL.curie('pmid'),
                   model_uri=SEPIO_LINKML.document__pmid, domain=None, range=Optional[str])

slots.document__doi = Slot(uri=SEPIO_MODEL.doi, name="document__doi", curie=SEPIO_MODEL.curie('doi'),
                   model_uri=SEPIO_LINKML.document__doi, domain=None, range=Optional[str])

slots.document__license = Slot(uri=SEPIO_MODEL.license, name="document__license", curie=SEPIO_MODEL.curie('license'),
                   model_uri=SEPIO_LINKML.document__license, domain=None, range=Optional[str])

slots.dataItem__subtype = Slot(uri=SEPIO_MODEL.subtype, name="dataItem__subtype", curie=SEPIO_MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.dataItem__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.dataItem__value = Slot(uri=SEPIO_MODEL.value, name="dataItem__value", curie=SEPIO_MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.dataItem__value, domain=None, range=str)

slots.dataItem__unit = Slot(uri=SEPIO_MODEL.unit, name="dataItem__unit", curie=SEPIO_MODEL.curie('unit'),
                   model_uri=SEPIO_LINKML.dataItem__unit, domain=None, range=Optional[Union[dict, Coding]])

slots.dataItem__variability_measures = Slot(uri=SEPIO_MODEL.variability_measures, name="dataItem__variability_measures", curie=SEPIO_MODEL.curie('variability_measures'),
                   model_uri=SEPIO_LINKML.dataItem__variability_measures, domain=None, range=Optional[Union[Union[dict, DataItem], list[Union[dict, DataItem]]]])

slots.dataItem__confidence_interval = Slot(uri=SEPIO_MODEL.confidence_interval, name="dataItem__confidence_interval", curie=SEPIO_MODEL.curie('confidence_interval'),
                   model_uri=SEPIO_LINKML.dataItem__confidence_interval, domain=None, range=Optional[Union[dict, DataItem]])

slots.dataItem__component_data_item = Slot(uri=SEPIO_MODEL.component_data_item, name="dataItem__component_data_item", curie=SEPIO_MODEL.curie('component_data_item'),
                   model_uri=SEPIO_LINKML.dataItem__component_data_item, domain=None, range=Optional[Union[Union[dict, DataItem], list[Union[dict, DataItem]]]])

slots.dataSet__subtype = Slot(uri=SEPIO_MODEL.subtype, name="dataSet__subtype", curie=SEPIO_MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.dataSet__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.dataSet__release_date = Slot(uri=SEPIO_MODEL.release_date, name="dataSet__release_date", curie=SEPIO_MODEL.curie('release_date'),
                   model_uri=SEPIO_LINKML.dataSet__release_date, domain=None, range=Optional[str])

slots.dataSet__version = Slot(uri=SEPIO_MODEL.version, name="dataSet__version", curie=SEPIO_MODEL.curie('version'),
                   model_uri=SEPIO_LINKML.dataSet__version, domain=None, range=Optional[str])

slots.dataSet__license = Slot(uri=SEPIO_MODEL.license, name="dataSet__license", curie=SEPIO_MODEL.curie('license'),
                   model_uri=SEPIO_LINKML.dataSet__license, domain=None, range=Optional[str])

slots.activity__subtype = Slot(uri=SEPIO_MODEL.subtype, name="activity__subtype", curie=SEPIO_MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.activity__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.activity__date = Slot(uri=SEPIO_MODEL.date, name="activity__date", curie=SEPIO_MODEL.curie('date'),
                   model_uri=SEPIO_LINKML.activity__date, domain=None, range=Optional[Union[str, XSDDate]])

slots.activity__performed_by = Slot(uri=SEPIO_MODEL.performed_by, name="activity__performed_by", curie=SEPIO_MODEL.curie('performed_by'),
                   model_uri=SEPIO_LINKML.activity__performed_by, domain=None, range=Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]])

slots.activity__specified_by = Slot(uri=SEPIO_MODEL.specified_by, name="activity__specified_by", curie=SEPIO_MODEL.curie('specified_by'),
                   model_uri=SEPIO_LINKML.activity__specified_by, domain=None, range=Optional[Union[Union[dict, Method], list[Union[dict, Method]]]])

slots.activity__input = Slot(uri=SEPIO_MODEL.input, name="activity__input", curie=SEPIO_MODEL.curie('input'),
                   model_uri=SEPIO_LINKML.activity__input, domain=None, range=Optional[Union[Union[dict, Entity], list[Union[dict, Entity]]]])

slots.activity__output = Slot(uri=SEPIO_MODEL.output, name="activity__output", curie=SEPIO_MODEL.curie('output'),
                   model_uri=SEPIO_LINKML.activity__output, domain=None, range=Optional[Union[Union[dict, Entity], list[Union[dict, Entity]]]])

slots.contribution__contributor = Slot(uri=SEPIO_MODEL.contributor, name="contribution__contributor", curie=SEPIO_MODEL.curie('contributor'),
                   model_uri=SEPIO_LINKML.contribution__contributor, domain=None, range=Optional[Union[dict, Agent]])

slots.contribution__activity_type = Slot(uri=SEPIO_MODEL.activity_type, name="contribution__activity_type", curie=SEPIO_MODEL.curie('activity_type'),
                   model_uri=SEPIO_LINKML.contribution__activity_type, domain=None, range=Optional[Union[Union[dict, Coding], list[Union[dict, Coding]]]])

slots.contribution__contribution_made_to = Slot(uri=SEPIO_MODEL.contribution_made_to, name="contribution__contribution_made_to", curie=SEPIO_MODEL.curie('contribution_made_to'),
                   model_uri=SEPIO_LINKML.contribution__contribution_made_to, domain=None, range=Optional[Union[dict, InformationEntity]])

slots.agent__subtype = Slot(uri=SEPIO_MODEL.subtype, name="agent__subtype", curie=SEPIO_MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.agent__subtype, domain=None, range=Optional[str])

slots.agent__name = Slot(uri=SEPIO_MODEL.name, name="agent__name", curie=SEPIO_MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.agent__name, domain=None, range=Optional[str])

slots.statement__statement_text = Slot(uri=SEPIO_MODEL.statement_text, name="statement__statement_text", curie=SEPIO_MODEL.curie('statement_text'),
                   model_uri=SEPIO_LINKML.statement__statement_text, domain=None, range=Optional[str])

slots.statement__proposition = Slot(uri=SEPIO_MODEL.proposition, name="statement__proposition", curie=SEPIO_MODEL.curie('proposition'),
                   model_uri=SEPIO_LINKML.statement__proposition, domain=None, range=Optional[Union[dict, Proposition]])

slots.statement__subject = Slot(uri=SEPIO_MODEL.subject, name="statement__subject", curie=SEPIO_MODEL.curie('subject'),
                   model_uri=SEPIO_LINKML.statement__subject, domain=None, range=Optional[str])

slots.statement__predicate = Slot(uri=SEPIO_MODEL.predicate, name="statement__predicate", curie=SEPIO_MODEL.curie('predicate'),
                   model_uri=SEPIO_LINKML.statement__predicate, domain=None, range=Optional[Union[dict, Coding]])

slots.statement__object = Slot(uri=SEPIO_MODEL.object, name="statement__object", curie=SEPIO_MODEL.curie('object'),
                   model_uri=SEPIO_LINKML.statement__object, domain=None, range=Optional[str])

slots.statement__qualifier = Slot(uri=SEPIO_MODEL.qualifier, name="statement__qualifier", curie=SEPIO_MODEL.curie('qualifier'),
                   model_uri=SEPIO_LINKML.statement__qualifier, domain=None, range=Optional[Union[Union[dict, Qualifier], list[Union[dict, Qualifier]]]])

slots.statement__direction = Slot(uri=SEPIO_MODEL.direction, name="statement__direction", curie=SEPIO_MODEL.curie('direction'),
                   model_uri=SEPIO_LINKML.statement__direction, domain=None, range=Optional[str])

slots.statement__strength = Slot(uri=SEPIO_MODEL.strength, name="statement__strength", curie=SEPIO_MODEL.curie('strength'),
                   model_uri=SEPIO_LINKML.statement__strength, domain=None, range=Optional[str])

slots.statement__score = Slot(uri=SEPIO_MODEL.score, name="statement__score", curie=SEPIO_MODEL.curie('score'),
                   model_uri=SEPIO_LINKML.statement__score, domain=None, range=Optional[float])

slots.statement__subject_classification = Slot(uri=SEPIO_MODEL.subject_classification, name="statement__subject_classification", curie=SEPIO_MODEL.curie('subject_classification'),
                   model_uri=SEPIO_LINKML.statement__subject_classification, domain=None, range=Optional[Union[dict, Coding]])

slots.statement__has_evidence_of_types = Slot(uri=SEPIO_MODEL.has_evidence_of_types, name="statement__has_evidence_of_types", curie=SEPIO_MODEL.curie('has_evidence_of_types'),
                   model_uri=SEPIO_LINKML.statement__has_evidence_of_types, domain=None, range=Optional[Union[str, list[str]]])

slots.statement__has_evidence_lines = Slot(uri=SEPIO_MODEL.has_evidence_lines, name="statement__has_evidence_lines", curie=SEPIO_MODEL.curie('has_evidence_lines'),
                   model_uri=SEPIO_LINKML.statement__has_evidence_lines, domain=None, range=Optional[Union[Union[dict, EvidenceLine], list[Union[dict, EvidenceLine]]]])

slots.statement__has_evidence = Slot(uri=SEPIO_MODEL.has_evidence, name="statement__has_evidence", curie=SEPIO_MODEL.curie('has_evidence'),
                   model_uri=SEPIO_LINKML.statement__has_evidence, domain=None, range=Optional[Union[Union[dict, InformationEntity], list[Union[dict, InformationEntity]]]])

slots.statement__has_evidence_from_sources = Slot(uri=SEPIO_MODEL.has_evidence_from_sources, name="statement__has_evidence_from_sources", curie=SEPIO_MODEL.curie('has_evidence_from_sources'),
                   model_uri=SEPIO_LINKML.statement__has_evidence_from_sources, domain=None, range=Optional[Union[Union[dict, InformationEntity], list[Union[dict, InformationEntity]]]])

slots.studyResult__focus = Slot(uri=SEPIO_MODEL.focus, name="studyResult__focus", curie=SEPIO_MODEL.curie('focus'),
                   model_uri=SEPIO_LINKML.studyResult__focus, domain=None, range=Optional[str])

slots.studyResult__data_items = Slot(uri=SEPIO_MODEL.data_items, name="studyResult__data_items", curie=SEPIO_MODEL.curie('data_items'),
                   model_uri=SEPIO_LINKML.studyResult__data_items, domain=None, range=Optional[Union[Union[dict, DataItem], list[Union[dict, DataItem]]]])

slots.studyResult__interpretation = Slot(uri=SEPIO_MODEL.interpretation, name="studyResult__interpretation", curie=SEPIO_MODEL.curie('interpretation'),
                   model_uri=SEPIO_LINKML.studyResult__interpretation, domain=None, range=Optional[Union[dict, Coding]])

slots.studyResult__source_data_set = Slot(uri=SEPIO_MODEL.source_data_set, name="studyResult__source_data_set", curie=SEPIO_MODEL.curie('source_data_set'),
                   model_uri=SEPIO_LINKML.studyResult__source_data_set, domain=None, range=Optional[Union[Union[dict, DataSet], list[Union[dict, DataSet]]]])

slots.studyResult__component_result = Slot(uri=SEPIO_MODEL.component_result, name="studyResult__component_result", curie=SEPIO_MODEL.curie('component_result'),
                   model_uri=SEPIO_LINKML.studyResult__component_result, domain=None, range=Optional[Union[Union[dict, StudyResult], list[Union[dict, StudyResult]]]])

slots.studyResult__study_group = Slot(uri=SEPIO_MODEL.study_group, name="studyResult__study_group", curie=SEPIO_MODEL.curie('study_group'),
                   model_uri=SEPIO_LINKML.studyResult__study_group, domain=None, range=Optional[Union[dict, StudyGroup]])

slots.evidenceLine__subtype = Slot(uri=SEPIO_MODEL.subtype, name="evidenceLine__subtype", curie=SEPIO_MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.evidenceLine__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.evidenceLine__target_proposition = Slot(uri=SEPIO_MODEL.target_proposition, name="evidenceLine__target_proposition", curie=SEPIO_MODEL.curie('target_proposition'),
                   model_uri=SEPIO_LINKML.evidenceLine__target_proposition, domain=None, range=Optional[Union[dict, Proposition]])

slots.evidenceLine__has_evidence_items = Slot(uri=SEPIO_MODEL.has_evidence_items, name="evidenceLine__has_evidence_items", curie=SEPIO_MODEL.curie('has_evidence_items'),
                   model_uri=SEPIO_LINKML.evidenceLine__has_evidence_items, domain=None, range=Optional[Union[Union[dict, InformationEntity], list[Union[dict, InformationEntity]]]])

slots.evidenceLine__direction_of_evidence_provided = Slot(uri=SEPIO_MODEL.direction_of_evidence_provided, name="evidenceLine__direction_of_evidence_provided", curie=SEPIO_MODEL.curie('direction_of_evidence_provided'),
                   model_uri=SEPIO_LINKML.evidenceLine__direction_of_evidence_provided, domain=None, range=Optional[str])

slots.evidenceLine__strength_of_evidence_provided = Slot(uri=SEPIO_MODEL.strength_of_evidence_provided, name="evidenceLine__strength_of_evidence_provided", curie=SEPIO_MODEL.curie('strength_of_evidence_provided'),
                   model_uri=SEPIO_LINKML.evidenceLine__strength_of_evidence_provided, domain=None, range=Optional[str])

slots.evidenceLine__score_of_evidence_provided = Slot(uri=SEPIO_MODEL.score_of_evidence_provided, name="evidenceLine__score_of_evidence_provided", curie=SEPIO_MODEL.curie('score_of_evidence_provided'),
                   model_uri=SEPIO_LINKML.evidenceLine__score_of_evidence_provided, domain=None, range=Optional[float])

slots.evidenceLine__evidence_item_sources = Slot(uri=SEPIO_MODEL.evidence_item_sources, name="evidenceLine__evidence_item_sources", curie=SEPIO_MODEL.curie('evidence_item_sources'),
                   model_uri=SEPIO_LINKML.evidenceLine__evidence_item_sources, domain=None, range=Optional[Union[str, list[str]]])

slots.proposition__proposition_text = Slot(uri=SEPIO_MODEL.proposition_text, name="proposition__proposition_text", curie=SEPIO_MODEL.curie('proposition_text'),
                   model_uri=SEPIO_LINKML.proposition__proposition_text, domain=None, range=Optional[str])

slots.proposition__subject = Slot(uri=SEPIO_MODEL.subject, name="proposition__subject", curie=SEPIO_MODEL.curie('subject'),
                   model_uri=SEPIO_LINKML.proposition__subject, domain=None, range=str)

slots.proposition__predicate = Slot(uri=SEPIO_MODEL.predicate, name="proposition__predicate", curie=SEPIO_MODEL.curie('predicate'),
                   model_uri=SEPIO_LINKML.proposition__predicate, domain=None, range=Union[dict, Coding])

slots.proposition__object = Slot(uri=SEPIO_MODEL.object, name="proposition__object", curie=SEPIO_MODEL.curie('object'),
                   model_uri=SEPIO_LINKML.proposition__object, domain=None, range=str)

slots.proposition__qualifier = Slot(uri=SEPIO_MODEL.qualifier, name="proposition__qualifier", curie=SEPIO_MODEL.curie('qualifier'),
                   model_uri=SEPIO_LINKML.proposition__qualifier, domain=None, range=Optional[Union[Union[dict, Qualifier], list[Union[dict, Qualifier]]]])

slots.proposition__negated = Slot(uri=SEPIO_MODEL.negated, name="proposition__negated", curie=SEPIO_MODEL.curie('negated'),
                   model_uri=SEPIO_LINKML.proposition__negated, domain=None, range=Optional[Union[bool, Bool]])

slots.studyGroup__member_count = Slot(uri=SEPIO_MODEL.member_count, name="studyGroup__member_count", curie=SEPIO_MODEL.curie('member_count'),
                   model_uri=SEPIO_LINKML.studyGroup__member_count, domain=None, range=Optional[int])

slots.studyGroup__is_subset_of = Slot(uri=SEPIO_MODEL.is_subset_of, name="studyGroup__is_subset_of", curie=SEPIO_MODEL.curie('is_subset_of'),
                   model_uri=SEPIO_LINKML.studyGroup__is_subset_of, domain=None, range=Optional[Union[Union[dict, StudyGroup], list[Union[dict, StudyGroup]]]])

slots.studyGroup__characteristics = Slot(uri=SEPIO_MODEL.characteristics, name="studyGroup__characteristics", curie=SEPIO_MODEL.curie('characteristics'),
                   model_uri=SEPIO_LINKML.studyGroup__characteristics, domain=None, range=Optional[Union[Union[dict, Characteristic], list[Union[dict, Characteristic]]]])

slots.coding__code = Slot(uri=SEPIO_MODEL.code, name="coding__code", curie=SEPIO_MODEL.curie('code'),
                   model_uri=SEPIO_LINKML.coding__code, domain=None, range=Optional[str])

slots.coding__label = Slot(uri=SEPIO_MODEL.label, name="coding__label", curie=SEPIO_MODEL.curie('label'),
                   model_uri=SEPIO_LINKML.coding__label, domain=None, range=Optional[str])

slots.coding__system = Slot(uri=SEPIO_MODEL.system, name="coding__system", curie=SEPIO_MODEL.curie('system'),
                   model_uri=SEPIO_LINKML.coding__system, domain=None, range=Optional[str])

slots.coding__system_version = Slot(uri=SEPIO_MODEL.system_version, name="coding__system_version", curie=SEPIO_MODEL.curie('system_version'),
                   model_uri=SEPIO_LINKML.coding__system_version, domain=None, range=Optional[str])

slots.qualifier__name = Slot(uri=SEPIO_MODEL.name, name="qualifier__name", curie=SEPIO_MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.qualifier__name, domain=None, range=str)

slots.qualifier__value = Slot(uri=SEPIO_MODEL.value, name="qualifier__value", curie=SEPIO_MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.qualifier__value, domain=None, range=str)

slots.expression__value = Slot(uri=SEPIO_MODEL.value, name="expression__value", curie=SEPIO_MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.expression__value, domain=None, range=str)

slots.expression__system_url = Slot(uri=SEPIO_MODEL.system_url, name="expression__system_url", curie=SEPIO_MODEL.curie('system_url'),
                   model_uri=SEPIO_LINKML.expression__system_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.expression__system_version = Slot(uri=SEPIO_MODEL.system_version, name="expression__system_version", curie=SEPIO_MODEL.curie('system_version'),
                   model_uri=SEPIO_LINKML.expression__system_version, domain=None, range=Optional[str])

slots.extension__extension_description = Slot(uri=SEPIO_MODEL.extension_description, name="extension__extension_description", curie=SEPIO_MODEL.curie('extension_description'),
                   model_uri=SEPIO_LINKML.extension__extension_description, domain=None, range=Optional[str])

slots.extension__name = Slot(uri=SEPIO_MODEL.name, name="extension__name", curie=SEPIO_MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.extension__name, domain=None, range=str)

slots.extension__value = Slot(uri=SEPIO_MODEL.value, name="extension__value", curie=SEPIO_MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.extension__value, domain=None, range=str)

slots.recordMetadata__record_identifier = Slot(uri=SEPIO_MODEL.record_identifier, name="recordMetadata__record_identifier", curie=SEPIO_MODEL.curie('record_identifier'),
                   model_uri=SEPIO_LINKML.recordMetadata__record_identifier, domain=None, range=Optional[str])

slots.recordMetadata__record_version = Slot(uri=SEPIO_MODEL.record_version, name="recordMetadata__record_version", curie=SEPIO_MODEL.curie('record_version'),
                   model_uri=SEPIO_LINKML.recordMetadata__record_version, domain=None, range=Optional[str])

slots.recordMetadata__derived_from_record = Slot(uri=SEPIO_MODEL.derived_from_record, name="recordMetadata__derived_from_record", curie=SEPIO_MODEL.curie('derived_from_record'),
                   model_uri=SEPIO_LINKML.recordMetadata__derived_from_record, domain=None, range=Optional[Union[str, list[str]]])

slots.recordMetadata__date_record_created = Slot(uri=SEPIO_MODEL.date_record_created, name="recordMetadata__date_record_created", curie=SEPIO_MODEL.curie('date_record_created'),
                   model_uri=SEPIO_LINKML.recordMetadata__date_record_created, domain=None, range=Optional[str])

slots.recordMetadata__contributions = Slot(uri=SEPIO_MODEL.contributions, name="recordMetadata__contributions", curie=SEPIO_MODEL.curie('contributions'),
                   model_uri=SEPIO_LINKML.recordMetadata__contributions, domain=None, range=Optional[Union[Union[dict, Contribution], list[Union[dict, Contribution]]]])

slots.characteristic__name = Slot(uri=SEPIO_MODEL.name, name="characteristic__name", curie=SEPIO_MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.characteristic__name, domain=None, range=str)

slots.characteristic__values = Slot(uri=SEPIO_MODEL.values, name="characteristic__values", curie=SEPIO_MODEL.curie('values'),
                   model_uri=SEPIO_LINKML.characteristic__values, domain=None, range=Union[str, list[str]])

slots.characteristic__value_operator = Slot(uri=SEPIO_MODEL.value_operator, name="characteristic__value_operator", curie=SEPIO_MODEL.curie('value_operator'),
                   model_uri=SEPIO_LINKML.characteristic__value_operator, domain=None, range=Optional[str])
