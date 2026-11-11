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


metamodel_version = "1.12.0"
version = "None"


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


linkml_meta = LinkMLMeta({'default_prefix': 'sepio_linkml',
     'default_range': 'string',
     'description': 'LinkML-based specification of the SEPIO information model.',
     'id': 'https://w3id.org/sepio-framework/sepio-linkml',
     'imports': ['linkml:types', 'sepio_classes'],
     'license': 'Apache Software License 2.0',
     'name': 'sepio-linkml',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'sepio_linkml': {'prefix_prefix': 'sepio_linkml',
                                   'prefix_reference': 'https://w3id.org/sepio-framework/sepio-linkml/'}},
     'see_also': ['https://sepio-framework.github.io/sepio-linkml'],
     'source_file': 'src/sepio_linkml/schema/sepio_linkml.yaml',
     'title': 'sepio-linkml'} )


class Entity(ConfiguredBaseModel):
    """
    Anything that exists, has existed, or will exist.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["Entity is the root class of the 'gks-common' core information "
                      'model. All common classes that have ids and other general '
                      'metadata like label,  description, type, or extensions descend '
                      'from this class and inherit its attributes.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Entity'})

    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class InformationEntity(Entity):
    """
    An abstract (non-physical) entity that is about something - representing the underlying 'information content' conveyed by physical or digital information artifacts like books, web pages, data tables, or photographs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['As abstract, non-physical entities, Information Entities '
                      'represent information independent of any specific language, '
                      'format, or physical/digital medium. They can be simultaneously '
                      'concretized in many distinct physical artifacts (e.g. all '
                      'physical copies of the first edition of "War and Peace" carry '
                      'the same information content, and thus concretize the same '
                      'Information Entity).'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Information Entity'})

    is_about: Optional[list[str]] = Field(default=None, description="""An entity or concept in the world that the information entity describes/is about.""", json_schema_extra = { "linkml_meta": {'comments': ['e.g. In the context of a Statement object, this attribute may '
                      'be used to indicate entities/concepts it is about, in lieu of '
                      'providing a more precise description of what the Statement '
                      'asserts to be true using subject, predicate, object, and '
                      'qualifier properties. e.g. the Statement that "BRCA2 c.8023A>G '
                      'is pathogenic for Breast Cancer" might be annotated to be about '
                      "the variant 'BRCA2 c.8023A>G', and the disease 'Breast "
                      "Cancer'."],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds one or more Contribution objects, which '
                      'provide structured descriptions of a contribution made to the '
                      'Information Entity by a particular agent.'],
         'domain_of': ['InformationEntity', 'RecordMetadata'],
         'status': 'Draft'} })
    date_authored: Optional[str] = Field(default=None, description="""Indicates when the information content expressed in the Information Entity was generated.""", json_schema_extra = { "linkml_meta": {'comments': ["The term 'authored' as used in the model refers to the "
                      "generation of 'information content' in the abstract  sense, as "
                      'opposed to a concrete encoding of this information in a '
                      'specific language or format. e.g. for a Statement, this '
                      'attribute captures when the information content expressed in '
                      'the Statement was first generated by an agent.  Information '
                      'about when a particular concrete encoding of this information '
                      'was created (e.g. as row in a table, or object in a json '
                      'document) would live in a RecordMetadata object attached to the '
                      'Information Entity).'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    specified_by: Optional[list[str]] = Field(default=None, description="""A specification that describes all or part of the process that led to creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples - an experimental protocol or data analysis '
                      'specification that describe how data were generated, or an '
                      'evidence interpretation guideline that describes steps taken to '
                      'interpret data in making a variant pathogenicity '
                      'classification.',
                      'Note that this attribute captures specific *instances* of '
                      'specifications/methods (e.g. the specific electron microscopy '
                      'method described in https://doi.org/10.1002/ cpz1.1045) - as '
                      'opposed to reporting a *type* of method applied (e.g. '
                      '"Transmission Electron Microscopy").'],
         'domain_of': ['InformationEntity', 'Activity'],
         'status': 'Draft'} })
    supporting_methods: Optional[list[str]] = Field(default=None, description="""Specific methods that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['These may include methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity - e.g. '
                      'methods used to produce data that was interpreted as evidence '
                      'to generate a Statement of knowledge.',
                      'This field captures terms representing specific INSTANCES of '
                      "methods applied, vs the 'supporting_method_types' attribute "
                      'which captures TYPES of methods used.'],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    supporting_method_types: Optional[list[Coding]] = Field(default=None, description="""Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This field captures terms representing TYPES of methods '
                      "applied, vs the 'specified_by' or'supporting_methods' "
                      'attributes which capture specific INSTANCES of methods used. '
                      'These may include types of methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity',
                      'Implementers should define a relevant source or set of method '
                      'type codes/terms to use here, based on the needs of the domain '
                      "or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    derived_from: Optional[list[InformationEntity]] = Field(default=None, description="""Another Information Entity from which this Information Entity is derived, in whole or in part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity'], 'status': 'Draft'} })
    reported_in: Optional[list[str]] = Field(default=None, description="""A document in which the Information Entity is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is used specifically to reference '
                      'documents/publications where the Information Entity is '
                      'expressed or reported.  For a Statement, this might be a '
                      'publication where the authors express the statement in text. '
                      'For a Data Item, this might be a publication with a table or '
                      'figure that reports the value of the  data.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    sources: Optional[list[str]] = Field(default=None, description="""A document or other informtion resource in which the information entity, or evidence supporting it, is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is more general than '
                      'InformationEntity.reported_in (which is used to references a '
                      'Docuement that directly reports the infrormation), and '
                      'Statement.has_evidence_from_sources (which is used to reference '
                      'resources that provided evidence used to generate the knowledge '
                      'expressed in a Statement). It can be used to cover both cases, '
                      'in situations where a data provider does not know which is the '
                      'case, or does not wish to make the distinction.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    information_quality: Optional[Coding] = Field(default=None, description="""A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.""", json_schema_extra = { "linkml_meta": {'comments': ['This is typically based on the quality of design and execution '
                      'of the study or curation activity that generated it (e.g. were '
                      'relevant controls assessed to show instruments were working, '
                      'were all samples taken care of and handled identically, are '
                      'methods sound and well documented, etc.).',
                      'The quality of information is intrinsic to the information '
                      'itself, and not to a particular application of the information '
                      '(e.g. as evidence for making an Assertion)',
                      'The quality of information is one factor that goes into the '
                      "confidence we have in the information''s veracity (i.e. that it "
                      'is an accurate reflection of reality it intends to measure or '
                      'describe). Other factors informing confidence may include who '
                      'did it (we may just not trust some Agents), when (if data '
                      'created 500 years ago, we may have less confidence in it), and '
                      'for Assertions, the relevance and abundance of supporting '
                      'evidence.',
                      'Implementers should define a relevant source of codes or terms '
                      "to use here, based on the needs of the domain or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    record_metadata: Optional[RecordMetadata] = Field(default=None, description="""Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds a structured RecordMetadata objects, which '
                      'can be used to capture when, how, and by whom a record '
                      'serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class Method(InformationEntity):
    """
    A set of instructions that specify how to achieve some objective.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['In scientific research, these include things like experimental '
                      'protocols, study designs, data analysis parameters,  curation '
                      'guidelines, cohort selection criteria, and rule sets.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'title': 'Method'})

    subtype: Optional[Coding] = Field(default=None, description="""A specific type of method that a Method instance represents (e.g. 'Variant Interpretation Guideline', or 'Experimental Protocol').""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute can be used to report a specific type for the '
                      'Method, in cases where a model does not define Method '
                      'subclasses for this purpose.  Implementers can define their own '
                      'set of method type codes/terms, to match the needs of the '
                      'domain or application.'],
         'domain_of': ['Method',
                       'Document',
                       'DataItem',
                       'DataSet',
                       'Activity',
                       'Agent',
                       'EvidenceLine'],
         'status': 'Draft'} })
    urls: Optional[list[str]] = Field(default=None, description="""The URL/web address from which the Method can be retrieved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method', 'Document'], 'status': 'Informative'} })
    is_about: Optional[list[str]] = Field(default=None, description="""An entity or concept in the world that the information entity describes/is about.""", json_schema_extra = { "linkml_meta": {'comments': ['e.g. In the context of a Statement object, this attribute may '
                      'be used to indicate entities/concepts it is about, in lieu of '
                      'providing a more precise description of what the Statement '
                      'asserts to be true using subject, predicate, object, and '
                      'qualifier properties. e.g. the Statement that "BRCA2 c.8023A>G '
                      'is pathogenic for Breast Cancer" might be annotated to be about '
                      "the variant 'BRCA2 c.8023A>G', and the disease 'Breast "
                      "Cancer'."],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds one or more Contribution objects, which '
                      'provide structured descriptions of a contribution made to the '
                      'Information Entity by a particular agent.'],
         'domain_of': ['InformationEntity', 'RecordMetadata'],
         'status': 'Draft'} })
    date_authored: Optional[str] = Field(default=None, description="""Indicates when the information content expressed in the Information Entity was generated.""", json_schema_extra = { "linkml_meta": {'comments': ["The term 'authored' as used in the model refers to the "
                      "generation of 'information content' in the abstract  sense, as "
                      'opposed to a concrete encoding of this information in a '
                      'specific language or format. e.g. for a Statement, this '
                      'attribute captures when the information content expressed in '
                      'the Statement was first generated by an agent.  Information '
                      'about when a particular concrete encoding of this information '
                      'was created (e.g. as row in a table, or object in a json '
                      'document) would live in a RecordMetadata object attached to the '
                      'Information Entity).'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    specified_by: Optional[list[str]] = Field(default=None, description="""A specification that describes all or part of the process that led to creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples - an experimental protocol or data analysis '
                      'specification that describe how data were generated, or an '
                      'evidence interpretation guideline that describes steps taken to '
                      'interpret data in making a variant pathogenicity '
                      'classification.',
                      'Note that this attribute captures specific *instances* of '
                      'specifications/methods (e.g. the specific electron microscopy '
                      'method described in https://doi.org/10.1002/ cpz1.1045) - as '
                      'opposed to reporting a *type* of method applied (e.g. '
                      '"Transmission Electron Microscopy").'],
         'domain_of': ['InformationEntity', 'Activity'],
         'status': 'Draft'} })
    supporting_methods: Optional[list[str]] = Field(default=None, description="""Specific methods that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['These may include methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity - e.g. '
                      'methods used to produce data that was interpreted as evidence '
                      'to generate a Statement of knowledge.',
                      'This field captures terms representing specific INSTANCES of '
                      "methods applied, vs the 'supporting_method_types' attribute "
                      'which captures TYPES of methods used.'],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    supporting_method_types: Optional[list[Coding]] = Field(default=None, description="""Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This field captures terms representing TYPES of methods '
                      "applied, vs the 'specified_by' or'supporting_methods' "
                      'attributes which capture specific INSTANCES of methods used. '
                      'These may include types of methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity',
                      'Implementers should define a relevant source or set of method '
                      'type codes/terms to use here, based on the needs of the domain '
                      "or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    derived_from: Optional[list[InformationEntity]] = Field(default=None, description="""Another Information Entity from which this Information Entity is derived, in whole or in part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity'], 'status': 'Draft'} })
    reported_in: Optional[list[str]] = Field(default=None, description="""A document in which the Information Entity is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is used specifically to reference '
                      'documents/publications where the Information Entity is '
                      'expressed or reported.  For a Statement, this might be a '
                      'publication where the authors express the statement in text. '
                      'For a Data Item, this might be a publication with a table or '
                      'figure that reports the value of the  data.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    sources: Optional[list[str]] = Field(default=None, description="""A document or other informtion resource in which the information entity, or evidence supporting it, is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is more general than '
                      'InformationEntity.reported_in (which is used to references a '
                      'Docuement that directly reports the infrormation), and '
                      'Statement.has_evidence_from_sources (which is used to reference '
                      'resources that provided evidence used to generate the knowledge '
                      'expressed in a Statement). It can be used to cover both cases, '
                      'in situations where a data provider does not know which is the '
                      'case, or does not wish to make the distinction.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    information_quality: Optional[Coding] = Field(default=None, description="""A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.""", json_schema_extra = { "linkml_meta": {'comments': ['This is typically based on the quality of design and execution '
                      'of the study or curation activity that generated it (e.g. were '
                      'relevant controls assessed to show instruments were working, '
                      'were all samples taken care of and handled identically, are '
                      'methods sound and well documented, etc.).',
                      'The quality of information is intrinsic to the information '
                      'itself, and not to a particular application of the information '
                      '(e.g. as evidence for making an Assertion)',
                      'The quality of information is one factor that goes into the '
                      "confidence we have in the information''s veracity (i.e. that it "
                      'is an accurate reflection of reality it intends to measure or '
                      'describe). Other factors informing confidence may include who '
                      'did it (we may just not trust some Agents), when (if data '
                      'created 500 years ago, we may have less confidence in it), and '
                      'for Assertions, the relevance and abundance of supporting '
                      'evidence.',
                      'Implementers should define a relevant source of codes or terms '
                      "to use here, based on the needs of the domain or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    record_metadata: Optional[RecordMetadata] = Field(default=None, description="""Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds a structured RecordMetadata objects, which '
                      'can be used to capture when, how, and by whom a record '
                      'serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class Document(InformationEntity):
    """
    A collection of information, usually in a text-based or graphic human-readable form, intended to be read and understood together as a whole.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['As an abstract InformationEntity, a Document instance is '
                      'defined by the informational content it conveys, not a '
                      'particular physical concretization of this information. A '
                      'single Document instance can simultaneously be concretized in '
                      'different languages, formats, and physical mediums.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Document'})

    subtype: Optional[Coding] = Field(default=None, description="""A specific type of document that a Document instance represents (e.g.  'publication', 'patent', 'pathology report')""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute can be used to report a specific type for the '
                      'Document, in cases where a model does not define Document '
                      'subclasses for this purpose.  Implementers can define their own '
                      'set of document type codes/terms, to match the needs of the '
                      'domain or application.'],
         'domain_of': ['Method',
                       'Document',
                       'DataItem',
                       'DataSet',
                       'Activity',
                       'Agent',
                       'EvidenceLine'],
         'status': 'Draft'} })
    title: Optional[str] = Field(default=None, description="""The official title given to the document by its authors.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Document']} })
    urls: Optional[list[str]] = Field(default=None, description="""One or more URLs from which the content of the Document can be retrieved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method', 'Document'], 'status': 'Draft'} })
    pmid: Optional[str] = Field(default=None, description="""A `PubMed unique identifier <https://en.wikipedia.org/wiki/PubMed#PubMed_identifier>`_ for the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Document'], 'status': 'Draft'} })
    doi: Optional[str] = Field(default=None, description="""A `Digital Object Identifier <https://www.doi.org/the-identifier/what-is-a-doi/>_` for the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Document'], 'status': 'Draft'} })
    license: Optional[str] = Field(default=None, description="""A specific license that dictates legal permissions for how a document can be used (by whom, where, for what purposes, with what additional requirements, etc.)""", json_schema_extra = { "linkml_meta": {'comments': ['Where possible, provide a URL pointing to the license or a '
                      'description of it (e.g. '
                      '"https://creativecommons.org/licenses/by/4.0/"). Otherwise, '
                      'provide a free-text name or description of the license (e.g. '
                      '"CC-BY").'],
         'domain_of': ['Document', 'DataSet'],
         'status': 'Informative'} })
    is_about: Optional[list[str]] = Field(default=None, description="""An entity or concept in the world that the information entity describes/is about.""", json_schema_extra = { "linkml_meta": {'comments': ['e.g. In the context of a Statement object, this attribute may '
                      'be used to indicate entities/concepts it is about, in lieu of '
                      'providing a more precise description of what the Statement '
                      'asserts to be true using subject, predicate, object, and '
                      'qualifier properties. e.g. the Statement that "BRCA2 c.8023A>G '
                      'is pathogenic for Breast Cancer" might be annotated to be about '
                      "the variant 'BRCA2 c.8023A>G', and the disease 'Breast "
                      "Cancer'."],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds one or more Contribution objects, which '
                      'provide structured descriptions of a contribution made to the '
                      'Information Entity by a particular agent.'],
         'domain_of': ['InformationEntity', 'RecordMetadata'],
         'status': 'Draft'} })
    date_authored: Optional[str] = Field(default=None, description="""Indicates when the information content expressed in the Information Entity was generated.""", json_schema_extra = { "linkml_meta": {'comments': ["The term 'authored' as used in the model refers to the "
                      "generation of 'information content' in the abstract  sense, as "
                      'opposed to a concrete encoding of this information in a '
                      'specific language or format. e.g. for a Statement, this '
                      'attribute captures when the information content expressed in '
                      'the Statement was first generated by an agent.  Information '
                      'about when a particular concrete encoding of this information '
                      'was created (e.g. as row in a table, or object in a json '
                      'document) would live in a RecordMetadata object attached to the '
                      'Information Entity).'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    specified_by: Optional[list[str]] = Field(default=None, description="""A specification that describes all or part of the process that led to creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples - an experimental protocol or data analysis '
                      'specification that describe how data were generated, or an '
                      'evidence interpretation guideline that describes steps taken to '
                      'interpret data in making a variant pathogenicity '
                      'classification.',
                      'Note that this attribute captures specific *instances* of '
                      'specifications/methods (e.g. the specific electron microscopy '
                      'method described in https://doi.org/10.1002/ cpz1.1045) - as '
                      'opposed to reporting a *type* of method applied (e.g. '
                      '"Transmission Electron Microscopy").'],
         'domain_of': ['InformationEntity', 'Activity'],
         'status': 'Draft'} })
    supporting_methods: Optional[list[str]] = Field(default=None, description="""Specific methods that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['These may include methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity - e.g. '
                      'methods used to produce data that was interpreted as evidence '
                      'to generate a Statement of knowledge.',
                      'This field captures terms representing specific INSTANCES of '
                      "methods applied, vs the 'supporting_method_types' attribute "
                      'which captures TYPES of methods used.'],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    supporting_method_types: Optional[list[Coding]] = Field(default=None, description="""Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This field captures terms representing TYPES of methods '
                      "applied, vs the 'specified_by' or'supporting_methods' "
                      'attributes which capture specific INSTANCES of methods used. '
                      'These may include types of methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity',
                      'Implementers should define a relevant source or set of method '
                      'type codes/terms to use here, based on the needs of the domain '
                      "or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    derived_from: Optional[list[InformationEntity]] = Field(default=None, description="""Another Information Entity from which this Information Entity is derived, in whole or in part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity'], 'status': 'Draft'} })
    reported_in: Optional[list[str]] = Field(default=None, description="""A document in which the Information Entity is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is used specifically to reference '
                      'documents/publications where the Information Entity is '
                      'expressed or reported.  For a Statement, this might be a '
                      'publication where the authors express the statement in text. '
                      'For a Data Item, this might be a publication with a table or '
                      'figure that reports the value of the  data.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    sources: Optional[list[str]] = Field(default=None, description="""A document or other informtion resource in which the information entity, or evidence supporting it, is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is more general than '
                      'InformationEntity.reported_in (which is used to references a '
                      'Docuement that directly reports the infrormation), and '
                      'Statement.has_evidence_from_sources (which is used to reference '
                      'resources that provided evidence used to generate the knowledge '
                      'expressed in a Statement). It can be used to cover both cases, '
                      'in situations where a data provider does not know which is the '
                      'case, or does not wish to make the distinction.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    information_quality: Optional[Coding] = Field(default=None, description="""A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.""", json_schema_extra = { "linkml_meta": {'comments': ['This is typically based on the quality of design and execution '
                      'of the study or curation activity that generated it (e.g. were '
                      'relevant controls assessed to show instruments were working, '
                      'were all samples taken care of and handled identically, are '
                      'methods sound and well documented, etc.).',
                      'The quality of information is intrinsic to the information '
                      'itself, and not to a particular application of the information '
                      '(e.g. as evidence for making an Assertion)',
                      'The quality of information is one factor that goes into the '
                      "confidence we have in the information''s veracity (i.e. that it "
                      'is an accurate reflection of reality it intends to measure or '
                      'describe). Other factors informing confidence may include who '
                      'did it (we may just not trust some Agents), when (if data '
                      'created 500 years ago, we may have less confidence in it), and '
                      'for Assertions, the relevance and abundance of supporting '
                      'evidence.',
                      'Implementers should define a relevant source of codes or terms '
                      "to use here, based on the needs of the domain or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    record_metadata: Optional[RecordMetadata] = Field(default=None, description="""Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds a structured RecordMetadata objects, which '
                      'can be used to capture when, how, and by whom a record '
                      'serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class DataItem(InformationEntity):
    """
    An Information Entity representing an individual piece of data, generated or acquired through methods which reliably produce truthful information about something.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Examples include raw observations or measurements such as an '
                      "allele count, or patient's weight, derived calculations such as "
                      'frequency or mean, and computed statistical scores/metrics such '
                      'as p-values and z-scores.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Informative',
         'title': 'Data Item'})

    subtype: Optional[Coding] = Field(default=None, description="""A specific type of data the DataItem instance represents (e.g. a 'specimen count', a 'patient weight', an 'allele frequency', a 'p-value')""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute can be used to report a specific type for the '
                      'DataItem, in cases where a model does not define DataItem '
                      'subclasses for this purpose.  Implementers can define their own '
                      'set of data item type codes/terms, to match the needs of the '
                      'domain or application.'],
         'domain_of': ['Method',
                       'Document',
                       'DataItem',
                       'DataSet',
                       'Activity',
                       'Agent',
                       'EvidenceLine'],
         'status': 'Informative'} })
    value: str = Field(default=..., description="""The value of the data item (could be quantitative or qualitative depending on the type of data item).""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataItem', 'Qualifier', 'Expression', 'Extension'],
         'status': 'Informative'} })
    unit: Optional[Coding] = Field(default=None, description="""A unit of measure for the value (e.g. meters, grams, fluorescent units, seconds, mg/ml, etc.)""", json_schema_extra = { "linkml_meta": {'comments': ['Implementers should define a relevant source or specific set of '
                      'unit terms/codes to use here based on the needs of the domain '
                      'or application.'],
         'domain_of': ['DataItem'],
         'status': 'Informative'} })
    variability_measures: Optional[list[DataItem]] = Field(default=None, description="""A statistical score describing the variability inherent in a data item representing a statistical summary of a set of observations/measurements (e.g. the standard deviation associated with a statistical mean calculated across several experimental replicates).""", json_schema_extra = { "linkml_meta": {'comments': ['Examples of statistical measures of variability include an '
                      'Interquartile Range, Variance, Standard Deviation, Standard '
                      'Error. The type of variability measure used here represents '
                      'should be reported in the DataItem instance created to '
                      'represent it.'],
         'domain_of': ['DataItem'],
         'status': 'Informative'} })
    confidence_interval: Optional[DataItem] = Field(default=None, description="""A measure of the probability that a parameter of interest will fall within a defined range of values around a mean or other statistical calculation.""", json_schema_extra = { "linkml_meta": {'comments': ['Confidence intervals reflect the degree of uncertainty in a '
                      'sampling method. They may be bounded on one or both sides, and '
                      'are  computed for a designated confidence level (most often 95% '
                      'or 99%.. For example, a Hazard Ratio of 0.47 might have a 95% '
                      'confidence interval between 0.42 and 0.55, with a p-value of = '
                      '0.001.',
                      'The DataItem used to represent a confidence interval will '
                      "indicate what type of interval is reported (e.g. ''95% CI''), "
                      'and will contain separate componentDataItems representing the '
                      "upper and lower bounds of the interval (e.g. ''0.42'' and "
                      "''0.55'').'"],
         'domain_of': ['DataItem'],
         'status': 'Informative'} })
    component_data_item: Optional[list[DataItem]] = Field(default=None, description="""A more foundational data item that is a logical component of a compound data item.""", json_schema_extra = { "linkml_meta": {'comments': ["Examples of 'compound' data items with component parts include "
                      'a confidence interval, which is comprised of data items '
                      'representing its lower and upper bounds,  or a blood pressure '
                      'reading, which is comprised of separate systolic and diastolic '
                      'measurements.'],
         'domain_of': ['DataItem'],
         'status': 'Informative'} })
    is_about: Optional[list[str]] = Field(default=None, description="""An entity or concept in the world that the information entity describes/is about.""", json_schema_extra = { "linkml_meta": {'comments': ['e.g. In the context of a Statement object, this attribute may '
                      'be used to indicate entities/concepts it is about, in lieu of '
                      'providing a more precise description of what the Statement '
                      'asserts to be true using subject, predicate, object, and '
                      'qualifier properties. e.g. the Statement that "BRCA2 c.8023A>G '
                      'is pathogenic for Breast Cancer" might be annotated to be about '
                      "the variant 'BRCA2 c.8023A>G', and the disease 'Breast "
                      "Cancer'."],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds one or more Contribution objects, which '
                      'provide structured descriptions of a contribution made to the '
                      'Information Entity by a particular agent.'],
         'domain_of': ['InformationEntity', 'RecordMetadata'],
         'status': 'Draft'} })
    date_authored: Optional[str] = Field(default=None, description="""Indicates when the information content expressed in the Information Entity was generated.""", json_schema_extra = { "linkml_meta": {'comments': ["The term 'authored' as used in the model refers to the "
                      "generation of 'information content' in the abstract  sense, as "
                      'opposed to a concrete encoding of this information in a '
                      'specific language or format. e.g. for a Statement, this '
                      'attribute captures when the information content expressed in '
                      'the Statement was first generated by an agent.  Information '
                      'about when a particular concrete encoding of this information '
                      'was created (e.g. as row in a table, or object in a json '
                      'document) would live in a RecordMetadata object attached to the '
                      'Information Entity).'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    specified_by: Optional[list[str]] = Field(default=None, description="""A specification that describes all or part of the process that led to creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples - an experimental protocol or data analysis '
                      'specification that describe how data were generated, or an '
                      'evidence interpretation guideline that describes steps taken to '
                      'interpret data in making a variant pathogenicity '
                      'classification.',
                      'Note that this attribute captures specific *instances* of '
                      'specifications/methods (e.g. the specific electron microscopy '
                      'method described in https://doi.org/10.1002/ cpz1.1045) - as '
                      'opposed to reporting a *type* of method applied (e.g. '
                      '"Transmission Electron Microscopy").'],
         'domain_of': ['InformationEntity', 'Activity'],
         'status': 'Draft'} })
    supporting_methods: Optional[list[str]] = Field(default=None, description="""Specific methods that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['These may include methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity - e.g. '
                      'methods used to produce data that was interpreted as evidence '
                      'to generate a Statement of knowledge.',
                      'This field captures terms representing specific INSTANCES of '
                      "methods applied, vs the 'supporting_method_types' attribute "
                      'which captures TYPES of methods used.'],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    supporting_method_types: Optional[list[Coding]] = Field(default=None, description="""Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This field captures terms representing TYPES of methods '
                      "applied, vs the 'specified_by' or'supporting_methods' "
                      'attributes which capture specific INSTANCES of methods used. '
                      'These may include types of methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity',
                      'Implementers should define a relevant source or set of method '
                      'type codes/terms to use here, based on the needs of the domain '
                      "or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    derived_from: Optional[list[InformationEntity]] = Field(default=None, description="""Another Information Entity from which this Information Entity is derived, in whole or in part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity'], 'status': 'Draft'} })
    reported_in: Optional[list[str]] = Field(default=None, description="""A document in which the Information Entity is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is used specifically to reference '
                      'documents/publications where the Information Entity is '
                      'expressed or reported.  For a Statement, this might be a '
                      'publication where the authors express the statement in text. '
                      'For a Data Item, this might be a publication with a table or '
                      'figure that reports the value of the  data.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    sources: Optional[list[str]] = Field(default=None, description="""A document or other informtion resource in which the information entity, or evidence supporting it, is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is more general than '
                      'InformationEntity.reported_in (which is used to references a '
                      'Docuement that directly reports the infrormation), and '
                      'Statement.has_evidence_from_sources (which is used to reference '
                      'resources that provided evidence used to generate the knowledge '
                      'expressed in a Statement). It can be used to cover both cases, '
                      'in situations where a data provider does not know which is the '
                      'case, or does not wish to make the distinction.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    information_quality: Optional[Coding] = Field(default=None, description="""A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.""", json_schema_extra = { "linkml_meta": {'comments': ['This is typically based on the quality of design and execution '
                      'of the study or curation activity that generated it (e.g. were '
                      'relevant controls assessed to show instruments were working, '
                      'were all samples taken care of and handled identically, are '
                      'methods sound and well documented, etc.).',
                      'The quality of information is intrinsic to the information '
                      'itself, and not to a particular application of the information '
                      '(e.g. as evidence for making an Assertion)',
                      'The quality of information is one factor that goes into the '
                      "confidence we have in the information''s veracity (i.e. that it "
                      'is an accurate reflection of reality it intends to measure or '
                      'describe). Other factors informing confidence may include who '
                      'did it (we may just not trust some Agents), when (if data '
                      'created 500 years ago, we may have less confidence in it), and '
                      'for Assertions, the relevance and abundance of supporting '
                      'evidence.',
                      'Implementers should define a relevant source of codes or terms '
                      "to use here, based on the needs of the domain or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    record_metadata: Optional[RecordMetadata] = Field(default=None, description="""Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds a structured RecordMetadata objects, which '
                      'can be used to capture when, how, and by whom a record '
                      'serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class DataSet(InformationEntity):
    """
    A collection of related data items or records that are organized together in a common format or structure, to enable their computational manipulation as a unit.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Instances of this class represent a *specific version* of a '
                      'given dataset. Examples include the  gnomAD version 3.1.2 '
                      'dataset carrying allele population frequencies, or a specific '
                      'version of a VCF file that describes variations observed in a '
                      'particular patient and various annotations made on them, or a '
                      'SIFT dataset of computational predictions functional impact for '
                      'a set of variants.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Data Set'})

    subtype: Optional[Coding] = Field(default=None, description="""A specific type of data set the DataSet instance represents (e.g. a 'clinical data set', a 'sequencing data set', a 'gene expression data set', a 'genome annotation data set').""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute can be used to report a specific type for the '
                      'DataSet, in cases where a model does not define DataSet '
                      'subclasses for this purpose.  Implementers can define their own '
                      'set of data set type codes/terms, to match the needs of the '
                      'domain or application.'],
         'domain_of': ['Method',
                       'Document',
                       'DataItem',
                       'DataSet',
                       'Activity',
                       'Agent',
                       'EvidenceLine'],
         'status': 'Informative'} })
    release_date: Optional[str] = Field(default=None, description="""Indicates when a version of a DataSet was formally released.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute may apply to version and distribution-level '
                      'DataSet representations. It refers to when the data set was '
                      'released, which may be different than the data set was '
                      'generated.'],
         'domain_of': ['DataSet'],
         'status': 'Informative'} })
    version: Optional[str] = Field(default=None, description="""The version of the DataSet, as assigned by its creator.""", json_schema_extra = { "linkml_meta": {'comments': ['This property can capture version information for resources '
                      'such as data sets and documents that get published and released '
                      'as a unit for community use. These may go through rounds of '
                      "revisions that add or modify content, but don't change the "
                      'identity of the resource. Use this attribute in cases where '
                      'version is not reflected in an identifier associated with the '
                      'data set'],
         'domain_of': ['DataSet'],
         'status': 'Informative'} })
    license: Optional[str] = Field(default=None, description="""A specific license that dictates legal permissions for how a data set can be used (by whom, where, for what purposes, with what additional requirements, etc.).""", json_schema_extra = { "linkml_meta": {'comments': ['Where possible, provide a URL pointing to the license or a '
                      'description of it (e.g. '
                      '"https://creativecommons.org/licenses/by/4.0/"). Otherwise, '
                      'provide a free-text name or description of the license (e.g. '
                      '"CC-BY").'],
         'domain_of': ['Document', 'DataSet'],
         'status': 'Informative'} })
    is_about: Optional[list[str]] = Field(default=None, description="""An entity or concept in the world that the information entity describes/is about.""", json_schema_extra = { "linkml_meta": {'comments': ['e.g. In the context of a Statement object, this attribute may '
                      'be used to indicate entities/concepts it is about, in lieu of '
                      'providing a more precise description of what the Statement '
                      'asserts to be true using subject, predicate, object, and '
                      'qualifier properties. e.g. the Statement that "BRCA2 c.8023A>G '
                      'is pathogenic for Breast Cancer" might be annotated to be about '
                      "the variant 'BRCA2 c.8023A>G', and the disease 'Breast "
                      "Cancer'."],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds one or more Contribution objects, which '
                      'provide structured descriptions of a contribution made to the '
                      'Information Entity by a particular agent.'],
         'domain_of': ['InformationEntity', 'RecordMetadata'],
         'status': 'Draft'} })
    date_authored: Optional[str] = Field(default=None, description="""Indicates when the information content expressed in the Information Entity was generated.""", json_schema_extra = { "linkml_meta": {'comments': ["The term 'authored' as used in the model refers to the "
                      "generation of 'information content' in the abstract  sense, as "
                      'opposed to a concrete encoding of this information in a '
                      'specific language or format. e.g. for a Statement, this '
                      'attribute captures when the information content expressed in '
                      'the Statement was first generated by an agent.  Information '
                      'about when a particular concrete encoding of this information '
                      'was created (e.g. as row in a table, or object in a json '
                      'document) would live in a RecordMetadata object attached to the '
                      'Information Entity).'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    specified_by: Optional[list[str]] = Field(default=None, description="""A specification that describes all or part of the process that led to creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples - an experimental protocol or data analysis '
                      'specification that describe how data were generated, or an '
                      'evidence interpretation guideline that describes steps taken to '
                      'interpret data in making a variant pathogenicity '
                      'classification.',
                      'Note that this attribute captures specific *instances* of '
                      'specifications/methods (e.g. the specific electron microscopy '
                      'method described in https://doi.org/10.1002/ cpz1.1045) - as '
                      'opposed to reporting a *type* of method applied (e.g. '
                      '"Transmission Electron Microscopy").'],
         'domain_of': ['InformationEntity', 'Activity'],
         'status': 'Draft'} })
    supporting_methods: Optional[list[str]] = Field(default=None, description="""Specific methods that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['These may include methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity - e.g. '
                      'methods used to produce data that was interpreted as evidence '
                      'to generate a Statement of knowledge.',
                      'This field captures terms representing specific INSTANCES of '
                      "methods applied, vs the 'supporting_method_types' attribute "
                      'which captures TYPES of methods used.'],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    supporting_method_types: Optional[list[Coding]] = Field(default=None, description="""Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This field captures terms representing TYPES of methods '
                      "applied, vs the 'specified_by' or'supporting_methods' "
                      'attributes which capture specific INSTANCES of methods used. '
                      'These may include types of methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity',
                      'Implementers should define a relevant source or set of method '
                      'type codes/terms to use here, based on the needs of the domain '
                      "or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    derived_from: Optional[list[InformationEntity]] = Field(default=None, description="""Another Information Entity from which this Information Entity is derived, in whole or in part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity'], 'status': 'Draft'} })
    reported_in: Optional[list[str]] = Field(default=None, description="""A document in which the Information Entity is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is used specifically to reference '
                      'documents/publications where the Information Entity is '
                      'expressed or reported.  For a Statement, this might be a '
                      'publication where the authors express the statement in text. '
                      'For a Data Item, this might be a publication with a table or '
                      'figure that reports the value of the  data.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    sources: Optional[list[str]] = Field(default=None, description="""A document or other informtion resource in which the information entity, or evidence supporting it, is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is more general than '
                      'InformationEntity.reported_in (which is used to references a '
                      'Docuement that directly reports the infrormation), and '
                      'Statement.has_evidence_from_sources (which is used to reference '
                      'resources that provided evidence used to generate the knowledge '
                      'expressed in a Statement). It can be used to cover both cases, '
                      'in situations where a data provider does not know which is the '
                      'case, or does not wish to make the distinction.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    information_quality: Optional[Coding] = Field(default=None, description="""A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.""", json_schema_extra = { "linkml_meta": {'comments': ['This is typically based on the quality of design and execution '
                      'of the study or curation activity that generated it (e.g. were '
                      'relevant controls assessed to show instruments were working, '
                      'were all samples taken care of and handled identically, are '
                      'methods sound and well documented, etc.).',
                      'The quality of information is intrinsic to the information '
                      'itself, and not to a particular application of the information '
                      '(e.g. as evidence for making an Assertion)',
                      'The quality of information is one factor that goes into the '
                      "confidence we have in the information''s veracity (i.e. that it "
                      'is an accurate reflection of reality it intends to measure or '
                      'describe). Other factors informing confidence may include who '
                      'did it (we may just not trust some Agents), when (if data '
                      'created 500 years ago, we may have less confidence in it), and '
                      'for Assertions, the relevance and abundance of supporting '
                      'evidence.',
                      'Implementers should define a relevant source of codes or terms '
                      "to use here, based on the needs of the domain or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    record_metadata: Optional[RecordMetadata] = Field(default=None, description="""Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds a structured RecordMetadata objects, which '
                      'can be used to capture when, how, and by whom a record '
                      'serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class Activity(Entity):
    """
    An action or set of actions performed by an agent, that occurs over a period of time. Activities may use, generate, modify, move, or destroy one or more entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Activities relevant to scientific knowledge generation, and '
                      'include things like observations of the natural world, '
                      'designing and performing experiments, data analysis and '
                      'transformation, publishing research results, data curation and '
                      'interpretation, and assessment and care of patients in clinical '
                      'settings.  These activities may produce information that gets '
                      'encoded in sharable artifacts which are used to generate '
                      'scientific knowledge. Agents can play different types of roles '
                      'in the generation and use of such artifacts.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Informative',
         'title': 'Activity'})

    subtype: Optional[Coding] = Field(default=None, description="""A specific type of activity the Activity instance represents.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute can be used to report a specific type for the '
                      'Activity, in cases where a model does not define Activity '
                      'subclasses for this purpose.  Implementers can define their own '
                      'set of data set type codes/terms, to match the needs of the '
                      'domain or application.'],
         'domain_of': ['Method',
                       'Document',
                       'DataItem',
                       'DataSet',
                       'Activity',
                       'Agent',
                       'EvidenceLine'],
         'status': 'Informative'} })
    date: Optional[date] = Field(default=None, description="""The date that the Activity was completed.""", json_schema_extra = { "linkml_meta": {'comments': ['By convention, populate this attribute with the date the '
                      'activity was completed (e.g.  in cases where the activity spans '
                      'multiple days). The date SHOULD be formatted as a date string '
                      'in ISO format "YYYY-MM-DD".'],
         'domain_of': ['Activity'],
         'status': 'Draft'} })
    performed_by: Optional[list[Agent]] = Field(default=None, description="""An Agent who participated in executing the Activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'status': 'Draft'} })
    specified_by: Optional[list[Method]] = Field(default=None, description="""A method that was followed in performing an Activity, that describes how it was executed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity', 'Activity'], 'status': 'Informative'} })
    input: Optional[list[Entity]] = Field(default=None, description="""An entity that was input into the Activity (could be material or information)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'status': 'Informative'} })
    output: Optional[list[Entity]] = Field(default=None, description="""An entity that was output from the Activity (could be material or information)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'status': 'Informative'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class Contribution(Activity):
    """
    An action or actions taken by a particular agent in the creation, modification, assessment, or deprecation of some entity (e.g. a Statement, Evidence Line, DataSet, Publication, etc.).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Contributions are used to organize information about when, '
                      'where, how (e.g. what roles were played), and on whose behalf '
                      'these actions were performed.',
                      'The scope of a Contribution instance includes only the actions '
                      'of a single agent in contributing to a single artifact, which '
                      'may be performed in one continuous effort, or several '
                      'discontinuous sessions of work.  The agent can be an individual '
                      'person, a software agent, or a group or organization of '
                      "individuals acting together.'"],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Contribution'})

    contributor: Optional[Agent] = Field(default=None, description="""The Agent that made the contribution.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that this must be a single agent (which can be a Person, '
                      'or an Organization).  If multiple Agents contributed to an '
                      'entity, a separate Contribution instances MUST be created for '
                      'each.'],
         'domain_of': ['Contribution'],
         'status': 'Draft'} })
    activity_type: Optional[list[Coding]] = Field(default=None, description="""The specific type of activity performed or role played by an agent in making the contribution (e.g. for a publication, agents may contribute as a primary author, editor, figure designer, data generator, etc. . Values of this property may be framed as activities or as contribution roles (e.g. using terms from the Contribution Role Ontology (CRO)).""", json_schema_extra = { "linkml_meta": {'comments': ['Each implementation can define terms for the specific types of '
                      'activities relevant to their use case/application. \\n- Note '
                      'that if the same Agent performed multiple types of activities '
                      'in contributing to some artifact, they may all be captured in a '
                      'single Contribution object. However, if data creators want to '
                      'provide metadata specific to each activity (e.g. when or how '
                      'each was performed), then a separate Contribution object should '
                      'be created for each activity.'],
         'domain_of': ['Contribution'],
         'status': 'Draft'} })
    contribution_made_to: Optional[InformationEntity] = Field(default=None, description="""The artifact toward which the contribution was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Contribution'], 'status': 'Informative'} })
    subtype: Optional[Coding] = Field(default=None, description="""A specific type of activity the Activity instance represents.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute can be used to report a specific type for the '
                      'Activity, in cases where a model does not define Activity '
                      'subclasses for this purpose.  Implementers can define their own '
                      'set of data set type codes/terms, to match the needs of the '
                      'domain or application.'],
         'domain_of': ['Method',
                       'Document',
                       'DataItem',
                       'DataSet',
                       'Activity',
                       'Agent',
                       'EvidenceLine'],
         'status': 'Informative'} })
    date: Optional[date] = Field(default=None, description="""The date that the Activity was completed.""", json_schema_extra = { "linkml_meta": {'comments': ['By convention, populate this attribute with the date the '
                      'activity was completed (e.g.  in cases where the activity spans '
                      'multiple days). The date SHOULD be formatted as a date string '
                      'in ISO format "YYYY-MM-DD".'],
         'domain_of': ['Activity'],
         'status': 'Draft'} })
    performed_by: Optional[list[Agent]] = Field(default=None, description="""An Agent who participated in executing the Activity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'status': 'Draft'} })
    specified_by: Optional[list[Method]] = Field(default=None, description="""A method that was followed in performing an Activity, that describes how it was executed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity', 'Activity'], 'status': 'Informative'} })
    input: Optional[list[Entity]] = Field(default=None, description="""An entity that was input into the Activity (could be material or information)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'status': 'Informative'} })
    output: Optional[list[Entity]] = Field(default=None, description="""An entity that was output from the Activity (could be material or information)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Activity'], 'status': 'Informative'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class Agent(Entity):
    """
    An autonomous actor (person, organization, or software agent) that bears some form of responsibility for an activity taking place,  for the existence of an entity, or for another agent's activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Agents perform activities and make contributions to entities. '
                      'An agent can be an individual person, an organization of '
                      'multiple individuals acting together, or a computational agent '
                      'such as a software program or automated pipeline.',
                      'Agents can belong to organizations, and act on behalf or in the '
                      'context of an organizational affiliation when contributing to '
                      'an entity. For example, curators generating these variant '
                      'pathogenicity interpretations may do so in the context of their '
                      'work with the ClinGen organization, which provides '
                      'administrative, technical, and funding support for their '
                      'contributions.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Agent'})

    subtype: Optional[str] = Field(default=None, description="""A specific type of agent the Agent object represents. Must be one of {person, organization, software}""", json_schema_extra = { "linkml_meta": {'comments': ['At present, there are no subclasses in the model representing '
                      'the three high level types of Agent (person, organization, or '
                      'software). If it is determined that there are enough unique '
                      'properties that need to be defined for these subtypes, separate '
                      'classes may be defined in a future release.'],
         'domain_of': ['Method',
                       'Document',
                       'DataItem',
                       'DataSet',
                       'Activity',
                       'Agent',
                       'EvidenceLine'],
         'status': 'Draft'} })
    name: Optional[str] = Field(default=None, description="""The given name of the Agent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent', 'Qualifier', 'Extension', 'Characteristic'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class Statement(InformationEntity):
    """
    A claim of purported truth as made by a particular agent, on a particular occasion. Statements may be used to simply put forth a possible fact (i.e. a 'proposition') as true, or to provide a more nuanced assessment of the level of confidence or evidence supporting a particular proposition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Primary assertions of knowledge about some subject entity are '
                      'captured in self-contained Statement objects. Every Statement '
                      "puts forth a 'proposition' - a possible fact it assesses or "
                      'reports to be true.  The semantics of this proposition are '
                      "explicitly captured using 'subject', 'predicate', and 'object' "
                      "attributes, and optional 'qualifier' slots (SPOQ).",
                      'The model supports two " modes of use" for Statements, which '
                      'differ in what they say about their proposition, and can be '
                      "distinguished by whether 'direction' and 'strength' or 'score' "
                      'attributes are populated.',
                      'In "Assertion Mode" a Statement simply reports an SPOQ '
                      'proposition to be true (e.g. that "BRCA2 c.8023A>G is '
                      'pathogenic for Breast Cancer"), and \'direction\', '
                      "'strength', and 'score' attributes are not populated.  Thos "
                      'mode is used by project reporting conclusive assertions about a '
                      'domain of discourse, but not providing confidence or evidence '
                      'level assessments.',
                      'In "Proposition Assessment Mode" a Statement describes the '
                      'overall state of evidence and/or confidence surrounding the '
                      'SPOQ proposition - which may or may not be true. The '
                      "'direction' and 'strength' or 'score' attributes are populated, "
                      'which allows for Statements to report that "there is very '
                      "strong evidence supporting the proposition that 'BRCA2 "
                      'c.8023A>G is pathogenic for Breast Cancer\'", or "we have high '
                      "confidence that the proposition 'BRCA2 c.8023A>G is pathogenic "
                      'for Breast Cancer\' is false").  This mode is used in curation '
                      'projects to track the evolving state of support for '
                      'propositions of interest, as curators continue to collect '
                      'evidence and work toward a conclusive assertion.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Statement'})

    statement_text: Optional[str] = Field(default=None, description="""A natural-language expression of what a Statement asserts to be true.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute captures what a Statement says as human readable '
                      'free text. e.g. that "BRCA2 c.8023A>G is pathogenic for Breast '
                      'Cancer", or that "there is moderate evidence supporting the '
                      'pathogenicity of BRCA2 c.8023A>G for Breast Cancer". This '
                      'optional attribute can be used instead of, or as a complement '
                      'to, a structured representation of Statement semantics that '
                      'uses the subject-predicate-object-qualifier pattern.'],
         'domain_of': ['Statement'],
         'status': 'Draft'} })
    proposition: Optional[Proposition] = Field(default=None, description="""A possible fact that the Statement assesses or puts forth as true.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute supports an alternate modeling pattern where the '
                      'structured semantics of the possible fact asserted or evaluated '
                      "by a Statement is encapsulated in a separate 'Proposition' "
                      'object. In such a case, the subject-predicate-object-qualifier '
                      'properties on the Statement are not utilized. A given '
                      'implementation should decide which pattern to follow and drop '
                      'attributes not required for their approach.'],
         'domain_of': ['Statement'],
         'status': 'Informative'} })
    subject: Optional[str] = Field(default=None, description="""The Entity or concept about which the Statement is made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Statement', 'Proposition'], 'status': 'Draft'} })
    predicate: Optional[Coding] = Field(default=None, description="""The relationship declared to hold between the subject and the object of the Statement.""", json_schema_extra = { "linkml_meta": {'comments': ['When applied to represent a particular type of Statement (via '
                      "'Profiling'), implementers can define a value set of predicates "
                      'for the relationships relevant in the domain - ideally using '
                      'terms from community ontologies or terminologies. For example, '
                      "in a  'Variant Pathogenicity Statement' Profile, the predicate "
                      'value set might include terms from the GENO ontology defining  '
                      "'pathogenic for condition', 'benign for condition', and "
                      "'uncertain significance for condition' relationships "
                      '(GENO:0000840, GENO:0000843, GENO:0000845).'],
         'domain_of': ['Statement', 'Proposition'],
         'status': 'Draft'} })
    object: Optional[str] = Field(default=None, description="""An Entity or concept that is related to the subject of a Statement via its predicate.""", json_schema_extra = { "linkml_meta": {'comments': ['The object of a Statement can be any Entity or concept that is '
                      'related to the subject, e.g. for Genetic Variation subjects the '
                      'object is often a disease, drug, gene, molecular consequence, '
                      'functional impact on gene or protein.'],
         'domain_of': ['Statement', 'Proposition'],
         'status': 'Draft'} })
    qualifier: Optional[list[Qualifier]] = Field(default=None, description="""An additional piece of information that extends or refines the meaning of a Statement's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context.""", json_schema_extra = { "linkml_meta": {'comments': ['-The qualifier attribute allows representation of more complex, '
                      'n-ary statements that may not be accommodated by a simple '
                      'subject-predicate-object (SPO) triple. For example, if an SPO '
                      "triple asserts that 'Variant X' - predicts sensitivity to - "
                      "'Treatment Y', a qualifier can be used to indicate that this "
                      "applies in the context of a particular 'Disease Z'. Qualifiers "
                      'can also add information that quantifies aspects of a Statement '
                      "- e.g. for a Statement triple asserting that a 'Variant X'- "
                      "causes - 'Phenotype Y', a qualifier can be used to add "
                      'frequency/penetrance information that quantifies the percentage '
                      'of carriers in which the phenotype is observed to manifest. '
                      'Statement profiles may define more than one qualifier, as '
                      'needed to capture different types of qualifying information.',
                      "The SEPIO core model specifies use of a key-value 'Qualifier' "
                      'object to capture the meaning and value of each type of '
                      'qualifying information relevant for a given type of Statement. '
                      'But in practice, profiles for specific Statement types may '
                      'choose to define one or more specializations of the generic '
                      "'qualifier' property as named attributes. This makes the data "
                      'more succinct and parsable, and allows specific constraints to '
                      'be applied and validated for different qualifiers. For example, '
                      'a VariantPathogenicityStatement profile may define a named '
                      "'alleleOriginQualifier' attribute that is required, and a named "
                      "'geneContextQualifier' attribute that is optional - both of "
                      "which conceptually specialize the core-im 'qualifier' property. "
                      "Under this approach, the core 'qualifier' acts as a placeholder "
                      'to seed such specializations, but is not used directly in '
                      'Statement profiles.'],
         'domain_of': ['Statement', 'Proposition'],
         'status': 'Informative'} })
    direction: Optional[str] = Field(default=None, description="""A term indicating whether the Statement supports, disputes, or remains neutral w.r.t. the validity of the Proposition it evaluates.""", json_schema_extra = { "linkml_meta": {'comments': ['Statements put forth a Proposition that expresses some possible '
                      'fact about the world, and may provide an assessment of this '
                      "proposition's validity (i.e. how likely it is to be true or "
                      'false based on evaluated evidence). The semantics of the '
                      "Proposition are captured in the 'subject',  'predicate', "
                      "'object', and optional 'qualifier' attributes. An assessment of "
                      "the Proposition's validity can be captured using 'direction', "
                      "'strength', and 'score' attributes. The 'direction'  attribute "
                      "is used to indicate whether the Statement's Proposition is "
                      "*supported* by the agent's assessment (when evidence favors its "
                      "validity), is *disputed* by the agent's assessment (when "
                      'evidence argues against its validity), or remains *neutral* '
                      '(when conflicting or insufficient evidence exists to assert one '
                      "direction or the other).  (Enumerated values = 'supports', "
                      "'disputes', 'neutral')."],
         'domain_of': ['Statement'],
         'status': 'Draft'} })
    strength: Optional[str] = Field(default=None, description="""A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be).  Implementers may choose to frame a strength assessment in terms of how *confident* an agent is that the Proposition is true or false, or in terms of the *strength of all evidence* they believe supports or disputes it.""", json_schema_extra = { "linkml_meta": {'comments': ['Statements put forth a Proposition that expresses some possible '
                      'fact about the world, and may provide an assessment of this '
                      "proposition's validity (i.e. how likely it is to be true or "
                      'false based on evaluated evidence). The semantics of the '
                      "Proposition are captured in the 'subject,' 'predicate', "
                      "'object', and optional 'qualifier' attributes. An assessment of "
                      "the Proposition's validity can be captured using 'direction',  "
                      "'strength', and 'score' attributes. The 'strength' attribute is "
                      'used to report the strength of this assessment in the direction '
                      'indicated. Strength can be framed as a *level of confidence* '
                      'that the Proposition is true or false, or as a *level of '
                      'evidence* that supports or disputes it. Data creators can '
                      "define the permissible values for the 'strength' attribute to "
                      "indicate which of these facets is being assessed (e.g. 'high "
                      "confidence' vs 'low confidence', or 'strong evidence' vs 'weak "
                      "evidence') - or they can choose values that don't commit to one "
                      "or the other if they don't want to make the distinction (e.g. "
                      "'high' vs 'medium' vs 'low')."],
         'domain_of': ['Statement'],
         'status': 'Draft'} })
    score: Optional[float] = Field(default=None, description="""A quantitative score that indicates the strength of a Proposition's validity assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be).  Depending on its implementation, a score may reflect how *confident* that agent is that the Proposition is true or false, or the *strength of evidence* they believe supports or disputes it.""", json_schema_extra = { "linkml_meta": {'comments': ['Statements put forth a Proposition that expresses some possible '
                      'fact about the world, and may provide an assessment of this '
                      "proposition's validity (i.e. how likely it is to be true or "
                      'false based on evaluated evidence). The semantics of the '
                      "Proposition are captured in the 'subject', 'predicate', "
                      "'object', and optional 'qualifier' attributes. The assessment "
                      "of the Proposition's validity are captured in 'direction', "
                      "'strength', and 'score' attributes.  The 'score' attribute "
                      "serves the same purpose as 'strength', but allows for a "
                      'quantitative assessment based on a numerical score.'],
         'domain_of': ['Statement'],
         'status': 'Draft'} })
    subject_classification: Optional[Coding] = Field(default=None, description="""A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's proposition, in terms of a classification of its subject.""", json_schema_extra = { "linkml_meta": {'comments': ['Permissible values for this attribute are  typically selected '
                      'to be succinct and familiar in the target community of practice '
                      "- and can be provided to report of a statement's conclusion in "
                      'user-friendly terms. For example, in a Statement assessing the '
                      'proposition that "BRCA2 c.8023A>G is pathogenic for Breast '
                      'Cancer", and reporting a direction of \'supports\' and strength '
                      "of 'likely', the term  'likely pathogenic' from the ACMG "
                      'Variant Interpretation Guidelines would be used as a subject '
                      'classification.'],
         'domain_of': ['Statement'],
         'status': 'Draft'} })
    has_evidence_of_types: Optional[list[str]] = Field(default=None, description="""A term describing a type of evidence used to assess the validity of Statement's proposition (e.g. 'sequence similarity evidence', 'in vitro assay evidence').""", json_schema_extra = { "linkml_meta": {'comments': ['This contrasts with has_evidence and hasEvidenceLine attributes '
                      'that describe specific instances of evidence information, such '
                      'as a particular data item, study result, or prior assertions, '
                      'etc. Where possible, data cretors should use of terms from '
                      'ontologies such as the Evidence and Conclusion Ontology (ECO) '
                      'to describe specific types of evidence (e.g. ECO:0000044 '
                      "'sequence similarity evidence')."],
         'domain_of': ['Statement'],
         'status': 'Informative'} })
    has_evidence_lines: Optional[list[EvidenceLine]] = Field(default=None, description="""An evidence-based argument that supports or disputes the validity of the proposition that a Statement assesses or puts forth as true. The strength and direction of this argument (whether it supports or disputes  the proposition, and how strongly) is based on an interpretation of one or more pieces of information as evidence (i.e. 'Evidence Items).""", json_schema_extra = { "linkml_meta": {'comments': ['Evidence Lines result from the interpretation of one or more '
                      'pieces of information to build an argument for or against a '
                      'particular Proposition. These arguments have direction '
                      '(supporting / disputing) and strength (e.g. strong, moderate, '
                      'weak) relative to the Proposition they are evaluated against. '
                      'For example, ExaC allele counts and frequency calculations for '
                      'the BRCA2 c.8023A>G variant in different populations may be '
                      "collectively assessed to provide an argument of 'moderate' "
                      "strength in 'support of ' a proposition that the variant is "
                      'pathogenicity for breast cancer.',
                      'Evidence Lines are useful in cases where a data provider wants '
                      'to describe in detail how information was  assessed as evidence '
                      'to generate and score different arguments for or against a '
                      "Statement''s proposition. Evidence Lines can be omitted if such "
                      'information is not available or needed.'],
         'domain_of': ['Statement'],
         'status': 'Draft'} })
    has_evidence: Optional[list[InformationEntity]] = Field(default=None, description="""A piece of information that represents or contributes to an argument for or against the validity of the Proposition put forth in a Statement. This is a shortcut relation that links a Statement directly to a piece of evidence supporting it, bypassing the Evidence Line class when used data creators do not utilize an Evidence Line object.""", json_schema_extra = { "linkml_meta": {'comments': ['- Evidence is any information that is interpreted in assessing '
                      'the truth of  the proposition a Statement puts forth as true or '
                      'false.  A piece of information only becomes evidence when it is '
                      'interpreted in this way. Different types of information '
                      'entities can be used and cited as evidence, including direct '
                      'observation or measurement data, derived statistical '
                      'calculations, data tables or figures in a publication, '
                      'conclusions/findings from a particular study, or prior '
                      'assertions of knowledge  that themselves are based on their own '
                      'set of evidence.',
                      'This is a shortcut relation that links a Statement directly to '
                      'a piece of evidence supporting it, bypassing the Evidence Line '
                      'class - to be used data creators cannot or do not wish to '
                      'create an Evidence Line object.'],
         'domain_of': ['Statement'],
         'status': 'Informative'} })
    has_evidence_from_sources: Optional[list[InformationEntity]] = Field(default=None, description="""An Information Entity (typically a publication, dataset, or database) that provided information used as evidence to generate the knowledge expressed in a Statement.""", json_schema_extra = { "linkml_meta": {'comments': ["This is a 'shortcut property' that can be used to directly link "
                      'a Statement to sources that provided evidence '
                      'supporting/disputing it, without having to create Evidence '
                      'Lines or Evidence Items in the data.'],
         'domain_of': ['Statement']} })
    is_about: Optional[list[str]] = Field(default=None, description="""An entity or concept in the world that the information entity describes/is about.""", json_schema_extra = { "linkml_meta": {'comments': ['e.g. In the context of a Statement object, this attribute may '
                      'be used to indicate entities/concepts it is about, in lieu of '
                      'providing a more precise description of what the Statement '
                      'asserts to be true using subject, predicate, object, and '
                      'qualifier properties. e.g. the Statement that "BRCA2 c.8023A>G '
                      'is pathogenic for Breast Cancer" might be annotated to be about '
                      "the variant 'BRCA2 c.8023A>G', and the disease 'Breast "
                      "Cancer'."],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds one or more Contribution objects, which '
                      'provide structured descriptions of a contribution made to the '
                      'Information Entity by a particular agent.'],
         'domain_of': ['InformationEntity', 'RecordMetadata'],
         'status': 'Draft'} })
    date_authored: Optional[str] = Field(default=None, description="""Indicates when the information content expressed in the Information Entity was generated.""", json_schema_extra = { "linkml_meta": {'comments': ["The term 'authored' as used in the model refers to the "
                      "generation of 'information content' in the abstract  sense, as "
                      'opposed to a concrete encoding of this information in a '
                      'specific language or format. e.g. for a Statement, this '
                      'attribute captures when the information content expressed in '
                      'the Statement was first generated by an agent.  Information '
                      'about when a particular concrete encoding of this information '
                      'was created (e.g. as row in a table, or object in a json '
                      'document) would live in a RecordMetadata object attached to the '
                      'Information Entity).'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    specified_by: Optional[list[str]] = Field(default=None, description="""A specification that describes all or part of the process that led to creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples - an experimental protocol or data analysis '
                      'specification that describe how data were generated, or an '
                      'evidence interpretation guideline that describes steps taken to '
                      'interpret data in making a variant pathogenicity '
                      'classification.',
                      'Note that this attribute captures specific *instances* of '
                      'specifications/methods (e.g. the specific electron microscopy '
                      'method described in https://doi.org/10.1002/ cpz1.1045) - as '
                      'opposed to reporting a *type* of method applied (e.g. '
                      '"Transmission Electron Microscopy").'],
         'domain_of': ['InformationEntity', 'Activity'],
         'status': 'Draft'} })
    supporting_methods: Optional[list[str]] = Field(default=None, description="""Specific methods that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['These may include methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity - e.g. '
                      'methods used to produce data that was interpreted as evidence '
                      'to generate a Statement of knowledge.',
                      'This field captures terms representing specific INSTANCES of '
                      "methods applied, vs the 'supporting_method_types' attribute "
                      'which captures TYPES of methods used.'],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    supporting_method_types: Optional[list[Coding]] = Field(default=None, description="""Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This field captures terms representing TYPES of methods '
                      "applied, vs the 'specified_by' or'supporting_methods' "
                      'attributes which capture specific INSTANCES of methods used. '
                      'These may include types of methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity',
                      'Implementers should define a relevant source or set of method '
                      'type codes/terms to use here, based on the needs of the domain '
                      "or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    derived_from: Optional[list[InformationEntity]] = Field(default=None, description="""Another Information Entity from which this Information Entity is derived, in whole or in part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity'], 'status': 'Draft'} })
    reported_in: Optional[list[str]] = Field(default=None, description="""A document in which the Information Entity is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is used specifically to reference '
                      'documents/publications where the Information Entity is '
                      'expressed or reported.  For a Statement, this might be a '
                      'publication where the authors express the statement in text. '
                      'For a Data Item, this might be a publication with a table or '
                      'figure that reports the value of the  data.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    sources: Optional[list[str]] = Field(default=None, description="""A document or other informtion resource in which the information entity, or evidence supporting it, is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is more general than '
                      'InformationEntity.reported_in (which is used to references a '
                      'Docuement that directly reports the infrormation), and '
                      'Statement.has_evidence_from_sources (which is used to reference '
                      'resources that provided evidence used to generate the knowledge '
                      'expressed in a Statement). It can be used to cover both cases, '
                      'in situations where a data provider does not know which is the '
                      'case, or does not wish to make the distinction.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    information_quality: Optional[Coding] = Field(default=None, description="""A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.""", json_schema_extra = { "linkml_meta": {'comments': ['This is typically based on the quality of design and execution '
                      'of the study or curation activity that generated it (e.g. were '
                      'relevant controls assessed to show instruments were working, '
                      'were all samples taken care of and handled identically, are '
                      'methods sound and well documented, etc.).',
                      'The quality of information is intrinsic to the information '
                      'itself, and not to a particular application of the information '
                      '(e.g. as evidence for making an Assertion)',
                      'The quality of information is one factor that goes into the '
                      "confidence we have in the information''s veracity (i.e. that it "
                      'is an accurate reflection of reality it intends to measure or '
                      'describe). Other factors informing confidence may include who '
                      'did it (we may just not trust some Agents), when (if data '
                      'created 500 years ago, we may have less confidence in it), and '
                      'for Assertions, the relevance and abundance of supporting '
                      'evidence.',
                      'Implementers should define a relevant source of codes or terms '
                      "to use here, based on the needs of the domain or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    record_metadata: Optional[RecordMetadata] = Field(default=None, description="""Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds a structured RecordMetadata objects, which '
                      'can be used to capture when, how, and by whom a record '
                      'serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class StudyResult(InformationEntity):
    """
    A collection of data items from a single study that pertain to a particular subject or experimental unit in the study, along with optional provenance information describing how these data items were generated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['- StudyResults provide a useful way to capture a subset of '
                      'items from a study dataset that are used as evidence in '
                      'generating higher order knowledge assertions about the entity '
                      'that is the focus of the study result. For example, a subset of '
                      'allele frequency data items about a particular variant of '
                      'interest in the complete gnomAD dataset can be reported in a '
                      'StudyResult object, along with relevant provenance information, '
                      'so they can be referenced as evidence for a higher-order '
                      "assertion about the variant's pathogenicity.",
                      'As an example, consider the comprehensive allele frequency '
                      'dataset provided by gnomAD, which covers millions of variants. '
                      'A curator looking to assess the pathogenicity of a particular '
                      'variant might create a StudyResult object to capture a subset '
                      'of data related to this focus allele, including  its count, '
                      'frequency, homozygous frequency, along with metadata concerning '
                      'the shared provenance or quality of this data. The StudyResult '
                      'could then be references as a piece of evidence used to inform '
                      'the focus alleles final pathogenicity classification.',
                      'Note that the use of a Study Results is not reserved only for '
                      'defining subsets of data from a larger HTP/clinical study data '
                      'sets.  A StudyResult might be used to organize the data from a '
                      'simple, small scale bench experiment - e.g. a western blot '
                      'analysis of protein expression, or an in vitro binding assay '
                      "focused on a single protein.  Even such small 'studies' can "
                      'generate multiple data items and metadata, and a StudyResult '
                      'object can be used to collect all or some of these data points '
                      'pertinent to a particular focus into an organized structure.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Study Result'})

    focus: Optional[str] = Field(default=None, description="""A specific subject or experimental unit in a Study, that data in the StudyResult object is about - e.g. a particular variant in a population allele frequency dataset like ExAC or gnomAD.""", json_schema_extra = { "linkml_meta": {'comments': ["The 'focus' of a StudyResult is the what anchors selection of "
                      'all data items and provenance information that it contains. '
                      'This focus may be a single participant or subject of a study '
                      '(e.g. one patient in a clinical study, or one allele in a '
                      'population frequency analysis). It may be a study group defined '
                      'as an experimental unit in the study (e.g. a specific treatment '
                      'arm of a clinical study). Or it may be a variable defined as a '
                      "unit of analysis in the study (e.g. 'exposure to nicotine' in "
                      'an analysis correlating this variable with clinical outcomes).'],
         'domain_of': ['StudyResult']} })
    data_items: Optional[list[DataItem]] = Field(default=None, description="""One or more data items that are included in the StudyResult because it pertains to the 'focus' of the result. This can be data that directly describes this 'focus' (e.g. the population frequency of an allele focus), or be metadata about how data about the 'focus' were generated (e.g the quality measures for the sequencing run used to determine this allele frequency).""", json_schema_extra = { "linkml_meta": {'comments': ['Any type of data item from a Study may be captured in a '
                      'StudyResult - including raw experimental/observational data, '
                      'derived calculations or quality measures, provenance '
                      'information about how the data were generated in the study, or '
                      'qualitative expert interpretations of the primary study data '
                      '(e.g. the interpretation of a blood cholesterol value of 250 '
                      "mg/dL as being 'high', or a Polyphen functional impact score of "
                      "0.115 as being 'deleterious').",
                      "The model specifies use of a key-value based 'DataItem' object "
                      'to capture the meaning and value of each type of data item '
                      'captured in a given StudyResult. But in practice, profiles for '
                      'specific StudyResult types may choose to define one or more '
                      "specializations of the generic 'data_items' property as named "
                      'attributes. This makes the data more succinct and parsable, and '
                      'allows specific constraints to be applied and validated for '
                      'different data items. For example, a '
                      'PopulaitonAlleleFrequencyStudyResult profile may define a named '
                      "'focusAlleleFrequency' attribute that is required, and a named "
                      "'focusAlleleCount' attribute that is optional - both of which "
                      "conceptually specialize the core-im 'data_items' property. "
                      "Under this approach, the core 'data_items' acts as a "
                      'placeholder to seed such specializations, but is not used '
                      'directly in StudyResult profiles.'],
         'domain_of': ['StudyResult'],
         'status': 'Informative'} })
    interpretation: Optional[Coding] = Field(default=None, description="""The outcome of an interpretation of lower-level data item(s) in a StudyResult, that express some broader conclusion or insight that was made (e.g. that data indicates a result to be is high, normal, or low).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute allows basic interpretations / classifications '
                      'to be included in a Study Result, such as binning a data item '
                      'or items as being in or out of some normal range.'],
         'domain_of': ['StudyResult'],
         'status': 'Informative'} })
    source_data_set: Optional[list[DataSet]] = Field(default=None, description="""A larger DataSet from which the content of the StudyResult was derived.""", json_schema_extra = { "linkml_meta": {'comments': ['In most cases, a StudyResult will be generated using data from '
                      'one source dataset - but it is possible multiple datasets '
                      'related to a single study contain data about a particular focus '
                      'that get collected into a single StudyResult instance.'],
         'domain_of': ['StudyResult'],
         'status': 'Draft'} })
    component_result: Optional[list[StudyResult]] = Field(default=None, description="""Another StudyResult comprised of data items about the same focus as its parent Result, but based on a more narrowly scoped analysis of the foundational data (e.g. an analysis based on data about a subset of the parent Results full study population).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute allows data creators to break down a StudyResult '
                      'into finer-grained StudyResult instances with a narrower scope. '
                      'For example, a StudyResult about the frequency of an allele in '
                      'a global population of individuals can be broken down into '
                      "separate 'component' Results about distinct subpopulations of "
                      'individuals in the source data (e.g. frequency of the allele in '
                      'asian vs african subpopulations, or male vs female subgroups).'],
         'domain_of': ['StudyResult'],
         'status': 'Draft'} })
    study_group: Optional[StudyGroup] = Field(default=None, description="""A description of a specific group or population of subjects interrogated in the ResearchStudy that produced the data captured in the StudyResult.""", json_schema_extra = { "linkml_meta": {'comments': ['For example, in a StudyResult holding allele frequency data, '
                      'this attribute points to a StudyGroup object that describes '
                      'characteristics of the population that the frequency data was '
                      "generated from (e.g. 'East Asian', 'Female')."],
         'domain_of': ['StudyResult']} })
    is_about: Optional[list[str]] = Field(default=None, description="""An entity or concept in the world that the information entity describes/is about.""", json_schema_extra = { "linkml_meta": {'comments': ['e.g. In the context of a Statement object, this attribute may '
                      'be used to indicate entities/concepts it is about, in lieu of '
                      'providing a more precise description of what the Statement '
                      'asserts to be true using subject, predicate, object, and '
                      'qualifier properties. e.g. the Statement that "BRCA2 c.8023A>G '
                      'is pathogenic for Breast Cancer" might be annotated to be about '
                      "the variant 'BRCA2 c.8023A>G', and the disease 'Breast "
                      "Cancer'."],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds one or more Contribution objects, which '
                      'provide structured descriptions of a contribution made to the '
                      'Information Entity by a particular agent.'],
         'domain_of': ['InformationEntity', 'RecordMetadata'],
         'status': 'Draft'} })
    date_authored: Optional[str] = Field(default=None, description="""Indicates when the information content expressed in the Information Entity was generated.""", json_schema_extra = { "linkml_meta": {'comments': ["The term 'authored' as used in the model refers to the "
                      "generation of 'information content' in the abstract  sense, as "
                      'opposed to a concrete encoding of this information in a '
                      'specific language or format. e.g. for a Statement, this '
                      'attribute captures when the information content expressed in '
                      'the Statement was first generated by an agent.  Information '
                      'about when a particular concrete encoding of this information '
                      'was created (e.g. as row in a table, or object in a json '
                      'document) would live in a RecordMetadata object attached to the '
                      'Information Entity).'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    specified_by: Optional[list[str]] = Field(default=None, description="""A specification that describes all or part of the process that led to creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples - an experimental protocol or data analysis '
                      'specification that describe how data were generated, or an '
                      'evidence interpretation guideline that describes steps taken to '
                      'interpret data in making a variant pathogenicity '
                      'classification.',
                      'Note that this attribute captures specific *instances* of '
                      'specifications/methods (e.g. the specific electron microscopy '
                      'method described in https://doi.org/10.1002/ cpz1.1045) - as '
                      'opposed to reporting a *type* of method applied (e.g. '
                      '"Transmission Electron Microscopy").'],
         'domain_of': ['InformationEntity', 'Activity'],
         'status': 'Draft'} })
    supporting_methods: Optional[list[str]] = Field(default=None, description="""Specific methods that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['These may include methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity - e.g. '
                      'methods used to produce data that was interpreted as evidence '
                      'to generate a Statement of knowledge.',
                      'This field captures terms representing specific INSTANCES of '
                      "methods applied, vs the 'supporting_method_types' attribute "
                      'which captures TYPES of methods used.'],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    supporting_method_types: Optional[list[Coding]] = Field(default=None, description="""Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This field captures terms representing TYPES of methods '
                      "applied, vs the 'specified_by' or'supporting_methods' "
                      'attributes which capture specific INSTANCES of methods used. '
                      'These may include types of methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity',
                      'Implementers should define a relevant source or set of method '
                      'type codes/terms to use here, based on the needs of the domain '
                      "or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    derived_from: Optional[list[InformationEntity]] = Field(default=None, description="""Another Information Entity from which this Information Entity is derived, in whole or in part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity'], 'status': 'Draft'} })
    reported_in: Optional[list[str]] = Field(default=None, description="""A document in which the Information Entity is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is used specifically to reference '
                      'documents/publications where the Information Entity is '
                      'expressed or reported.  For a Statement, this might be a '
                      'publication where the authors express the statement in text. '
                      'For a Data Item, this might be a publication with a table or '
                      'figure that reports the value of the  data.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    sources: Optional[list[str]] = Field(default=None, description="""A document or other informtion resource in which the information entity, or evidence supporting it, is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is more general than '
                      'InformationEntity.reported_in (which is used to references a '
                      'Docuement that directly reports the infrormation), and '
                      'Statement.has_evidence_from_sources (which is used to reference '
                      'resources that provided evidence used to generate the knowledge '
                      'expressed in a Statement). It can be used to cover both cases, '
                      'in situations where a data provider does not know which is the '
                      'case, or does not wish to make the distinction.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    information_quality: Optional[Coding] = Field(default=None, description="""A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.""", json_schema_extra = { "linkml_meta": {'comments': ['This is typically based on the quality of design and execution '
                      'of the study or curation activity that generated it (e.g. were '
                      'relevant controls assessed to show instruments were working, '
                      'were all samples taken care of and handled identically, are '
                      'methods sound and well documented, etc.).',
                      'The quality of information is intrinsic to the information '
                      'itself, and not to a particular application of the information '
                      '(e.g. as evidence for making an Assertion)',
                      'The quality of information is one factor that goes into the '
                      "confidence we have in the information''s veracity (i.e. that it "
                      'is an accurate reflection of reality it intends to measure or '
                      'describe). Other factors informing confidence may include who '
                      'did it (we may just not trust some Agents), when (if data '
                      'created 500 years ago, we may have less confidence in it), and '
                      'for Assertions, the relevance and abundance of supporting '
                      'evidence.',
                      'Implementers should define a relevant source of codes or terms '
                      "to use here, based on the needs of the domain or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    record_metadata: Optional[RecordMetadata] = Field(default=None, description="""Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds a structured RecordMetadata objects, which '
                      'can be used to capture when, how, and by whom a record '
                      'serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class EvidenceLine(InformationEntity):
    """
    An independent, evidence-based argument that may support or refute the validity of a specific proposition. The strength and direction of this argument is based on an interpretation of one or more pieces of information as evidence for or against the target proposition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Evidence Lines are used to capture various pieces of '
                      "information (i.e. 'evidence items') that are assessed together "
                      "as an argument for or against some 'target proposition' - and "
                      'to report the direction (supports or disputes) and strength '
                      '(e.g. strong, moderate, weak) that the argument is determined '
                      'to make. For example, the various allele counts and population '
                      'frequency calculations for the BRCA2 c.8023A>G variant in the '
                      'ExAC database are evidence items that may be collectively '
                      "assessed to build an EvidenceLine making argument of 'moderate' "
                      "strength that 'supports' a target proposition that the variant "
                      'is pathogenic for Breast Cancer.',
                      'Evidence Lines are flexible with respect to the granularity of '
                      'arguments they support, and the scope of evidence items they '
                      'can collectively assess. Narrow scoping will bucket available '
                      'evidence into many, fine-grained Evidence Lines that make the '
                      'most atomic independently meaningful arguments possible. The '
                      'ACMG Variant Pathogenicity Interpretation Guidelines are an '
                      'example of a fairly fine-grained evidence interpretation '
                      'framework. Broader scoping approaches may organize the same '
                      'available evidence into fewer Evidence Lines that build and '
                      'assess less atomic arguments based on a wider and more diverse '
                      'set of evidence items.  For example, CIViC curators assess the '
                      'strength and direction of evidence items at the level of *all '
                      'information reported in a publication for a specific study* - '
                      'which can encompass many different results and evidence types '
                      'that under more fine-grained interpretation approaches might be '
                      'split apart and assessed as separate lines of evidence.',
                      'This CIViC EID5682 record '
                      '(https://civicdb.org/evidence/5682/summary) is a clear example '
                      'of this - illustrating how ACMG-curated evidence assessed at a '
                      'finer-grained level would lend itself to SEPIO representations '
                      'that creates a larger number of more atomic Evidence Lines, as '
                      'compared to how CIViC-curated evidence from the same source or '
                      'publication would be represented. We see here that CIViC '
                      'evidence assessments are performed at the level of all results '
                      'reported in PMID:23143947 - which SEPIO would capture as a '
                      'single Evidence Line that assigns a strength (level C) and '
                      'direction (supports) to the collective argument made by this '
                      'evidence. However, as detailed in the free-text summary of this '
                      'EID, the more fine-grained ACMG framework breaks out and '
                      'separately assess two arguments here - one based on criterion '
                      'PP1 (disease co-segregation evidence), and one based on '
                      'criterion PP4 (highly specific gene-phenotype information) - '
                      'which SEPIO woudl capture as two distinct Evidence Lines.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Evidence Line'})

    subtype: Optional[Coding] = Field(default=None, description="""A specific type of evidence the EvidenceLine instance represents (e.g. 'mutant phenotype evidence', 'evidence from manual interpretation', 'ACMG PM2 evidence')""", json_schema_extra = { "linkml_meta": {'comments': ['Data creators may choose to define specific types of evidence '
                      'lines relevant for their domain/use case, based on the type of '
                      'evidence items that comprise it, the methodology that guided '
                      'evidence interpretation, or the type of statement the evidence '
                      'line supports.  Terms from ontologies like the Evidence and '
                      'Conclusion Ontology (ECO), or categories from evidence '
                      'interpretation frameworks like the ACMG Variant Interpretation '
                      'Guidelines, can be used as values here.'],
         'domain_of': ['Method',
                       'Document',
                       'DataItem',
                       'DataSet',
                       'Activity',
                       'Agent',
                       'EvidenceLine'],
         'status': 'Informative'} })
    target_proposition: Optional[Proposition] = Field(default=None, description="""The possible fact against which evidence items contained in an Evidence Line were collectively evaluated, in determining the overall strength and direction of support they provide. For example, in an ACMG Guideline-based assessment of variant pathogenicity, the support provided by distinct lines of evidence are assessed against a target proposition that some variant is pathogenic for a specific disease.""", json_schema_extra = { "linkml_meta": {'comments': ['An example based on the ACMG Guidelines for germline variant '
                      'pathogenicity interpretation: Consider a curator assessing the '
                      'evidence provided by population frequency data for a specific '
                      'variant based on the ACMG criteria. In order to assign a '
                      'strength (e.g. moderate vs strong) and direction (supports vs '
                      "disputes) to this data as evidence, there must be some 'target "
                      "proposition' toward which the evidence is assessed - which in "
                      'this cases is the proposition that the variant is pathogenic '
                      'for the disease of interest. If the PM2 criteria is deemed '
                      "'met', this indicates that the population frequency evidence "
                      "provides 'moderate' (strength) 'support' (direction) for this "
                      'target proposition.'],
         'domain_of': ['EvidenceLine'],
         'status': 'Informative'} })
    has_evidence_items: Optional[list[InformationEntity]] = Field(default=None, description="""An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.""", json_schema_extra = { "linkml_meta": {'comments': ['A given Evidence Line may be supported by one or many '
                      'individual evidence items. What matters is that all evidence '
                      'items in a given Evidence Line get collectively assessed and '
                      'assigned direction and strength  as a single argument for or '
                      'against a target proposition.',
                      'Different types and scales of information entity can serve as '
                      'evidence (experimental measurements or observations, data '
                      'tables or figures, images, prior assertions, etc.) Only when '
                      'assessed as evidence do we consider the information to be an '
                      "'Evidence Item'.  For example, a piece of population frequency "
                      'data about BRCA2 c.8023A>G  becomes an Evidence Item when it is '
                      'assessed for the support it may offer for a target proposition '
                      '(e.g. the prospect of the variant’s pathogenicity).'],
         'domain_of': ['EvidenceLine'],
         'status': 'Draft'} })
    direction_of_evidence_provided: Optional[str] = Field(default=None, description="""The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EvidenceLine'], 'status': 'Draft'} })
    strength_of_evidence_provided: Optional[str] = Field(default=None, description="""The strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the direction_of_evidence_provided.""", json_schema_extra = { "linkml_meta": {'comments': ['Values of this attribute can be defined by for a given profile '
                      'based on domain/application needs, but should be framed in '
                      "qualitative terms (e.g. 'strong', 'moderate', 'weak'). The "
                      "'score_of_evidence_provided' attribute can be used to report "
                      'quantitative assessments of evidence provided.'],
         'domain_of': ['EvidenceLine'],
         'status': 'Draft'} })
    score_of_evidence_provided: Optional[float] = Field(default=None, description="""A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the direction_of_evidence_provided value.""", json_schema_extra = { "linkml_meta": {'comments': ['A given profile or implementation can define a scoring scale '
                      'and rules that meet the needs of their domain or application.'],
         'domain_of': ['EvidenceLine'],
         'status': 'Draft'} })
    evidence_item_sources: Optional[list[str]] = Field(default=None, description="""An information resource (e.g. document, dataset, digital resource such as a database or  knowledgebase) that provides information interpreted as evidence in building an Evidence Line.""", json_schema_extra = { "linkml_meta": {'comments': ["This is a 'shortcut relation' that can be used to directly link "
                      'an Evidence Line to sources of its supporting Evidence Items, '
                      'without having to represent those Evidence Items directly. '
                      'Populate with the name or uri or curie of a source of '
                      'information. Future work will define a more formal framework '
                      'for referencing information sources.'],
         'domain_of': ['EvidenceLine'],
         'status': 'Informative'} })
    is_about: Optional[list[str]] = Field(default=None, description="""An entity or concept in the world that the information entity describes/is about.""", json_schema_extra = { "linkml_meta": {'comments': ['e.g. In the context of a Statement object, this attribute may '
                      'be used to indicate entities/concepts it is about, in lieu of '
                      'providing a more precise description of what the Statement '
                      'asserts to be true using subject, predicate, object, and '
                      'qualifier properties. e.g. the Statement that "BRCA2 c.8023A>G '
                      'is pathogenic for Breast Cancer" might be annotated to be about '
                      "the variant 'BRCA2 c.8023A>G', and the disease 'Breast "
                      "Cancer'."],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds one or more Contribution objects, which '
                      'provide structured descriptions of a contribution made to the '
                      'Information Entity by a particular agent.'],
         'domain_of': ['InformationEntity', 'RecordMetadata'],
         'status': 'Draft'} })
    date_authored: Optional[str] = Field(default=None, description="""Indicates when the information content expressed in the Information Entity was generated.""", json_schema_extra = { "linkml_meta": {'comments': ["The term 'authored' as used in the model refers to the "
                      "generation of 'information content' in the abstract  sense, as "
                      'opposed to a concrete encoding of this information in a '
                      'specific language or format. e.g. for a Statement, this '
                      'attribute captures when the information content expressed in '
                      'the Statement was first generated by an agent.  Information '
                      'about when a particular concrete encoding of this information '
                      'was created (e.g. as row in a table, or object in a json '
                      'document) would live in a RecordMetadata object attached to the '
                      'Information Entity).'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    specified_by: Optional[list[str]] = Field(default=None, description="""A specification that describes all or part of the process that led to creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['Examples - an experimental protocol or data analysis '
                      'specification that describe how data were generated, or an '
                      'evidence interpretation guideline that describes steps taken to '
                      'interpret data in making a variant pathogenicity '
                      'classification.',
                      'Note that this attribute captures specific *instances* of '
                      'specifications/methods (e.g. the specific electron microscopy '
                      'method described in https://doi.org/10.1002/ cpz1.1045) - as '
                      'opposed to reporting a *type* of method applied (e.g. '
                      '"Transmission Electron Microscopy").'],
         'domain_of': ['InformationEntity', 'Activity'],
         'status': 'Draft'} })
    supporting_methods: Optional[list[str]] = Field(default=None, description="""Specific methods that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['These may include methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity - e.g. '
                      'methods used to produce data that was interpreted as evidence '
                      'to generate a Statement of knowledge.',
                      'This field captures terms representing specific INSTANCES of '
                      "methods applied, vs the 'supporting_method_types' attribute "
                      'which captures TYPES of methods used.'],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    supporting_method_types: Optional[list[Coding]] = Field(default=None, description="""Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['This field captures terms representing TYPES of methods '
                      "applied, vs the 'specified_by' or'supporting_methods' "
                      'attributes which capture specific INSTANCES of methods used. '
                      'These may include types of methods that directly produced the '
                      'Information Entity, or upstream/accessory methods that '
                      'indirectly support creation of the Information Entity',
                      'Implementers should define a relevant source or set of method '
                      'type codes/terms to use here, based on the needs of the domain '
                      "or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    derived_from: Optional[list[InformationEntity]] = Field(default=None, description="""Another Information Entity from which this Information Entity is derived, in whole or in part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity'], 'status': 'Draft'} })
    reported_in: Optional[list[str]] = Field(default=None, description="""A document in which the Information Entity is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is used specifically to reference '
                      'documents/publications where the Information Entity is '
                      'expressed or reported.  For a Statement, this might be a '
                      'publication where the authors express the statement in text. '
                      'For a Data Item, this might be a publication with a table or '
                      'figure that reports the value of the  data.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    sources: Optional[list[str]] = Field(default=None, description="""A document or other informtion resource in which the information entity, or evidence supporting it, is reported.""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute is more general than '
                      'InformationEntity.reported_in (which is used to references a '
                      'Docuement that directly reports the infrormation), and '
                      'Statement.has_evidence_from_sources (which is used to reference '
                      'resources that provided evidence used to generate the knowledge '
                      'expressed in a Statement). It can be used to cover both cases, '
                      'in situations where a data provider does not know which is the '
                      'case, or does not wish to make the distinction.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    information_quality: Optional[Coding] = Field(default=None, description="""A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.""", json_schema_extra = { "linkml_meta": {'comments': ['This is typically based on the quality of design and execution '
                      'of the study or curation activity that generated it (e.g. were '
                      'relevant controls assessed to show instruments were working, '
                      'were all samples taken care of and handled identically, are '
                      'methods sound and well documented, etc.).',
                      'The quality of information is intrinsic to the information '
                      'itself, and not to a particular application of the information '
                      '(e.g. as evidence for making an Assertion)',
                      'The quality of information is one factor that goes into the '
                      "confidence we have in the information''s veracity (i.e. that it "
                      'is an accurate reflection of reality it intends to measure or '
                      'describe). Other factors informing confidence may include who '
                      'did it (we may just not trust some Agents), when (if data '
                      'created 500 years ago, we may have less confidence in it), and '
                      'for Assertions, the relevance and abundance of supporting '
                      'evidence.',
                      'Implementers should define a relevant source of codes or terms '
                      "to use here, based on the needs of the domain or application.'"],
         'domain_of': ['InformationEntity'],
         'status': 'Informative'} })
    record_metadata: Optional[RecordMetadata] = Field(default=None, description="""Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).""", json_schema_extra = { "linkml_meta": {'comments': ['This attribute holds a structured RecordMetadata objects, which '
                      'can be used to capture when, how, and by whom a record '
                      'serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'domain_of': ['InformationEntity'],
         'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class Proposition(Entity):
    """
    An abstract entity representing a possible fact that is either true or false.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Propositions are taken to represent the semantic content of '
                      'sentences or larger lexical entities formulated in some natural '
                      'or artificial language.  As abstract entities, Propositions '
                      "capture a 'sharable' piece of meaning that can be put forth as "
                      'true or false in many different Statement instances made by '
                      'different Agents on different occasions.  Their identity and '
                      'existence are independent of space and time, and of whether '
                      'they are ever asserted to be true by some agent.',
                      'Propositions may be used in two contexts in this model: (1) in '
                      'Statements to represent the possible fact that is put forth as '
                      'true, or  that is subjected to an assessment of the level of '
                      'evidence supporting it; (2) in Evidence Lines to represent the '
                      'possible fact that an argument built from evidence items is '
                      'evaluated against.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Informative',
         'title': 'Proposition'})

    proposition_text: Optional[str] = Field(default=None, description="""A natural-language expression of the Proposition's meaning (i.e. the 'possible fact' it expresses).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Proposition'], 'status': 'Informative'} })
    subject: str = Field(default=..., description="""The Entity or concept about which the Proposition is made.""", json_schema_extra = { "linkml_meta": {'comments': ['While the Core Information Model is domain-agnostic, and '
                      'supports Propositions about any type of Entity, for most VA use '
                      'cases, the subject will be  some type of genetic variation. But '
                      'data creators may want to make statements about other entities '
                      'or concepts that represent evidence for a statement about '
                      'variation (e.g. a statement that a gene is valid for some '
                      'disease is one type of evidence that may support the '
                      'pathogenicity of a variant that affects that gene).'],
         'domain_of': ['Statement', 'Proposition'],
         'status': 'Informative'} })
    predicate: Coding = Field(default=..., description="""The relationship declared to hold between the subject and the object of the Proposition.""", json_schema_extra = { "linkml_meta": {'comments': ['When applied to represent a particular type of Proposition (via '
                      "'Profiling'), implementers can define a value set of predicates "
                      'for the relationships relevant in the domain - ideally using '
                      'terms from community ontologies or terminologies. For example, '
                      "in a  'Variant Pathogenicity Statement' Profile, the predicate "
                      'value set might include terms from the GENO ontology defining  '
                      "'pathogenic for condition', 'benign for condition', and "
                      "'uncertain significance for condition' relationships "
                      '(GENO:0000840, GENO:0000843, GENO:0000845).'],
         'domain_of': ['Statement', 'Proposition'],
         'status': 'Informative'} })
    object: str = Field(default=..., description="""An Entity or concept that is related to the subject of a Proposition via its predicate.""", json_schema_extra = { "linkml_meta": {'comments': ['The object of a Proposition can be any Entity or concept that '
                      'is related to the subject, e.g. for Genetic Variation subjects '
                      'this is often a disease, drug, gene, molecular consequence, '
                      'functional impact on gene or protein.'],
         'domain_of': ['Statement', 'Proposition'],
         'status': 'Informative'} })
    qualifier: Optional[list[Qualifier]] = Field(default=None, description="""An additional piece of information that extends or refines the meaning of a Propositions's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context.""", json_schema_extra = { "linkml_meta": {'comments': ['The qualifier attribute allows representation of more complex, '
                      'n-ary propositions that may not be accommodated by a simple '
                      'subject-predicate-object (SPO) triple. For example, if a triple '
                      "asserts that 'Variant X' - predicts sensitivity to - 'Treatment "
                      "Y', a qualifier can be used to indicate that this applies in "
                      "the context of a particular 'Disease Z'. Qualifiers can also "
                      'add information that quantifies aspects of a Statement - e.g. '
                      "for an SPO triple asserting that a 'Variant X'- causes - "
                      "'Phenotype Y', a qualifier can be used to add "
                      'frequency/penetrance information that quantifies the percentage '
                      'of carriers in which the phenotype is observed to manifest. '
                      'Profiles of specific proposition types may define more than one '
                      'qualifier, as needed to capture different types of qualifying '
                      'information.',
                      "The SEPIO core model specifies use of a key-value 'Qualifier' "
                      'object to capture the meaning and value of each type of '
                      'qualifying information relevant for a given type of Statement. '
                      'But in practice, profiles for specific Proposition types may '
                      'choose to define one or more specializations of the generic '
                      "'qualifier' property as named attributes. This makes the data "
                      'more succinct and parsable, and allows specific constraints to '
                      'be applied and validated for different qualifiers. For example, '
                      'a VariantPathogenicityStatement profile may define a named '
                      "'alleleOriginQualifier' attribute that is required, and a named "
                      "'geneContextQualifier' attribute that is optional - both of "
                      "which conceptually specialize the core-im 'qualifier' property. "
                      "Under this approach, the core 'qualifier' acts as a placeholder "
                      'to seed such specializations, but is not used directly in '
                      'profiles.'],
         'domain_of': ['Statement', 'Proposition'],
         'status': 'Informative'} })
    negated: Optional[bool] = Field(default=None, description="""A boolean flag set to 'true' to represent a negation of the proposition expressed by the subject, predicate, object, and qualifier(s) (e.g. that \"Variant X is NOT pathogenic for Disease Y\")""", json_schema_extra = { "linkml_meta": {'comments': ["Along with the 'subject', predicate', 'object', and 'qualifier' "
                      "attributes, the 'negated' element contributes to the semantics "
                      "of the 'possible fact' that a Proposition expresses."],
         'domain_of': ['Proposition'],
         'status': 'Informative'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class StudyGroup(Entity):
    """
    A collection of individuals or specimens from the same taxonomic class, selected for analysis in a scientific study based on their exhibiting one or more common characteristics  (e.g. species, race, age, gender, disease state, income). May be referred to as a 'cohort' or 'population' in specific research settings.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['A Study Group may include all participants in a given study, or '
                      'specific subsets that are designated based on shared roles or '
                      'characteristics.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Study Group'})

    member_count: Optional[int] = Field(default=None, description="""The total number of individual members in the StudyGroup.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyGroup'], 'status': 'Informative'} })
    is_subset_of: Optional[list[StudyGroup]] = Field(default=None, description="""A larger StudyGroup of which this StudyGroup represents a subset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyGroup'], 'status': 'Draft'} })
    characteristics: Optional[list[Characteristic]] = Field(default=None, description="""A feature or role shared by all members of the StudyGroup, representing a criterion for membership in the group.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyGroup'], 'status': 'Draft'} })
    id: str = Field(default=..., description="""The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.""", json_schema_extra = { "linkml_meta": {'comments': ['Note that it is common for implementers to create their own '
                      'internal logical ids - typically a serially or randomly '
                      'generated value like a UUID that is assigned to the data object '
                      'as it is created in a system. But an implementer may choose to '
                      'reuse an existing, globally unique id from an external system '
                      'or authority for this purpose (e.g. an HGNC id for a Gene '
                      'object) - as long as it is unique within the implementing '
                      'system, and can be used to reference the identified object in '
                      'this context.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    identifiers: Optional[list[str]] = Field(default=None, description="""A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.""", json_schema_extra = { "linkml_meta": {'comments': ['Preferred values for this attribute are CURIEs or URIs - so the '
                      'system that provisioned the identifier is clear.',
                      'A given real world entity - e.g. a genetic variant - may have '
                      'many business identifiers defined by different systems, which '
                      'can be captured in the "identifiers" property to indicate that '
                      'they represent the same thing.'],
         'domain_of': ['Entity'],
         'status': 'Informative'} })
    type: str = Field(default=..., description="""The name of the class that is instantiated by a data object representing the Entity.""", json_schema_extra = { "linkml_meta": {'comments': ['MUST be the label of a concrete class from the data model.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })
    label: Optional[str] = Field(default=None, description="""A primary name for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding'], 'status': 'Draft'} })
    alternative_labels: Optional[list[str]] = Field(default=None, description="""Alternative name(s) for the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    description: Optional[str] = Field(default=None, description="""A free text description of the Entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'status': 'Draft'} })
    extensions: Optional[list[Extension]] = Field(default=None, description="""A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.""", json_schema_extra = { "linkml_meta": {'comments': ['Extension objects have a key-value data structure that allows '
                      'definition of custom fields in the data itself. Extensions are '
                      'not expected to be natively understood, but may be used for '
                      'pre-negotiated exchange of message attributes between systems.'],
         'domain_of': ['Entity'],
         'status': 'Draft'} })


class Utility(ConfiguredBaseModel):
    """
    An abstract organizational class that groups classes acting as complex datatypes in the model - providing reusable collections of fields that can be plugged into other objects to capture sets of related information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['The Utility class itself is abstract and has no direct '
                      'attributes. Implementers would always use one of its concrete '
                      'subtypes with specifically defined fields (e.g. Coding, '
                      'Expression, Extension).'],
         'from_schema': 'https://w3id.org/sepio-model'})

    pass


class Coding(Utility):
    """
    A structured representation of a code for a defined concept in a terminology or code system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Either a code, label, or both must be provided.',
                      'Coding supports use of terms form ontologies/terminologies in '
                      'structured object that reports id, label, and metadata about '
                      'system it came from.  follows FHIR approach.  Used in model '
                      'when implementers are free to create own value sets of terms '
                      'which get reported within coding objects in SEPIO data. '
                      'Validation requires additional tooling - as constraints are not '
                      'defined in schema itself.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'title': 'Coding'})

    code: Optional[str] = Field(default=None, description="""A symbol uniquely identifying the concept, as in a syntax defined by the code system.  CURIE format is preferred where possible (e.g. ‘SO:0000704’ is the CURIE form of the Sequence Ontology code for 'gene').""", json_schema_extra = { "linkml_meta": {'domain_of': ['Coding']} })
    label: Optional[str] = Field(default=None, description="""The human-readable name for the coded concept, as defined by the code system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'Coding']} })
    system: Optional[str] = Field(default=None, description="""The terminology/code system that defined the code.  May be reported as a free-text name (e.g. ‘Sequence Ontology’), but it is preferable to provide  a uri/url for the system. When the 'code' is reported as a CURIE, the 'system' should be reported as the uri that the CURIE's prefix expands to (e.g. 'http://purl.obofoundry.org/so.owl/' for the Sequence Ontology).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Coding']} })
    system_version: Optional[str] = Field(default=None, description="""Version of the terminology or code system that provided the code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Coding', 'Expression']} })


class Qualifier(Utility):
    """
    A key-value object used to capture additional piece of information that extends or refines the meaning of a Statement's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Qualifiers allow representation of more complex, n-ary '
                      'statements that may not be accommodated by a simple '
                      'subject-predicate-object (SPO) triple. For example, if a triple '
                      "asserts that 'Variant X' - predicts sensitivity to - 'Treatment "
                      "Y', a qualifier can be used to indicate that this applies in "
                      "the context of a particular 'Disease Z'. Qualifiers can also "
                      "add information that 'quantifies' aspects of a Statement - e.g. "
                      "for a Statement triple asserting that a 'Variant X'- causes - "
                      "'Phenotype Y', a qualifier can be used to add "
                      'frequency/penetrance information that quantifies the percentage '
                      'of carriers in which the phenotype is observed to manifest.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Informative',
         'title': 'Qualifier'})

    name: str = Field(default=..., description="""A descriptive name that describes the type of information captured in the Qualifier value.""", json_schema_extra = { "linkml_meta": {'comments': ['Recommended convention is to treat this like the name of an '
                      'attribute in the model - use snake case syntax, and append '
                      "'Qualifier' to the end of the name. e.g. "
                      "'diseaseContextQualifier', or 'alleleOriginQualifier'."],
         'domain_of': ['Agent', 'Qualifier', 'Extension', 'Characteristic'],
         'status': 'Informative'} })
    value: str = Field(default=..., description="""The value of the qualifier - holding information that refines/extends the meaning of the Statement.""", json_schema_extra = { "linkml_meta": {'comments': ['Value can be of any data type - a string, an integer or float, '
                      'a uriorcurie, a Coding, etc.'],
         'domain_of': ['DataItem', 'Qualifier', 'Expression', 'Extension'],
         'status': 'Informative'} })


class Expression(Utility):
    """
    A structure for labels representing systematic expressions that describe an entity, as generated by formal nomenclatures (e.g. HGVS for genetic variants, ISCN for karyotypes, HLA nomenclature for HLA genes/alleles).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["Similar to the 'Coding' data type, which provides the same "
                      'fields but for coded values, as opposed to human-readable '
                      'names.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'title': 'Expression'})

    value: str = Field(default=..., description="""A free-text rendering of the expression used as a label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataItem', 'Qualifier', 'Expression', 'Extension']} })
    system_url: Optional[str] = Field(default=None, description="""A URL for the nomenclature system""", json_schema_extra = { "linkml_meta": {'domain_of': ['Expression']} })
    system_version: Optional[str] = Field(default=None, description="""The version of the nomenclature system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Coding', 'Expression']} })


class Extension(Utility):
    """
    A data structure that allows custom attributes to be defined for an Entity, to capture information unique to a given content provider, or not currently supported by the core specification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Extension objects allow for  descriptions of an class with '
                      'additional attributes unique to a content provider',
                      'The modeling pattern and use of Extensions is based on that '
                      'defined by the FHIR Speciufication - see '
                      'https://build.fhir.org/extensibility.html'],
         'from_schema': 'https://w3id.org/sepio-model',
         'title': 'Extension'})

    extension_description: Optional[str] = Field(default=None, description="""A free text description of the intended meaning and use of the extension element, which may include the types of values it takes, and how to interpret these values in the context of the parent Class.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Extension']} })
    name: str = Field(default=..., description="""A name for the Extension. Should be indicative of its meaning and/or the type of information it value represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent', 'Qualifier', 'Extension', 'Characteristic']} })
    value: str = Field(default=..., description="""The value of the Extension - can be any primitive or structured object""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataItem', 'Qualifier', 'Expression', 'Extension']} })


class RecordMetadata(Utility):
    """
    A reusable structure that encapsulates provenance metadata about a serialized data record or object in a particular dataset (as opposed to provenance of the real world entity this record or object represents).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Record-level metadata applies to a specific concrete '
                      'encoding/serialization of information (e.g as a record in a '
                      'specific data/knowlegebase, or an online digital resource). A '
                      'RecordMetadata object can capture when, how, and by whom a '
                      'record serialization was generated or modified; what upstream '
                      'resources it was derived or retrieved from; and record-level '
                      'administrative information such as versioning and lifecycle '
                      'status.'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Record Metadata'})

    record_identifier: Optional[str] = Field(default=None, description="""The identifier of the record described in the RecordMetadata object (required when the record described is not the one in the present system).""", json_schema_extra = { "linkml_meta": {'comments': ['This is needed only when the RecordMetadata object describes an '
                      'upstream source record, as opposed to the record in the present '
                      'system, so it is clear what the metadata it contains is about.  '
                      'e.g. when ClinGen ingests and transforms ClinVar data, it wants '
                      'to maintain a record of when the source ClinVar record was '
                      'submitted and by whom.  A RecordMetadata object could be '
                      'created that describes this upstream source record, including '
                      'information about its submission to ClinVar.'],
         'domain_of': ['RecordMetadata'],
         'status': 'Draft'} })
    record_version: Optional[str] = Field(default=None, description="""The version number of the record-level artifact the object describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RecordMetadata'], 'status': 'Draft'} })
    derived_from_record: Optional[list[str]] = Field(default=None, description="""Another data record from which the record described here was derived, through a data ingest and/or transformation process.""", json_schema_extra = { "linkml_meta": {'comments': ['Value should be a string representing the identifier of the '
                      'source record.'],
         'domain_of': ['RecordMetadata'],
         'status': 'Draft'} })
    date_record_created: Optional[str] = Field(default=None, description="""The date the record was initially created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RecordMetadata'], 'status': 'Draft'} })
    contributions: Optional[list[Contribution]] = Field(default=None, description="""describes specific contributions made by an human or software agent to the creation, modification, or administrative management of a data record or object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InformationEntity', 'RecordMetadata'], 'status': 'Draft'} })


class Characteristic(Utility):
    """
    An object holding a name-value pair used to describe a trait or role of an individual member of a StudyGroup.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['This flexible key-value like object is where specific inclusion '
                      'or exclusion criteria for membership in a StudyGroup are '
                      'formally defined.  It should be used to capture characteristics '
                      'that inhere in individual members of the StudyGroup (e.g. '
                      'inherent traits like their sex, race, or age, or roles assigned '
                      'to them in a particular context such as being a control in a '
                      'study).'],
         'from_schema': 'https://w3id.org/sepio-model',
         'status': 'Draft',
         'title': 'Characteristic'})

    name: str = Field(default=..., description="""The type of the trait or role described by the trait (e.g. 'ethnicity', 'sex', 'age', 'disease status').""", json_schema_extra = { "linkml_meta": {'domain_of': ['Agent', 'Qualifier', 'Extension', 'Characteristic'],
         'status': 'Draft'} })
    values: list[str] = Field(default=..., description="""The specific value(s) that the indicated traitor role  holds in all population members (e.g. 'east asian', 'female', 'adolescent', 'cancer').""", json_schema_extra = { "linkml_meta": {'domain_of': ['Characteristic'], 'status': 'Draft'} })
    value_operator: Optional[str] = Field(default=None, description="""An operation that defines how to logically interpret a set of more than one Characteristic values ('AND', 'OR', 'NOT').""", json_schema_extra = { "linkml_meta": {'comments': ["An 'AND' operator indicates that an individual exhibits all of "
                      "the characteristic values listed.  An 'OR' operator indicates "
                      'the individual exhibits one or more of the characteristic '
                      "values listed. A 'NOT' indicates that the individual does not "
                      'exhibit the characteristic value or values listed.'],
         'domain_of': ['Characteristic'],
         'status': 'Informative'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Entity.model_rebuild()
InformationEntity.model_rebuild()
Method.model_rebuild()
Document.model_rebuild()
DataItem.model_rebuild()
DataSet.model_rebuild()
Activity.model_rebuild()
Contribution.model_rebuild()
Agent.model_rebuild()
Statement.model_rebuild()
StudyResult.model_rebuild()
EvidenceLine.model_rebuild()
Proposition.model_rebuild()
StudyGroup.model_rebuild()
Utility.model_rebuild()
Coding.model_rebuild()
Qualifier.model_rebuild()
Expression.model_rebuild()
Extension.model_rebuild()
RecordMetadata.model_rebuild()
Characteristic.model_rebuild()
