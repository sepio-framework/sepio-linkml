# Auto generated from sepio_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-09-13T16:54:36
# Schema: sepio-linkml
#
# id: https://w3id.org/sepio-framework/sepio-linkml
# description: LinkML-based specification of the SEPIO information model.
# license: Apache Software License 2.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Entity"]
    class_class_curie: ClassVar[str] = "sepio-model:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Entity

    id: str = None
    type: str = None
    identifiers: Optional[Union[str, List[str]]] = empty_list()
    label: Optional[str] = None
    alternativeLabels: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    extensions: Optional[Union[Union[dict, "Extension"], List[Union[dict, "Extension"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if not isinstance(self.alternativeLabels, list):
            self.alternativeLabels = [self.alternativeLabels] if self.alternativeLabels is not None else []
        self.alternativeLabels = [v if isinstance(v, str) else str(v) for v in self.alternativeLabels]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_dict(slot_name="extensions", slot_type=Extension, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationEntity(Entity):
    """
    An abstract (non-physical) entity that is about something - representing the underlying 'information content'
    conveyed by physical or digital information artifacts like books, web pages, data tables, or photographs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["InformationEntity"]
    class_class_curie: ClassVar[str] = "sepio-model:InformationEntity"
    class_name: ClassVar[str] = "InformationEntity"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.InformationEntity

    id: str = None
    type: str = None
    isAbout: Optional[Union[str, List[str]]] = empty_list()
    contributions: Optional[Union[Union[dict, "Contribution"], List[Union[dict, "Contribution"]]]] = empty_list()
    dateAuthored: Optional[str] = None
    specifiedBy: Optional[Union[str, List[str]]] = empty_list()
    methodTypes: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    derivedFrom: Optional[Union[Union[dict, "InformationEntity"], List[Union[dict, "InformationEntity"]]]] = empty_list()
    reportedIn: Optional[Union[str, List[str]]] = empty_list()
    informationQuality: Optional[Union[dict, "Coding"]] = None
    recordMetadata: Optional[Union[dict, "RecordMetadata"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.isAbout, list):
            self.isAbout = [self.isAbout] if self.isAbout is not None else []
        self.isAbout = [v if isinstance(v, str) else str(v) for v in self.isAbout]

        self._normalize_inlined_as_dict(slot_name="contributions", slot_type=Contribution, key_name="id", keyed=False)

        if self.dateAuthored is not None and not isinstance(self.dateAuthored, str):
            self.dateAuthored = str(self.dateAuthored)

        if not isinstance(self.specifiedBy, list):
            self.specifiedBy = [self.specifiedBy] if self.specifiedBy is not None else []
        self.specifiedBy = [v if isinstance(v, str) else str(v) for v in self.specifiedBy]

        if not isinstance(self.methodTypes, list):
            self.methodTypes = [self.methodTypes] if self.methodTypes is not None else []
        self.methodTypes = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.methodTypes]

        self._normalize_inlined_as_dict(slot_name="derivedFrom", slot_type=InformationEntity, key_name="id", keyed=False)

        if not isinstance(self.reportedIn, list):
            self.reportedIn = [self.reportedIn] if self.reportedIn is not None else []
        self.reportedIn = [v if isinstance(v, str) else str(v) for v in self.reportedIn]

        if self.informationQuality is not None and not isinstance(self.informationQuality, Coding):
            self.informationQuality = Coding(**as_dict(self.informationQuality))

        if self.recordMetadata is not None and not isinstance(self.recordMetadata, RecordMetadata):
            self.recordMetadata = RecordMetadata(**as_dict(self.recordMetadata))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Method(InformationEntity):
    """
    A set of instructions that specify how to achieve some objective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Method"]
    class_class_curie: ClassVar[str] = "sepio-model:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Method

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    urls: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Document"]
    class_class_curie: ClassVar[str] = "sepio-model:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Document

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    title: Optional[str] = None
    urls: Optional[Union[str, List[str]]] = empty_list()
    pmid: Optional[str] = None
    doi: Optional[str] = None
    license: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["DataItem"]
    class_class_curie: ClassVar[str] = "sepio-model:DataItem"
    class_name: ClassVar[str] = "DataItem"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.DataItem

    id: str = None
    type: str = None
    value: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    unit: Optional[Union[dict, "Coding"]] = None
    variabilityMeasures: Optional[Union[Union[dict, "DataItem"], List[Union[dict, "DataItem"]]]] = empty_list()
    confidenceInterval: Optional[Union[dict, "DataItem"]] = None
    componentDataItem: Optional[Union[Union[dict, "DataItem"], List[Union[dict, "DataItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.unit is not None and not isinstance(self.unit, Coding):
            self.unit = Coding(**as_dict(self.unit))

        self._normalize_inlined_as_dict(slot_name="variabilityMeasures", slot_type=DataItem, key_name="id", keyed=False)

        if self.confidenceInterval is not None and not isinstance(self.confidenceInterval, DataItem):
            self.confidenceInterval = DataItem(**as_dict(self.confidenceInterval))

        self._normalize_inlined_as_dict(slot_name="componentDataItem", slot_type=DataItem, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSet(InformationEntity):
    """
    A collection of related data items or records that are organized together in a common format or structure, to
    enable their computational manipulation as a unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["DataSet"]
    class_class_curie: ClassVar[str] = "sepio-model:DataSet"
    class_name: ClassVar[str] = "DataSet"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.DataSet

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    releaseDate: Optional[str] = None
    version: Optional[str] = None
    license: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.releaseDate is not None and not isinstance(self.releaseDate, str):
            self.releaseDate = str(self.releaseDate)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Activity"]
    class_class_curie: ClassVar[str] = "sepio-model:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Activity

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    date: Optional[Union[str, XSDDate]] = None
    performedBy: Optional[Union[Union[dict, "Agent"], List[Union[dict, "Agent"]]]] = empty_list()
    specifiedBy: Optional[Union[Union[dict, Method], List[Union[dict, Method]]]] = empty_list()
    input: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()
    output: Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.date is not None and not isinstance(self.date, XSDDate):
            self.date = XSDDate(self.date)

        self._normalize_inlined_as_dict(slot_name="performedBy", slot_type=Agent, key_name="id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="specifiedBy", slot_type=Method, key_name="id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="input", slot_type=Entity, key_name="id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="output", slot_type=Entity, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Contribution(Activity):
    """
    An action or actions taken by a particular agent in the creation, modification, assessment, or deprecation of some
    entity (e.g. a Statement, Evidence Line, DataSet, Publication, etc.).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Contribution"]
    class_class_curie: ClassVar[str] = "sepio-model:Contribution"
    class_name: ClassVar[str] = "Contribution"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Contribution

    id: str = None
    type: str = None
    contributor: Optional[Union[dict, "Agent"]] = None
    activityType: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    contributionMadeTo: Optional[Union[dict, InformationEntity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contributor is not None and not isinstance(self.contributor, Agent):
            self.contributor = Agent(**as_dict(self.contributor))

        if not isinstance(self.activityType, list):
            self.activityType = [self.activityType] if self.activityType is not None else []
        self.activityType = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.activityType]

        if self.contributionMadeTo is not None and not isinstance(self.contributionMadeTo, InformationEntity):
            self.contributionMadeTo = InformationEntity(**as_dict(self.contributionMadeTo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agent(Entity):
    """
    An autonomous actor (person, organization, or software agent) that bears some form of responsibility for an
    activity taking place, for the existence of an entity, or for another agent’s activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Agent"]
    class_class_curie: ClassVar[str] = "sepio-model:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Agent

    id: str = None
    type: str = None
    subtype: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Statement"]
    class_class_curie: ClassVar[str] = "sepio-model:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Statement

    id: str = None
    type: str = None
    statementText: Optional[str] = None
    proposition: Optional[Union[dict, "Proposition"]] = None
    subject: Optional[str] = None
    predicate: Optional[Union[dict, "Coding"]] = None
    object: Optional[str] = None
    qualifier: Optional[Union[Union[dict, "Qualifier"], List[Union[dict, "Qualifier"]]]] = empty_list()
    direction: Optional[str] = None
    strength: Optional[str] = None
    score: Optional[float] = None
    subjectClassification: Optional[Union[dict, "Coding"]] = None
    hasEvidenceOfTypes: Optional[Union[str, List[str]]] = empty_list()
    hasEvidenceLines: Optional[Union[Union[dict, "EvidenceLine"], List[Union[dict, "EvidenceLine"]]]] = empty_list()
    hasEvidence: Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.statementText is not None and not isinstance(self.statementText, str):
            self.statementText = str(self.statementText)

        if self.proposition is not None and not isinstance(self.proposition, Proposition):
            self.proposition = Proposition(**as_dict(self.proposition))

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, Coding):
            self.predicate = Coding(**as_dict(self.predicate))

        if self.object is not None and not isinstance(self.object, str):
            self.object = str(self.object)

        self._normalize_inlined_as_dict(slot_name="qualifier", slot_type=Qualifier, key_name="name", keyed=False)

        if self.direction is not None and not isinstance(self.direction, str):
            self.direction = str(self.direction)

        if self.strength is not None and not isinstance(self.strength, str):
            self.strength = str(self.strength)

        if self.score is not None and not isinstance(self.score, float):
            self.score = float(self.score)

        if self.subjectClassification is not None and not isinstance(self.subjectClassification, Coding):
            self.subjectClassification = Coding(**as_dict(self.subjectClassification))

        if not isinstance(self.hasEvidenceOfTypes, list):
            self.hasEvidenceOfTypes = [self.hasEvidenceOfTypes] if self.hasEvidenceOfTypes is not None else []
        self.hasEvidenceOfTypes = [v if isinstance(v, str) else str(v) for v in self.hasEvidenceOfTypes]

        self._normalize_inlined_as_dict(slot_name="hasEvidenceLines", slot_type=EvidenceLine, key_name="id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="hasEvidence", slot_type=InformationEntity, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyResult(InformationEntity):
    """
    A collection of data items from a single study that pertain to a particular subject or experimental unit in the
    study, along with optional provenance information describing how these data items were generated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["StudyResult"]
    class_class_curie: ClassVar[str] = "sepio-model:StudyResult"
    class_name: ClassVar[str] = "StudyResult"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.StudyResult

    id: str = None
    type: str = None
    focus: Optional[str] = None
    dataItems: Optional[Union[Union[dict, DataItem], List[Union[dict, DataItem]]]] = empty_list()
    interpretation: Optional[Union[dict, "Coding"]] = None
    sourceDataSet: Optional[Union[Union[dict, DataSet], List[Union[dict, DataSet]]]] = empty_list()
    componentResult: Optional[Union[Union[dict, "StudyResult"], List[Union[dict, "StudyResult"]]]] = empty_list()
    studyGroup: Optional[Union[dict, "StudyGroup"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.focus is not None and not isinstance(self.focus, str):
            self.focus = str(self.focus)

        self._normalize_inlined_as_dict(slot_name="dataItems", slot_type=DataItem, key_name="id", keyed=False)

        if self.interpretation is not None and not isinstance(self.interpretation, Coding):
            self.interpretation = Coding(**as_dict(self.interpretation))

        self._normalize_inlined_as_dict(slot_name="sourceDataSet", slot_type=DataSet, key_name="id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="componentResult", slot_type=StudyResult, key_name="id", keyed=False)

        if self.studyGroup is not None and not isinstance(self.studyGroup, StudyGroup):
            self.studyGroup = StudyGroup(**as_dict(self.studyGroup))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceLine(InformationEntity):
    """
    An independent, evidence-based argument that may support or refute the validity of a specific proposition. The
    strength and direction of this argument is based on an interpretation of one or more pieces of information as
    evidence for or against the target proposition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["EvidenceLine"]
    class_class_curie: ClassVar[str] = "sepio-model:EvidenceLine"
    class_name: ClassVar[str] = "EvidenceLine"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.EvidenceLine

    id: str = None
    type: str = None
    subtype: Optional[Union[dict, "Coding"]] = None
    targetProposition: Optional[Union[dict, "Proposition"]] = None
    hasEvidenceItems: Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]] = empty_list()
    directionOfEvidenceProvided: Optional[str] = None
    strengthOfEvidenceProvided: Optional[str] = None
    scoreOfEvidenceProvided: Optional[float] = None
    evidenceItemSources: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subtype is not None and not isinstance(self.subtype, Coding):
            self.subtype = Coding(**as_dict(self.subtype))

        if self.targetProposition is not None and not isinstance(self.targetProposition, Proposition):
            self.targetProposition = Proposition(**as_dict(self.targetProposition))

        self._normalize_inlined_as_dict(slot_name="hasEvidenceItems", slot_type=InformationEntity, key_name="id", keyed=False)

        if self.directionOfEvidenceProvided is not None and not isinstance(self.directionOfEvidenceProvided, str):
            self.directionOfEvidenceProvided = str(self.directionOfEvidenceProvided)

        if self.strengthOfEvidenceProvided is not None and not isinstance(self.strengthOfEvidenceProvided, str):
            self.strengthOfEvidenceProvided = str(self.strengthOfEvidenceProvided)

        if self.scoreOfEvidenceProvided is not None and not isinstance(self.scoreOfEvidenceProvided, float):
            self.scoreOfEvidenceProvided = float(self.scoreOfEvidenceProvided)

        if not isinstance(self.evidenceItemSources, list):
            self.evidenceItemSources = [self.evidenceItemSources] if self.evidenceItemSources is not None else []
        self.evidenceItemSources = [v if isinstance(v, str) else str(v) for v in self.evidenceItemSources]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Proposition(Entity):
    """
    An abstract entity representing a possible fact that is either true or false.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Proposition"]
    class_class_curie: ClassVar[str] = "sepio-model:Proposition"
    class_name: ClassVar[str] = "Proposition"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Proposition

    id: str = None
    type: str = None
    subject: str = None
    predicate: Union[dict, "Coding"] = None
    object: str = None
    propositionText: Optional[str] = None
    qualifier: Optional[Union[Union[dict, "Qualifier"], List[Union[dict, "Qualifier"]]]] = empty_list()
    negated: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.propositionText is not None and not isinstance(self.propositionText, str):
            self.propositionText = str(self.propositionText)

        self._normalize_inlined_as_dict(slot_name="qualifier", slot_type=Qualifier, key_name="name", keyed=False)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["StudyGroup"]
    class_class_curie: ClassVar[str] = "sepio-model:StudyGroup"
    class_name: ClassVar[str] = "StudyGroup"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.StudyGroup

    id: str = None
    type: str = None
    memberCount: Optional[int] = None
    isSubsetOf: Optional[Union[Union[dict, "StudyGroup"], List[Union[dict, "StudyGroup"]]]] = empty_list()
    characteristics: Optional[Union[Union[dict, "Characteristic"], List[Union[dict, "Characteristic"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.memberCount is not None and not isinstance(self.memberCount, int):
            self.memberCount = int(self.memberCount)

        self._normalize_inlined_as_dict(slot_name="isSubsetOf", slot_type=StudyGroup, key_name="id", keyed=False)

        self._normalize_inlined_as_dict(slot_name="characteristics", slot_type=Characteristic, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


class Utility(YAMLRoot):
    """
    An abstract organizational class that groups classes acting as complex datatypes in the model - providing reusable
    collections of fields that can be plugged into other objects to capture sets of related information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Utility"]
    class_class_curie: ClassVar[str] = "sepio-model:Utility"
    class_name: ClassVar[str] = "Utility"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Utility


@dataclass(repr=False)
class Coding(Utility):
    """
    A structured representation of a code for a defined concept in a terminology or code system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Coding"]
    class_class_curie: ClassVar[str] = "sepio-model:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Coding

    code: Optional[str] = None
    label: Optional[str] = None
    system: Optional[str] = None
    systemVersion: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.system is not None and not isinstance(self.system, str):
            self.system = str(self.system)

        if self.systemVersion is not None and not isinstance(self.systemVersion, str):
            self.systemVersion = str(self.systemVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Qualifier(Utility):
    """
    A key-value object used to capture additional piece of information that extends or refines the meaning of a
    Statement's core subject - predicate - object 'triple' - by providing additional detail, or constraining the
    statement to apply in a particular context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Qualifier"]
    class_class_curie: ClassVar[str] = "sepio-model:Qualifier"
    class_name: ClassVar[str] = "Qualifier"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Qualifier

    name: str = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Expression"]
    class_class_curie: ClassVar[str] = "sepio-model:Expression"
    class_name: ClassVar[str] = "Expression"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Expression

    value: str = None
    systemURL: Optional[Union[str, URIorCURIE]] = None
    systemVersion: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.systemURL is not None and not isinstance(self.systemURL, URIorCURIE):
            self.systemURL = URIorCURIE(self.systemURL)

        if self.systemVersion is not None and not isinstance(self.systemVersion, str):
            self.systemVersion = str(self.systemVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Extension(Utility):
    """
    A data structure that allows custom attributes to be defined for an Entity, to capture information unique to a
    given content provider, or not currently supported by the core specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Extension"]
    class_class_curie: ClassVar[str] = "sepio-model:Extension"
    class_name: ClassVar[str] = "Extension"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Extension

    name: str = None
    value: str = None
    extensionDescription: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.extensionDescription is not None and not isinstance(self.extensionDescription, str):
            self.extensionDescription = str(self.extensionDescription)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecordMetadata(Utility):
    """
    A reusable structure that encapsulates provenance metadata about a serialized data record or object in a
    particular dataset (as opposed to provenance of the real world entity this record or object represents).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["RecordMetadata"]
    class_class_curie: ClassVar[str] = "sepio-model:RecordMetadata"
    class_name: ClassVar[str] = "RecordMetadata"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.RecordMetadata

    recordIdentifier: Optional[str] = None
    recordVersion: Optional[str] = None
    derivedFromRecord: Optional[Union[str, List[str]]] = empty_list()
    dateRecordCreated: Optional[str] = None
    contributions: Optional[Union[Union[dict, Contribution], List[Union[dict, Contribution]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.recordIdentifier is not None and not isinstance(self.recordIdentifier, str):
            self.recordIdentifier = str(self.recordIdentifier)

        if self.recordVersion is not None and not isinstance(self.recordVersion, str):
            self.recordVersion = str(self.recordVersion)

        if not isinstance(self.derivedFromRecord, list):
            self.derivedFromRecord = [self.derivedFromRecord] if self.derivedFromRecord is not None else []
        self.derivedFromRecord = [v if isinstance(v, str) else str(v) for v in self.derivedFromRecord]

        if self.dateRecordCreated is not None and not isinstance(self.dateRecordCreated, str):
            self.dateRecordCreated = str(self.dateRecordCreated)

        self._normalize_inlined_as_dict(slot_name="contributions", slot_type=Contribution, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Characteristic(Utility):
    """
    An object holding a name-value pair used to describe a trait or role of an individual member of a StudyGroup.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-MODEL["Characteristic"]
    class_class_curie: ClassVar[str] = "sepio-model:Characteristic"
    class_name: ClassVar[str] = "Characteristic"
    class_model_uri: ClassVar[URIRef] = SEPIO_LINKML.Characteristic

    name: str = None
    values: Union[str, List[str]] = None
    valueOperator: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.values):
            self.MissingRequiredField("values")
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        if self.valueOperator is not None and not isinstance(self.valueOperator, str):
            self.valueOperator = str(self.valueOperator)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SEPIO-MODEL.id, name="id", curie=SEPIO-MODEL.curie('id'),
                   model_uri=SEPIO_LINKML.id, domain=None, range=Optional[str])

slots.identifiers = Slot(uri=SEPIO-MODEL.identifiers, name="identifiers", curie=SEPIO-MODEL.curie('identifiers'),
                   model_uri=SEPIO_LINKML.identifiers, domain=None, range=Optional[str])

slots.type = Slot(uri=SEPIO-MODEL.type, name="type", curie=SEPIO-MODEL.curie('type'),
                   model_uri=SEPIO_LINKML.type, domain=None, range=Optional[str])

slots.label = Slot(uri=SEPIO-MODEL.label, name="label", curie=SEPIO-MODEL.curie('label'),
                   model_uri=SEPIO_LINKML.label, domain=None, range=Optional[str])

slots.alternativeLabels = Slot(uri=SEPIO-MODEL.alternativeLabels, name="alternativeLabels", curie=SEPIO-MODEL.curie('alternativeLabels'),
                   model_uri=SEPIO_LINKML.alternativeLabels, domain=None, range=Optional[str])

slots.description = Slot(uri=SEPIO-MODEL.description, name="description", curie=SEPIO-MODEL.curie('description'),
                   model_uri=SEPIO_LINKML.description, domain=None, range=Optional[str])

slots.extensions = Slot(uri=SEPIO-MODEL.extensions, name="extensions", curie=SEPIO-MODEL.curie('extensions'),
                   model_uri=SEPIO_LINKML.extensions, domain=None, range=Optional[str])

slots.isAbout = Slot(uri=SEPIO-MODEL.isAbout, name="isAbout", curie=SEPIO-MODEL.curie('isAbout'),
                   model_uri=SEPIO_LINKML.isAbout, domain=None, range=Optional[str])

slots.contributions = Slot(uri=SEPIO-MODEL.contributions, name="contributions", curie=SEPIO-MODEL.curie('contributions'),
                   model_uri=SEPIO_LINKML.contributions, domain=None, range=Optional[str])

slots.dateAuthored = Slot(uri=SEPIO-MODEL.dateAuthored, name="dateAuthored", curie=SEPIO-MODEL.curie('dateAuthored'),
                   model_uri=SEPIO_LINKML.dateAuthored, domain=None, range=Optional[str])

slots.specifiedBy = Slot(uri=SEPIO-MODEL.specifiedBy, name="specifiedBy", curie=SEPIO-MODEL.curie('specifiedBy'),
                   model_uri=SEPIO_LINKML.specifiedBy, domain=None, range=Optional[str])

slots.methodTypes = Slot(uri=SEPIO-MODEL.methodTypes, name="methodTypes", curie=SEPIO-MODEL.curie('methodTypes'),
                   model_uri=SEPIO_LINKML.methodTypes, domain=None, range=Optional[str])

slots.derivedFrom = Slot(uri=SEPIO-MODEL.derivedFrom, name="derivedFrom", curie=SEPIO-MODEL.curie('derivedFrom'),
                   model_uri=SEPIO_LINKML.derivedFrom, domain=None, range=Optional[str])

slots.reportedIn = Slot(uri=SEPIO-MODEL.reportedIn, name="reportedIn", curie=SEPIO-MODEL.curie('reportedIn'),
                   model_uri=SEPIO_LINKML.reportedIn, domain=None, range=Optional[str])

slots.informationQuality = Slot(uri=SEPIO-MODEL.informationQuality, name="informationQuality", curie=SEPIO-MODEL.curie('informationQuality'),
                   model_uri=SEPIO_LINKML.informationQuality, domain=None, range=Optional[str])

slots.recordMetadata = Slot(uri=SEPIO-MODEL.recordMetadata, name="recordMetadata", curie=SEPIO-MODEL.curie('recordMetadata'),
                   model_uri=SEPIO_LINKML.recordMetadata, domain=None, range=Optional[str])

slots.subtype = Slot(uri=SEPIO-MODEL.subtype, name="subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.subtype, domain=None, range=Optional[str])

slots.urls = Slot(uri=SEPIO-MODEL.urls, name="urls", curie=SEPIO-MODEL.curie('urls'),
                   model_uri=SEPIO_LINKML.urls, domain=None, range=Optional[str])

slots.title = Slot(uri=SEPIO-MODEL.title, name="title", curie=SEPIO-MODEL.curie('title'),
                   model_uri=SEPIO_LINKML.title, domain=None, range=Optional[str])

slots.pmid = Slot(uri=SEPIO-MODEL.pmid, name="pmid", curie=SEPIO-MODEL.curie('pmid'),
                   model_uri=SEPIO_LINKML.pmid, domain=None, range=Optional[str])

slots.doi = Slot(uri=SEPIO-MODEL.doi, name="doi", curie=SEPIO-MODEL.curie('doi'),
                   model_uri=SEPIO_LINKML.doi, domain=None, range=Optional[str])

slots.license = Slot(uri=SEPIO-MODEL.license, name="license", curie=SEPIO-MODEL.curie('license'),
                   model_uri=SEPIO_LINKML.license, domain=None, range=Optional[str])

slots.value = Slot(uri=SEPIO-MODEL.value, name="value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.value, domain=None, range=Optional[str])

slots.unit = Slot(uri=SEPIO-MODEL.unit, name="unit", curie=SEPIO-MODEL.curie('unit'),
                   model_uri=SEPIO_LINKML.unit, domain=None, range=Optional[str])

slots.variabilityMeasures = Slot(uri=SEPIO-MODEL.variabilityMeasures, name="variabilityMeasures", curie=SEPIO-MODEL.curie('variabilityMeasures'),
                   model_uri=SEPIO_LINKML.variabilityMeasures, domain=None, range=Optional[str])

slots.confidenceInterval = Slot(uri=SEPIO-MODEL.confidenceInterval, name="confidenceInterval", curie=SEPIO-MODEL.curie('confidenceInterval'),
                   model_uri=SEPIO_LINKML.confidenceInterval, domain=None, range=Optional[str])

slots.componentDataItem = Slot(uri=SEPIO-MODEL.componentDataItem, name="componentDataItem", curie=SEPIO-MODEL.curie('componentDataItem'),
                   model_uri=SEPIO_LINKML.componentDataItem, domain=None, range=Optional[str])

slots.releaseDate = Slot(uri=SEPIO-MODEL.releaseDate, name="releaseDate", curie=SEPIO-MODEL.curie('releaseDate'),
                   model_uri=SEPIO_LINKML.releaseDate, domain=None, range=Optional[str])

slots.version = Slot(uri=SEPIO-MODEL.version, name="version", curie=SEPIO-MODEL.curie('version'),
                   model_uri=SEPIO_LINKML.version, domain=None, range=Optional[str])

slots.date = Slot(uri=SEPIO-MODEL.date, name="date", curie=SEPIO-MODEL.curie('date'),
                   model_uri=SEPIO_LINKML.date, domain=None, range=Optional[str])

slots.performedBy = Slot(uri=SEPIO-MODEL.performedBy, name="performedBy", curie=SEPIO-MODEL.curie('performedBy'),
                   model_uri=SEPIO_LINKML.performedBy, domain=None, range=Optional[str])

slots.input = Slot(uri=SEPIO-MODEL.input, name="input", curie=SEPIO-MODEL.curie('input'),
                   model_uri=SEPIO_LINKML.input, domain=None, range=Optional[str])

slots.output = Slot(uri=SEPIO-MODEL.output, name="output", curie=SEPIO-MODEL.curie('output'),
                   model_uri=SEPIO_LINKML.output, domain=None, range=Optional[str])

slots.contributor = Slot(uri=SEPIO-MODEL.contributor, name="contributor", curie=SEPIO-MODEL.curie('contributor'),
                   model_uri=SEPIO_LINKML.contributor, domain=None, range=Optional[str])

slots.activityType = Slot(uri=SEPIO-MODEL.activityType, name="activityType", curie=SEPIO-MODEL.curie('activityType'),
                   model_uri=SEPIO_LINKML.activityType, domain=None, range=Optional[str])

slots.contributionMadeTo = Slot(uri=SEPIO-MODEL.contributionMadeTo, name="contributionMadeTo", curie=SEPIO-MODEL.curie('contributionMadeTo'),
                   model_uri=SEPIO_LINKML.contributionMadeTo, domain=None, range=Optional[str])

slots.name = Slot(uri=SEPIO-MODEL.name, name="name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.name, domain=None, range=Optional[str])

slots.statementText = Slot(uri=SEPIO-MODEL.statementText, name="statementText", curie=SEPIO-MODEL.curie('statementText'),
                   model_uri=SEPIO_LINKML.statementText, domain=None, range=Optional[str])

slots.proposition = Slot(uri=SEPIO-MODEL.proposition, name="proposition", curie=SEPIO-MODEL.curie('proposition'),
                   model_uri=SEPIO_LINKML.proposition, domain=None, range=Optional[str])

slots.subject = Slot(uri=SEPIO-MODEL.subject, name="subject", curie=SEPIO-MODEL.curie('subject'),
                   model_uri=SEPIO_LINKML.subject, domain=None, range=Optional[str])

slots.predicate = Slot(uri=SEPIO-MODEL.predicate, name="predicate", curie=SEPIO-MODEL.curie('predicate'),
                   model_uri=SEPIO_LINKML.predicate, domain=None, range=Optional[str])

slots.object = Slot(uri=SEPIO-MODEL.object, name="object", curie=SEPIO-MODEL.curie('object'),
                   model_uri=SEPIO_LINKML.object, domain=None, range=Optional[str])

slots.qualifier = Slot(uri=SEPIO-MODEL.qualifier, name="qualifier", curie=SEPIO-MODEL.curie('qualifier'),
                   model_uri=SEPIO_LINKML.qualifier, domain=None, range=Optional[str])

slots.direction = Slot(uri=SEPIO-MODEL.direction, name="direction", curie=SEPIO-MODEL.curie('direction'),
                   model_uri=SEPIO_LINKML.direction, domain=None, range=Optional[str])

slots.strength = Slot(uri=SEPIO-MODEL.strength, name="strength", curie=SEPIO-MODEL.curie('strength'),
                   model_uri=SEPIO_LINKML.strength, domain=None, range=Optional[str])

slots.score = Slot(uri=SEPIO-MODEL.score, name="score", curie=SEPIO-MODEL.curie('score'),
                   model_uri=SEPIO_LINKML.score, domain=None, range=Optional[str])

slots.subjectClassification = Slot(uri=SEPIO-MODEL.subjectClassification, name="subjectClassification", curie=SEPIO-MODEL.curie('subjectClassification'),
                   model_uri=SEPIO_LINKML.subjectClassification, domain=None, range=Optional[str])

slots.hasEvidenceOfTypes = Slot(uri=SEPIO-MODEL.hasEvidenceOfTypes, name="hasEvidenceOfTypes", curie=SEPIO-MODEL.curie('hasEvidenceOfTypes'),
                   model_uri=SEPIO_LINKML.hasEvidenceOfTypes, domain=None, range=Optional[str])

slots.hasEvidenceLines = Slot(uri=SEPIO-MODEL.hasEvidenceLines, name="hasEvidenceLines", curie=SEPIO-MODEL.curie('hasEvidenceLines'),
                   model_uri=SEPIO_LINKML.hasEvidenceLines, domain=None, range=Optional[str])

slots.hasEvidence = Slot(uri=SEPIO-MODEL.hasEvidence, name="hasEvidence", curie=SEPIO-MODEL.curie('hasEvidence'),
                   model_uri=SEPIO_LINKML.hasEvidence, domain=None, range=Optional[str])

slots.focus = Slot(uri=SEPIO-MODEL.focus, name="focus", curie=SEPIO-MODEL.curie('focus'),
                   model_uri=SEPIO_LINKML.focus, domain=None, range=Optional[str])

slots.dataItems = Slot(uri=SEPIO-MODEL.dataItems, name="dataItems", curie=SEPIO-MODEL.curie('dataItems'),
                   model_uri=SEPIO_LINKML.dataItems, domain=None, range=Optional[str])

slots.interpretation = Slot(uri=SEPIO-MODEL.interpretation, name="interpretation", curie=SEPIO-MODEL.curie('interpretation'),
                   model_uri=SEPIO_LINKML.interpretation, domain=None, range=Optional[str])

slots.sourceDataSet = Slot(uri=SEPIO-MODEL.sourceDataSet, name="sourceDataSet", curie=SEPIO-MODEL.curie('sourceDataSet'),
                   model_uri=SEPIO_LINKML.sourceDataSet, domain=None, range=Optional[str])

slots.componentResult = Slot(uri=SEPIO-MODEL.componentResult, name="componentResult", curie=SEPIO-MODEL.curie('componentResult'),
                   model_uri=SEPIO_LINKML.componentResult, domain=None, range=Optional[str])

slots.studyGroup = Slot(uri=SEPIO-MODEL.studyGroup, name="studyGroup", curie=SEPIO-MODEL.curie('studyGroup'),
                   model_uri=SEPIO_LINKML.studyGroup, domain=None, range=Optional[str])

slots.targetProposition = Slot(uri=SEPIO-MODEL.targetProposition, name="targetProposition", curie=SEPIO-MODEL.curie('targetProposition'),
                   model_uri=SEPIO_LINKML.targetProposition, domain=None, range=Optional[str])

slots.hasEvidenceItems = Slot(uri=SEPIO-MODEL.hasEvidenceItems, name="hasEvidenceItems", curie=SEPIO-MODEL.curie('hasEvidenceItems'),
                   model_uri=SEPIO_LINKML.hasEvidenceItems, domain=None, range=Optional[str])

slots.directionOfEvidenceProvided = Slot(uri=SEPIO-MODEL.directionOfEvidenceProvided, name="directionOfEvidenceProvided", curie=SEPIO-MODEL.curie('directionOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.directionOfEvidenceProvided, domain=None, range=Optional[str])

slots.strengthOfEvidenceProvided = Slot(uri=SEPIO-MODEL.strengthOfEvidenceProvided, name="strengthOfEvidenceProvided", curie=SEPIO-MODEL.curie('strengthOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.strengthOfEvidenceProvided, domain=None, range=Optional[str])

slots.scoreOfEvidenceProvided = Slot(uri=SEPIO-MODEL.scoreOfEvidenceProvided, name="scoreOfEvidenceProvided", curie=SEPIO-MODEL.curie('scoreOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.scoreOfEvidenceProvided, domain=None, range=Optional[str])

slots.evidenceItemSources = Slot(uri=SEPIO-MODEL.evidenceItemSources, name="evidenceItemSources", curie=SEPIO-MODEL.curie('evidenceItemSources'),
                   model_uri=SEPIO_LINKML.evidenceItemSources, domain=None, range=Optional[str])

slots.propositionText = Slot(uri=SEPIO-MODEL.propositionText, name="propositionText", curie=SEPIO-MODEL.curie('propositionText'),
                   model_uri=SEPIO_LINKML.propositionText, domain=None, range=Optional[str])

slots.negated = Slot(uri=SEPIO-MODEL.negated, name="negated", curie=SEPIO-MODEL.curie('negated'),
                   model_uri=SEPIO_LINKML.negated, domain=None, range=Optional[str])

slots.memberCount = Slot(uri=SEPIO-MODEL.memberCount, name="memberCount", curie=SEPIO-MODEL.curie('memberCount'),
                   model_uri=SEPIO_LINKML.memberCount, domain=None, range=Optional[str])

slots.isSubsetOf = Slot(uri=SEPIO-MODEL.isSubsetOf, name="isSubsetOf", curie=SEPIO-MODEL.curie('isSubsetOf'),
                   model_uri=SEPIO_LINKML.isSubsetOf, domain=None, range=Optional[str])

slots.characteristics = Slot(uri=SEPIO-MODEL.characteristics, name="characteristics", curie=SEPIO-MODEL.curie('characteristics'),
                   model_uri=SEPIO_LINKML.characteristics, domain=None, range=Optional[str])

slots.code = Slot(uri=SEPIO-MODEL.code, name="code", curie=SEPIO-MODEL.curie('code'),
                   model_uri=SEPIO_LINKML.code, domain=None, range=Optional[str])

slots.system = Slot(uri=SEPIO-MODEL.system, name="system", curie=SEPIO-MODEL.curie('system'),
                   model_uri=SEPIO_LINKML.system, domain=None, range=Optional[str])

slots.systemVersion = Slot(uri=SEPIO-MODEL.systemVersion, name="systemVersion", curie=SEPIO-MODEL.curie('systemVersion'),
                   model_uri=SEPIO_LINKML.systemVersion, domain=None, range=Optional[str])

slots.systemURL = Slot(uri=SEPIO-MODEL.systemURL, name="systemURL", curie=SEPIO-MODEL.curie('systemURL'),
                   model_uri=SEPIO_LINKML.systemURL, domain=None, range=Optional[str])

slots.extensionDescription = Slot(uri=SEPIO-MODEL.extensionDescription, name="extensionDescription", curie=SEPIO-MODEL.curie('extensionDescription'),
                   model_uri=SEPIO_LINKML.extensionDescription, domain=None, range=Optional[str])

slots.recordIdentifier = Slot(uri=SEPIO-MODEL.recordIdentifier, name="recordIdentifier", curie=SEPIO-MODEL.curie('recordIdentifier'),
                   model_uri=SEPIO_LINKML.recordIdentifier, domain=None, range=Optional[str])

slots.recordVersion = Slot(uri=SEPIO-MODEL.recordVersion, name="recordVersion", curie=SEPIO-MODEL.curie('recordVersion'),
                   model_uri=SEPIO_LINKML.recordVersion, domain=None, range=Optional[str])

slots.derivedFromRecord = Slot(uri=SEPIO-MODEL.derivedFromRecord, name="derivedFromRecord", curie=SEPIO-MODEL.curie('derivedFromRecord'),
                   model_uri=SEPIO_LINKML.derivedFromRecord, domain=None, range=Optional[str])

slots.dateRecordCreated = Slot(uri=SEPIO-MODEL.dateRecordCreated, name="dateRecordCreated", curie=SEPIO-MODEL.curie('dateRecordCreated'),
                   model_uri=SEPIO_LINKML.dateRecordCreated, domain=None, range=Optional[str])

slots.values = Slot(uri=SEPIO-MODEL.values, name="values", curie=SEPIO-MODEL.curie('values'),
                   model_uri=SEPIO_LINKML.values, domain=None, range=Optional[str])

slots.valueOperator = Slot(uri=SEPIO-MODEL.valueOperator, name="valueOperator", curie=SEPIO-MODEL.curie('valueOperator'),
                   model_uri=SEPIO_LINKML.valueOperator, domain=None, range=Optional[str])

slots.Entity_id = Slot(uri=SEPIO-MODEL.id, name="Entity_id", curie=SEPIO-MODEL.curie('id'),
                   model_uri=SEPIO_LINKML.Entity_id, domain=Entity, range=str)

slots.Entity_identifiers = Slot(uri=SEPIO-MODEL.identifiers, name="Entity_identifiers", curie=SEPIO-MODEL.curie('identifiers'),
                   model_uri=SEPIO_LINKML.Entity_identifiers, domain=Entity, range=Optional[Union[str, List[str]]])

slots.Entity_type = Slot(uri=SEPIO-MODEL.type, name="Entity_type", curie=SEPIO-MODEL.curie('type'),
                   model_uri=SEPIO_LINKML.Entity_type, domain=Entity, range=str)

slots.Entity_label = Slot(uri=SEPIO-MODEL.label, name="Entity_label", curie=SEPIO-MODEL.curie('label'),
                   model_uri=SEPIO_LINKML.Entity_label, domain=Entity, range=Optional[str])

slots.Entity_alternativeLabels = Slot(uri=SEPIO-MODEL.alternativeLabels, name="Entity_alternativeLabels", curie=SEPIO-MODEL.curie('alternativeLabels'),
                   model_uri=SEPIO_LINKML.Entity_alternativeLabels, domain=Entity, range=Optional[Union[str, List[str]]])

slots.Entity_description = Slot(uri=SEPIO-MODEL.description, name="Entity_description", curie=SEPIO-MODEL.curie('description'),
                   model_uri=SEPIO_LINKML.Entity_description, domain=Entity, range=Optional[str])

slots.Entity_extensions = Slot(uri=SEPIO-MODEL.extensions, name="Entity_extensions", curie=SEPIO-MODEL.curie('extensions'),
                   model_uri=SEPIO_LINKML.Entity_extensions, domain=Entity, range=Optional[Union[Union[dict, "Extension"], List[Union[dict, "Extension"]]]])

slots.InformationEntity_isAbout = Slot(uri=SEPIO-MODEL.isAbout, name="InformationEntity_isAbout", curie=SEPIO-MODEL.curie('isAbout'),
                   model_uri=SEPIO_LINKML.InformationEntity_isAbout, domain=InformationEntity, range=Optional[Union[str, List[str]]])

slots.InformationEntity_contributions = Slot(uri=SEPIO-MODEL.contributions, name="InformationEntity_contributions", curie=SEPIO-MODEL.curie('contributions'),
                   model_uri=SEPIO_LINKML.InformationEntity_contributions, domain=InformationEntity, range=Optional[Union[Union[dict, "Contribution"], List[Union[dict, "Contribution"]]]])

slots.InformationEntity_dateAuthored = Slot(uri=SEPIO-MODEL.dateAuthored, name="InformationEntity_dateAuthored", curie=SEPIO-MODEL.curie('dateAuthored'),
                   model_uri=SEPIO_LINKML.InformationEntity_dateAuthored, domain=InformationEntity, range=Optional[str])

slots.InformationEntity_specifiedBy = Slot(uri=SEPIO-MODEL.specifiedBy, name="InformationEntity_specifiedBy", curie=SEPIO-MODEL.curie('specifiedBy'),
                   model_uri=SEPIO_LINKML.InformationEntity_specifiedBy, domain=InformationEntity, range=Optional[Union[str, List[str]]])

slots.InformationEntity_methodTypes = Slot(uri=SEPIO-MODEL.methodTypes, name="InformationEntity_methodTypes", curie=SEPIO-MODEL.curie('methodTypes'),
                   model_uri=SEPIO_LINKML.InformationEntity_methodTypes, domain=InformationEntity, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.InformationEntity_derivedFrom = Slot(uri=SEPIO-MODEL.derivedFrom, name="InformationEntity_derivedFrom", curie=SEPIO-MODEL.curie('derivedFrom'),
                   model_uri=SEPIO_LINKML.InformationEntity_derivedFrom, domain=InformationEntity, range=Optional[Union[Union[dict, "InformationEntity"], List[Union[dict, "InformationEntity"]]]])

slots.InformationEntity_reportedIn = Slot(uri=SEPIO-MODEL.reportedIn, name="InformationEntity_reportedIn", curie=SEPIO-MODEL.curie('reportedIn'),
                   model_uri=SEPIO_LINKML.InformationEntity_reportedIn, domain=InformationEntity, range=Optional[Union[str, List[str]]])

slots.InformationEntity_informationQuality = Slot(uri=SEPIO-MODEL.informationQuality, name="InformationEntity_informationQuality", curie=SEPIO-MODEL.curie('informationQuality'),
                   model_uri=SEPIO_LINKML.InformationEntity_informationQuality, domain=InformationEntity, range=Optional[Union[dict, "Coding"]])

slots.InformationEntity_recordMetadata = Slot(uri=SEPIO-MODEL.recordMetadata, name="InformationEntity_recordMetadata", curie=SEPIO-MODEL.curie('recordMetadata'),
                   model_uri=SEPIO_LINKML.InformationEntity_recordMetadata, domain=InformationEntity, range=Optional[Union[dict, "RecordMetadata"]])

slots.Method_subtype = Slot(uri=SEPIO-MODEL.subtype, name="Method_subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.Method_subtype, domain=Method, range=Optional[Union[dict, "Coding"]])

slots.Method_urls = Slot(uri=SEPIO-MODEL.urls, name="Method_urls", curie=SEPIO-MODEL.curie('urls'),
                   model_uri=SEPIO_LINKML.Method_urls, domain=Method, range=Optional[Union[str, List[str]]])

slots.Document_subtype = Slot(uri=SEPIO-MODEL.subtype, name="Document_subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.Document_subtype, domain=Document, range=Optional[Union[dict, "Coding"]])

slots.Document_title = Slot(uri=SEPIO-MODEL.title, name="Document_title", curie=SEPIO-MODEL.curie('title'),
                   model_uri=SEPIO_LINKML.Document_title, domain=Document, range=Optional[str])

slots.Document_urls = Slot(uri=SEPIO-MODEL.urls, name="Document_urls", curie=SEPIO-MODEL.curie('urls'),
                   model_uri=SEPIO_LINKML.Document_urls, domain=Document, range=Optional[Union[str, List[str]]])

slots.Document_pmid = Slot(uri=SEPIO-MODEL.pmid, name="Document_pmid", curie=SEPIO-MODEL.curie('pmid'),
                   model_uri=SEPIO_LINKML.Document_pmid, domain=Document, range=Optional[str])

slots.Document_doi = Slot(uri=SEPIO-MODEL.doi, name="Document_doi", curie=SEPIO-MODEL.curie('doi'),
                   model_uri=SEPIO_LINKML.Document_doi, domain=Document, range=Optional[str])

slots.Document_license = Slot(uri=SEPIO-MODEL.license, name="Document_license", curie=SEPIO-MODEL.curie('license'),
                   model_uri=SEPIO_LINKML.Document_license, domain=Document, range=Optional[str])

slots.DataItem_subtype = Slot(uri=SEPIO-MODEL.subtype, name="DataItem_subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.DataItem_subtype, domain=DataItem, range=Optional[Union[dict, "Coding"]])

slots.DataItem_value = Slot(uri=SEPIO-MODEL.value, name="DataItem_value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.DataItem_value, domain=DataItem, range=str)

slots.DataItem_unit = Slot(uri=SEPIO-MODEL.unit, name="DataItem_unit", curie=SEPIO-MODEL.curie('unit'),
                   model_uri=SEPIO_LINKML.DataItem_unit, domain=DataItem, range=Optional[Union[dict, "Coding"]])

slots.DataItem_variabilityMeasures = Slot(uri=SEPIO-MODEL.variabilityMeasures, name="DataItem_variabilityMeasures", curie=SEPIO-MODEL.curie('variabilityMeasures'),
                   model_uri=SEPIO_LINKML.DataItem_variabilityMeasures, domain=DataItem, range=Optional[Union[Union[dict, "DataItem"], List[Union[dict, "DataItem"]]]])

slots.DataItem_confidenceInterval = Slot(uri=SEPIO-MODEL.confidenceInterval, name="DataItem_confidenceInterval", curie=SEPIO-MODEL.curie('confidenceInterval'),
                   model_uri=SEPIO_LINKML.DataItem_confidenceInterval, domain=DataItem, range=Optional[Union[dict, "DataItem"]])

slots.DataItem_componentDataItem = Slot(uri=SEPIO-MODEL.componentDataItem, name="DataItem_componentDataItem", curie=SEPIO-MODEL.curie('componentDataItem'),
                   model_uri=SEPIO_LINKML.DataItem_componentDataItem, domain=DataItem, range=Optional[Union[Union[dict, "DataItem"], List[Union[dict, "DataItem"]]]])

slots.DataSet_subtype = Slot(uri=SEPIO-MODEL.subtype, name="DataSet_subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.DataSet_subtype, domain=DataSet, range=Optional[Union[dict, "Coding"]])

slots.DataSet_releaseDate = Slot(uri=SEPIO-MODEL.releaseDate, name="DataSet_releaseDate", curie=SEPIO-MODEL.curie('releaseDate'),
                   model_uri=SEPIO_LINKML.DataSet_releaseDate, domain=DataSet, range=Optional[str])

slots.DataSet_version = Slot(uri=SEPIO-MODEL.version, name="DataSet_version", curie=SEPIO-MODEL.curie('version'),
                   model_uri=SEPIO_LINKML.DataSet_version, domain=DataSet, range=Optional[str])

slots.DataSet_license = Slot(uri=SEPIO-MODEL.license, name="DataSet_license", curie=SEPIO-MODEL.curie('license'),
                   model_uri=SEPIO_LINKML.DataSet_license, domain=DataSet, range=Optional[str])

slots.Activity_subtype = Slot(uri=SEPIO-MODEL.subtype, name="Activity_subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.Activity_subtype, domain=Activity, range=Optional[Union[dict, "Coding"]])

slots.Activity_date = Slot(uri=SEPIO-MODEL.date, name="Activity_date", curie=SEPIO-MODEL.curie('date'),
                   model_uri=SEPIO_LINKML.Activity_date, domain=Activity, range=Optional[Union[str, XSDDate]])

slots.Activity_performedBy = Slot(uri=SEPIO-MODEL.performedBy, name="Activity_performedBy", curie=SEPIO-MODEL.curie('performedBy'),
                   model_uri=SEPIO_LINKML.Activity_performedBy, domain=Activity, range=Optional[Union[Union[dict, "Agent"], List[Union[dict, "Agent"]]]])

slots.Activity_specifiedBy = Slot(uri=SEPIO-MODEL.specifiedBy, name="Activity_specifiedBy", curie=SEPIO-MODEL.curie('specifiedBy'),
                   model_uri=SEPIO_LINKML.Activity_specifiedBy, domain=Activity, range=Optional[Union[Union[dict, Method], List[Union[dict, Method]]]])

slots.Activity_input = Slot(uri=SEPIO-MODEL.input, name="Activity_input", curie=SEPIO-MODEL.curie('input'),
                   model_uri=SEPIO_LINKML.Activity_input, domain=Activity, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.Activity_output = Slot(uri=SEPIO-MODEL.output, name="Activity_output", curie=SEPIO-MODEL.curie('output'),
                   model_uri=SEPIO_LINKML.Activity_output, domain=Activity, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.Contribution_contributor = Slot(uri=SEPIO-MODEL.contributor, name="Contribution_contributor", curie=SEPIO-MODEL.curie('contributor'),
                   model_uri=SEPIO_LINKML.Contribution_contributor, domain=Contribution, range=Optional[Union[dict, "Agent"]])

slots.Contribution_activityType = Slot(uri=SEPIO-MODEL.activityType, name="Contribution_activityType", curie=SEPIO-MODEL.curie('activityType'),
                   model_uri=SEPIO_LINKML.Contribution_activityType, domain=Contribution, range=Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]])

slots.Contribution_contributionMadeTo = Slot(uri=SEPIO-MODEL.contributionMadeTo, name="Contribution_contributionMadeTo", curie=SEPIO-MODEL.curie('contributionMadeTo'),
                   model_uri=SEPIO_LINKML.Contribution_contributionMadeTo, domain=Contribution, range=Optional[Union[dict, InformationEntity]])

slots.Agent_subtype = Slot(uri=SEPIO-MODEL.subtype, name="Agent_subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.Agent_subtype, domain=Agent, range=Optional[str])

slots.Agent_name = Slot(uri=SEPIO-MODEL.name, name="Agent_name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.Agent_name, domain=Agent, range=Optional[str])

slots.Statement_statementText = Slot(uri=SEPIO-MODEL.statementText, name="Statement_statementText", curie=SEPIO-MODEL.curie('statementText'),
                   model_uri=SEPIO_LINKML.Statement_statementText, domain=Statement, range=Optional[str])

slots.Statement_proposition = Slot(uri=SEPIO-MODEL.proposition, name="Statement_proposition", curie=SEPIO-MODEL.curie('proposition'),
                   model_uri=SEPIO_LINKML.Statement_proposition, domain=Statement, range=Optional[Union[dict, "Proposition"]])

slots.Statement_subject = Slot(uri=SEPIO-MODEL.subject, name="Statement_subject", curie=SEPIO-MODEL.curie('subject'),
                   model_uri=SEPIO_LINKML.Statement_subject, domain=Statement, range=Optional[str])

slots.Statement_predicate = Slot(uri=SEPIO-MODEL.predicate, name="Statement_predicate", curie=SEPIO-MODEL.curie('predicate'),
                   model_uri=SEPIO_LINKML.Statement_predicate, domain=Statement, range=Optional[Union[dict, "Coding"]])

slots.Statement_object = Slot(uri=SEPIO-MODEL.object, name="Statement_object", curie=SEPIO-MODEL.curie('object'),
                   model_uri=SEPIO_LINKML.Statement_object, domain=Statement, range=Optional[str])

slots.Statement_qualifier = Slot(uri=SEPIO-MODEL.qualifier, name="Statement_qualifier", curie=SEPIO-MODEL.curie('qualifier'),
                   model_uri=SEPIO_LINKML.Statement_qualifier, domain=Statement, range=Optional[Union[Union[dict, "Qualifier"], List[Union[dict, "Qualifier"]]]])

slots.Statement_direction = Slot(uri=SEPIO-MODEL.direction, name="Statement_direction", curie=SEPIO-MODEL.curie('direction'),
                   model_uri=SEPIO_LINKML.Statement_direction, domain=Statement, range=Optional[str])

slots.Statement_strength = Slot(uri=SEPIO-MODEL.strength, name="Statement_strength", curie=SEPIO-MODEL.curie('strength'),
                   model_uri=SEPIO_LINKML.Statement_strength, domain=Statement, range=Optional[str])

slots.Statement_score = Slot(uri=SEPIO-MODEL.score, name="Statement_score", curie=SEPIO-MODEL.curie('score'),
                   model_uri=SEPIO_LINKML.Statement_score, domain=Statement, range=Optional[float])

slots.Statement_subjectClassification = Slot(uri=SEPIO-MODEL.subjectClassification, name="Statement_subjectClassification", curie=SEPIO-MODEL.curie('subjectClassification'),
                   model_uri=SEPIO_LINKML.Statement_subjectClassification, domain=Statement, range=Optional[Union[dict, "Coding"]])

slots.Statement_hasEvidenceOfTypes = Slot(uri=SEPIO-MODEL.hasEvidenceOfTypes, name="Statement_hasEvidenceOfTypes", curie=SEPIO-MODEL.curie('hasEvidenceOfTypes'),
                   model_uri=SEPIO_LINKML.Statement_hasEvidenceOfTypes, domain=Statement, range=Optional[Union[str, List[str]]])

slots.Statement_hasEvidenceLines = Slot(uri=SEPIO-MODEL.hasEvidenceLines, name="Statement_hasEvidenceLines", curie=SEPIO-MODEL.curie('hasEvidenceLines'),
                   model_uri=SEPIO_LINKML.Statement_hasEvidenceLines, domain=Statement, range=Optional[Union[Union[dict, "EvidenceLine"], List[Union[dict, "EvidenceLine"]]]])

slots.Statement_hasEvidence = Slot(uri=SEPIO-MODEL.hasEvidence, name="Statement_hasEvidence", curie=SEPIO-MODEL.curie('hasEvidence'),
                   model_uri=SEPIO_LINKML.Statement_hasEvidence, domain=Statement, range=Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]])

slots.StudyResult_focus = Slot(uri=SEPIO-MODEL.focus, name="StudyResult_focus", curie=SEPIO-MODEL.curie('focus'),
                   model_uri=SEPIO_LINKML.StudyResult_focus, domain=StudyResult, range=Optional[str])

slots.StudyResult_dataItems = Slot(uri=SEPIO-MODEL.dataItems, name="StudyResult_dataItems", curie=SEPIO-MODEL.curie('dataItems'),
                   model_uri=SEPIO_LINKML.StudyResult_dataItems, domain=StudyResult, range=Optional[Union[Union[dict, DataItem], List[Union[dict, DataItem]]]])

slots.StudyResult_interpretation = Slot(uri=SEPIO-MODEL.interpretation, name="StudyResult_interpretation", curie=SEPIO-MODEL.curie('interpretation'),
                   model_uri=SEPIO_LINKML.StudyResult_interpretation, domain=StudyResult, range=Optional[Union[dict, "Coding"]])

slots.StudyResult_sourceDataSet = Slot(uri=SEPIO-MODEL.sourceDataSet, name="StudyResult_sourceDataSet", curie=SEPIO-MODEL.curie('sourceDataSet'),
                   model_uri=SEPIO_LINKML.StudyResult_sourceDataSet, domain=StudyResult, range=Optional[Union[Union[dict, DataSet], List[Union[dict, DataSet]]]])

slots.StudyResult_componentResult = Slot(uri=SEPIO-MODEL.componentResult, name="StudyResult_componentResult", curie=SEPIO-MODEL.curie('componentResult'),
                   model_uri=SEPIO_LINKML.StudyResult_componentResult, domain=StudyResult, range=Optional[Union[Union[dict, "StudyResult"], List[Union[dict, "StudyResult"]]]])

slots.StudyResult_studyGroup = Slot(uri=SEPIO-MODEL.studyGroup, name="StudyResult_studyGroup", curie=SEPIO-MODEL.curie('studyGroup'),
                   model_uri=SEPIO_LINKML.StudyResult_studyGroup, domain=StudyResult, range=Optional[Union[dict, "StudyGroup"]])

slots.EvidenceLine_subtype = Slot(uri=SEPIO-MODEL.subtype, name="EvidenceLine_subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.EvidenceLine_subtype, domain=EvidenceLine, range=Optional[Union[dict, "Coding"]])

slots.EvidenceLine_targetProposition = Slot(uri=SEPIO-MODEL.targetProposition, name="EvidenceLine_targetProposition", curie=SEPIO-MODEL.curie('targetProposition'),
                   model_uri=SEPIO_LINKML.EvidenceLine_targetProposition, domain=EvidenceLine, range=Optional[Union[dict, "Proposition"]])

slots.EvidenceLine_hasEvidenceItems = Slot(uri=SEPIO-MODEL.hasEvidenceItems, name="EvidenceLine_hasEvidenceItems", curie=SEPIO-MODEL.curie('hasEvidenceItems'),
                   model_uri=SEPIO_LINKML.EvidenceLine_hasEvidenceItems, domain=EvidenceLine, range=Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]])

slots.EvidenceLine_directionOfEvidenceProvided = Slot(uri=SEPIO-MODEL.directionOfEvidenceProvided, name="EvidenceLine_directionOfEvidenceProvided", curie=SEPIO-MODEL.curie('directionOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.EvidenceLine_directionOfEvidenceProvided, domain=EvidenceLine, range=Optional[str])

slots.EvidenceLine_strengthOfEvidenceProvided = Slot(uri=SEPIO-MODEL.strengthOfEvidenceProvided, name="EvidenceLine_strengthOfEvidenceProvided", curie=SEPIO-MODEL.curie('strengthOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.EvidenceLine_strengthOfEvidenceProvided, domain=EvidenceLine, range=Optional[str])

slots.EvidenceLine_scoreOfEvidenceProvided = Slot(uri=SEPIO-MODEL.scoreOfEvidenceProvided, name="EvidenceLine_scoreOfEvidenceProvided", curie=SEPIO-MODEL.curie('scoreOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.EvidenceLine_scoreOfEvidenceProvided, domain=EvidenceLine, range=Optional[float])

slots.EvidenceLine_evidenceItemSources = Slot(uri=SEPIO-MODEL.evidenceItemSources, name="EvidenceLine_evidenceItemSources", curie=SEPIO-MODEL.curie('evidenceItemSources'),
                   model_uri=SEPIO_LINKML.EvidenceLine_evidenceItemSources, domain=EvidenceLine, range=Optional[Union[str, List[str]]])

slots.Proposition_propositionText = Slot(uri=SEPIO-MODEL.propositionText, name="Proposition_propositionText", curie=SEPIO-MODEL.curie('propositionText'),
                   model_uri=SEPIO_LINKML.Proposition_propositionText, domain=Proposition, range=Optional[str])

slots.Proposition_subject = Slot(uri=SEPIO-MODEL.subject, name="Proposition_subject", curie=SEPIO-MODEL.curie('subject'),
                   model_uri=SEPIO_LINKML.Proposition_subject, domain=Proposition, range=str)

slots.Proposition_predicate = Slot(uri=SEPIO-MODEL.predicate, name="Proposition_predicate", curie=SEPIO-MODEL.curie('predicate'),
                   model_uri=SEPIO_LINKML.Proposition_predicate, domain=Proposition, range=Union[dict, "Coding"])

slots.Proposition_object = Slot(uri=SEPIO-MODEL.object, name="Proposition_object", curie=SEPIO-MODEL.curie('object'),
                   model_uri=SEPIO_LINKML.Proposition_object, domain=Proposition, range=str)

slots.Proposition_qualifier = Slot(uri=SEPIO-MODEL.qualifier, name="Proposition_qualifier", curie=SEPIO-MODEL.curie('qualifier'),
                   model_uri=SEPIO_LINKML.Proposition_qualifier, domain=Proposition, range=Optional[Union[Union[dict, "Qualifier"], List[Union[dict, "Qualifier"]]]])

slots.Proposition_negated = Slot(uri=SEPIO-MODEL.negated, name="Proposition_negated", curie=SEPIO-MODEL.curie('negated'),
                   model_uri=SEPIO_LINKML.Proposition_negated, domain=Proposition, range=Optional[Union[bool, Bool]])

slots.StudyGroup_memberCount = Slot(uri=SEPIO-MODEL.memberCount, name="StudyGroup_memberCount", curie=SEPIO-MODEL.curie('memberCount'),
                   model_uri=SEPIO_LINKML.StudyGroup_memberCount, domain=StudyGroup, range=Optional[int])

slots.StudyGroup_isSubsetOf = Slot(uri=SEPIO-MODEL.isSubsetOf, name="StudyGroup_isSubsetOf", curie=SEPIO-MODEL.curie('isSubsetOf'),
                   model_uri=SEPIO_LINKML.StudyGroup_isSubsetOf, domain=StudyGroup, range=Optional[Union[Union[dict, "StudyGroup"], List[Union[dict, "StudyGroup"]]]])

slots.StudyGroup_characteristics = Slot(uri=SEPIO-MODEL.characteristics, name="StudyGroup_characteristics", curie=SEPIO-MODEL.curie('characteristics'),
                   model_uri=SEPIO_LINKML.StudyGroup_characteristics, domain=StudyGroup, range=Optional[Union[Union[dict, "Characteristic"], List[Union[dict, "Characteristic"]]]])

slots.Coding_code = Slot(uri=SEPIO-MODEL.code, name="Coding_code", curie=SEPIO-MODEL.curie('code'),
                   model_uri=SEPIO_LINKML.Coding_code, domain=Coding, range=Optional[str])

slots.Coding_label = Slot(uri=SEPIO-MODEL.label, name="Coding_label", curie=SEPIO-MODEL.curie('label'),
                   model_uri=SEPIO_LINKML.Coding_label, domain=Coding, range=Optional[str])

slots.Coding_system = Slot(uri=SEPIO-MODEL.system, name="Coding_system", curie=SEPIO-MODEL.curie('system'),
                   model_uri=SEPIO_LINKML.Coding_system, domain=Coding, range=Optional[str])

slots.Coding_systemVersion = Slot(uri=SEPIO-MODEL.systemVersion, name="Coding_systemVersion", curie=SEPIO-MODEL.curie('systemVersion'),
                   model_uri=SEPIO_LINKML.Coding_systemVersion, domain=Coding, range=Optional[str])

slots.Qualifier_name = Slot(uri=SEPIO-MODEL.name, name="Qualifier_name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.Qualifier_name, domain=Qualifier, range=str)

slots.Qualifier_value = Slot(uri=SEPIO-MODEL.value, name="Qualifier_value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.Qualifier_value, domain=Qualifier, range=str)

slots.Expression_value = Slot(uri=SEPIO-MODEL.value, name="Expression_value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.Expression_value, domain=Expression, range=str)

slots.Expression_systemURL = Slot(uri=SEPIO-MODEL.systemURL, name="Expression_systemURL", curie=SEPIO-MODEL.curie('systemURL'),
                   model_uri=SEPIO_LINKML.Expression_systemURL, domain=Expression, range=Optional[Union[str, URIorCURIE]])

slots.Expression_systemVersion = Slot(uri=SEPIO-MODEL.systemVersion, name="Expression_systemVersion", curie=SEPIO-MODEL.curie('systemVersion'),
                   model_uri=SEPIO_LINKML.Expression_systemVersion, domain=Expression, range=Optional[str])

slots.Extension_extensionDescription = Slot(uri=SEPIO-MODEL.extensionDescription, name="Extension_extensionDescription", curie=SEPIO-MODEL.curie('extensionDescription'),
                   model_uri=SEPIO_LINKML.Extension_extensionDescription, domain=Extension, range=Optional[str])

slots.Extension_name = Slot(uri=SEPIO-MODEL.name, name="Extension_name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.Extension_name, domain=Extension, range=str)

slots.Extension_value = Slot(uri=SEPIO-MODEL.value, name="Extension_value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.Extension_value, domain=Extension, range=str)

slots.RecordMetadata_recordIdentifier = Slot(uri=SEPIO-MODEL.recordIdentifier, name="RecordMetadata_recordIdentifier", curie=SEPIO-MODEL.curie('recordIdentifier'),
                   model_uri=SEPIO_LINKML.RecordMetadata_recordIdentifier, domain=RecordMetadata, range=Optional[str])

slots.RecordMetadata_recordVersion = Slot(uri=SEPIO-MODEL.recordVersion, name="RecordMetadata_recordVersion", curie=SEPIO-MODEL.curie('recordVersion'),
                   model_uri=SEPIO_LINKML.RecordMetadata_recordVersion, domain=RecordMetadata, range=Optional[str])

slots.RecordMetadata_derivedFromRecord = Slot(uri=SEPIO-MODEL.derivedFromRecord, name="RecordMetadata_derivedFromRecord", curie=SEPIO-MODEL.curie('derivedFromRecord'),
                   model_uri=SEPIO_LINKML.RecordMetadata_derivedFromRecord, domain=RecordMetadata, range=Optional[Union[str, List[str]]])

slots.RecordMetadata_dateRecordCreated = Slot(uri=SEPIO-MODEL.dateRecordCreated, name="RecordMetadata_dateRecordCreated", curie=SEPIO-MODEL.curie('dateRecordCreated'),
                   model_uri=SEPIO_LINKML.RecordMetadata_dateRecordCreated, domain=RecordMetadata, range=Optional[str])

slots.RecordMetadata_contributions = Slot(uri=SEPIO-MODEL.contributions, name="RecordMetadata_contributions", curie=SEPIO-MODEL.curie('contributions'),
                   model_uri=SEPIO_LINKML.RecordMetadata_contributions, domain=RecordMetadata, range=Optional[Union[Union[dict, Contribution], List[Union[dict, Contribution]]]])

slots.Characteristic_name = Slot(uri=SEPIO-MODEL.name, name="Characteristic_name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.Characteristic_name, domain=Characteristic, range=str)

slots.Characteristic_values = Slot(uri=SEPIO-MODEL.values, name="Characteristic_values", curie=SEPIO-MODEL.curie('values'),
                   model_uri=SEPIO_LINKML.Characteristic_values, domain=Characteristic, range=Union[str, List[str]])

slots.Characteristic_valueOperator = Slot(uri=SEPIO-MODEL.valueOperator, name="Characteristic_valueOperator", curie=SEPIO-MODEL.curie('valueOperator'),
                   model_uri=SEPIO_LINKML.Characteristic_valueOperator, domain=Characteristic, range=Optional[str])