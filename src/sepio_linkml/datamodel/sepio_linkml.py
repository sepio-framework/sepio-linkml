# Auto generated from sepio_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-10-08T16:29:14
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
    supportingMethods: Optional[Union[str, List[str]]] = empty_list()
    supportingMethodTypes: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
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

        if not isinstance(self.supportingMethods, list):
            self.supportingMethods = [self.supportingMethods] if self.supportingMethods is not None else []
        self.supportingMethods = [v if isinstance(v, str) else str(v) for v in self.supportingMethods]

        if not isinstance(self.supportingMethodTypes, list):
            self.supportingMethodTypes = [self.supportingMethodTypes] if self.supportingMethodTypes is not None else []
        self.supportingMethodTypes = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.supportingMethodTypes]

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
    activity taking place, for the existence of an entity, or for another agent's activity.
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

slots.entity__id = Slot(uri=SEPIO-MODEL.id, name="entity__id", curie=SEPIO-MODEL.curie('id'),
                   model_uri=SEPIO_LINKML.entity__id, domain=None, range=str)

slots.entity__identifiers = Slot(uri=SEPIO-MODEL.identifiers, name="entity__identifiers", curie=SEPIO-MODEL.curie('identifiers'),
                   model_uri=SEPIO_LINKML.entity__identifiers, domain=None, range=Optional[Union[str, List[str]]])

slots.entity__type = Slot(uri=SEPIO-MODEL.type, name="entity__type", curie=SEPIO-MODEL.curie('type'),
                   model_uri=SEPIO_LINKML.entity__type, domain=None, range=str)

slots.entity__label = Slot(uri=SEPIO-MODEL.label, name="entity__label", curie=SEPIO-MODEL.curie('label'),
                   model_uri=SEPIO_LINKML.entity__label, domain=None, range=Optional[str])

slots.entity__alternativeLabels = Slot(uri=SEPIO-MODEL.alternativeLabels, name="entity__alternativeLabels", curie=SEPIO-MODEL.curie('alternativeLabels'),
                   model_uri=SEPIO_LINKML.entity__alternativeLabels, domain=None, range=Optional[Union[str, List[str]]])

slots.entity__description = Slot(uri=SEPIO-MODEL.description, name="entity__description", curie=SEPIO-MODEL.curie('description'),
                   model_uri=SEPIO_LINKML.entity__description, domain=None, range=Optional[str])

slots.entity__extensions = Slot(uri=SEPIO-MODEL.extensions, name="entity__extensions", curie=SEPIO-MODEL.curie('extensions'),
                   model_uri=SEPIO_LINKML.entity__extensions, domain=None, range=Optional[Union[Union[dict, Extension], List[Union[dict, Extension]]]])

slots.informationEntity__isAbout = Slot(uri=SEPIO-MODEL.isAbout, name="informationEntity__isAbout", curie=SEPIO-MODEL.curie('isAbout'),
                   model_uri=SEPIO_LINKML.informationEntity__isAbout, domain=None, range=Optional[Union[str, List[str]]])

slots.informationEntity__contributions = Slot(uri=SEPIO-MODEL.contributions, name="informationEntity__contributions", curie=SEPIO-MODEL.curie('contributions'),
                   model_uri=SEPIO_LINKML.informationEntity__contributions, domain=None, range=Optional[Union[Union[dict, Contribution], List[Union[dict, Contribution]]]])

slots.informationEntity__dateAuthored = Slot(uri=SEPIO-MODEL.dateAuthored, name="informationEntity__dateAuthored", curie=SEPIO-MODEL.curie('dateAuthored'),
                   model_uri=SEPIO_LINKML.informationEntity__dateAuthored, domain=None, range=Optional[str])

slots.informationEntity__specifiedBy = Slot(uri=SEPIO-MODEL.specifiedBy, name="informationEntity__specifiedBy", curie=SEPIO-MODEL.curie('specifiedBy'),
                   model_uri=SEPIO_LINKML.informationEntity__specifiedBy, domain=None, range=Optional[Union[str, List[str]]])

slots.informationEntity__supportingMethods = Slot(uri=SEPIO-MODEL.supportingMethods, name="informationEntity__supportingMethods", curie=SEPIO-MODEL.curie('supportingMethods'),
                   model_uri=SEPIO_LINKML.informationEntity__supportingMethods, domain=None, range=Optional[Union[str, List[str]]])

slots.informationEntity__supportingMethodTypes = Slot(uri=SEPIO-MODEL.supportingMethodTypes, name="informationEntity__supportingMethodTypes", curie=SEPIO-MODEL.curie('supportingMethodTypes'),
                   model_uri=SEPIO_LINKML.informationEntity__supportingMethodTypes, domain=None, range=Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]])

slots.informationEntity__derivedFrom = Slot(uri=SEPIO-MODEL.derivedFrom, name="informationEntity__derivedFrom", curie=SEPIO-MODEL.curie('derivedFrom'),
                   model_uri=SEPIO_LINKML.informationEntity__derivedFrom, domain=None, range=Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]])

slots.informationEntity__reportedIn = Slot(uri=SEPIO-MODEL.reportedIn, name="informationEntity__reportedIn", curie=SEPIO-MODEL.curie('reportedIn'),
                   model_uri=SEPIO_LINKML.informationEntity__reportedIn, domain=None, range=Optional[Union[str, List[str]]])

slots.informationEntity__informationQuality = Slot(uri=SEPIO-MODEL.informationQuality, name="informationEntity__informationQuality", curie=SEPIO-MODEL.curie('informationQuality'),
                   model_uri=SEPIO_LINKML.informationEntity__informationQuality, domain=None, range=Optional[Union[dict, Coding]])

slots.informationEntity__recordMetadata = Slot(uri=SEPIO-MODEL.recordMetadata, name="informationEntity__recordMetadata", curie=SEPIO-MODEL.curie('recordMetadata'),
                   model_uri=SEPIO_LINKML.informationEntity__recordMetadata, domain=None, range=Optional[Union[dict, RecordMetadata]])

slots.method__subtype = Slot(uri=SEPIO-MODEL.subtype, name="method__subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.method__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.method__urls = Slot(uri=SEPIO-MODEL.urls, name="method__urls", curie=SEPIO-MODEL.curie('urls'),
                   model_uri=SEPIO_LINKML.method__urls, domain=None, range=Optional[Union[str, List[str]]])

slots.document__subtype = Slot(uri=SEPIO-MODEL.subtype, name="document__subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.document__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.document__title = Slot(uri=SEPIO-MODEL.title, name="document__title", curie=SEPIO-MODEL.curie('title'),
                   model_uri=SEPIO_LINKML.document__title, domain=None, range=Optional[str])

slots.document__urls = Slot(uri=SEPIO-MODEL.urls, name="document__urls", curie=SEPIO-MODEL.curie('urls'),
                   model_uri=SEPIO_LINKML.document__urls, domain=None, range=Optional[Union[str, List[str]]])

slots.document__pmid = Slot(uri=SEPIO-MODEL.pmid, name="document__pmid", curie=SEPIO-MODEL.curie('pmid'),
                   model_uri=SEPIO_LINKML.document__pmid, domain=None, range=Optional[str])

slots.document__doi = Slot(uri=SEPIO-MODEL.doi, name="document__doi", curie=SEPIO-MODEL.curie('doi'),
                   model_uri=SEPIO_LINKML.document__doi, domain=None, range=Optional[str])

slots.document__license = Slot(uri=SEPIO-MODEL.license, name="document__license", curie=SEPIO-MODEL.curie('license'),
                   model_uri=SEPIO_LINKML.document__license, domain=None, range=Optional[str])

slots.dataItem__subtype = Slot(uri=SEPIO-MODEL.subtype, name="dataItem__subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.dataItem__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.dataItem__value = Slot(uri=SEPIO-MODEL.value, name="dataItem__value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.dataItem__value, domain=None, range=str)

slots.dataItem__unit = Slot(uri=SEPIO-MODEL.unit, name="dataItem__unit", curie=SEPIO-MODEL.curie('unit'),
                   model_uri=SEPIO_LINKML.dataItem__unit, domain=None, range=Optional[Union[dict, Coding]])

slots.dataItem__variabilityMeasures = Slot(uri=SEPIO-MODEL.variabilityMeasures, name="dataItem__variabilityMeasures", curie=SEPIO-MODEL.curie('variabilityMeasures'),
                   model_uri=SEPIO_LINKML.dataItem__variabilityMeasures, domain=None, range=Optional[Union[Union[dict, DataItem], List[Union[dict, DataItem]]]])

slots.dataItem__confidenceInterval = Slot(uri=SEPIO-MODEL.confidenceInterval, name="dataItem__confidenceInterval", curie=SEPIO-MODEL.curie('confidenceInterval'),
                   model_uri=SEPIO_LINKML.dataItem__confidenceInterval, domain=None, range=Optional[Union[dict, DataItem]])

slots.dataItem__componentDataItem = Slot(uri=SEPIO-MODEL.componentDataItem, name="dataItem__componentDataItem", curie=SEPIO-MODEL.curie('componentDataItem'),
                   model_uri=SEPIO_LINKML.dataItem__componentDataItem, domain=None, range=Optional[Union[Union[dict, DataItem], List[Union[dict, DataItem]]]])

slots.dataSet__subtype = Slot(uri=SEPIO-MODEL.subtype, name="dataSet__subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.dataSet__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.dataSet__releaseDate = Slot(uri=SEPIO-MODEL.releaseDate, name="dataSet__releaseDate", curie=SEPIO-MODEL.curie('releaseDate'),
                   model_uri=SEPIO_LINKML.dataSet__releaseDate, domain=None, range=Optional[str])

slots.dataSet__version = Slot(uri=SEPIO-MODEL.version, name="dataSet__version", curie=SEPIO-MODEL.curie('version'),
                   model_uri=SEPIO_LINKML.dataSet__version, domain=None, range=Optional[str])

slots.dataSet__license = Slot(uri=SEPIO-MODEL.license, name="dataSet__license", curie=SEPIO-MODEL.curie('license'),
                   model_uri=SEPIO_LINKML.dataSet__license, domain=None, range=Optional[str])

slots.activity__subtype = Slot(uri=SEPIO-MODEL.subtype, name="activity__subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.activity__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.activity__date = Slot(uri=SEPIO-MODEL.date, name="activity__date", curie=SEPIO-MODEL.curie('date'),
                   model_uri=SEPIO_LINKML.activity__date, domain=None, range=Optional[Union[str, XSDDate]])

slots.activity__performedBy = Slot(uri=SEPIO-MODEL.performedBy, name="activity__performedBy", curie=SEPIO-MODEL.curie('performedBy'),
                   model_uri=SEPIO_LINKML.activity__performedBy, domain=None, range=Optional[Union[Union[dict, Agent], List[Union[dict, Agent]]]])

slots.activity__specifiedBy = Slot(uri=SEPIO-MODEL.specifiedBy, name="activity__specifiedBy", curie=SEPIO-MODEL.curie('specifiedBy'),
                   model_uri=SEPIO_LINKML.activity__specifiedBy, domain=None, range=Optional[Union[Union[dict, Method], List[Union[dict, Method]]]])

slots.activity__input = Slot(uri=SEPIO-MODEL.input, name="activity__input", curie=SEPIO-MODEL.curie('input'),
                   model_uri=SEPIO_LINKML.activity__input, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.activity__output = Slot(uri=SEPIO-MODEL.output, name="activity__output", curie=SEPIO-MODEL.curie('output'),
                   model_uri=SEPIO_LINKML.activity__output, domain=None, range=Optional[Union[Union[dict, Entity], List[Union[dict, Entity]]]])

slots.contribution__contributor = Slot(uri=SEPIO-MODEL.contributor, name="contribution__contributor", curie=SEPIO-MODEL.curie('contributor'),
                   model_uri=SEPIO_LINKML.contribution__contributor, domain=None, range=Optional[Union[dict, Agent]])

slots.contribution__activityType = Slot(uri=SEPIO-MODEL.activityType, name="contribution__activityType", curie=SEPIO-MODEL.curie('activityType'),
                   model_uri=SEPIO_LINKML.contribution__activityType, domain=None, range=Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]])

slots.contribution__contributionMadeTo = Slot(uri=SEPIO-MODEL.contributionMadeTo, name="contribution__contributionMadeTo", curie=SEPIO-MODEL.curie('contributionMadeTo'),
                   model_uri=SEPIO_LINKML.contribution__contributionMadeTo, domain=None, range=Optional[Union[dict, InformationEntity]])

slots.agent__subtype = Slot(uri=SEPIO-MODEL.subtype, name="agent__subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.agent__subtype, domain=None, range=Optional[str])

slots.agent__name = Slot(uri=SEPIO-MODEL.name, name="agent__name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.agent__name, domain=None, range=Optional[str])

slots.statement__statementText = Slot(uri=SEPIO-MODEL.statementText, name="statement__statementText", curie=SEPIO-MODEL.curie('statementText'),
                   model_uri=SEPIO_LINKML.statement__statementText, domain=None, range=Optional[str])

slots.statement__proposition = Slot(uri=SEPIO-MODEL.proposition, name="statement__proposition", curie=SEPIO-MODEL.curie('proposition'),
                   model_uri=SEPIO_LINKML.statement__proposition, domain=None, range=Optional[Union[dict, Proposition]])

slots.statement__subject = Slot(uri=SEPIO-MODEL.subject, name="statement__subject", curie=SEPIO-MODEL.curie('subject'),
                   model_uri=SEPIO_LINKML.statement__subject, domain=None, range=Optional[str])

slots.statement__predicate = Slot(uri=SEPIO-MODEL.predicate, name="statement__predicate", curie=SEPIO-MODEL.curie('predicate'),
                   model_uri=SEPIO_LINKML.statement__predicate, domain=None, range=Optional[Union[dict, Coding]])

slots.statement__object = Slot(uri=SEPIO-MODEL.object, name="statement__object", curie=SEPIO-MODEL.curie('object'),
                   model_uri=SEPIO_LINKML.statement__object, domain=None, range=Optional[str])

slots.statement__qualifier = Slot(uri=SEPIO-MODEL.qualifier, name="statement__qualifier", curie=SEPIO-MODEL.curie('qualifier'),
                   model_uri=SEPIO_LINKML.statement__qualifier, domain=None, range=Optional[Union[Union[dict, Qualifier], List[Union[dict, Qualifier]]]])

slots.statement__direction = Slot(uri=SEPIO-MODEL.direction, name="statement__direction", curie=SEPIO-MODEL.curie('direction'),
                   model_uri=SEPIO_LINKML.statement__direction, domain=None, range=Optional[str])

slots.statement__strength = Slot(uri=SEPIO-MODEL.strength, name="statement__strength", curie=SEPIO-MODEL.curie('strength'),
                   model_uri=SEPIO_LINKML.statement__strength, domain=None, range=Optional[str])

slots.statement__score = Slot(uri=SEPIO-MODEL.score, name="statement__score", curie=SEPIO-MODEL.curie('score'),
                   model_uri=SEPIO_LINKML.statement__score, domain=None, range=Optional[float])

slots.statement__subjectClassification = Slot(uri=SEPIO-MODEL.subjectClassification, name="statement__subjectClassification", curie=SEPIO-MODEL.curie('subjectClassification'),
                   model_uri=SEPIO_LINKML.statement__subjectClassification, domain=None, range=Optional[Union[dict, Coding]])

slots.statement__hasEvidenceOfTypes = Slot(uri=SEPIO-MODEL.hasEvidenceOfTypes, name="statement__hasEvidenceOfTypes", curie=SEPIO-MODEL.curie('hasEvidenceOfTypes'),
                   model_uri=SEPIO_LINKML.statement__hasEvidenceOfTypes, domain=None, range=Optional[Union[str, List[str]]])

slots.statement__hasEvidenceLines = Slot(uri=SEPIO-MODEL.hasEvidenceLines, name="statement__hasEvidenceLines", curie=SEPIO-MODEL.curie('hasEvidenceLines'),
                   model_uri=SEPIO_LINKML.statement__hasEvidenceLines, domain=None, range=Optional[Union[Union[dict, EvidenceLine], List[Union[dict, EvidenceLine]]]])

slots.statement__hasEvidence = Slot(uri=SEPIO-MODEL.hasEvidence, name="statement__hasEvidence", curie=SEPIO-MODEL.curie('hasEvidence'),
                   model_uri=SEPIO_LINKML.statement__hasEvidence, domain=None, range=Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]])

slots.studyResult__focus = Slot(uri=SEPIO-MODEL.focus, name="studyResult__focus", curie=SEPIO-MODEL.curie('focus'),
                   model_uri=SEPIO_LINKML.studyResult__focus, domain=None, range=Optional[str])

slots.studyResult__dataItems = Slot(uri=SEPIO-MODEL.dataItems, name="studyResult__dataItems", curie=SEPIO-MODEL.curie('dataItems'),
                   model_uri=SEPIO_LINKML.studyResult__dataItems, domain=None, range=Optional[Union[Union[dict, DataItem], List[Union[dict, DataItem]]]])

slots.studyResult__interpretation = Slot(uri=SEPIO-MODEL.interpretation, name="studyResult__interpretation", curie=SEPIO-MODEL.curie('interpretation'),
                   model_uri=SEPIO_LINKML.studyResult__interpretation, domain=None, range=Optional[Union[dict, Coding]])

slots.studyResult__sourceDataSet = Slot(uri=SEPIO-MODEL.sourceDataSet, name="studyResult__sourceDataSet", curie=SEPIO-MODEL.curie('sourceDataSet'),
                   model_uri=SEPIO_LINKML.studyResult__sourceDataSet, domain=None, range=Optional[Union[Union[dict, DataSet], List[Union[dict, DataSet]]]])

slots.studyResult__componentResult = Slot(uri=SEPIO-MODEL.componentResult, name="studyResult__componentResult", curie=SEPIO-MODEL.curie('componentResult'),
                   model_uri=SEPIO_LINKML.studyResult__componentResult, domain=None, range=Optional[Union[Union[dict, StudyResult], List[Union[dict, StudyResult]]]])

slots.studyResult__studyGroup = Slot(uri=SEPIO-MODEL.studyGroup, name="studyResult__studyGroup", curie=SEPIO-MODEL.curie('studyGroup'),
                   model_uri=SEPIO_LINKML.studyResult__studyGroup, domain=None, range=Optional[Union[dict, StudyGroup]])

slots.evidenceLine__subtype = Slot(uri=SEPIO-MODEL.subtype, name="evidenceLine__subtype", curie=SEPIO-MODEL.curie('subtype'),
                   model_uri=SEPIO_LINKML.evidenceLine__subtype, domain=None, range=Optional[Union[dict, Coding]])

slots.evidenceLine__targetProposition = Slot(uri=SEPIO-MODEL.targetProposition, name="evidenceLine__targetProposition", curie=SEPIO-MODEL.curie('targetProposition'),
                   model_uri=SEPIO_LINKML.evidenceLine__targetProposition, domain=None, range=Optional[Union[dict, Proposition]])

slots.evidenceLine__hasEvidenceItems = Slot(uri=SEPIO-MODEL.hasEvidenceItems, name="evidenceLine__hasEvidenceItems", curie=SEPIO-MODEL.curie('hasEvidenceItems'),
                   model_uri=SEPIO_LINKML.evidenceLine__hasEvidenceItems, domain=None, range=Optional[Union[Union[dict, InformationEntity], List[Union[dict, InformationEntity]]]])

slots.evidenceLine__directionOfEvidenceProvided = Slot(uri=SEPIO-MODEL.directionOfEvidenceProvided, name="evidenceLine__directionOfEvidenceProvided", curie=SEPIO-MODEL.curie('directionOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.evidenceLine__directionOfEvidenceProvided, domain=None, range=Optional[str])

slots.evidenceLine__strengthOfEvidenceProvided = Slot(uri=SEPIO-MODEL.strengthOfEvidenceProvided, name="evidenceLine__strengthOfEvidenceProvided", curie=SEPIO-MODEL.curie('strengthOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.evidenceLine__strengthOfEvidenceProvided, domain=None, range=Optional[str])

slots.evidenceLine__scoreOfEvidenceProvided = Slot(uri=SEPIO-MODEL.scoreOfEvidenceProvided, name="evidenceLine__scoreOfEvidenceProvided", curie=SEPIO-MODEL.curie('scoreOfEvidenceProvided'),
                   model_uri=SEPIO_LINKML.evidenceLine__scoreOfEvidenceProvided, domain=None, range=Optional[float])

slots.evidenceLine__evidenceItemSources = Slot(uri=SEPIO-MODEL.evidenceItemSources, name="evidenceLine__evidenceItemSources", curie=SEPIO-MODEL.curie('evidenceItemSources'),
                   model_uri=SEPIO_LINKML.evidenceLine__evidenceItemSources, domain=None, range=Optional[Union[str, List[str]]])

slots.proposition__propositionText = Slot(uri=SEPIO-MODEL.propositionText, name="proposition__propositionText", curie=SEPIO-MODEL.curie('propositionText'),
                   model_uri=SEPIO_LINKML.proposition__propositionText, domain=None, range=Optional[str])

slots.proposition__subject = Slot(uri=SEPIO-MODEL.subject, name="proposition__subject", curie=SEPIO-MODEL.curie('subject'),
                   model_uri=SEPIO_LINKML.proposition__subject, domain=None, range=str)

slots.proposition__predicate = Slot(uri=SEPIO-MODEL.predicate, name="proposition__predicate", curie=SEPIO-MODEL.curie('predicate'),
                   model_uri=SEPIO_LINKML.proposition__predicate, domain=None, range=Union[dict, Coding])

slots.proposition__object = Slot(uri=SEPIO-MODEL.object, name="proposition__object", curie=SEPIO-MODEL.curie('object'),
                   model_uri=SEPIO_LINKML.proposition__object, domain=None, range=str)

slots.proposition__qualifier = Slot(uri=SEPIO-MODEL.qualifier, name="proposition__qualifier", curie=SEPIO-MODEL.curie('qualifier'),
                   model_uri=SEPIO_LINKML.proposition__qualifier, domain=None, range=Optional[Union[Union[dict, Qualifier], List[Union[dict, Qualifier]]]])

slots.proposition__negated = Slot(uri=SEPIO-MODEL.negated, name="proposition__negated", curie=SEPIO-MODEL.curie('negated'),
                   model_uri=SEPIO_LINKML.proposition__negated, domain=None, range=Optional[Union[bool, Bool]])

slots.studyGroup__memberCount = Slot(uri=SEPIO-MODEL.memberCount, name="studyGroup__memberCount", curie=SEPIO-MODEL.curie('memberCount'),
                   model_uri=SEPIO_LINKML.studyGroup__memberCount, domain=None, range=Optional[int])

slots.studyGroup__isSubsetOf = Slot(uri=SEPIO-MODEL.isSubsetOf, name="studyGroup__isSubsetOf", curie=SEPIO-MODEL.curie('isSubsetOf'),
                   model_uri=SEPIO_LINKML.studyGroup__isSubsetOf, domain=None, range=Optional[Union[Union[dict, StudyGroup], List[Union[dict, StudyGroup]]]])

slots.studyGroup__characteristics = Slot(uri=SEPIO-MODEL.characteristics, name="studyGroup__characteristics", curie=SEPIO-MODEL.curie('characteristics'),
                   model_uri=SEPIO_LINKML.studyGroup__characteristics, domain=None, range=Optional[Union[Union[dict, Characteristic], List[Union[dict, Characteristic]]]])

slots.coding__code = Slot(uri=SEPIO-MODEL.code, name="coding__code", curie=SEPIO-MODEL.curie('code'),
                   model_uri=SEPIO_LINKML.coding__code, domain=None, range=Optional[str])

slots.coding__label = Slot(uri=SEPIO-MODEL.label, name="coding__label", curie=SEPIO-MODEL.curie('label'),
                   model_uri=SEPIO_LINKML.coding__label, domain=None, range=Optional[str])

slots.coding__system = Slot(uri=SEPIO-MODEL.system, name="coding__system", curie=SEPIO-MODEL.curie('system'),
                   model_uri=SEPIO_LINKML.coding__system, domain=None, range=Optional[str])

slots.coding__systemVersion = Slot(uri=SEPIO-MODEL.systemVersion, name="coding__systemVersion", curie=SEPIO-MODEL.curie('systemVersion'),
                   model_uri=SEPIO_LINKML.coding__systemVersion, domain=None, range=Optional[str])

slots.qualifier__name = Slot(uri=SEPIO-MODEL.name, name="qualifier__name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.qualifier__name, domain=None, range=str)

slots.qualifier__value = Slot(uri=SEPIO-MODEL.value, name="qualifier__value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.qualifier__value, domain=None, range=str)

slots.expression__value = Slot(uri=SEPIO-MODEL.value, name="expression__value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.expression__value, domain=None, range=str)

slots.expression__systemURL = Slot(uri=SEPIO-MODEL.systemURL, name="expression__systemURL", curie=SEPIO-MODEL.curie('systemURL'),
                   model_uri=SEPIO_LINKML.expression__systemURL, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.expression__systemVersion = Slot(uri=SEPIO-MODEL.systemVersion, name="expression__systemVersion", curie=SEPIO-MODEL.curie('systemVersion'),
                   model_uri=SEPIO_LINKML.expression__systemVersion, domain=None, range=Optional[str])

slots.extension__extensionDescription = Slot(uri=SEPIO-MODEL.extensionDescription, name="extension__extensionDescription", curie=SEPIO-MODEL.curie('extensionDescription'),
                   model_uri=SEPIO_LINKML.extension__extensionDescription, domain=None, range=Optional[str])

slots.extension__name = Slot(uri=SEPIO-MODEL.name, name="extension__name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.extension__name, domain=None, range=str)

slots.extension__value = Slot(uri=SEPIO-MODEL.value, name="extension__value", curie=SEPIO-MODEL.curie('value'),
                   model_uri=SEPIO_LINKML.extension__value, domain=None, range=str)

slots.recordMetadata__recordIdentifier = Slot(uri=SEPIO-MODEL.recordIdentifier, name="recordMetadata__recordIdentifier", curie=SEPIO-MODEL.curie('recordIdentifier'),
                   model_uri=SEPIO_LINKML.recordMetadata__recordIdentifier, domain=None, range=Optional[str])

slots.recordMetadata__recordVersion = Slot(uri=SEPIO-MODEL.recordVersion, name="recordMetadata__recordVersion", curie=SEPIO-MODEL.curie('recordVersion'),
                   model_uri=SEPIO_LINKML.recordMetadata__recordVersion, domain=None, range=Optional[str])

slots.recordMetadata__derivedFromRecord = Slot(uri=SEPIO-MODEL.derivedFromRecord, name="recordMetadata__derivedFromRecord", curie=SEPIO-MODEL.curie('derivedFromRecord'),
                   model_uri=SEPIO_LINKML.recordMetadata__derivedFromRecord, domain=None, range=Optional[Union[str, List[str]]])

slots.recordMetadata__dateRecordCreated = Slot(uri=SEPIO-MODEL.dateRecordCreated, name="recordMetadata__dateRecordCreated", curie=SEPIO-MODEL.curie('dateRecordCreated'),
                   model_uri=SEPIO_LINKML.recordMetadata__dateRecordCreated, domain=None, range=Optional[str])

slots.recordMetadata__contributions = Slot(uri=SEPIO-MODEL.contributions, name="recordMetadata__contributions", curie=SEPIO-MODEL.curie('contributions'),
                   model_uri=SEPIO_LINKML.recordMetadata__contributions, domain=None, range=Optional[Union[Union[dict, Contribution], List[Union[dict, Contribution]]]])

slots.characteristic__name = Slot(uri=SEPIO-MODEL.name, name="characteristic__name", curie=SEPIO-MODEL.curie('name'),
                   model_uri=SEPIO_LINKML.characteristic__name, domain=None, range=str)

slots.characteristic__values = Slot(uri=SEPIO-MODEL.values, name="characteristic__values", curie=SEPIO-MODEL.curie('values'),
                   model_uri=SEPIO_LINKML.characteristic__values, domain=None, range=Union[str, List[str]])

slots.characteristic__valueOperator = Slot(uri=SEPIO-MODEL.valueOperator, name="characteristic__valueOperator", curie=SEPIO-MODEL.curie('valueOperator'),
                   model_uri=SEPIO_LINKML.characteristic__valueOperator, domain=None, range=Optional[str])