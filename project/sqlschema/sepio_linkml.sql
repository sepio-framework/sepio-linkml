-- # Class: Entity Description: Anything that exists, has existed, or will exist.
--     * Slot: uid
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
-- # Class: InformationEntity Description: An abstract (non-physical) entity that is about something - representing the underlying 'information content' conveyed by physical or digital information artifacts like books, web pages, data tables, or photographs.
--     * Slot: uid
--     * Slot: date_authored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: information_quality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: record_metadata_id Description: Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
-- # Class: Method Description: A set of instructions that specify how to achieve some objective.
--     * Slot: uid
--     * Slot: date_authored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of method that a Method instance represents (e.g. 'Variant Interpretation Guideline', or 'Experimental Protocol').
--     * Slot: information_quality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: record_metadata_id Description: Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
-- # Class: Document Description: A collection of information, usually in a text-based or graphic human-readable form, intended to be read and understood together as a whole.
--     * Slot: uid
--     * Slot: title Description: The official title given to the document by its authors.
--     * Slot: pmid Description: A `PubMed unique identifier <https://en.wikipedia.org/wiki/PubMed#PubMed_identifier>`_ for the document.
--     * Slot: doi Description: A `Digital Object Identifier <https://www.doi.org/the-identifier/what-is-a-doi/>_` for the document.
--     * Slot: license Description: A specific license that dictates legal permissions for how a document can be used (by whom, where, for what purposes, with what additional requirements, etc.)
--     * Slot: date_authored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of document that a Document instance represents (e.g.  'publication', 'patent', 'pathology report')
--     * Slot: information_quality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: record_metadata_id Description: Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
-- # Class: DataItem Description: An Information Entity representing an individual piece of data, generated or acquired through methods which reliably produce truthful information about something.
--     * Slot: uid
--     * Slot: value Description: The value of the data item (could be quantitative or qualitative depending on the type of data item).
--     * Slot: date_authored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of data the DataItem instance represents (e.g. a 'specimen count', a 'patient weight', an 'allele frequency', a 'p-value')
--     * Slot: unit_id Description: A unit of measure for the value (e.g. meters, grams, fluorescent units, seconds, mg/ml, etc.)
--     * Slot: confidence_interval_uid Description: A measure of the probability that a parameter of interest will fall within a defined range of values around a mean or other statistical calculation.
--     * Slot: information_quality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: record_metadata_id Description: Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
-- # Class: DataSet Description: A collection of related data items or records that are organized together in a common format or structure, to enable their computational manipulation as a unit.
--     * Slot: uid
--     * Slot: release_date Description: Indicates when a version of a DataSet was formally released.
--     * Slot: version Description: The version of the DataSet, as assigned by its creator.
--     * Slot: license Description: A specific license that dictates legal permissions for how a data set can be used (by whom, where, for what purposes, with what additional requirements, etc.).
--     * Slot: date_authored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of data set the DataSet instance represents (e.g. a 'clinical data set', a 'sequencing data set', a 'gene expression data set', a 'genome annotation data set').
--     * Slot: information_quality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: record_metadata_id Description: Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
-- # Class: Activity Description: An action or set of actions performed by an agent, that occurs over a period of time. Activities may use, generate, modify, move, or destroy one or more entities.
--     * Slot: uid
--     * Slot: date Description: The date that the Activity was completed.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of activity the Activity instance represents.
-- # Class: Contribution Description: An action or actions taken by a particular agent in the creation, modification, assessment, or deprecation of some entity (e.g. a Statement, Evidence Line, DataSet, Publication, etc.).
--     * Slot: uid
--     * Slot: date Description: The date that the Activity was completed.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: contributor_uid Description: The Agent that made the contribution.
--     * Slot: contribution_made_to_uid Description: The artifact toward which the contribution was made.
--     * Slot: subtype_id Description: A specific type of activity the Activity instance represents.
-- # Class: Agent Description: An autonomous actor (person, organization, or software agent) that bears some form of responsibility for an activity taking place,  for the existence of an entity, or for another agent's activity.
--     * Slot: uid
--     * Slot: subtype Description: A specific type of agent the Agent object represents. Must be one of {person, organization, software}
--     * Slot: name Description: The given name of the Agent.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
-- # Class: Statement Description: A claim of purported truth as made by a particular agent, on a particular occasion. Statements may be used to simply put forth a possible fact (i.e. a 'proposition') as true, or to provide a more nuanced assessment of the level of confidence or evidence supporting a particular proposition.
--     * Slot: uid
--     * Slot: statement_text Description: A natural-language expression of what a Statement asserts to be true.
--     * Slot: subject Description: The Entity or concept about which the Statement is made.
--     * Slot: object Description: An Entity or concept that is related to the subject of a Statement via its predicate.
--     * Slot: direction Description: A term indicating whether the Statement supports, disputes, or remains neutral w.r.t. the validity of the Proposition it evaluates.
--     * Slot: strength Description: A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be).  Implementers may choose to frame a strength assessment in terms of how *confident* an agent is that the Proposition is true or false, or in terms of the *strength of all evidence* they believe supports or disputes it.
--     * Slot: score Description: A quantitative score that indicates the strength of a Proposition's validity assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be).  Depending on its implementation, a score may reflect how *confident* that agent is that the Proposition is true or false, or the *strength of evidence* they believe supports or disputes it.
--     * Slot: date_authored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: proposition_uid Description: A possible fact that the Statement assesses or puts forth as true.
--     * Slot: predicate_id Description: The relationship declared to hold between the subject and the object of the Statement.
--     * Slot: subject_classification_id Description: A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's proposition, in terms of a classification of its subject.
--     * Slot: information_quality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: record_metadata_id Description: Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
-- # Class: StudyResult Description: A collection of data items from a single study that pertain to a particular subject or experimental unit in the study, along with optional provenance information describing how these data items were generated.
--     * Slot: uid
--     * Slot: focus Description: A specific subject or experimental unit in a Study, that data in the StudyResult object is about - e.g. a particular variant in a population allele frequency dataset like ExAC or gnomAD.
--     * Slot: date_authored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: interpretation_id Description: The outcome of an interpretation of lower-level data item(s) in a StudyResult, that express some broader conclusion or insight that was made (e.g. that data indicates a result to be is high, normal, or low).
--     * Slot: study_group_uid Description: A description of a specific group or population of subjects interrogated in the ResearchStudy that produced the data captured in the StudyResult.
--     * Slot: information_quality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: record_metadata_id Description: Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
-- # Class: EvidenceLine Description: An independent, evidence-based argument that may support or refute the validity of a specific proposition. The strength and direction of this argument is based on an interpretation of one or more pieces of information as evidence for or against the target proposition.
--     * Slot: uid
--     * Slot: direction_of_evidence_provided Description: The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral).
--     * Slot: strength_of_evidence_provided Description: The strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the direction_of_evidence_provided.
--     * Slot: score_of_evidence_provided Description: A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the direction_of_evidence_provided value.
--     * Slot: date_authored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of evidence the EvidenceLine instance represents (e.g. 'mutant phenotype evidence', 'evidence from manual interpretation', 'ACMG PM2 evidence')
--     * Slot: target_proposition_uid Description: The possible fact against which evidence items contained in an Evidence Line were collectively evaluated, in determining the overall strength and direction of support they provide. For example, in an ACMG Guideline-based assessment of variant pathogenicity, the support provided by distinct lines of evidence are assessed against a target proposition that some variant is pathogenic for a specific disease.
--     * Slot: information_quality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: record_metadata_id Description: Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
-- # Class: Proposition Description: An abstract entity representing a possible fact that is either true or false.
--     * Slot: uid
--     * Slot: proposition_text Description: A natural-language expression of the Proposition's meaning (i.e. the 'possible fact' it expresses).
--     * Slot: subject Description: The Entity or concept about which the Proposition is made.
--     * Slot: object Description: An Entity or concept that is related to the subject of a Proposition via its predicate.
--     * Slot: negated Description: A boolean flag set to 'true' to represent a negation of the proposition expressed by the subject, predicate, object, and qualifier(s) (e.g. that "Variant X is NOT pathogenic for Disease Y")
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: predicate_id Description: The relationship declared to hold between the subject and the object of the Proposition.
-- # Class: StudyGroup Description: A collection of individuals or specimens from the same taxonomic class, selected for analysis in a scientific study based on their exhibiting one or more common characteristics  (e.g. species, race, age, gender, disease state, income). May be referred to as a 'cohort' or 'population' in specific research settings.
--     * Slot: uid
--     * Slot: member_count Description: The total number of individual members in the StudyGroup.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
-- # Class: Utility Description: An abstract organizational class that groups classes acting as complex datatypes in the model - providing reusable collections of fields that can be plugged into other objects to capture sets of related information.
--     * Slot: id
-- # Class: Coding Description: A structured representation of a code for a defined concept in a terminology or code system.
--     * Slot: id
--     * Slot: code Description: A symbol uniquely identifying the concept, as in a syntax defined by the code system.  CURIE format is preferred where possible (e.g. ‘SO:0000704’ is the CURIE form of the Sequence Ontology code for 'gene').
--     * Slot: label Description: The human-readable name for the coded concept, as defined by the code system.
--     * Slot: system Description: The terminology/code system that defined the code.  May be reported as a free-text name (e.g. ‘Sequence Ontology’), but it is preferable to provide  a uri/url for the system. When the 'code' is reported as a CURIE, the 'system' should be reported as the uri that the CURIE's prefix expands to (e.g. 'http://purl.obofoundry.org/so.owl/' for the Sequence Ontology).
--     * Slot: system_version Description: Version of the terminology or code system that provided the code.
-- # Class: Qualifier Description: A key-value object used to capture additional piece of information that extends or refines the meaning of a Statement's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context.
--     * Slot: id
--     * Slot: name Description: A descriptive name that describes the type of information captured in the Qualifier value.
--     * Slot: value Description: The value of the qualifier - holding information that refines/extends the meaning of the Statement.
-- # Class: Expression Description: A structure for labels representing systematic expressions that describe an entity, as generated by formal nomenclatures (e.g. HGVS for genetic variants, ISCN for karyotypes, HLA nomenclature for HLA genes/alleles).
--     * Slot: id
--     * Slot: value Description: A free-text rendering of the expression used as a label for the entity
--     * Slot: system_url Description: A URL for the nomenclature system
--     * Slot: system_version Description: The version of the nomenclature system.
-- # Class: Extension Description: A data structure that allows custom attributes to be defined for an Entity, to capture information unique to a given content provider, or not currently supported by the core specification.
--     * Slot: id
--     * Slot: extension_description Description: A free text description of the intended meaning and use of the extension element, which may include the types of values it takes, and how to interpret these values in the context of the parent Class.
--     * Slot: name Description: A name for the Extension. Should be indicative of its meaning and/or the type of information it value represents.
--     * Slot: value Description: The value of the Extension - can be any primitive or structured object
-- # Class: RecordMetadata Description: A reusable structure that encapsulates provenance metadata about a serialized data record or object in a particular dataset (as opposed to provenance of the real world entity this record or object represents).
--     * Slot: id
--     * Slot: record_identifier Description: The identifier of the record described in the RecordMetadata object (required when the record described is not the one in the present system).
--     * Slot: record_version Description: The version number of the record-level artifact the object describes.
--     * Slot: date_record_created Description: The date the record was initially created.
-- # Class: Characteristic Description: An object holding a name-value pair used to describe a trait or role of an individual member of a StudyGroup.
--     * Slot: id
--     * Slot: name Description: The type of the trait or role described by the trait (e.g. 'ethnicity', 'sex', 'age', 'disease status').
--     * Slot: value_operator Description: An operation that defines how to logically interpret a set of more than one Characteristic values ('AND', 'OR', 'NOT').
-- # Class: Entity_identifiers
--     * Slot: Entity_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: Entity_alternative_labels
--     * Slot: Entity_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: Entity_extensions
--     * Slot: Entity_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: InformationEntity_is_about
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: is_about Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: InformationEntity_contributions
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: InformationEntity_specified_by
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: specified_by Description: A specification that describes all or part of the process that led to creation of the Information Entity.
-- # Class: InformationEntity_supporting_methods
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: supporting_methods Description: Specific methods that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: InformationEntity_supporting_method_types
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: supporting_method_types_id Description: Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: InformationEntity_derived_from
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: derived_from_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part.
-- # Class: InformationEntity_reported_in
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: reported_in Description: A document in which the Information Entity is reported.
-- # Class: InformationEntity_sources
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: sources Description: A document or other informtion resource in which the information entity, or evidence supporting it, is reported.
-- # Class: InformationEntity_identifiers
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: InformationEntity_alternative_labels
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: InformationEntity_extensions
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: Method_urls
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: urls Description: The URL/web address from which the Method can be retrieved.
-- # Class: Method_is_about
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: is_about Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: Method_contributions
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: Method_specified_by
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: specified_by Description: A specification that describes all or part of the process that led to creation of the Information Entity.
-- # Class: Method_supporting_methods
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: supporting_methods Description: Specific methods that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: Method_supporting_method_types
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: supporting_method_types_id Description: Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: Method_derived_from
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: derived_from_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part.
-- # Class: Method_reported_in
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: reported_in Description: A document in which the Information Entity is reported.
-- # Class: Method_sources
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: sources Description: A document or other informtion resource in which the information entity, or evidence supporting it, is reported.
-- # Class: Method_identifiers
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: Method_alternative_labels
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: Method_extensions
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: Document_urls
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: urls Description: One or more URLs from which the content of the Document can be retrieved.
-- # Class: Document_is_about
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: is_about Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: Document_contributions
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: Document_specified_by
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: specified_by Description: A specification that describes all or part of the process that led to creation of the Information Entity.
-- # Class: Document_supporting_methods
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: supporting_methods Description: Specific methods that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: Document_supporting_method_types
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: supporting_method_types_id Description: Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: Document_derived_from
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: derived_from_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part.
-- # Class: Document_reported_in
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: reported_in Description: A document in which the Information Entity is reported.
-- # Class: Document_sources
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: sources Description: A document or other informtion resource in which the information entity, or evidence supporting it, is reported.
-- # Class: Document_identifiers
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: Document_alternative_labels
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: Document_extensions
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: DataItem_variability_measures
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: variability_measures_uid Description: A statistical score describing the variability inherent in a data item representing a statistical summary of a set of observations/measurements (e.g. the standard deviation associated with a statistical mean calculated across several experimental replicates).
-- # Class: DataItem_component_data_item
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: component_data_item_uid Description: A more foundational data item that is a logical component of a compound data item.
-- # Class: DataItem_is_about
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: is_about Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: DataItem_contributions
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: DataItem_specified_by
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: specified_by Description: A specification that describes all or part of the process that led to creation of the Information Entity.
-- # Class: DataItem_supporting_methods
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: supporting_methods Description: Specific methods that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: DataItem_supporting_method_types
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: supporting_method_types_id Description: Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: DataItem_derived_from
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: derived_from_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part.
-- # Class: DataItem_reported_in
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: reported_in Description: A document in which the Information Entity is reported.
-- # Class: DataItem_sources
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: sources Description: A document or other informtion resource in which the information entity, or evidence supporting it, is reported.
-- # Class: DataItem_identifiers
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: DataItem_alternative_labels
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: DataItem_extensions
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: DataSet_is_about
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: is_about Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: DataSet_contributions
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: DataSet_specified_by
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: specified_by Description: A specification that describes all or part of the process that led to creation of the Information Entity.
-- # Class: DataSet_supporting_methods
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: supporting_methods Description: Specific methods that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: DataSet_supporting_method_types
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: supporting_method_types_id Description: Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: DataSet_derived_from
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: derived_from_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part.
-- # Class: DataSet_reported_in
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: reported_in Description: A document in which the Information Entity is reported.
-- # Class: DataSet_sources
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: sources Description: A document or other informtion resource in which the information entity, or evidence supporting it, is reported.
-- # Class: DataSet_identifiers
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: DataSet_alternative_labels
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: DataSet_extensions
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: Activity_performed_by
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: performed_by_uid Description: An Agent who participated in executing the Activity.
-- # Class: Activity_specified_by
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: specified_by_uid Description: A method that was followed in performing an Activity, that describes how it was executed.
-- # Class: Activity_input
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: input_uid Description: An entity that was input into the Activity (could be material or information)
-- # Class: Activity_output
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: output_uid Description: An entity that was output from the Activity (could be material or information)
-- # Class: Activity_identifiers
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: Activity_alternative_labels
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: Activity_extensions
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: Contribution_activity_type
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: activity_type_id Description: The specific type of activity performed or role played by an agent in making the contribution (e.g. for a publication, agents may contribute as a primary author, editor, figure designer, data generator, etc. . Values of this property may be framed as activities or as contribution roles (e.g. using terms from the Contribution Role Ontology (CRO)).
-- # Class: Contribution_performed_by
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: performed_by_uid Description: An Agent who participated in executing the Activity.
-- # Class: Contribution_specified_by
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: specified_by_uid Description: A method that was followed in performing an Activity, that describes how it was executed.
-- # Class: Contribution_input
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: input_uid Description: An entity that was input into the Activity (could be material or information)
-- # Class: Contribution_output
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: output_uid Description: An entity that was output from the Activity (could be material or information)
-- # Class: Contribution_identifiers
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: Contribution_alternative_labels
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: Contribution_extensions
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: Agent_identifiers
--     * Slot: Agent_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: Agent_alternative_labels
--     * Slot: Agent_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: Agent_extensions
--     * Slot: Agent_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: Statement_qualifier
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: qualifier_id Description: An additional piece of information that extends or refines the meaning of a Statement's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context.
-- # Class: Statement_has_evidence_of_types
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: has_evidence_of_types Description: A term describing a type of evidence used to assess the validity of Statement's proposition (e.g. 'sequence similarity evidence', 'in vitro assay evidence').
-- # Class: Statement_has_evidence_lines
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: has_evidence_lines_uid Description: An evidence-based argument that supports or disputes the validity of the proposition that a Statement assesses or puts forth as true. The strength and direction of this argument (whether it supports or disputes  the proposition, and how strongly) is based on an interpretation of one or more pieces of information as evidence (i.e. 'Evidence Items).
-- # Class: Statement_has_evidence
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: has_evidence_uid Description: A piece of information that represents or contributes to an argument for or against the validity of the Proposition put forth in a Statement. This is a shortcut relation that links a Statement directly to a piece of evidence supporting it, bypassing the Evidence Line class when used data creators do not utilize an Evidence Line object.
-- # Class: Statement_has_evidence_from_sources
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: has_evidence_from_sources_uid Description: An Information Entity (typically a publication, dataset, or database) that provided information used as evidence to generate the knowledge expressed in a Statement.
-- # Class: Statement_is_about
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: is_about Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: Statement_contributions
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: Statement_specified_by
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: specified_by Description: A specification that describes all or part of the process that led to creation of the Information Entity.
-- # Class: Statement_supporting_methods
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: supporting_methods Description: Specific methods that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: Statement_supporting_method_types
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: supporting_method_types_id Description: Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: Statement_derived_from
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: derived_from_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part.
-- # Class: Statement_reported_in
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: reported_in Description: A document in which the Information Entity is reported.
-- # Class: Statement_sources
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: sources Description: A document or other informtion resource in which the information entity, or evidence supporting it, is reported.
-- # Class: Statement_identifiers
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: Statement_alternative_labels
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: Statement_extensions
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: StudyResult_data_items
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: data_items_uid Description: One or more data items that are included in the StudyResult because it pertains to the 'focus' of the result. This can be data that directly describes this 'focus' (e.g. the population frequency of an allele focus), or be metadata about how data about the 'focus' were generated (e.g the quality measures for the sequencing run used to determine this allele frequency).
-- # Class: StudyResult_source_data_set
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: source_data_set_uid Description: A larger DataSet from which the content of the StudyResult was derived.
-- # Class: StudyResult_component_result
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: component_result_uid Description: Another StudyResult comprised of data items about the same focus as its parent Result, but based on a more narrowly scoped analysis of the foundational data (e.g. an analysis based on data about a subset of the parent Results full study population).
-- # Class: StudyResult_is_about
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: is_about Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: StudyResult_contributions
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: StudyResult_specified_by
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: specified_by Description: A specification that describes all or part of the process that led to creation of the Information Entity.
-- # Class: StudyResult_supporting_methods
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: supporting_methods Description: Specific methods that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: StudyResult_supporting_method_types
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: supporting_method_types_id Description: Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: StudyResult_derived_from
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: derived_from_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part.
-- # Class: StudyResult_reported_in
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: reported_in Description: A document in which the Information Entity is reported.
-- # Class: StudyResult_sources
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: sources Description: A document or other informtion resource in which the information entity, or evidence supporting it, is reported.
-- # Class: StudyResult_identifiers
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: StudyResult_alternative_labels
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: StudyResult_extensions
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: EvidenceLine_has_evidence_items
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: has_evidence_items_uid Description: An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.
-- # Class: EvidenceLine_evidence_item_sources
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: evidence_item_sources Description: An information resource (e.g. document, dataset, digital resource such as a database or  knowledgebase) that provides information interpreted as evidence in building an Evidence Line.
-- # Class: EvidenceLine_is_about
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: is_about Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: EvidenceLine_contributions
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: EvidenceLine_specified_by
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: specified_by Description: A specification that describes all or part of the process that led to creation of the Information Entity.
-- # Class: EvidenceLine_supporting_methods
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: supporting_methods Description: Specific methods that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: EvidenceLine_supporting_method_types
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: supporting_method_types_id Description: Types of methodological approaches that were executed to directly or indirectly support creation of the Information Entity.
-- # Class: EvidenceLine_derived_from
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: derived_from_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part.
-- # Class: EvidenceLine_reported_in
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: reported_in Description: A document in which the Information Entity is reported.
-- # Class: EvidenceLine_sources
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: sources Description: A document or other informtion resource in which the information entity, or evidence supporting it, is reported.
-- # Class: EvidenceLine_identifiers
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: EvidenceLine_alternative_labels
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: EvidenceLine_extensions
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: Proposition_qualifier
--     * Slot: Proposition_uid Description: Autocreated FK slot
--     * Slot: qualifier_id Description: An additional piece of information that extends or refines the meaning of a Propositions's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context.
-- # Class: Proposition_identifiers
--     * Slot: Proposition_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: Proposition_alternative_labels
--     * Slot: Proposition_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: Proposition_extensions
--     * Slot: Proposition_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: StudyGroup_is_subset_of
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: is_subset_of_uid Description: A larger StudyGroup of which this StudyGroup represents a subset.
-- # Class: StudyGroup_characteristics
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: characteristics_id Description: A feature or role shared by all members of the StudyGroup, representing a criterion for membership in the group.
-- # Class: StudyGroup_identifiers
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: StudyGroup_alternative_labels
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: alternative_labels Description: Alternative name(s) for the Entity.
-- # Class: StudyGroup_extensions
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: RecordMetadata_derived_from_record
--     * Slot: RecordMetadata_id Description: Autocreated FK slot
--     * Slot: derived_from_record Description: Another data record from which the record described here was derived, through a data ingest and/or transformation process.
-- # Class: RecordMetadata_contributions
--     * Slot: RecordMetadata_id Description: Autocreated FK slot
--     * Slot: contributions_uid Description: describes specific contributions made by an human or software agent to the creation, modification, or administrative management of a data record or object.
-- # Class: Characteristic_values
--     * Slot: Characteristic_id Description: Autocreated FK slot
--     * Slot: values Description: The specific value(s) that the indicated traitor role  holds in all population members (e.g. 'east asian', 'female', 'adolescent', 'cancer').

CREATE TABLE "Entity" (
	uid INTEGER NOT NULL,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Entity_uid" ON "Entity" (uid);

CREATE TABLE "Agent" (
	uid INTEGER NOT NULL,
	subtype TEXT,
	name TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Agent_uid" ON "Agent" (uid);

CREATE TABLE "StudyGroup" (
	uid INTEGER NOT NULL,
	member_count INTEGER,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_StudyGroup_uid" ON "StudyGroup" (uid);

CREATE TABLE "Utility" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Utility_id" ON "Utility" (id);

CREATE TABLE "Coding" (
	id INTEGER NOT NULL,
	code TEXT,
	label TEXT,
	system TEXT,
	system_version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Coding_id" ON "Coding" (id);

CREATE TABLE "Qualifier" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Qualifier_id" ON "Qualifier" (id);

CREATE TABLE "Expression" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	system_url TEXT,
	system_version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Expression_id" ON "Expression" (id);

CREATE TABLE "Extension" (
	id INTEGER NOT NULL,
	extension_description TEXT,
	name TEXT NOT NULL,
	value TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Extension_id" ON "Extension" (id);

CREATE TABLE "RecordMetadata" (
	id INTEGER NOT NULL,
	record_identifier TEXT,
	record_version TEXT,
	date_record_created TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RecordMetadata_id" ON "RecordMetadata" (id);

CREATE TABLE "Characteristic" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	value_operator TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Characteristic_id" ON "Characteristic" (id);

CREATE TABLE "InformationEntity" (
	uid INTEGER NOT NULL,
	date_authored TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	information_quality_id INTEGER,
	record_metadata_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(information_quality_id) REFERENCES "Coding" (id),
	FOREIGN KEY(record_metadata_id) REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_InformationEntity_uid" ON "InformationEntity" (uid);

CREATE TABLE "Method" (
	uid INTEGER NOT NULL,
	date_authored TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	subtype_id INTEGER,
	information_quality_id INTEGER,
	record_metadata_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id),
	FOREIGN KEY(information_quality_id) REFERENCES "Coding" (id),
	FOREIGN KEY(record_metadata_id) REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_Method_uid" ON "Method" (uid);

CREATE TABLE "Document" (
	uid INTEGER NOT NULL,
	title TEXT,
	pmid TEXT,
	doi TEXT,
	license TEXT,
	date_authored TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	subtype_id INTEGER,
	information_quality_id INTEGER,
	record_metadata_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id),
	FOREIGN KEY(information_quality_id) REFERENCES "Coding" (id),
	FOREIGN KEY(record_metadata_id) REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_Document_uid" ON "Document" (uid);

CREATE TABLE "DataItem" (
	uid INTEGER NOT NULL,
	value TEXT NOT NULL,
	date_authored TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	subtype_id INTEGER,
	unit_id INTEGER,
	confidence_interval_uid INTEGER,
	information_quality_id INTEGER,
	record_metadata_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id),
	FOREIGN KEY(unit_id) REFERENCES "Coding" (id),
	FOREIGN KEY(confidence_interval_uid) REFERENCES "DataItem" (uid),
	FOREIGN KEY(information_quality_id) REFERENCES "Coding" (id),
	FOREIGN KEY(record_metadata_id) REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_DataItem_uid" ON "DataItem" (uid);

CREATE TABLE "DataSet" (
	uid INTEGER NOT NULL,
	release_date TEXT,
	version TEXT,
	license TEXT,
	date_authored TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	subtype_id INTEGER,
	information_quality_id INTEGER,
	record_metadata_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id),
	FOREIGN KEY(information_quality_id) REFERENCES "Coding" (id),
	FOREIGN KEY(record_metadata_id) REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_DataSet_uid" ON "DataSet" (uid);

CREATE TABLE "Activity" (
	uid INTEGER NOT NULL,
	date DATE,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	subtype_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_Activity_uid" ON "Activity" (uid);

CREATE TABLE "StudyResult" (
	uid INTEGER NOT NULL,
	focus TEXT,
	date_authored TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	interpretation_id INTEGER,
	study_group_uid INTEGER,
	information_quality_id INTEGER,
	record_metadata_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(interpretation_id) REFERENCES "Coding" (id),
	FOREIGN KEY(study_group_uid) REFERENCES "StudyGroup" (uid),
	FOREIGN KEY(information_quality_id) REFERENCES "Coding" (id),
	FOREIGN KEY(record_metadata_id) REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_StudyResult_uid" ON "StudyResult" (uid);

CREATE TABLE "Proposition" (
	uid INTEGER NOT NULL,
	proposition_text TEXT,
	subject TEXT NOT NULL,
	object TEXT NOT NULL,
	negated BOOLEAN,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	predicate_id INTEGER NOT NULL,
	PRIMARY KEY (uid),
	FOREIGN KEY(predicate_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_Proposition_uid" ON "Proposition" (uid);

CREATE TABLE "Entity_identifiers" (
	"Entity_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("Entity_uid", identifiers),
	FOREIGN KEY("Entity_uid") REFERENCES "Entity" (uid)
);
CREATE INDEX "ix_Entity_identifiers_identifiers" ON "Entity_identifiers" (identifiers);
CREATE INDEX "ix_Entity_identifiers_Entity_uid" ON "Entity_identifiers" ("Entity_uid");

CREATE TABLE "Entity_alternative_labels" (
	"Entity_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("Entity_uid", alternative_labels),
	FOREIGN KEY("Entity_uid") REFERENCES "Entity" (uid)
);
CREATE INDEX "ix_Entity_alternative_labels_Entity_uid" ON "Entity_alternative_labels" ("Entity_uid");
CREATE INDEX "ix_Entity_alternative_labels_alternative_labels" ON "Entity_alternative_labels" (alternative_labels);

CREATE TABLE "Entity_extensions" (
	"Entity_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("Entity_uid", extensions_id),
	FOREIGN KEY("Entity_uid") REFERENCES "Entity" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Entity_extensions_Entity_uid" ON "Entity_extensions" ("Entity_uid");
CREATE INDEX "ix_Entity_extensions_extensions_id" ON "Entity_extensions" (extensions_id);

CREATE TABLE "Agent_identifiers" (
	"Agent_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("Agent_uid", identifiers),
	FOREIGN KEY("Agent_uid") REFERENCES "Agent" (uid)
);
CREATE INDEX "ix_Agent_identifiers_Agent_uid" ON "Agent_identifiers" ("Agent_uid");
CREATE INDEX "ix_Agent_identifiers_identifiers" ON "Agent_identifiers" (identifiers);

CREATE TABLE "Agent_alternative_labels" (
	"Agent_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("Agent_uid", alternative_labels),
	FOREIGN KEY("Agent_uid") REFERENCES "Agent" (uid)
);
CREATE INDEX "ix_Agent_alternative_labels_Agent_uid" ON "Agent_alternative_labels" ("Agent_uid");
CREATE INDEX "ix_Agent_alternative_labels_alternative_labels" ON "Agent_alternative_labels" (alternative_labels);

CREATE TABLE "Agent_extensions" (
	"Agent_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("Agent_uid", extensions_id),
	FOREIGN KEY("Agent_uid") REFERENCES "Agent" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Agent_extensions_Agent_uid" ON "Agent_extensions" ("Agent_uid");
CREATE INDEX "ix_Agent_extensions_extensions_id" ON "Agent_extensions" (extensions_id);

CREATE TABLE "StudyGroup_is_subset_of" (
	"StudyGroup_uid" INTEGER,
	is_subset_of_uid INTEGER,
	PRIMARY KEY ("StudyGroup_uid", is_subset_of_uid),
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid),
	FOREIGN KEY(is_subset_of_uid) REFERENCES "StudyGroup" (uid)
);
CREATE INDEX "ix_StudyGroup_is_subset_of_StudyGroup_uid" ON "StudyGroup_is_subset_of" ("StudyGroup_uid");
CREATE INDEX "ix_StudyGroup_is_subset_of_is_subset_of_uid" ON "StudyGroup_is_subset_of" (is_subset_of_uid);

CREATE TABLE "StudyGroup_characteristics" (
	"StudyGroup_uid" INTEGER,
	characteristics_id INTEGER,
	PRIMARY KEY ("StudyGroup_uid", characteristics_id),
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid),
	FOREIGN KEY(characteristics_id) REFERENCES "Characteristic" (id)
);
CREATE INDEX "ix_StudyGroup_characteristics_StudyGroup_uid" ON "StudyGroup_characteristics" ("StudyGroup_uid");
CREATE INDEX "ix_StudyGroup_characteristics_characteristics_id" ON "StudyGroup_characteristics" (characteristics_id);

CREATE TABLE "StudyGroup_identifiers" (
	"StudyGroup_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("StudyGroup_uid", identifiers),
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid)
);
CREATE INDEX "ix_StudyGroup_identifiers_identifiers" ON "StudyGroup_identifiers" (identifiers);
CREATE INDEX "ix_StudyGroup_identifiers_StudyGroup_uid" ON "StudyGroup_identifiers" ("StudyGroup_uid");

CREATE TABLE "StudyGroup_alternative_labels" (
	"StudyGroup_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("StudyGroup_uid", alternative_labels),
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid)
);
CREATE INDEX "ix_StudyGroup_alternative_labels_StudyGroup_uid" ON "StudyGroup_alternative_labels" ("StudyGroup_uid");
CREATE INDEX "ix_StudyGroup_alternative_labels_alternative_labels" ON "StudyGroup_alternative_labels" (alternative_labels);

CREATE TABLE "StudyGroup_extensions" (
	"StudyGroup_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("StudyGroup_uid", extensions_id),
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_StudyGroup_extensions_StudyGroup_uid" ON "StudyGroup_extensions" ("StudyGroup_uid");
CREATE INDEX "ix_StudyGroup_extensions_extensions_id" ON "StudyGroup_extensions" (extensions_id);

CREATE TABLE "RecordMetadata_derived_from_record" (
	"RecordMetadata_id" INTEGER,
	derived_from_record TEXT,
	PRIMARY KEY ("RecordMetadata_id", derived_from_record),
	FOREIGN KEY("RecordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_RecordMetadata_derived_from_record_derived_from_record" ON "RecordMetadata_derived_from_record" (derived_from_record);
CREATE INDEX "ix_RecordMetadata_derived_from_record_RecordMetadata_id" ON "RecordMetadata_derived_from_record" ("RecordMetadata_id");

CREATE TABLE "Characteristic_values" (
	"Characteristic_id" INTEGER,
	"values" TEXT NOT NULL,
	PRIMARY KEY ("Characteristic_id", "values"),
	FOREIGN KEY("Characteristic_id") REFERENCES "Characteristic" (id)
);
CREATE INDEX "ix_Characteristic_values_values" ON "Characteristic_values" ("values");
CREATE INDEX "ix_Characteristic_values_Characteristic_id" ON "Characteristic_values" ("Characteristic_id");

CREATE TABLE "Contribution" (
	uid INTEGER NOT NULL,
	date DATE,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	contributor_uid INTEGER,
	contribution_made_to_uid INTEGER,
	subtype_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(contributor_uid) REFERENCES "Agent" (uid),
	FOREIGN KEY(contribution_made_to_uid) REFERENCES "InformationEntity" (uid),
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_Contribution_uid" ON "Contribution" (uid);

CREATE TABLE "Statement" (
	uid INTEGER NOT NULL,
	statement_text TEXT,
	subject TEXT,
	object TEXT,
	direction TEXT,
	strength TEXT,
	score FLOAT,
	date_authored TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	proposition_uid INTEGER,
	predicate_id INTEGER,
	subject_classification_id INTEGER,
	information_quality_id INTEGER,
	record_metadata_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(proposition_uid) REFERENCES "Proposition" (uid),
	FOREIGN KEY(predicate_id) REFERENCES "Coding" (id),
	FOREIGN KEY(subject_classification_id) REFERENCES "Coding" (id),
	FOREIGN KEY(information_quality_id) REFERENCES "Coding" (id),
	FOREIGN KEY(record_metadata_id) REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_Statement_uid" ON "Statement" (uid);

CREATE TABLE "EvidenceLine" (
	uid INTEGER NOT NULL,
	direction_of_evidence_provided TEXT,
	strength_of_evidence_provided TEXT,
	score_of_evidence_provided FLOAT,
	date_authored TEXT,
	id TEXT NOT NULL,
	type TEXT NOT NULL,
	label TEXT,
	description TEXT,
	subtype_id INTEGER,
	target_proposition_uid INTEGER,
	information_quality_id INTEGER,
	record_metadata_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id),
	FOREIGN KEY(target_proposition_uid) REFERENCES "Proposition" (uid),
	FOREIGN KEY(information_quality_id) REFERENCES "Coding" (id),
	FOREIGN KEY(record_metadata_id) REFERENCES "RecordMetadata" (id)
);
CREATE INDEX "ix_EvidenceLine_uid" ON "EvidenceLine" (uid);

CREATE TABLE "InformationEntity_is_about" (
	"InformationEntity_uid" INTEGER,
	is_about TEXT,
	PRIMARY KEY ("InformationEntity_uid", is_about),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_InformationEntity_is_about_InformationEntity_uid" ON "InformationEntity_is_about" ("InformationEntity_uid");
CREATE INDEX "ix_InformationEntity_is_about_is_about" ON "InformationEntity_is_about" (is_about);

CREATE TABLE "InformationEntity_specified_by" (
	"InformationEntity_uid" INTEGER,
	specified_by TEXT,
	PRIMARY KEY ("InformationEntity_uid", specified_by),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_InformationEntity_specified_by_InformationEntity_uid" ON "InformationEntity_specified_by" ("InformationEntity_uid");
CREATE INDEX "ix_InformationEntity_specified_by_specified_by" ON "InformationEntity_specified_by" (specified_by);

CREATE TABLE "InformationEntity_supporting_methods" (
	"InformationEntity_uid" INTEGER,
	supporting_methods TEXT,
	PRIMARY KEY ("InformationEntity_uid", supporting_methods),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_InformationEntity_supporting_methods_InformationEntity_uid" ON "InformationEntity_supporting_methods" ("InformationEntity_uid");
CREATE INDEX "ix_InformationEntity_supporting_methods_supporting_methods" ON "InformationEntity_supporting_methods" (supporting_methods);

CREATE TABLE "InformationEntity_supporting_method_types" (
	"InformationEntity_uid" INTEGER,
	supporting_method_types_id INTEGER,
	PRIMARY KEY ("InformationEntity_uid", supporting_method_types_id),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid),
	FOREIGN KEY(supporting_method_types_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_InformationEntity_supporting_method_types_InformationEntity_uid" ON "InformationEntity_supporting_method_types" ("InformationEntity_uid");
CREATE INDEX "ix_InformationEntity_supporting_method_types_supporting_method_types_id" ON "InformationEntity_supporting_method_types" (supporting_method_types_id);

CREATE TABLE "InformationEntity_derived_from" (
	"InformationEntity_uid" INTEGER,
	derived_from_uid INTEGER,
	PRIMARY KEY ("InformationEntity_uid", derived_from_uid),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid),
	FOREIGN KEY(derived_from_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_InformationEntity_derived_from_derived_from_uid" ON "InformationEntity_derived_from" (derived_from_uid);
CREATE INDEX "ix_InformationEntity_derived_from_InformationEntity_uid" ON "InformationEntity_derived_from" ("InformationEntity_uid");

CREATE TABLE "InformationEntity_reported_in" (
	"InformationEntity_uid" INTEGER,
	reported_in TEXT,
	PRIMARY KEY ("InformationEntity_uid", reported_in),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_InformationEntity_reported_in_reported_in" ON "InformationEntity_reported_in" (reported_in);
CREATE INDEX "ix_InformationEntity_reported_in_InformationEntity_uid" ON "InformationEntity_reported_in" ("InformationEntity_uid");

CREATE TABLE "InformationEntity_sources" (
	"InformationEntity_uid" INTEGER,
	sources TEXT,
	PRIMARY KEY ("InformationEntity_uid", sources),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_InformationEntity_sources_InformationEntity_uid" ON "InformationEntity_sources" ("InformationEntity_uid");
CREATE INDEX "ix_InformationEntity_sources_sources" ON "InformationEntity_sources" (sources);

CREATE TABLE "InformationEntity_identifiers" (
	"InformationEntity_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("InformationEntity_uid", identifiers),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_InformationEntity_identifiers_identifiers" ON "InformationEntity_identifiers" (identifiers);
CREATE INDEX "ix_InformationEntity_identifiers_InformationEntity_uid" ON "InformationEntity_identifiers" ("InformationEntity_uid");

CREATE TABLE "InformationEntity_alternative_labels" (
	"InformationEntity_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("InformationEntity_uid", alternative_labels),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_InformationEntity_alternative_labels_alternative_labels" ON "InformationEntity_alternative_labels" (alternative_labels);
CREATE INDEX "ix_InformationEntity_alternative_labels_InformationEntity_uid" ON "InformationEntity_alternative_labels" ("InformationEntity_uid");

CREATE TABLE "InformationEntity_extensions" (
	"InformationEntity_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("InformationEntity_uid", extensions_id),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_InformationEntity_extensions_InformationEntity_uid" ON "InformationEntity_extensions" ("InformationEntity_uid");
CREATE INDEX "ix_InformationEntity_extensions_extensions_id" ON "InformationEntity_extensions" (extensions_id);

CREATE TABLE "Method_urls" (
	"Method_uid" INTEGER,
	urls TEXT,
	PRIMARY KEY ("Method_uid", urls),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Method_urls_Method_uid" ON "Method_urls" ("Method_uid");
CREATE INDEX "ix_Method_urls_urls" ON "Method_urls" (urls);

CREATE TABLE "Method_is_about" (
	"Method_uid" INTEGER,
	is_about TEXT,
	PRIMARY KEY ("Method_uid", is_about),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Method_is_about_Method_uid" ON "Method_is_about" ("Method_uid");
CREATE INDEX "ix_Method_is_about_is_about" ON "Method_is_about" (is_about);

CREATE TABLE "Method_specified_by" (
	"Method_uid" INTEGER,
	specified_by TEXT,
	PRIMARY KEY ("Method_uid", specified_by),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Method_specified_by_specified_by" ON "Method_specified_by" (specified_by);
CREATE INDEX "ix_Method_specified_by_Method_uid" ON "Method_specified_by" ("Method_uid");

CREATE TABLE "Method_supporting_methods" (
	"Method_uid" INTEGER,
	supporting_methods TEXT,
	PRIMARY KEY ("Method_uid", supporting_methods),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Method_supporting_methods_Method_uid" ON "Method_supporting_methods" ("Method_uid");
CREATE INDEX "ix_Method_supporting_methods_supporting_methods" ON "Method_supporting_methods" (supporting_methods);

CREATE TABLE "Method_supporting_method_types" (
	"Method_uid" INTEGER,
	supporting_method_types_id INTEGER,
	PRIMARY KEY ("Method_uid", supporting_method_types_id),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid),
	FOREIGN KEY(supporting_method_types_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_Method_supporting_method_types_supporting_method_types_id" ON "Method_supporting_method_types" (supporting_method_types_id);
CREATE INDEX "ix_Method_supporting_method_types_Method_uid" ON "Method_supporting_method_types" ("Method_uid");

CREATE TABLE "Method_derived_from" (
	"Method_uid" INTEGER,
	derived_from_uid INTEGER,
	PRIMARY KEY ("Method_uid", derived_from_uid),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid),
	FOREIGN KEY(derived_from_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_Method_derived_from_derived_from_uid" ON "Method_derived_from" (derived_from_uid);
CREATE INDEX "ix_Method_derived_from_Method_uid" ON "Method_derived_from" ("Method_uid");

CREATE TABLE "Method_reported_in" (
	"Method_uid" INTEGER,
	reported_in TEXT,
	PRIMARY KEY ("Method_uid", reported_in),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Method_reported_in_reported_in" ON "Method_reported_in" (reported_in);
CREATE INDEX "ix_Method_reported_in_Method_uid" ON "Method_reported_in" ("Method_uid");

CREATE TABLE "Method_sources" (
	"Method_uid" INTEGER,
	sources TEXT,
	PRIMARY KEY ("Method_uid", sources),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Method_sources_sources" ON "Method_sources" (sources);
CREATE INDEX "ix_Method_sources_Method_uid" ON "Method_sources" ("Method_uid");

CREATE TABLE "Method_identifiers" (
	"Method_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("Method_uid", identifiers),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Method_identifiers_Method_uid" ON "Method_identifiers" ("Method_uid");
CREATE INDEX "ix_Method_identifiers_identifiers" ON "Method_identifiers" (identifiers);

CREATE TABLE "Method_alternative_labels" (
	"Method_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("Method_uid", alternative_labels),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Method_alternative_labels_alternative_labels" ON "Method_alternative_labels" (alternative_labels);
CREATE INDEX "ix_Method_alternative_labels_Method_uid" ON "Method_alternative_labels" ("Method_uid");

CREATE TABLE "Method_extensions" (
	"Method_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("Method_uid", extensions_id),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Method_extensions_Method_uid" ON "Method_extensions" ("Method_uid");
CREATE INDEX "ix_Method_extensions_extensions_id" ON "Method_extensions" (extensions_id);

CREATE TABLE "Document_urls" (
	"Document_uid" INTEGER,
	urls TEXT,
	PRIMARY KEY ("Document_uid", urls),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE INDEX "ix_Document_urls_urls" ON "Document_urls" (urls);
CREATE INDEX "ix_Document_urls_Document_uid" ON "Document_urls" ("Document_uid");

CREATE TABLE "Document_is_about" (
	"Document_uid" INTEGER,
	is_about TEXT,
	PRIMARY KEY ("Document_uid", is_about),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE INDEX "ix_Document_is_about_Document_uid" ON "Document_is_about" ("Document_uid");
CREATE INDEX "ix_Document_is_about_is_about" ON "Document_is_about" (is_about);

CREATE TABLE "Document_specified_by" (
	"Document_uid" INTEGER,
	specified_by TEXT,
	PRIMARY KEY ("Document_uid", specified_by),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE INDEX "ix_Document_specified_by_Document_uid" ON "Document_specified_by" ("Document_uid");
CREATE INDEX "ix_Document_specified_by_specified_by" ON "Document_specified_by" (specified_by);

CREATE TABLE "Document_supporting_methods" (
	"Document_uid" INTEGER,
	supporting_methods TEXT,
	PRIMARY KEY ("Document_uid", supporting_methods),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE INDEX "ix_Document_supporting_methods_Document_uid" ON "Document_supporting_methods" ("Document_uid");
CREATE INDEX "ix_Document_supporting_methods_supporting_methods" ON "Document_supporting_methods" (supporting_methods);

CREATE TABLE "Document_supporting_method_types" (
	"Document_uid" INTEGER,
	supporting_method_types_id INTEGER,
	PRIMARY KEY ("Document_uid", supporting_method_types_id),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid),
	FOREIGN KEY(supporting_method_types_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_Document_supporting_method_types_supporting_method_types_id" ON "Document_supporting_method_types" (supporting_method_types_id);
CREATE INDEX "ix_Document_supporting_method_types_Document_uid" ON "Document_supporting_method_types" ("Document_uid");

CREATE TABLE "Document_derived_from" (
	"Document_uid" INTEGER,
	derived_from_uid INTEGER,
	PRIMARY KEY ("Document_uid", derived_from_uid),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid),
	FOREIGN KEY(derived_from_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_Document_derived_from_Document_uid" ON "Document_derived_from" ("Document_uid");
CREATE INDEX "ix_Document_derived_from_derived_from_uid" ON "Document_derived_from" (derived_from_uid);

CREATE TABLE "Document_reported_in" (
	"Document_uid" INTEGER,
	reported_in TEXT,
	PRIMARY KEY ("Document_uid", reported_in),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE INDEX "ix_Document_reported_in_Document_uid" ON "Document_reported_in" ("Document_uid");
CREATE INDEX "ix_Document_reported_in_reported_in" ON "Document_reported_in" (reported_in);

CREATE TABLE "Document_sources" (
	"Document_uid" INTEGER,
	sources TEXT,
	PRIMARY KEY ("Document_uid", sources),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE INDEX "ix_Document_sources_sources" ON "Document_sources" (sources);
CREATE INDEX "ix_Document_sources_Document_uid" ON "Document_sources" ("Document_uid");

CREATE TABLE "Document_identifiers" (
	"Document_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("Document_uid", identifiers),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE INDEX "ix_Document_identifiers_identifiers" ON "Document_identifiers" (identifiers);
CREATE INDEX "ix_Document_identifiers_Document_uid" ON "Document_identifiers" ("Document_uid");

CREATE TABLE "Document_alternative_labels" (
	"Document_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("Document_uid", alternative_labels),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE INDEX "ix_Document_alternative_labels_Document_uid" ON "Document_alternative_labels" ("Document_uid");
CREATE INDEX "ix_Document_alternative_labels_alternative_labels" ON "Document_alternative_labels" (alternative_labels);

CREATE TABLE "Document_extensions" (
	"Document_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("Document_uid", extensions_id),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Document_extensions_Document_uid" ON "Document_extensions" ("Document_uid");
CREATE INDEX "ix_Document_extensions_extensions_id" ON "Document_extensions" (extensions_id);

CREATE TABLE "DataItem_variability_measures" (
	"DataItem_uid" INTEGER,
	variability_measures_uid INTEGER,
	PRIMARY KEY ("DataItem_uid", variability_measures_uid),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid),
	FOREIGN KEY(variability_measures_uid) REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_variability_measures_variability_measures_uid" ON "DataItem_variability_measures" (variability_measures_uid);
CREATE INDEX "ix_DataItem_variability_measures_DataItem_uid" ON "DataItem_variability_measures" ("DataItem_uid");

CREATE TABLE "DataItem_component_data_item" (
	"DataItem_uid" INTEGER,
	component_data_item_uid INTEGER,
	PRIMARY KEY ("DataItem_uid", component_data_item_uid),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid),
	FOREIGN KEY(component_data_item_uid) REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_component_data_item_DataItem_uid" ON "DataItem_component_data_item" ("DataItem_uid");
CREATE INDEX "ix_DataItem_component_data_item_component_data_item_uid" ON "DataItem_component_data_item" (component_data_item_uid);

CREATE TABLE "DataItem_is_about" (
	"DataItem_uid" INTEGER,
	is_about TEXT,
	PRIMARY KEY ("DataItem_uid", is_about),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_is_about_is_about" ON "DataItem_is_about" (is_about);
CREATE INDEX "ix_DataItem_is_about_DataItem_uid" ON "DataItem_is_about" ("DataItem_uid");

CREATE TABLE "DataItem_specified_by" (
	"DataItem_uid" INTEGER,
	specified_by TEXT,
	PRIMARY KEY ("DataItem_uid", specified_by),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_specified_by_DataItem_uid" ON "DataItem_specified_by" ("DataItem_uid");
CREATE INDEX "ix_DataItem_specified_by_specified_by" ON "DataItem_specified_by" (specified_by);

CREATE TABLE "DataItem_supporting_methods" (
	"DataItem_uid" INTEGER,
	supporting_methods TEXT,
	PRIMARY KEY ("DataItem_uid", supporting_methods),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_supporting_methods_DataItem_uid" ON "DataItem_supporting_methods" ("DataItem_uid");
CREATE INDEX "ix_DataItem_supporting_methods_supporting_methods" ON "DataItem_supporting_methods" (supporting_methods);

CREATE TABLE "DataItem_supporting_method_types" (
	"DataItem_uid" INTEGER,
	supporting_method_types_id INTEGER,
	PRIMARY KEY ("DataItem_uid", supporting_method_types_id),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid),
	FOREIGN KEY(supporting_method_types_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_DataItem_supporting_method_types_supporting_method_types_id" ON "DataItem_supporting_method_types" (supporting_method_types_id);
CREATE INDEX "ix_DataItem_supporting_method_types_DataItem_uid" ON "DataItem_supporting_method_types" ("DataItem_uid");

CREATE TABLE "DataItem_derived_from" (
	"DataItem_uid" INTEGER,
	derived_from_uid INTEGER,
	PRIMARY KEY ("DataItem_uid", derived_from_uid),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid),
	FOREIGN KEY(derived_from_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_DataItem_derived_from_derived_from_uid" ON "DataItem_derived_from" (derived_from_uid);
CREATE INDEX "ix_DataItem_derived_from_DataItem_uid" ON "DataItem_derived_from" ("DataItem_uid");

CREATE TABLE "DataItem_reported_in" (
	"DataItem_uid" INTEGER,
	reported_in TEXT,
	PRIMARY KEY ("DataItem_uid", reported_in),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_reported_in_reported_in" ON "DataItem_reported_in" (reported_in);
CREATE INDEX "ix_DataItem_reported_in_DataItem_uid" ON "DataItem_reported_in" ("DataItem_uid");

CREATE TABLE "DataItem_sources" (
	"DataItem_uid" INTEGER,
	sources TEXT,
	PRIMARY KEY ("DataItem_uid", sources),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_sources_sources" ON "DataItem_sources" (sources);
CREATE INDEX "ix_DataItem_sources_DataItem_uid" ON "DataItem_sources" ("DataItem_uid");

CREATE TABLE "DataItem_identifiers" (
	"DataItem_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("DataItem_uid", identifiers),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_identifiers_identifiers" ON "DataItem_identifiers" (identifiers);
CREATE INDEX "ix_DataItem_identifiers_DataItem_uid" ON "DataItem_identifiers" ("DataItem_uid");

CREATE TABLE "DataItem_alternative_labels" (
	"DataItem_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("DataItem_uid", alternative_labels),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_DataItem_alternative_labels_DataItem_uid" ON "DataItem_alternative_labels" ("DataItem_uid");
CREATE INDEX "ix_DataItem_alternative_labels_alternative_labels" ON "DataItem_alternative_labels" (alternative_labels);

CREATE TABLE "DataItem_extensions" (
	"DataItem_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("DataItem_uid", extensions_id),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_DataItem_extensions_DataItem_uid" ON "DataItem_extensions" ("DataItem_uid");
CREATE INDEX "ix_DataItem_extensions_extensions_id" ON "DataItem_extensions" (extensions_id);

CREATE TABLE "DataSet_is_about" (
	"DataSet_uid" INTEGER,
	is_about TEXT,
	PRIMARY KEY ("DataSet_uid", is_about),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE INDEX "ix_DataSet_is_about_DataSet_uid" ON "DataSet_is_about" ("DataSet_uid");
CREATE INDEX "ix_DataSet_is_about_is_about" ON "DataSet_is_about" (is_about);

CREATE TABLE "DataSet_specified_by" (
	"DataSet_uid" INTEGER,
	specified_by TEXT,
	PRIMARY KEY ("DataSet_uid", specified_by),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE INDEX "ix_DataSet_specified_by_specified_by" ON "DataSet_specified_by" (specified_by);
CREATE INDEX "ix_DataSet_specified_by_DataSet_uid" ON "DataSet_specified_by" ("DataSet_uid");

CREATE TABLE "DataSet_supporting_methods" (
	"DataSet_uid" INTEGER,
	supporting_methods TEXT,
	PRIMARY KEY ("DataSet_uid", supporting_methods),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE INDEX "ix_DataSet_supporting_methods_supporting_methods" ON "DataSet_supporting_methods" (supporting_methods);
CREATE INDEX "ix_DataSet_supporting_methods_DataSet_uid" ON "DataSet_supporting_methods" ("DataSet_uid");

CREATE TABLE "DataSet_supporting_method_types" (
	"DataSet_uid" INTEGER,
	supporting_method_types_id INTEGER,
	PRIMARY KEY ("DataSet_uid", supporting_method_types_id),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid),
	FOREIGN KEY(supporting_method_types_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_DataSet_supporting_method_types_DataSet_uid" ON "DataSet_supporting_method_types" ("DataSet_uid");
CREATE INDEX "ix_DataSet_supporting_method_types_supporting_method_types_id" ON "DataSet_supporting_method_types" (supporting_method_types_id);

CREATE TABLE "DataSet_derived_from" (
	"DataSet_uid" INTEGER,
	derived_from_uid INTEGER,
	PRIMARY KEY ("DataSet_uid", derived_from_uid),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid),
	FOREIGN KEY(derived_from_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_DataSet_derived_from_DataSet_uid" ON "DataSet_derived_from" ("DataSet_uid");
CREATE INDEX "ix_DataSet_derived_from_derived_from_uid" ON "DataSet_derived_from" (derived_from_uid);

CREATE TABLE "DataSet_reported_in" (
	"DataSet_uid" INTEGER,
	reported_in TEXT,
	PRIMARY KEY ("DataSet_uid", reported_in),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE INDEX "ix_DataSet_reported_in_DataSet_uid" ON "DataSet_reported_in" ("DataSet_uid");
CREATE INDEX "ix_DataSet_reported_in_reported_in" ON "DataSet_reported_in" (reported_in);

CREATE TABLE "DataSet_sources" (
	"DataSet_uid" INTEGER,
	sources TEXT,
	PRIMARY KEY ("DataSet_uid", sources),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE INDEX "ix_DataSet_sources_DataSet_uid" ON "DataSet_sources" ("DataSet_uid");
CREATE INDEX "ix_DataSet_sources_sources" ON "DataSet_sources" (sources);

CREATE TABLE "DataSet_identifiers" (
	"DataSet_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("DataSet_uid", identifiers),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE INDEX "ix_DataSet_identifiers_DataSet_uid" ON "DataSet_identifiers" ("DataSet_uid");
CREATE INDEX "ix_DataSet_identifiers_identifiers" ON "DataSet_identifiers" (identifiers);

CREATE TABLE "DataSet_alternative_labels" (
	"DataSet_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("DataSet_uid", alternative_labels),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE INDEX "ix_DataSet_alternative_labels_DataSet_uid" ON "DataSet_alternative_labels" ("DataSet_uid");
CREATE INDEX "ix_DataSet_alternative_labels_alternative_labels" ON "DataSet_alternative_labels" (alternative_labels);

CREATE TABLE "DataSet_extensions" (
	"DataSet_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("DataSet_uid", extensions_id),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_DataSet_extensions_extensions_id" ON "DataSet_extensions" (extensions_id);
CREATE INDEX "ix_DataSet_extensions_DataSet_uid" ON "DataSet_extensions" ("DataSet_uid");

CREATE TABLE "Activity_performed_by" (
	"Activity_uid" INTEGER,
	performed_by_uid INTEGER,
	PRIMARY KEY ("Activity_uid", performed_by_uid),
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid),
	FOREIGN KEY(performed_by_uid) REFERENCES "Agent" (uid)
);
CREATE INDEX "ix_Activity_performed_by_performed_by_uid" ON "Activity_performed_by" (performed_by_uid);
CREATE INDEX "ix_Activity_performed_by_Activity_uid" ON "Activity_performed_by" ("Activity_uid");

CREATE TABLE "Activity_specified_by" (
	"Activity_uid" INTEGER,
	specified_by_uid INTEGER,
	PRIMARY KEY ("Activity_uid", specified_by_uid),
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid),
	FOREIGN KEY(specified_by_uid) REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Activity_specified_by_Activity_uid" ON "Activity_specified_by" ("Activity_uid");
CREATE INDEX "ix_Activity_specified_by_specified_by_uid" ON "Activity_specified_by" (specified_by_uid);

CREATE TABLE "Activity_input" (
	"Activity_uid" INTEGER,
	input_uid INTEGER,
	PRIMARY KEY ("Activity_uid", input_uid),
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid),
	FOREIGN KEY(input_uid) REFERENCES "Entity" (uid)
);
CREATE INDEX "ix_Activity_input_Activity_uid" ON "Activity_input" ("Activity_uid");
CREATE INDEX "ix_Activity_input_input_uid" ON "Activity_input" (input_uid);

CREATE TABLE "Activity_output" (
	"Activity_uid" INTEGER,
	output_uid INTEGER,
	PRIMARY KEY ("Activity_uid", output_uid),
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid),
	FOREIGN KEY(output_uid) REFERENCES "Entity" (uid)
);
CREATE INDEX "ix_Activity_output_Activity_uid" ON "Activity_output" ("Activity_uid");
CREATE INDEX "ix_Activity_output_output_uid" ON "Activity_output" (output_uid);

CREATE TABLE "Activity_identifiers" (
	"Activity_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("Activity_uid", identifiers),
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid)
);
CREATE INDEX "ix_Activity_identifiers_identifiers" ON "Activity_identifiers" (identifiers);
CREATE INDEX "ix_Activity_identifiers_Activity_uid" ON "Activity_identifiers" ("Activity_uid");

CREATE TABLE "Activity_alternative_labels" (
	"Activity_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("Activity_uid", alternative_labels),
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid)
);
CREATE INDEX "ix_Activity_alternative_labels_alternative_labels" ON "Activity_alternative_labels" (alternative_labels);
CREATE INDEX "ix_Activity_alternative_labels_Activity_uid" ON "Activity_alternative_labels" ("Activity_uid");

CREATE TABLE "Activity_extensions" (
	"Activity_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("Activity_uid", extensions_id),
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Activity_extensions_Activity_uid" ON "Activity_extensions" ("Activity_uid");
CREATE INDEX "ix_Activity_extensions_extensions_id" ON "Activity_extensions" (extensions_id);

CREATE TABLE "StudyResult_data_items" (
	"StudyResult_uid" INTEGER,
	data_items_uid INTEGER,
	PRIMARY KEY ("StudyResult_uid", data_items_uid),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid),
	FOREIGN KEY(data_items_uid) REFERENCES "DataItem" (uid)
);
CREATE INDEX "ix_StudyResult_data_items_data_items_uid" ON "StudyResult_data_items" (data_items_uid);
CREATE INDEX "ix_StudyResult_data_items_StudyResult_uid" ON "StudyResult_data_items" ("StudyResult_uid");

CREATE TABLE "StudyResult_source_data_set" (
	"StudyResult_uid" INTEGER,
	source_data_set_uid INTEGER,
	PRIMARY KEY ("StudyResult_uid", source_data_set_uid),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid),
	FOREIGN KEY(source_data_set_uid) REFERENCES "DataSet" (uid)
);
CREATE INDEX "ix_StudyResult_source_data_set_source_data_set_uid" ON "StudyResult_source_data_set" (source_data_set_uid);
CREATE INDEX "ix_StudyResult_source_data_set_StudyResult_uid" ON "StudyResult_source_data_set" ("StudyResult_uid");

CREATE TABLE "StudyResult_component_result" (
	"StudyResult_uid" INTEGER,
	component_result_uid INTEGER,
	PRIMARY KEY ("StudyResult_uid", component_result_uid),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid),
	FOREIGN KEY(component_result_uid) REFERENCES "StudyResult" (uid)
);
CREATE INDEX "ix_StudyResult_component_result_StudyResult_uid" ON "StudyResult_component_result" ("StudyResult_uid");
CREATE INDEX "ix_StudyResult_component_result_component_result_uid" ON "StudyResult_component_result" (component_result_uid);

CREATE TABLE "StudyResult_is_about" (
	"StudyResult_uid" INTEGER,
	is_about TEXT,
	PRIMARY KEY ("StudyResult_uid", is_about),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE INDEX "ix_StudyResult_is_about_StudyResult_uid" ON "StudyResult_is_about" ("StudyResult_uid");
CREATE INDEX "ix_StudyResult_is_about_is_about" ON "StudyResult_is_about" (is_about);

CREATE TABLE "StudyResult_specified_by" (
	"StudyResult_uid" INTEGER,
	specified_by TEXT,
	PRIMARY KEY ("StudyResult_uid", specified_by),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE INDEX "ix_StudyResult_specified_by_specified_by" ON "StudyResult_specified_by" (specified_by);
CREATE INDEX "ix_StudyResult_specified_by_StudyResult_uid" ON "StudyResult_specified_by" ("StudyResult_uid");

CREATE TABLE "StudyResult_supporting_methods" (
	"StudyResult_uid" INTEGER,
	supporting_methods TEXT,
	PRIMARY KEY ("StudyResult_uid", supporting_methods),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE INDEX "ix_StudyResult_supporting_methods_StudyResult_uid" ON "StudyResult_supporting_methods" ("StudyResult_uid");
CREATE INDEX "ix_StudyResult_supporting_methods_supporting_methods" ON "StudyResult_supporting_methods" (supporting_methods);

CREATE TABLE "StudyResult_supporting_method_types" (
	"StudyResult_uid" INTEGER,
	supporting_method_types_id INTEGER,
	PRIMARY KEY ("StudyResult_uid", supporting_method_types_id),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid),
	FOREIGN KEY(supporting_method_types_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_StudyResult_supporting_method_types_StudyResult_uid" ON "StudyResult_supporting_method_types" ("StudyResult_uid");
CREATE INDEX "ix_StudyResult_supporting_method_types_supporting_method_types_id" ON "StudyResult_supporting_method_types" (supporting_method_types_id);

CREATE TABLE "StudyResult_derived_from" (
	"StudyResult_uid" INTEGER,
	derived_from_uid INTEGER,
	PRIMARY KEY ("StudyResult_uid", derived_from_uid),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid),
	FOREIGN KEY(derived_from_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_StudyResult_derived_from_derived_from_uid" ON "StudyResult_derived_from" (derived_from_uid);
CREATE INDEX "ix_StudyResult_derived_from_StudyResult_uid" ON "StudyResult_derived_from" ("StudyResult_uid");

CREATE TABLE "StudyResult_reported_in" (
	"StudyResult_uid" INTEGER,
	reported_in TEXT,
	PRIMARY KEY ("StudyResult_uid", reported_in),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE INDEX "ix_StudyResult_reported_in_reported_in" ON "StudyResult_reported_in" (reported_in);
CREATE INDEX "ix_StudyResult_reported_in_StudyResult_uid" ON "StudyResult_reported_in" ("StudyResult_uid");

CREATE TABLE "StudyResult_sources" (
	"StudyResult_uid" INTEGER,
	sources TEXT,
	PRIMARY KEY ("StudyResult_uid", sources),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE INDEX "ix_StudyResult_sources_sources" ON "StudyResult_sources" (sources);
CREATE INDEX "ix_StudyResult_sources_StudyResult_uid" ON "StudyResult_sources" ("StudyResult_uid");

CREATE TABLE "StudyResult_identifiers" (
	"StudyResult_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("StudyResult_uid", identifiers),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE INDEX "ix_StudyResult_identifiers_StudyResult_uid" ON "StudyResult_identifiers" ("StudyResult_uid");
CREATE INDEX "ix_StudyResult_identifiers_identifiers" ON "StudyResult_identifiers" (identifiers);

CREATE TABLE "StudyResult_alternative_labels" (
	"StudyResult_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("StudyResult_uid", alternative_labels),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE INDEX "ix_StudyResult_alternative_labels_alternative_labels" ON "StudyResult_alternative_labels" (alternative_labels);
CREATE INDEX "ix_StudyResult_alternative_labels_StudyResult_uid" ON "StudyResult_alternative_labels" ("StudyResult_uid");

CREATE TABLE "StudyResult_extensions" (
	"StudyResult_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("StudyResult_uid", extensions_id),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_StudyResult_extensions_extensions_id" ON "StudyResult_extensions" (extensions_id);
CREATE INDEX "ix_StudyResult_extensions_StudyResult_uid" ON "StudyResult_extensions" ("StudyResult_uid");

CREATE TABLE "Proposition_qualifier" (
	"Proposition_uid" INTEGER,
	qualifier_id INTEGER,
	PRIMARY KEY ("Proposition_uid", qualifier_id),
	FOREIGN KEY("Proposition_uid") REFERENCES "Proposition" (uid),
	FOREIGN KEY(qualifier_id) REFERENCES "Qualifier" (id)
);
CREATE INDEX "ix_Proposition_qualifier_qualifier_id" ON "Proposition_qualifier" (qualifier_id);
CREATE INDEX "ix_Proposition_qualifier_Proposition_uid" ON "Proposition_qualifier" ("Proposition_uid");

CREATE TABLE "Proposition_identifiers" (
	"Proposition_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("Proposition_uid", identifiers),
	FOREIGN KEY("Proposition_uid") REFERENCES "Proposition" (uid)
);
CREATE INDEX "ix_Proposition_identifiers_Proposition_uid" ON "Proposition_identifiers" ("Proposition_uid");
CREATE INDEX "ix_Proposition_identifiers_identifiers" ON "Proposition_identifiers" (identifiers);

CREATE TABLE "Proposition_alternative_labels" (
	"Proposition_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("Proposition_uid", alternative_labels),
	FOREIGN KEY("Proposition_uid") REFERENCES "Proposition" (uid)
);
CREATE INDEX "ix_Proposition_alternative_labels_Proposition_uid" ON "Proposition_alternative_labels" ("Proposition_uid");
CREATE INDEX "ix_Proposition_alternative_labels_alternative_labels" ON "Proposition_alternative_labels" (alternative_labels);

CREATE TABLE "Proposition_extensions" (
	"Proposition_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("Proposition_uid", extensions_id),
	FOREIGN KEY("Proposition_uid") REFERENCES "Proposition" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Proposition_extensions_Proposition_uid" ON "Proposition_extensions" ("Proposition_uid");
CREATE INDEX "ix_Proposition_extensions_extensions_id" ON "Proposition_extensions" (extensions_id);

CREATE TABLE "InformationEntity_contributions" (
	"InformationEntity_uid" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("InformationEntity_uid", contributions_uid),
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_InformationEntity_contributions_InformationEntity_uid" ON "InformationEntity_contributions" ("InformationEntity_uid");
CREATE INDEX "ix_InformationEntity_contributions_contributions_uid" ON "InformationEntity_contributions" (contributions_uid);

CREATE TABLE "Method_contributions" (
	"Method_uid" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("Method_uid", contributions_uid),
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_Method_contributions_contributions_uid" ON "Method_contributions" (contributions_uid);
CREATE INDEX "ix_Method_contributions_Method_uid" ON "Method_contributions" ("Method_uid");

CREATE TABLE "Document_contributions" (
	"Document_uid" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("Document_uid", contributions_uid),
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_Document_contributions_Document_uid" ON "Document_contributions" ("Document_uid");
CREATE INDEX "ix_Document_contributions_contributions_uid" ON "Document_contributions" (contributions_uid);

CREATE TABLE "DataItem_contributions" (
	"DataItem_uid" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("DataItem_uid", contributions_uid),
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_DataItem_contributions_contributions_uid" ON "DataItem_contributions" (contributions_uid);
CREATE INDEX "ix_DataItem_contributions_DataItem_uid" ON "DataItem_contributions" ("DataItem_uid");

CREATE TABLE "DataSet_contributions" (
	"DataSet_uid" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("DataSet_uid", contributions_uid),
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_DataSet_contributions_DataSet_uid" ON "DataSet_contributions" ("DataSet_uid");
CREATE INDEX "ix_DataSet_contributions_contributions_uid" ON "DataSet_contributions" (contributions_uid);

CREATE TABLE "Contribution_activity_type" (
	"Contribution_uid" INTEGER,
	activity_type_id INTEGER,
	PRIMARY KEY ("Contribution_uid", activity_type_id),
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid),
	FOREIGN KEY(activity_type_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_Contribution_activity_type_activity_type_id" ON "Contribution_activity_type" (activity_type_id);
CREATE INDEX "ix_Contribution_activity_type_Contribution_uid" ON "Contribution_activity_type" ("Contribution_uid");

CREATE TABLE "Contribution_performed_by" (
	"Contribution_uid" INTEGER,
	performed_by_uid INTEGER,
	PRIMARY KEY ("Contribution_uid", performed_by_uid),
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid),
	FOREIGN KEY(performed_by_uid) REFERENCES "Agent" (uid)
);
CREATE INDEX "ix_Contribution_performed_by_Contribution_uid" ON "Contribution_performed_by" ("Contribution_uid");
CREATE INDEX "ix_Contribution_performed_by_performed_by_uid" ON "Contribution_performed_by" (performed_by_uid);

CREATE TABLE "Contribution_specified_by" (
	"Contribution_uid" INTEGER,
	specified_by_uid INTEGER,
	PRIMARY KEY ("Contribution_uid", specified_by_uid),
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid),
	FOREIGN KEY(specified_by_uid) REFERENCES "Method" (uid)
);
CREATE INDEX "ix_Contribution_specified_by_specified_by_uid" ON "Contribution_specified_by" (specified_by_uid);
CREATE INDEX "ix_Contribution_specified_by_Contribution_uid" ON "Contribution_specified_by" ("Contribution_uid");

CREATE TABLE "Contribution_input" (
	"Contribution_uid" INTEGER,
	input_uid INTEGER,
	PRIMARY KEY ("Contribution_uid", input_uid),
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid),
	FOREIGN KEY(input_uid) REFERENCES "Entity" (uid)
);
CREATE INDEX "ix_Contribution_input_Contribution_uid" ON "Contribution_input" ("Contribution_uid");
CREATE INDEX "ix_Contribution_input_input_uid" ON "Contribution_input" (input_uid);

CREATE TABLE "Contribution_output" (
	"Contribution_uid" INTEGER,
	output_uid INTEGER,
	PRIMARY KEY ("Contribution_uid", output_uid),
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid),
	FOREIGN KEY(output_uid) REFERENCES "Entity" (uid)
);
CREATE INDEX "ix_Contribution_output_Contribution_uid" ON "Contribution_output" ("Contribution_uid");
CREATE INDEX "ix_Contribution_output_output_uid" ON "Contribution_output" (output_uid);

CREATE TABLE "Contribution_identifiers" (
	"Contribution_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("Contribution_uid", identifiers),
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_Contribution_identifiers_Contribution_uid" ON "Contribution_identifiers" ("Contribution_uid");
CREATE INDEX "ix_Contribution_identifiers_identifiers" ON "Contribution_identifiers" (identifiers);

CREATE TABLE "Contribution_alternative_labels" (
	"Contribution_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("Contribution_uid", alternative_labels),
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_Contribution_alternative_labels_Contribution_uid" ON "Contribution_alternative_labels" ("Contribution_uid");
CREATE INDEX "ix_Contribution_alternative_labels_alternative_labels" ON "Contribution_alternative_labels" (alternative_labels);

CREATE TABLE "Contribution_extensions" (
	"Contribution_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("Contribution_uid", extensions_id),
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Contribution_extensions_extensions_id" ON "Contribution_extensions" (extensions_id);
CREATE INDEX "ix_Contribution_extensions_Contribution_uid" ON "Contribution_extensions" ("Contribution_uid");

CREATE TABLE "Statement_qualifier" (
	"Statement_uid" INTEGER,
	qualifier_id INTEGER,
	PRIMARY KEY ("Statement_uid", qualifier_id),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid),
	FOREIGN KEY(qualifier_id) REFERENCES "Qualifier" (id)
);
CREATE INDEX "ix_Statement_qualifier_qualifier_id" ON "Statement_qualifier" (qualifier_id);
CREATE INDEX "ix_Statement_qualifier_Statement_uid" ON "Statement_qualifier" ("Statement_uid");

CREATE TABLE "Statement_has_evidence_of_types" (
	"Statement_uid" INTEGER,
	has_evidence_of_types TEXT,
	PRIMARY KEY ("Statement_uid", has_evidence_of_types),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE INDEX "ix_Statement_has_evidence_of_types_has_evidence_of_types" ON "Statement_has_evidence_of_types" (has_evidence_of_types);
CREATE INDEX "ix_Statement_has_evidence_of_types_Statement_uid" ON "Statement_has_evidence_of_types" ("Statement_uid");

CREATE TABLE "Statement_has_evidence_lines" (
	"Statement_uid" INTEGER,
	has_evidence_lines_uid INTEGER,
	PRIMARY KEY ("Statement_uid", has_evidence_lines_uid),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid),
	FOREIGN KEY(has_evidence_lines_uid) REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_Statement_has_evidence_lines_has_evidence_lines_uid" ON "Statement_has_evidence_lines" (has_evidence_lines_uid);
CREATE INDEX "ix_Statement_has_evidence_lines_Statement_uid" ON "Statement_has_evidence_lines" ("Statement_uid");

CREATE TABLE "Statement_has_evidence" (
	"Statement_uid" INTEGER,
	has_evidence_uid INTEGER,
	PRIMARY KEY ("Statement_uid", has_evidence_uid),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid),
	FOREIGN KEY(has_evidence_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_Statement_has_evidence_Statement_uid" ON "Statement_has_evidence" ("Statement_uid");
CREATE INDEX "ix_Statement_has_evidence_has_evidence_uid" ON "Statement_has_evidence" (has_evidence_uid);

CREATE TABLE "Statement_has_evidence_from_sources" (
	"Statement_uid" INTEGER,
	has_evidence_from_sources_uid INTEGER,
	PRIMARY KEY ("Statement_uid", has_evidence_from_sources_uid),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid),
	FOREIGN KEY(has_evidence_from_sources_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_Statement_has_evidence_from_sources_has_evidence_from_sources_uid" ON "Statement_has_evidence_from_sources" (has_evidence_from_sources_uid);
CREATE INDEX "ix_Statement_has_evidence_from_sources_Statement_uid" ON "Statement_has_evidence_from_sources" ("Statement_uid");

CREATE TABLE "Statement_is_about" (
	"Statement_uid" INTEGER,
	is_about TEXT,
	PRIMARY KEY ("Statement_uid", is_about),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE INDEX "ix_Statement_is_about_is_about" ON "Statement_is_about" (is_about);
CREATE INDEX "ix_Statement_is_about_Statement_uid" ON "Statement_is_about" ("Statement_uid");

CREATE TABLE "Statement_contributions" (
	"Statement_uid" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("Statement_uid", contributions_uid),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_Statement_contributions_Statement_uid" ON "Statement_contributions" ("Statement_uid");
CREATE INDEX "ix_Statement_contributions_contributions_uid" ON "Statement_contributions" (contributions_uid);

CREATE TABLE "Statement_specified_by" (
	"Statement_uid" INTEGER,
	specified_by TEXT,
	PRIMARY KEY ("Statement_uid", specified_by),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE INDEX "ix_Statement_specified_by_specified_by" ON "Statement_specified_by" (specified_by);
CREATE INDEX "ix_Statement_specified_by_Statement_uid" ON "Statement_specified_by" ("Statement_uid");

CREATE TABLE "Statement_supporting_methods" (
	"Statement_uid" INTEGER,
	supporting_methods TEXT,
	PRIMARY KEY ("Statement_uid", supporting_methods),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE INDEX "ix_Statement_supporting_methods_supporting_methods" ON "Statement_supporting_methods" (supporting_methods);
CREATE INDEX "ix_Statement_supporting_methods_Statement_uid" ON "Statement_supporting_methods" ("Statement_uid");

CREATE TABLE "Statement_supporting_method_types" (
	"Statement_uid" INTEGER,
	supporting_method_types_id INTEGER,
	PRIMARY KEY ("Statement_uid", supporting_method_types_id),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid),
	FOREIGN KEY(supporting_method_types_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_Statement_supporting_method_types_supporting_method_types_id" ON "Statement_supporting_method_types" (supporting_method_types_id);
CREATE INDEX "ix_Statement_supporting_method_types_Statement_uid" ON "Statement_supporting_method_types" ("Statement_uid");

CREATE TABLE "Statement_derived_from" (
	"Statement_uid" INTEGER,
	derived_from_uid INTEGER,
	PRIMARY KEY ("Statement_uid", derived_from_uid),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid),
	FOREIGN KEY(derived_from_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_Statement_derived_from_Statement_uid" ON "Statement_derived_from" ("Statement_uid");
CREATE INDEX "ix_Statement_derived_from_derived_from_uid" ON "Statement_derived_from" (derived_from_uid);

CREATE TABLE "Statement_reported_in" (
	"Statement_uid" INTEGER,
	reported_in TEXT,
	PRIMARY KEY ("Statement_uid", reported_in),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE INDEX "ix_Statement_reported_in_Statement_uid" ON "Statement_reported_in" ("Statement_uid");
CREATE INDEX "ix_Statement_reported_in_reported_in" ON "Statement_reported_in" (reported_in);

CREATE TABLE "Statement_sources" (
	"Statement_uid" INTEGER,
	sources TEXT,
	PRIMARY KEY ("Statement_uid", sources),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE INDEX "ix_Statement_sources_sources" ON "Statement_sources" (sources);
CREATE INDEX "ix_Statement_sources_Statement_uid" ON "Statement_sources" ("Statement_uid");

CREATE TABLE "Statement_identifiers" (
	"Statement_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("Statement_uid", identifiers),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE INDEX "ix_Statement_identifiers_Statement_uid" ON "Statement_identifiers" ("Statement_uid");
CREATE INDEX "ix_Statement_identifiers_identifiers" ON "Statement_identifiers" (identifiers);

CREATE TABLE "Statement_alternative_labels" (
	"Statement_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("Statement_uid", alternative_labels),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE INDEX "ix_Statement_alternative_labels_Statement_uid" ON "Statement_alternative_labels" ("Statement_uid");
CREATE INDEX "ix_Statement_alternative_labels_alternative_labels" ON "Statement_alternative_labels" (alternative_labels);

CREATE TABLE "Statement_extensions" (
	"Statement_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("Statement_uid", extensions_id),
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_Statement_extensions_Statement_uid" ON "Statement_extensions" ("Statement_uid");
CREATE INDEX "ix_Statement_extensions_extensions_id" ON "Statement_extensions" (extensions_id);

CREATE TABLE "StudyResult_contributions" (
	"StudyResult_uid" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("StudyResult_uid", contributions_uid),
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_StudyResult_contributions_StudyResult_uid" ON "StudyResult_contributions" ("StudyResult_uid");
CREATE INDEX "ix_StudyResult_contributions_contributions_uid" ON "StudyResult_contributions" (contributions_uid);

CREATE TABLE "EvidenceLine_has_evidence_items" (
	"EvidenceLine_uid" INTEGER,
	has_evidence_items_uid INTEGER,
	PRIMARY KEY ("EvidenceLine_uid", has_evidence_items_uid),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid),
	FOREIGN KEY(has_evidence_items_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_EvidenceLine_has_evidence_items_EvidenceLine_uid" ON "EvidenceLine_has_evidence_items" ("EvidenceLine_uid");
CREATE INDEX "ix_EvidenceLine_has_evidence_items_has_evidence_items_uid" ON "EvidenceLine_has_evidence_items" (has_evidence_items_uid);

CREATE TABLE "EvidenceLine_evidence_item_sources" (
	"EvidenceLine_uid" INTEGER,
	evidence_item_sources TEXT,
	PRIMARY KEY ("EvidenceLine_uid", evidence_item_sources),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_EvidenceLine_evidence_item_sources_EvidenceLine_uid" ON "EvidenceLine_evidence_item_sources" ("EvidenceLine_uid");
CREATE INDEX "ix_EvidenceLine_evidence_item_sources_evidence_item_sources" ON "EvidenceLine_evidence_item_sources" (evidence_item_sources);

CREATE TABLE "EvidenceLine_is_about" (
	"EvidenceLine_uid" INTEGER,
	is_about TEXT,
	PRIMARY KEY ("EvidenceLine_uid", is_about),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_EvidenceLine_is_about_is_about" ON "EvidenceLine_is_about" (is_about);
CREATE INDEX "ix_EvidenceLine_is_about_EvidenceLine_uid" ON "EvidenceLine_is_about" ("EvidenceLine_uid");

CREATE TABLE "EvidenceLine_contributions" (
	"EvidenceLine_uid" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("EvidenceLine_uid", contributions_uid),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_EvidenceLine_contributions_contributions_uid" ON "EvidenceLine_contributions" (contributions_uid);
CREATE INDEX "ix_EvidenceLine_contributions_EvidenceLine_uid" ON "EvidenceLine_contributions" ("EvidenceLine_uid");

CREATE TABLE "EvidenceLine_specified_by" (
	"EvidenceLine_uid" INTEGER,
	specified_by TEXT,
	PRIMARY KEY ("EvidenceLine_uid", specified_by),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_EvidenceLine_specified_by_EvidenceLine_uid" ON "EvidenceLine_specified_by" ("EvidenceLine_uid");
CREATE INDEX "ix_EvidenceLine_specified_by_specified_by" ON "EvidenceLine_specified_by" (specified_by);

CREATE TABLE "EvidenceLine_supporting_methods" (
	"EvidenceLine_uid" INTEGER,
	supporting_methods TEXT,
	PRIMARY KEY ("EvidenceLine_uid", supporting_methods),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_EvidenceLine_supporting_methods_EvidenceLine_uid" ON "EvidenceLine_supporting_methods" ("EvidenceLine_uid");
CREATE INDEX "ix_EvidenceLine_supporting_methods_supporting_methods" ON "EvidenceLine_supporting_methods" (supporting_methods);

CREATE TABLE "EvidenceLine_supporting_method_types" (
	"EvidenceLine_uid" INTEGER,
	supporting_method_types_id INTEGER,
	PRIMARY KEY ("EvidenceLine_uid", supporting_method_types_id),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid),
	FOREIGN KEY(supporting_method_types_id) REFERENCES "Coding" (id)
);
CREATE INDEX "ix_EvidenceLine_supporting_method_types_supporting_method_types_id" ON "EvidenceLine_supporting_method_types" (supporting_method_types_id);
CREATE INDEX "ix_EvidenceLine_supporting_method_types_EvidenceLine_uid" ON "EvidenceLine_supporting_method_types" ("EvidenceLine_uid");

CREATE TABLE "EvidenceLine_derived_from" (
	"EvidenceLine_uid" INTEGER,
	derived_from_uid INTEGER,
	PRIMARY KEY ("EvidenceLine_uid", derived_from_uid),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid),
	FOREIGN KEY(derived_from_uid) REFERENCES "InformationEntity" (uid)
);
CREATE INDEX "ix_EvidenceLine_derived_from_EvidenceLine_uid" ON "EvidenceLine_derived_from" ("EvidenceLine_uid");
CREATE INDEX "ix_EvidenceLine_derived_from_derived_from_uid" ON "EvidenceLine_derived_from" (derived_from_uid);

CREATE TABLE "EvidenceLine_reported_in" (
	"EvidenceLine_uid" INTEGER,
	reported_in TEXT,
	PRIMARY KEY ("EvidenceLine_uid", reported_in),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_EvidenceLine_reported_in_reported_in" ON "EvidenceLine_reported_in" (reported_in);
CREATE INDEX "ix_EvidenceLine_reported_in_EvidenceLine_uid" ON "EvidenceLine_reported_in" ("EvidenceLine_uid");

CREATE TABLE "EvidenceLine_sources" (
	"EvidenceLine_uid" INTEGER,
	sources TEXT,
	PRIMARY KEY ("EvidenceLine_uid", sources),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_EvidenceLine_sources_sources" ON "EvidenceLine_sources" (sources);
CREATE INDEX "ix_EvidenceLine_sources_EvidenceLine_uid" ON "EvidenceLine_sources" ("EvidenceLine_uid");

CREATE TABLE "EvidenceLine_identifiers" (
	"EvidenceLine_uid" INTEGER,
	identifiers TEXT,
	PRIMARY KEY ("EvidenceLine_uid", identifiers),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_EvidenceLine_identifiers_EvidenceLine_uid" ON "EvidenceLine_identifiers" ("EvidenceLine_uid");
CREATE INDEX "ix_EvidenceLine_identifiers_identifiers" ON "EvidenceLine_identifiers" (identifiers);

CREATE TABLE "EvidenceLine_alternative_labels" (
	"EvidenceLine_uid" INTEGER,
	alternative_labels TEXT,
	PRIMARY KEY ("EvidenceLine_uid", alternative_labels),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE INDEX "ix_EvidenceLine_alternative_labels_EvidenceLine_uid" ON "EvidenceLine_alternative_labels" ("EvidenceLine_uid");
CREATE INDEX "ix_EvidenceLine_alternative_labels_alternative_labels" ON "EvidenceLine_alternative_labels" (alternative_labels);

CREATE TABLE "EvidenceLine_extensions" (
	"EvidenceLine_uid" INTEGER,
	extensions_id INTEGER,
	PRIMARY KEY ("EvidenceLine_uid", extensions_id),
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid),
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE INDEX "ix_EvidenceLine_extensions_EvidenceLine_uid" ON "EvidenceLine_extensions" ("EvidenceLine_uid");
CREATE INDEX "ix_EvidenceLine_extensions_extensions_id" ON "EvidenceLine_extensions" (extensions_id);

CREATE TABLE "RecordMetadata_contributions" (
	"RecordMetadata_id" INTEGER,
	contributions_uid INTEGER,
	PRIMARY KEY ("RecordMetadata_id", contributions_uid),
	FOREIGN KEY("RecordMetadata_id") REFERENCES "RecordMetadata" (id),
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE INDEX "ix_RecordMetadata_contributions_RecordMetadata_id" ON "RecordMetadata_contributions" ("RecordMetadata_id");
CREATE INDEX "ix_RecordMetadata_contributions_contributions_uid" ON "RecordMetadata_contributions" (contributions_uid);
