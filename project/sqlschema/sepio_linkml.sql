-- # Class: "Entity" Description: "Anything that exists, has existed, or will exist."
--     * Slot: uid Description: 
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
-- # Class: "InformationEntity" Description: "An abstract (non-physical) entity that is about something. It represents the abstract 'information content' conveyed by physical or digital information artifacts like books, web pages, data tables, or photographs."
--     * Slot: uid Description: 
--     * Slot: dateAuthored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: informationQuality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: recordMetadata_id Description: Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
-- # Class: "Method" Description: "A set of instructions that specify how to achieve some objective. These may vary in the level of detail they provide, and in scientific research, these include things like experimental protocols, study designs, data analysis parameters,  curation guidelines, cohort selection criteria, and rule sets."
--     * Slot: uid Description: 
--     * Slot: dateAuthored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of method that a Method instance represents (e.g. 'Variant Interpretation Guideline', or 'Experimental Protocol')
--     * Slot: informationQuality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: recordMetadata_id Description: Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
-- # Class: "Document" Description: "A collection of information, usually in a text-based or graphic human-readable form, intended to be read and understood together as a whole."
--     * Slot: uid Description: 
--     * Slot: title Description: The official title given to the document by its authors.
--     * Slot: pmid Description: A `PubMed unique identifier <https://en.wikipedia.org/wiki/PubMed#PubMed_identifier>`_ for the document.
--     * Slot: doi Description: A `Digital Object Identifier <https://www.doi.org/the-identifier/what-is-a-doi/>_` for the document.
--     * Slot: license Description: A specific license that dictates legal permissions for how a document can be used (by whom, where, for what purposes, with what additional requirements, etc.)
--     * Slot: dateAuthored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of document that a Document instance represents (e.g.  'publication', 'patent', 'pathology report')
--     * Slot: informationQuality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: recordMetadata_id Description: Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
-- # Class: "DataItem" Description: "An Information Entity representing an individual piece of data, generated or acquired through methods which reliably produce truthful information about something."
--     * Slot: uid Description: 
--     * Slot: value Description: The value of the data item (could be quantitative or qualitative depending on the type of data item).
--     * Slot: dateAuthored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of data the DataItem instance represents (e.g. a 'specimen count', a 'patient weight', an 'allele frequency', a 'p-value')
--     * Slot: unit_id Description: A unit of measure for the value (e.g. meters, grams, fluorescent units, seconds, mg/ml, etc.)
--     * Slot: confidenceInterval_uid Description: A measure of the probability that a parameter of interest will fall within a defined range of values around a mean or other statistical calculation.
--     * Slot: informationQuality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: recordMetadata_id Description: Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
-- # Class: "DataSet" Description: "A collection of related data items or records that are organized together in a common format or structure, to enable their computational manipulation as a unit."
--     * Slot: uid Description: 
--     * Slot: releaseDate Description: Indicates when a version of a DataSet was formally released.
--     * Slot: version Description: The version of the DataSet, as assigned by its creator.
--     * Slot: license Description: A specific license that dictates legal permissions for how a data set can be used (by whom, where, for what purposes, with what additional requirements, etc.)
--     * Slot: dateAuthored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of data set the DataSet instance represents (e.g. a 'clinical data set', a 'sequencing data set', a 'gene expression data set', a 'genome annotation data set')
--     * Slot: informationQuality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: recordMetadata_id Description: Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
-- # Class: "Activity" Description: "An action or set of actions performed by an agent, that occurs over a period of time. Activities may use, generate, modify, move, or destroy one or more entities."
--     * Slot: uid Description: 
--     * Slot: date Description: The date that the Activity was completed.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: subtype_id Description: A specific type of activity the Activity instance represents.
-- # Class: "Contribution" Description: "An action or actions taken by a particular agent in the creation, modification, assessment, or deprecation of some entity (e.g. a Statement, Evidence Line, DataSet, Publication, etc.)"
--     * Slot: uid Description: 
--     * Slot: date Description: The date that the Activity was completed.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: contributor_uid Description: The Agent that made the contribution.
--     * Slot: contributionMadeTo_uid Description: The artifact toward which the contribution was made.
--     * Slot: subtype_id Description: A specific type of activity the Activity instance represents.
-- # Class: "Agent" Description: "An autonomous actor (person, organization, or software agent) that bears some form of responsibility for an activity taking place,  for the existence of an entity, or for another agent’s activity."
--     * Slot: uid Description: 
--     * Slot: subtype Description: A specific type of agent the Agent object represents. Must be one of {person, organization, software}
--     * Slot: name Description: The given name of the Agent.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
-- # Class: "Statement" Description: "A claim of purported truth as made by a particular agent, on a particular occasion. Statements may be used to simply put forth a possible fact (i.e. a 'proposition') as true, or to provide a more nuanced assessment of the level of confidence or evidence supporting a particular proposition."
--     * Slot: uid Description: 
--     * Slot: statementText Description: A natural-language expression of what a Statement asserts to be true.
--     * Slot: subject Description: The Entity or concept about which the Statement is made.
--     * Slot: object Description: An Entity or concept that is related to the subject of a Statement via its predicate.
--     * Slot: direction Description: A term indicating whether the Statement supports, disputes, or remains neutral w.r.t. the validity of the Proposition it evaluates.
--     * Slot: strength Description: A term used to report the strength of a Proposition's validity assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be).  Depending on its implementation, a strength assessment may be framed in terms of how *confident* the agent is that the Proposition is true or false, or in terms of the *strength of evidence* they believe supports or disputes it.
--     * Slot: score Description: A quantitative score that indicates the strength of a Proposition's validity assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be).  Depending on its implementation, a score may reflect how *confident* that agent is that the Proposition is true or false, or the *strength of evidence* they believe supports or disputes it.
--     * Slot: dateAuthored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: proposition_uid Description: A possible fact that the Statement assesses or puts forth as true.
--     * Slot: predicate_id Description: The relationship declared to hold between the subject and the object of the Statement.
--     * Slot: subjectClassification_id Description: A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's proposition, in terms of a classification of its subject.
--     * Slot: informationQuality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: recordMetadata_id Description: Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
-- # Class: "StudyResult" Description: "A collection of data items from a single study that pertain to a particular subject or experimental unit in the study, along with optional provenance information describing how these data items were generated."
--     * Slot: uid Description: 
--     * Slot: focus Description: A specific subject or experimental unit in a Study, that data in the StudyResult object is about - e.g. a particular variant in a population allele frequency dataset like ExAC or gnomAD.
--     * Slot: dateAuthored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: interpretation_id Description: The outcome of an interpretation of lower-level data item(s) in a StudyResult, that express some broader conclusion or insight that was made (e.g. that data indicates a result to be is high, normal, or low).
--     * Slot: studyGroup_uid Description: A description of a specific group or population of subjects interrogated in the ResearchStudy that produced the data captured in the StudyResult.
--     * Slot: informationQuality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: recordMetadata_id Description: Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
-- # Class: "EvidenceLine" Description: "An independent, evidence-based argument that may support or refute the validity of a specific proposition. The strength and direction of this argument is based on an interpretation of one or more pieces of information as evidence for or against the target proposition."
--     * Slot: uid Description: 
--     * Slot: directionOfEvidenceProvided Description: The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral)
--     * Slot: strengthOfEvidenceProvided Description: The strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided
--     * Slot: scoreOfEvidenceProvided Description: A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
--     * Slot: dateAuthored Description: Indicates when the information content expressed in the Information Entity was generated.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: targetProposition_uid Description: The possible fact against which evidence items contained in an Evidence Line were collectively evaluated, in determining the overall strength and direction of support they provide. For example, in an ACMG Guideline-based assessment of variant pathogenicity, the support provided by distinct lines of evidence are assessed against a target proposition that some variant is pathogenic for a specific disease.
--     * Slot: informationQuality_id Description: A qualitative term indicating the scientific rigor or reliability with which the information was generated/collected.
--     * Slot: recordMetadata_id Description: Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
-- # Class: "Proposition" Description: "An abstract entity representing a possible fact that is either true or false."
--     * Slot: uid Description: 
--     * Slot: propositionText Description: A natural-language expression of the Proposition's meaning (i.e. the 'possible fact' it expresses).
--     * Slot: subject Description: The Entity or concept about which the Proposition is made.
--     * Slot: object Description: An Entity or concept that is related to the subject of a Proposition via its predicate.
--     * Slot: negated Description: A boolean flag set to 'true' to represent a negation of the proposition expressed by the subject, predicate, object, and qualifier(s) (e.g. that "Variant X is NOT pathogenic for Disease Y")
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
--     * Slot: predicate_id Description: The relationship declared to hold between the subject and the object of the Proposition.
-- # Class: "StudyGroup" Description: "A collection of individuals or specimens from the same taxonomic class, selected for analysis in a scientific study based on their exhibiting one or more common characteristics  (e.g. species, race, age, gender, disease state, income) May be referred to as a 'cohort' or 'population' in specific research settings."
--     * Slot: uid Description: 
--     * Slot: memberCount Description: The total number of individual members in the StudyGroup.
--     * Slot: id Description: The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference one object from another.
--     * Slot: type Description: The name of the class that is instantiated by a data object representing the Entity.
--     * Slot: label Description: A primary name for the Entity.
--     * Slot: description Description: A free text description of the Entity.
-- # Class: "Utility" Description: "An abstract organizational class that groups classes acting as complex datatypes in the model - providing reusable collections of fields that can be plugged into other objects to capture sets of related information."
--     * Slot: id Description: 
-- # Class: "Coding" Description: "A structured representation of a code for a defined concept in a terminology or code system."
--     * Slot: id Description: 
--     * Slot: code Description: A symbol uniquely identifying the concept, as in a syntax defined by the code system.  CURIE format is preferred where possible (e.g. ‘SO:0000704’ is the CURIE form of the Sequence Ontology code for 'gene').
--     * Slot: label Description: The human-readable name for the coded concept, as defined by the code system.
--     * Slot: system Description: The terminology/code system that defined the code.  May be reported as a free-text name (e.g. ‘Sequence Ontology’), but it is preferable to provide  a uri/url for the system. When the 'code' is reported as a CURIE, the 'system' should be reported as the uri that the CURIE's prefix expands to (e.g. 'http://purl.obofoundry.org/so.owl/' for the Sequence Ontology).
--     * Slot: systemVersion Description: Version of the terminology or code system that provided the code.
-- # Class: "Qualifier" Description: "A key-value object used to capture additional piece of information that extends or refines the meaning of a Statement's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context."
--     * Slot: id Description: 
--     * Slot: name Description: A descriptive name that describes the type of information captured in the Qualifier value.
--     * Slot: value Description: The value of the qualifier - holding information that refines/extends the meaning of the Statement.
-- # Class: "Expression" Description: "A structure for labels representing systematic expressions that describe an entity, as generated by formal nomenclatures (e.g. HGVS for genetic variants, ISCN for karyotypes, HLA nomenclature for HLA genes/alleles)."
--     * Slot: id Description: 
--     * Slot: value Description: A free-text rendering of the expression used as a label for the entity
--     * Slot: systemURL Description: A URL for the nomenclature system
--     * Slot: systemVersion Description: The version of the nomenclature system.
-- # Class: "Extension" Description: "A data structure that allows custom attributes to be defined for an Entity, to capture information unique to a given content provider, or not currently supported by the core specification."
--     * Slot: id Description: 
--     * Slot: extensionDescription Description: A free text description of the intended meaning and use of the extension element, which may include the types of values it takes, and how to interpret these values in the context of the parent Class.
--     * Slot: name Description: A name for the Extension. Should be indicative of its meaning and/or the type of information it value represents.
--     * Slot: value Description: The value of the Extension - can be any primitive or structured object
-- # Class: "RecordMetadata" Description: "A reusable structure that encapsulates provenance metadata about a serialized data record or object in a particular dataset (as opposed to provenance of the real world entity this record or object represents)."
--     * Slot: id Description: 
--     * Slot: recordIdentifier Description: The identifier of the record described in the RecordMetadata object (required when the record described is not the one in the present system)
--     * Slot: recordVersion Description: The version number of the record-level artifact the object describes
--     * Slot: dateRecordCreated Description: The date the record was initially created.
-- # Class: "Characteristic" Description: "An object holding a name-value pair used to describe a trait or role of an individual member of a StudyGroup."
--     * Slot: id Description: 
--     * Slot: name Description: The type of the trait or role described by the trait (e.g. 'ethnicity', 'sex', 'age', 'disease status').
--     * Slot: valueOperator Description: An operation that defines how to logically interpret a set of more than one Characteristic values ('AND', 'OR', 'NOT')
-- # Class: "Entity_identifiers" Description: ""
--     * Slot: Entity_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "Entity_alternativeLabels" Description: ""
--     * Slot: Entity_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "Entity_extensions" Description: ""
--     * Slot: Entity_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "InformationEntity_isAbout" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: isAbout Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: "InformationEntity_contributions" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: "InformationEntity_specifiedBy" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: specifiedBy Description: A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
-- # Class: "InformationEntity_methodTypes" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: methodTypes_id Description: Types of methodological approaches used to collect, generate, or evaluate the reported information.
-- # Class: "InformationEntity_derivedFrom" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: derivedFrom_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part
-- # Class: "InformationEntity_reportedIn" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: reportedIn Description: A document in which the Information Entity is reported
-- # Class: "InformationEntity_identifiers" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "InformationEntity_alternativeLabels" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "InformationEntity_extensions" Description: ""
--     * Slot: InformationEntity_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "Method_urls" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: urls Description: The URL/web address from which the Method can be retrieved.
-- # Class: "Method_isAbout" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: isAbout Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: "Method_contributions" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: "Method_specifiedBy" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: specifiedBy Description: A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
-- # Class: "Method_methodTypes" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: methodTypes_id Description: Types of methodological approaches used to collect, generate, or evaluate the reported information.
-- # Class: "Method_derivedFrom" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: derivedFrom_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part
-- # Class: "Method_reportedIn" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: reportedIn Description: A document in which the Information Entity is reported
-- # Class: "Method_identifiers" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "Method_alternativeLabels" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "Method_extensions" Description: ""
--     * Slot: Method_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "Document_urls" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: urls Description: The URL/web address from which the content of the Document can be retrieved.
-- # Class: "Document_isAbout" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: isAbout Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: "Document_contributions" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: "Document_specifiedBy" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: specifiedBy Description: A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
-- # Class: "Document_methodTypes" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: methodTypes_id Description: Types of methodological approaches used to collect, generate, or evaluate the reported information.
-- # Class: "Document_derivedFrom" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: derivedFrom_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part
-- # Class: "Document_reportedIn" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: reportedIn Description: A document in which the Information Entity is reported
-- # Class: "Document_identifiers" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "Document_alternativeLabels" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "Document_extensions" Description: ""
--     * Slot: Document_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "DataItem_variabilityMeasures" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: variabilityMeasures_uid Description: A statistical score describing the variability inherent in a data item representing a statistical summary of a set of observations/measurements (e.g. the standard deviation associated with a statistical mean calculated across several experimental replicates).
-- # Class: "DataItem_componentDataItem" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: componentDataItem_uid Description: A more foundational data item that is a logical component of a compound data item.
-- # Class: "DataItem_isAbout" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: isAbout Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: "DataItem_contributions" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: "DataItem_specifiedBy" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: specifiedBy Description: A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
-- # Class: "DataItem_methodTypes" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: methodTypes_id Description: Types of methodological approaches used to collect, generate, or evaluate the reported information.
-- # Class: "DataItem_derivedFrom" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: derivedFrom_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part
-- # Class: "DataItem_reportedIn" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: reportedIn Description: A document in which the Information Entity is reported
-- # Class: "DataItem_identifiers" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "DataItem_alternativeLabels" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "DataItem_extensions" Description: ""
--     * Slot: DataItem_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "DataSet_isAbout" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: isAbout Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: "DataSet_contributions" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: "DataSet_specifiedBy" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: specifiedBy Description: A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
-- # Class: "DataSet_methodTypes" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: methodTypes_id Description: Types of methodological approaches used to collect, generate, or evaluate the reported information.
-- # Class: "DataSet_derivedFrom" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: derivedFrom_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part
-- # Class: "DataSet_reportedIn" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: reportedIn Description: A document in which the Information Entity is reported
-- # Class: "DataSet_identifiers" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "DataSet_alternativeLabels" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "DataSet_extensions" Description: ""
--     * Slot: DataSet_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "Activity_performedBy" Description: ""
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: performedBy_uid Description: An Agent who participated in executing the Activity.
-- # Class: "Activity_specifiedBy" Description: ""
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: specifiedBy_uid Description: A method that was followed in performing an Activity, that describes how it was executed.
-- # Class: "Activity_input" Description: ""
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: input_uid Description: An entity that was input into the Activity (could be material or information)
-- # Class: "Activity_output" Description: ""
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: output_uid Description: An entity that was output from the Activity (could be material or information)
-- # Class: "Activity_identifiers" Description: ""
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "Activity_alternativeLabels" Description: ""
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "Activity_extensions" Description: ""
--     * Slot: Activity_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "Contribution_activityType" Description: ""
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: activityType_id Description: The specific type of activity performed or role played by an agent in making the contribution (e.g. for a publication, agents may contribute as a primary author, editor, figure designer, data generator, etc. . Values of this property may be framed as activities or as contribution roles (e.g. using terms from the Contribution Role Ontology (CRO).)
-- # Class: "Contribution_performedBy" Description: ""
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: performedBy_uid Description: An Agent who participated in executing the Activity.
-- # Class: "Contribution_specifiedBy" Description: ""
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: specifiedBy_uid Description: A method that was followed in performing an Activity, that describes how it was executed.
-- # Class: "Contribution_input" Description: ""
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: input_uid Description: An entity that was input into the Activity (could be material or information)
-- # Class: "Contribution_output" Description: ""
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: output_uid Description: An entity that was output from the Activity (could be material or information)
-- # Class: "Contribution_identifiers" Description: ""
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "Contribution_alternativeLabels" Description: ""
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "Contribution_extensions" Description: ""
--     * Slot: Contribution_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "Agent_identifiers" Description: ""
--     * Slot: Agent_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "Agent_alternativeLabels" Description: ""
--     * Slot: Agent_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "Agent_extensions" Description: ""
--     * Slot: Agent_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "Statement_qualifier" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: qualifier_id Description: An additional piece of information that extends or refines the meaning of a Statement's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context.
-- # Class: "Statement_hasEvidenceOfTypes" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: hasEvidenceOfTypes Description: A term describing a type of evidence used to assess the validity of Statement's proposition (e.g. 'sequence similarity evidence', 'in vitro assay evidence').
-- # Class: "Statement_hasEvidenceLines" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: hasEvidenceLines_uid Description: An evidence-based argument that supports or disputes the validity of the proposition that a Statement assesses or puts forth as true. The strength and direction of this argument (whether it supports or disputes  the proposition, and how strongly) is based on an interpretation of one or more pieces of information as evidence (i.e. 'Evidence Items).
-- # Class: "Statement_hasEvidence" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: hasEvidence_uid Description: A piece of information that represents or contributes to an argument for or against the validity of the Proposition put forth in a Statement. This is a shortcut relation that links a Statement directly to a piece of evidence supporting it, bypassing the Evidence Line class when used data creators do not utilize an Evidence Line object.
-- # Class: "Statement_isAbout" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: isAbout Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: "Statement_contributions" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: "Statement_specifiedBy" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: specifiedBy Description: A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
-- # Class: "Statement_methodTypes" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: methodTypes_id Description: Types of methodological approaches used to collect, generate, or evaluate the reported information.
-- # Class: "Statement_derivedFrom" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: derivedFrom_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part
-- # Class: "Statement_reportedIn" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: reportedIn Description: A document in which the Information Entity is reported
-- # Class: "Statement_identifiers" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "Statement_alternativeLabels" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "Statement_extensions" Description: ""
--     * Slot: Statement_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "StudyResult_dataItems" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: dataItems_uid Description: A DataItem that is included in the StudyResult because it pertains to the entity that is the 'focus'. This data can directly describe this focus, or represent metadata about how data in the Result was generated.
-- # Class: "StudyResult_sourceDataSet" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: sourceDataSet_uid Description: A larger DataSet from which the content of the StudyResult was derived.
-- # Class: "StudyResult_componentResult" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: componentResult_uid Description: Another StudyResult comprised of data items about the same focus as its parent Result, but based on a more narrowly scoped analysis of the foundational data (e.g. an analysis based on data about a subset of the parent Results full study population) .
-- # Class: "StudyResult_isAbout" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: isAbout Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: "StudyResult_contributions" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: "StudyResult_specifiedBy" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: specifiedBy Description: A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
-- # Class: "StudyResult_methodTypes" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: methodTypes_id Description: Types of methodological approaches used to collect, generate, or evaluate the reported information.
-- # Class: "StudyResult_derivedFrom" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: derivedFrom_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part
-- # Class: "StudyResult_reportedIn" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: reportedIn Description: A document in which the Information Entity is reported
-- # Class: "StudyResult_identifiers" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "StudyResult_alternativeLabels" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "StudyResult_extensions" Description: ""
--     * Slot: StudyResult_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "EvidenceLine_evidenceItems" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: evidenceItems_uid Description: An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.
-- # Class: "EvidenceLine_isAbout" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: isAbout Description: An entity or concept in the world that the information entity describes/is about.
-- # Class: "EvidenceLine_contributions" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: contributions_uid Description: Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
-- # Class: "EvidenceLine_specifiedBy" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: specifiedBy Description: A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
-- # Class: "EvidenceLine_methodTypes" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: methodTypes_id Description: Types of methodological approaches used to collect, generate, or evaluate the reported information.
-- # Class: "EvidenceLine_derivedFrom" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: derivedFrom_uid Description: Another Information Entity from which this Information Entity is derived, in whole or in part
-- # Class: "EvidenceLine_reportedIn" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: reportedIn Description: A document in which the Information Entity is reported
-- # Class: "EvidenceLine_identifiers" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "EvidenceLine_alternativeLabels" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "EvidenceLine_extensions" Description: ""
--     * Slot: EvidenceLine_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "Proposition_qualifier" Description: ""
--     * Slot: Proposition_uid Description: Autocreated FK slot
--     * Slot: qualifier_id Description: An additional piece of information that extends or refines the meaning of a Propositions's core subject - predicate - object 'triple' - by providing additional detail, or constraining the statement to apply in a particular context.
-- # Class: "Proposition_identifiers" Description: ""
--     * Slot: Proposition_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "Proposition_alternativeLabels" Description: ""
--     * Slot: Proposition_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "Proposition_extensions" Description: ""
--     * Slot: Proposition_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "StudyGroup_isSubsetOf" Description: ""
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: isSubsetOf_uid Description: A larger StudyGroup of which this StudyGroup represents a subset.
-- # Class: "StudyGroup_characteristics" Description: ""
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: characteristics_id Description: A feature or role shared by all members of the StudyGroup, representing a criterion for membership in the group.
-- # Class: "StudyGroup_identifiers" Description: ""
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: identifiers Description: A globally-unique 'business' identifier or accession number for the real-world entity represented by a data object. These are typically assigned by an external system or authority, and used to connect entities and share content across different systems.
-- # Class: "StudyGroup_alternativeLabels" Description: ""
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: alternativeLabels Description: Alternative name(s) for the Entity.
-- # Class: "StudyGroup_extensions" Description: ""
--     * Slot: StudyGroup_uid Description: Autocreated FK slot
--     * Slot: extensions_id Description: A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
-- # Class: "RecordMetadata_derivedFromRecord" Description: ""
--     * Slot: RecordMetadata_id Description: Autocreated FK slot
--     * Slot: derivedFromRecord Description: Another data record from which the record described here was derived, through a data ingest and/or transformation process.
-- # Class: "RecordMetadata_contributions" Description: ""
--     * Slot: RecordMetadata_id Description: Autocreated FK slot
--     * Slot: contributions_uid Description: describes specific contributions made by an human or software agent to the creation, modification, or administrative management of a data record or object
-- # Class: "Characteristic_values" Description: ""
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
CREATE TABLE "StudyGroup" (
	uid INTEGER NOT NULL, 
	"memberCount" INTEGER, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	PRIMARY KEY (uid)
);
CREATE TABLE "Utility" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Coding" (
	id INTEGER NOT NULL, 
	code TEXT, 
	label TEXT, 
	system TEXT, 
	"systemVersion" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Qualifier" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Expression" (
	id INTEGER NOT NULL, 
	value TEXT NOT NULL, 
	"systemURL" TEXT, 
	"systemVersion" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Extension" (
	id INTEGER NOT NULL, 
	"extensionDescription" TEXT, 
	name TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "RecordMetadata" (
	id INTEGER NOT NULL, 
	"recordIdentifier" TEXT, 
	"recordVersion" TEXT, 
	"dateRecordCreated" DATE, 
	PRIMARY KEY (id)
);
CREATE TABLE "Characteristic" (
	id INTEGER NOT NULL, 
	name TEXT NOT NULL, 
	"valueOperator" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "InformationEntity" (
	uid INTEGER NOT NULL, 
	"dateAuthored" TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	"informationQuality_id" INTEGER, 
	"recordMetadata_id" INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY("informationQuality_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("recordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE TABLE "Method" (
	uid INTEGER NOT NULL, 
	"dateAuthored" TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	subtype_id INTEGER, 
	"informationQuality_id" INTEGER, 
	"recordMetadata_id" INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id), 
	FOREIGN KEY("informationQuality_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("recordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE TABLE "Document" (
	uid INTEGER NOT NULL, 
	title TEXT, 
	pmid TEXT, 
	doi TEXT, 
	license TEXT, 
	"dateAuthored" TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	subtype_id INTEGER, 
	"informationQuality_id" INTEGER, 
	"recordMetadata_id" INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id), 
	FOREIGN KEY("informationQuality_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("recordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE TABLE "DataItem" (
	uid INTEGER NOT NULL, 
	value TEXT NOT NULL, 
	"dateAuthored" TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	subtype_id INTEGER, 
	unit_id INTEGER, 
	"confidenceInterval_uid" INTEGER, 
	"informationQuality_id" INTEGER, 
	"recordMetadata_id" INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id), 
	FOREIGN KEY(unit_id) REFERENCES "Coding" (id), 
	FOREIGN KEY("confidenceInterval_uid") REFERENCES "DataItem" (uid), 
	FOREIGN KEY("informationQuality_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("recordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE TABLE "DataSet" (
	uid INTEGER NOT NULL, 
	"releaseDate" DATE, 
	version TEXT, 
	license TEXT, 
	"dateAuthored" TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	subtype_id INTEGER, 
	"informationQuality_id" INTEGER, 
	"recordMetadata_id" INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id), 
	FOREIGN KEY("informationQuality_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("recordMetadata_id") REFERENCES "RecordMetadata" (id)
);
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
CREATE TABLE "StudyResult" (
	uid INTEGER NOT NULL, 
	focus TEXT, 
	"dateAuthored" TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	interpretation_id INTEGER, 
	"studyGroup_uid" INTEGER, 
	"informationQuality_id" INTEGER, 
	"recordMetadata_id" INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(interpretation_id) REFERENCES "Coding" (id), 
	FOREIGN KEY("studyGroup_uid") REFERENCES "StudyGroup" (uid), 
	FOREIGN KEY("informationQuality_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("recordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE TABLE "Proposition" (
	uid INTEGER NOT NULL, 
	"propositionText" TEXT, 
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
CREATE TABLE "Entity_identifiers" (
	"Entity_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("Entity_uid", identifiers), 
	FOREIGN KEY("Entity_uid") REFERENCES "Entity" (uid)
);
CREATE TABLE "Entity_alternativeLabels" (
	"Entity_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("Entity_uid", "alternativeLabels"), 
	FOREIGN KEY("Entity_uid") REFERENCES "Entity" (uid)
);
CREATE TABLE "Entity_extensions" (
	"Entity_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("Entity_uid", extensions_id), 
	FOREIGN KEY("Entity_uid") REFERENCES "Entity" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "Agent_identifiers" (
	"Agent_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("Agent_uid", identifiers), 
	FOREIGN KEY("Agent_uid") REFERENCES "Agent" (uid)
);
CREATE TABLE "Agent_alternativeLabels" (
	"Agent_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("Agent_uid", "alternativeLabels"), 
	FOREIGN KEY("Agent_uid") REFERENCES "Agent" (uid)
);
CREATE TABLE "Agent_extensions" (
	"Agent_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("Agent_uid", extensions_id), 
	FOREIGN KEY("Agent_uid") REFERENCES "Agent" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "StudyGroup_isSubsetOf" (
	"StudyGroup_uid" INTEGER, 
	"isSubsetOf_uid" INTEGER, 
	PRIMARY KEY ("StudyGroup_uid", "isSubsetOf_uid"), 
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid), 
	FOREIGN KEY("isSubsetOf_uid") REFERENCES "StudyGroup" (uid)
);
CREATE TABLE "StudyGroup_characteristics" (
	"StudyGroup_uid" INTEGER, 
	characteristics_id INTEGER, 
	PRIMARY KEY ("StudyGroup_uid", characteristics_id), 
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid), 
	FOREIGN KEY(characteristics_id) REFERENCES "Characteristic" (id)
);
CREATE TABLE "StudyGroup_identifiers" (
	"StudyGroup_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("StudyGroup_uid", identifiers), 
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid)
);
CREATE TABLE "StudyGroup_alternativeLabels" (
	"StudyGroup_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("StudyGroup_uid", "alternativeLabels"), 
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid)
);
CREATE TABLE "StudyGroup_extensions" (
	"StudyGroup_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("StudyGroup_uid", extensions_id), 
	FOREIGN KEY("StudyGroup_uid") REFERENCES "StudyGroup" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "RecordMetadata_derivedFromRecord" (
	"RecordMetadata_id" INTEGER, 
	"derivedFromRecord" TEXT, 
	PRIMARY KEY ("RecordMetadata_id", "derivedFromRecord"), 
	FOREIGN KEY("RecordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE TABLE "Characteristic_values" (
	"Characteristic_id" INTEGER, 
	"values" TEXT NOT NULL, 
	PRIMARY KEY ("Characteristic_id", "values"), 
	FOREIGN KEY("Characteristic_id") REFERENCES "Characteristic" (id)
);
CREATE TABLE "Contribution" (
	uid INTEGER NOT NULL, 
	date DATE, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	contributor_uid INTEGER, 
	"contributionMadeTo_uid" INTEGER, 
	subtype_id INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(contributor_uid) REFERENCES "Agent" (uid), 
	FOREIGN KEY("contributionMadeTo_uid") REFERENCES "InformationEntity" (uid), 
	FOREIGN KEY(subtype_id) REFERENCES "Coding" (id)
);
CREATE TABLE "Statement" (
	uid INTEGER NOT NULL, 
	"statementText" TEXT, 
	subject TEXT, 
	object TEXT, 
	direction TEXT, 
	strength TEXT, 
	score FLOAT, 
	"dateAuthored" TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	proposition_uid INTEGER, 
	predicate_id INTEGER, 
	"subjectClassification_id" INTEGER, 
	"informationQuality_id" INTEGER, 
	"recordMetadata_id" INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(proposition_uid) REFERENCES "Proposition" (uid), 
	FOREIGN KEY(predicate_id) REFERENCES "Coding" (id), 
	FOREIGN KEY("subjectClassification_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("informationQuality_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("recordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE TABLE "EvidenceLine" (
	uid INTEGER NOT NULL, 
	"directionOfEvidenceProvided" TEXT, 
	"strengthOfEvidenceProvided" TEXT, 
	"scoreOfEvidenceProvided" FLOAT, 
	"dateAuthored" TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	"targetProposition_uid" INTEGER, 
	"informationQuality_id" INTEGER, 
	"recordMetadata_id" INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY("targetProposition_uid") REFERENCES "Proposition" (uid), 
	FOREIGN KEY("informationQuality_id") REFERENCES "Coding" (id), 
	FOREIGN KEY("recordMetadata_id") REFERENCES "RecordMetadata" (id)
);
CREATE TABLE "InformationEntity_isAbout" (
	"InformationEntity_uid" INTEGER, 
	"isAbout" TEXT, 
	PRIMARY KEY ("InformationEntity_uid", "isAbout"), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "InformationEntity_specifiedBy" (
	"InformationEntity_uid" INTEGER, 
	"specifiedBy" TEXT, 
	PRIMARY KEY ("InformationEntity_uid", "specifiedBy"), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "InformationEntity_methodTypes" (
	"InformationEntity_uid" INTEGER, 
	"methodTypes_id" INTEGER, 
	PRIMARY KEY ("InformationEntity_uid", "methodTypes_id"), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid), 
	FOREIGN KEY("methodTypes_id") REFERENCES "Coding" (id)
);
CREATE TABLE "InformationEntity_derivedFrom" (
	"InformationEntity_uid" INTEGER, 
	"derivedFrom_uid" INTEGER, 
	PRIMARY KEY ("InformationEntity_uid", "derivedFrom_uid"), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid), 
	FOREIGN KEY("derivedFrom_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "InformationEntity_reportedIn" (
	"InformationEntity_uid" INTEGER, 
	"reportedIn" TEXT, 
	PRIMARY KEY ("InformationEntity_uid", "reportedIn"), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "InformationEntity_identifiers" (
	"InformationEntity_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("InformationEntity_uid", identifiers), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "InformationEntity_alternativeLabels" (
	"InformationEntity_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("InformationEntity_uid", "alternativeLabels"), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "InformationEntity_extensions" (
	"InformationEntity_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("InformationEntity_uid", extensions_id), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "Method_urls" (
	"Method_uid" INTEGER, 
	urls TEXT, 
	PRIMARY KEY ("Method_uid", urls), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE TABLE "Method_isAbout" (
	"Method_uid" INTEGER, 
	"isAbout" TEXT, 
	PRIMARY KEY ("Method_uid", "isAbout"), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE TABLE "Method_specifiedBy" (
	"Method_uid" INTEGER, 
	"specifiedBy" TEXT, 
	PRIMARY KEY ("Method_uid", "specifiedBy"), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE TABLE "Method_methodTypes" (
	"Method_uid" INTEGER, 
	"methodTypes_id" INTEGER, 
	PRIMARY KEY ("Method_uid", "methodTypes_id"), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid), 
	FOREIGN KEY("methodTypes_id") REFERENCES "Coding" (id)
);
CREATE TABLE "Method_derivedFrom" (
	"Method_uid" INTEGER, 
	"derivedFrom_uid" INTEGER, 
	PRIMARY KEY ("Method_uid", "derivedFrom_uid"), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid), 
	FOREIGN KEY("derivedFrom_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "Method_reportedIn" (
	"Method_uid" INTEGER, 
	"reportedIn" TEXT, 
	PRIMARY KEY ("Method_uid", "reportedIn"), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE TABLE "Method_identifiers" (
	"Method_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("Method_uid", identifiers), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE TABLE "Method_alternativeLabels" (
	"Method_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("Method_uid", "alternativeLabels"), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid)
);
CREATE TABLE "Method_extensions" (
	"Method_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("Method_uid", extensions_id), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "Document_urls" (
	"Document_uid" INTEGER, 
	urls TEXT, 
	PRIMARY KEY ("Document_uid", urls), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE TABLE "Document_isAbout" (
	"Document_uid" INTEGER, 
	"isAbout" TEXT, 
	PRIMARY KEY ("Document_uid", "isAbout"), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE TABLE "Document_specifiedBy" (
	"Document_uid" INTEGER, 
	"specifiedBy" TEXT, 
	PRIMARY KEY ("Document_uid", "specifiedBy"), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE TABLE "Document_methodTypes" (
	"Document_uid" INTEGER, 
	"methodTypes_id" INTEGER, 
	PRIMARY KEY ("Document_uid", "methodTypes_id"), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid), 
	FOREIGN KEY("methodTypes_id") REFERENCES "Coding" (id)
);
CREATE TABLE "Document_derivedFrom" (
	"Document_uid" INTEGER, 
	"derivedFrom_uid" INTEGER, 
	PRIMARY KEY ("Document_uid", "derivedFrom_uid"), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid), 
	FOREIGN KEY("derivedFrom_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "Document_reportedIn" (
	"Document_uid" INTEGER, 
	"reportedIn" TEXT, 
	PRIMARY KEY ("Document_uid", "reportedIn"), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE TABLE "Document_identifiers" (
	"Document_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("Document_uid", identifiers), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE TABLE "Document_alternativeLabels" (
	"Document_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("Document_uid", "alternativeLabels"), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid)
);
CREATE TABLE "Document_extensions" (
	"Document_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("Document_uid", extensions_id), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "DataItem_variabilityMeasures" (
	"DataItem_uid" INTEGER, 
	"variabilityMeasures_uid" INTEGER, 
	PRIMARY KEY ("DataItem_uid", "variabilityMeasures_uid"), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid), 
	FOREIGN KEY("variabilityMeasures_uid") REFERENCES "DataItem" (uid)
);
CREATE TABLE "DataItem_componentDataItem" (
	"DataItem_uid" INTEGER, 
	"componentDataItem_uid" INTEGER, 
	PRIMARY KEY ("DataItem_uid", "componentDataItem_uid"), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid), 
	FOREIGN KEY("componentDataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE TABLE "DataItem_isAbout" (
	"DataItem_uid" INTEGER, 
	"isAbout" TEXT, 
	PRIMARY KEY ("DataItem_uid", "isAbout"), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE TABLE "DataItem_specifiedBy" (
	"DataItem_uid" INTEGER, 
	"specifiedBy" TEXT, 
	PRIMARY KEY ("DataItem_uid", "specifiedBy"), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE TABLE "DataItem_methodTypes" (
	"DataItem_uid" INTEGER, 
	"methodTypes_id" INTEGER, 
	PRIMARY KEY ("DataItem_uid", "methodTypes_id"), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid), 
	FOREIGN KEY("methodTypes_id") REFERENCES "Coding" (id)
);
CREATE TABLE "DataItem_derivedFrom" (
	"DataItem_uid" INTEGER, 
	"derivedFrom_uid" INTEGER, 
	PRIMARY KEY ("DataItem_uid", "derivedFrom_uid"), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid), 
	FOREIGN KEY("derivedFrom_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "DataItem_reportedIn" (
	"DataItem_uid" INTEGER, 
	"reportedIn" TEXT, 
	PRIMARY KEY ("DataItem_uid", "reportedIn"), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE TABLE "DataItem_identifiers" (
	"DataItem_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("DataItem_uid", identifiers), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE TABLE "DataItem_alternativeLabels" (
	"DataItem_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("DataItem_uid", "alternativeLabels"), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid)
);
CREATE TABLE "DataItem_extensions" (
	"DataItem_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("DataItem_uid", extensions_id), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "DataSet_isAbout" (
	"DataSet_uid" INTEGER, 
	"isAbout" TEXT, 
	PRIMARY KEY ("DataSet_uid", "isAbout"), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE TABLE "DataSet_specifiedBy" (
	"DataSet_uid" INTEGER, 
	"specifiedBy" TEXT, 
	PRIMARY KEY ("DataSet_uid", "specifiedBy"), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE TABLE "DataSet_methodTypes" (
	"DataSet_uid" INTEGER, 
	"methodTypes_id" INTEGER, 
	PRIMARY KEY ("DataSet_uid", "methodTypes_id"), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid), 
	FOREIGN KEY("methodTypes_id") REFERENCES "Coding" (id)
);
CREATE TABLE "DataSet_derivedFrom" (
	"DataSet_uid" INTEGER, 
	"derivedFrom_uid" INTEGER, 
	PRIMARY KEY ("DataSet_uid", "derivedFrom_uid"), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid), 
	FOREIGN KEY("derivedFrom_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "DataSet_reportedIn" (
	"DataSet_uid" INTEGER, 
	"reportedIn" TEXT, 
	PRIMARY KEY ("DataSet_uid", "reportedIn"), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE TABLE "DataSet_identifiers" (
	"DataSet_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("DataSet_uid", identifiers), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE TABLE "DataSet_alternativeLabels" (
	"DataSet_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("DataSet_uid", "alternativeLabels"), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE TABLE "DataSet_extensions" (
	"DataSet_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("DataSet_uid", extensions_id), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "Activity_performedBy" (
	"Activity_uid" INTEGER, 
	"performedBy_uid" INTEGER, 
	PRIMARY KEY ("Activity_uid", "performedBy_uid"), 
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid), 
	FOREIGN KEY("performedBy_uid") REFERENCES "Agent" (uid)
);
CREATE TABLE "Activity_specifiedBy" (
	"Activity_uid" INTEGER, 
	"specifiedBy_uid" INTEGER, 
	PRIMARY KEY ("Activity_uid", "specifiedBy_uid"), 
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid), 
	FOREIGN KEY("specifiedBy_uid") REFERENCES "Method" (uid)
);
CREATE TABLE "Activity_input" (
	"Activity_uid" INTEGER, 
	input_uid INTEGER, 
	PRIMARY KEY ("Activity_uid", input_uid), 
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid), 
	FOREIGN KEY(input_uid) REFERENCES "Entity" (uid)
);
CREATE TABLE "Activity_output" (
	"Activity_uid" INTEGER, 
	output_uid INTEGER, 
	PRIMARY KEY ("Activity_uid", output_uid), 
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid), 
	FOREIGN KEY(output_uid) REFERENCES "Entity" (uid)
);
CREATE TABLE "Activity_identifiers" (
	"Activity_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("Activity_uid", identifiers), 
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid)
);
CREATE TABLE "Activity_alternativeLabels" (
	"Activity_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("Activity_uid", "alternativeLabels"), 
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid)
);
CREATE TABLE "Activity_extensions" (
	"Activity_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("Activity_uid", extensions_id), 
	FOREIGN KEY("Activity_uid") REFERENCES "Activity" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "StudyResult_dataItems" (
	"StudyResult_uid" INTEGER, 
	"dataItems_uid" INTEGER, 
	PRIMARY KEY ("StudyResult_uid", "dataItems_uid"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid), 
	FOREIGN KEY("dataItems_uid") REFERENCES "DataItem" (uid)
);
CREATE TABLE "StudyResult_sourceDataSet" (
	"StudyResult_uid" INTEGER, 
	"sourceDataSet_uid" INTEGER, 
	PRIMARY KEY ("StudyResult_uid", "sourceDataSet_uid"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid), 
	FOREIGN KEY("sourceDataSet_uid") REFERENCES "DataSet" (uid)
);
CREATE TABLE "StudyResult_componentResult" (
	"StudyResult_uid" INTEGER, 
	"componentResult_uid" INTEGER, 
	PRIMARY KEY ("StudyResult_uid", "componentResult_uid"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid), 
	FOREIGN KEY("componentResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE TABLE "StudyResult_isAbout" (
	"StudyResult_uid" INTEGER, 
	"isAbout" TEXT, 
	PRIMARY KEY ("StudyResult_uid", "isAbout"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE TABLE "StudyResult_specifiedBy" (
	"StudyResult_uid" INTEGER, 
	"specifiedBy" TEXT, 
	PRIMARY KEY ("StudyResult_uid", "specifiedBy"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE TABLE "StudyResult_methodTypes" (
	"StudyResult_uid" INTEGER, 
	"methodTypes_id" INTEGER, 
	PRIMARY KEY ("StudyResult_uid", "methodTypes_id"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid), 
	FOREIGN KEY("methodTypes_id") REFERENCES "Coding" (id)
);
CREATE TABLE "StudyResult_derivedFrom" (
	"StudyResult_uid" INTEGER, 
	"derivedFrom_uid" INTEGER, 
	PRIMARY KEY ("StudyResult_uid", "derivedFrom_uid"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid), 
	FOREIGN KEY("derivedFrom_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "StudyResult_reportedIn" (
	"StudyResult_uid" INTEGER, 
	"reportedIn" TEXT, 
	PRIMARY KEY ("StudyResult_uid", "reportedIn"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE TABLE "StudyResult_identifiers" (
	"StudyResult_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("StudyResult_uid", identifiers), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE TABLE "StudyResult_alternativeLabels" (
	"StudyResult_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("StudyResult_uid", "alternativeLabels"), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid)
);
CREATE TABLE "StudyResult_extensions" (
	"StudyResult_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("StudyResult_uid", extensions_id), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "Proposition_qualifier" (
	"Proposition_uid" INTEGER, 
	qualifier_id INTEGER, 
	PRIMARY KEY ("Proposition_uid", qualifier_id), 
	FOREIGN KEY("Proposition_uid") REFERENCES "Proposition" (uid), 
	FOREIGN KEY(qualifier_id) REFERENCES "Qualifier" (id)
);
CREATE TABLE "Proposition_identifiers" (
	"Proposition_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("Proposition_uid", identifiers), 
	FOREIGN KEY("Proposition_uid") REFERENCES "Proposition" (uid)
);
CREATE TABLE "Proposition_alternativeLabels" (
	"Proposition_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("Proposition_uid", "alternativeLabels"), 
	FOREIGN KEY("Proposition_uid") REFERENCES "Proposition" (uid)
);
CREATE TABLE "Proposition_extensions" (
	"Proposition_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("Proposition_uid", extensions_id), 
	FOREIGN KEY("Proposition_uid") REFERENCES "Proposition" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "InformationEntity_contributions" (
	"InformationEntity_uid" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("InformationEntity_uid", contributions_uid), 
	FOREIGN KEY("InformationEntity_uid") REFERENCES "InformationEntity" (uid), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE TABLE "Method_contributions" (
	"Method_uid" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("Method_uid", contributions_uid), 
	FOREIGN KEY("Method_uid") REFERENCES "Method" (uid), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE TABLE "Document_contributions" (
	"Document_uid" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("Document_uid", contributions_uid), 
	FOREIGN KEY("Document_uid") REFERENCES "Document" (uid), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE TABLE "DataItem_contributions" (
	"DataItem_uid" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("DataItem_uid", contributions_uid), 
	FOREIGN KEY("DataItem_uid") REFERENCES "DataItem" (uid), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE TABLE "DataSet_contributions" (
	"DataSet_uid" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("DataSet_uid", contributions_uid), 
	FOREIGN KEY("DataSet_uid") REFERENCES "DataSet" (uid), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE TABLE "Contribution_activityType" (
	"Contribution_uid" INTEGER, 
	"activityType_id" INTEGER, 
	PRIMARY KEY ("Contribution_uid", "activityType_id"), 
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid), 
	FOREIGN KEY("activityType_id") REFERENCES "Coding" (id)
);
CREATE TABLE "Contribution_performedBy" (
	"Contribution_uid" INTEGER, 
	"performedBy_uid" INTEGER, 
	PRIMARY KEY ("Contribution_uid", "performedBy_uid"), 
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid), 
	FOREIGN KEY("performedBy_uid") REFERENCES "Agent" (uid)
);
CREATE TABLE "Contribution_specifiedBy" (
	"Contribution_uid" INTEGER, 
	"specifiedBy_uid" INTEGER, 
	PRIMARY KEY ("Contribution_uid", "specifiedBy_uid"), 
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid), 
	FOREIGN KEY("specifiedBy_uid") REFERENCES "Method" (uid)
);
CREATE TABLE "Contribution_input" (
	"Contribution_uid" INTEGER, 
	input_uid INTEGER, 
	PRIMARY KEY ("Contribution_uid", input_uid), 
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid), 
	FOREIGN KEY(input_uid) REFERENCES "Entity" (uid)
);
CREATE TABLE "Contribution_output" (
	"Contribution_uid" INTEGER, 
	output_uid INTEGER, 
	PRIMARY KEY ("Contribution_uid", output_uid), 
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid), 
	FOREIGN KEY(output_uid) REFERENCES "Entity" (uid)
);
CREATE TABLE "Contribution_identifiers" (
	"Contribution_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("Contribution_uid", identifiers), 
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid)
);
CREATE TABLE "Contribution_alternativeLabels" (
	"Contribution_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("Contribution_uid", "alternativeLabels"), 
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid)
);
CREATE TABLE "Contribution_extensions" (
	"Contribution_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("Contribution_uid", extensions_id), 
	FOREIGN KEY("Contribution_uid") REFERENCES "Contribution" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "Statement_qualifier" (
	"Statement_uid" INTEGER, 
	qualifier_id INTEGER, 
	PRIMARY KEY ("Statement_uid", qualifier_id), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid), 
	FOREIGN KEY(qualifier_id) REFERENCES "Qualifier" (id)
);
CREATE TABLE "Statement_hasEvidenceOfTypes" (
	"Statement_uid" INTEGER, 
	"hasEvidenceOfTypes" TEXT, 
	PRIMARY KEY ("Statement_uid", "hasEvidenceOfTypes"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE TABLE "Statement_hasEvidenceLines" (
	"Statement_uid" INTEGER, 
	"hasEvidenceLines_uid" INTEGER, 
	PRIMARY KEY ("Statement_uid", "hasEvidenceLines_uid"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid), 
	FOREIGN KEY("hasEvidenceLines_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE TABLE "Statement_hasEvidence" (
	"Statement_uid" INTEGER, 
	"hasEvidence_uid" INTEGER, 
	PRIMARY KEY ("Statement_uid", "hasEvidence_uid"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid), 
	FOREIGN KEY("hasEvidence_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "Statement_isAbout" (
	"Statement_uid" INTEGER, 
	"isAbout" TEXT, 
	PRIMARY KEY ("Statement_uid", "isAbout"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE TABLE "Statement_contributions" (
	"Statement_uid" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("Statement_uid", contributions_uid), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE TABLE "Statement_specifiedBy" (
	"Statement_uid" INTEGER, 
	"specifiedBy" TEXT, 
	PRIMARY KEY ("Statement_uid", "specifiedBy"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE TABLE "Statement_methodTypes" (
	"Statement_uid" INTEGER, 
	"methodTypes_id" INTEGER, 
	PRIMARY KEY ("Statement_uid", "methodTypes_id"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid), 
	FOREIGN KEY("methodTypes_id") REFERENCES "Coding" (id)
);
CREATE TABLE "Statement_derivedFrom" (
	"Statement_uid" INTEGER, 
	"derivedFrom_uid" INTEGER, 
	PRIMARY KEY ("Statement_uid", "derivedFrom_uid"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid), 
	FOREIGN KEY("derivedFrom_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "Statement_reportedIn" (
	"Statement_uid" INTEGER, 
	"reportedIn" TEXT, 
	PRIMARY KEY ("Statement_uid", "reportedIn"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE TABLE "Statement_identifiers" (
	"Statement_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("Statement_uid", identifiers), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE TABLE "Statement_alternativeLabels" (
	"Statement_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("Statement_uid", "alternativeLabels"), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid)
);
CREATE TABLE "Statement_extensions" (
	"Statement_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("Statement_uid", extensions_id), 
	FOREIGN KEY("Statement_uid") REFERENCES "Statement" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "StudyResult_contributions" (
	"StudyResult_uid" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("StudyResult_uid", contributions_uid), 
	FOREIGN KEY("StudyResult_uid") REFERENCES "StudyResult" (uid), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE TABLE "EvidenceLine_evidenceItems" (
	"EvidenceLine_uid" INTEGER, 
	"evidenceItems_uid" INTEGER, 
	PRIMARY KEY ("EvidenceLine_uid", "evidenceItems_uid"), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid), 
	FOREIGN KEY("evidenceItems_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "EvidenceLine_isAbout" (
	"EvidenceLine_uid" INTEGER, 
	"isAbout" TEXT, 
	PRIMARY KEY ("EvidenceLine_uid", "isAbout"), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE TABLE "EvidenceLine_contributions" (
	"EvidenceLine_uid" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("EvidenceLine_uid", contributions_uid), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);
CREATE TABLE "EvidenceLine_specifiedBy" (
	"EvidenceLine_uid" INTEGER, 
	"specifiedBy" TEXT, 
	PRIMARY KEY ("EvidenceLine_uid", "specifiedBy"), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE TABLE "EvidenceLine_methodTypes" (
	"EvidenceLine_uid" INTEGER, 
	"methodTypes_id" INTEGER, 
	PRIMARY KEY ("EvidenceLine_uid", "methodTypes_id"), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid), 
	FOREIGN KEY("methodTypes_id") REFERENCES "Coding" (id)
);
CREATE TABLE "EvidenceLine_derivedFrom" (
	"EvidenceLine_uid" INTEGER, 
	"derivedFrom_uid" INTEGER, 
	PRIMARY KEY ("EvidenceLine_uid", "derivedFrom_uid"), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid), 
	FOREIGN KEY("derivedFrom_uid") REFERENCES "InformationEntity" (uid)
);
CREATE TABLE "EvidenceLine_reportedIn" (
	"EvidenceLine_uid" INTEGER, 
	"reportedIn" TEXT, 
	PRIMARY KEY ("EvidenceLine_uid", "reportedIn"), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE TABLE "EvidenceLine_identifiers" (
	"EvidenceLine_uid" INTEGER, 
	identifiers TEXT, 
	PRIMARY KEY ("EvidenceLine_uid", identifiers), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE TABLE "EvidenceLine_alternativeLabels" (
	"EvidenceLine_uid" INTEGER, 
	"alternativeLabels" TEXT, 
	PRIMARY KEY ("EvidenceLine_uid", "alternativeLabels"), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid)
);
CREATE TABLE "EvidenceLine_extensions" (
	"EvidenceLine_uid" INTEGER, 
	extensions_id INTEGER, 
	PRIMARY KEY ("EvidenceLine_uid", extensions_id), 
	FOREIGN KEY("EvidenceLine_uid") REFERENCES "EvidenceLine" (uid), 
	FOREIGN KEY(extensions_id) REFERENCES "Extension" (id)
);
CREATE TABLE "RecordMetadata_contributions" (
	"RecordMetadata_id" INTEGER, 
	contributions_uid INTEGER, 
	PRIMARY KEY ("RecordMetadata_id", contributions_uid), 
	FOREIGN KEY("RecordMetadata_id") REFERENCES "RecordMetadata" (id), 
	FOREIGN KEY(contributions_uid) REFERENCES "Contribution" (uid)
);