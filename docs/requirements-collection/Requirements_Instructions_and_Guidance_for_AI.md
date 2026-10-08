# Evidence, Provenance, Confidence (EPC) Requirements Collection

**Detailed Instructions & Guidance for AI Agents Completing the SEPIO Requirements Forms**

This document provides the detailed semantic and field-level guidance an AI agent should use when completing `Requirements_Collection_Forms.xlsx` on behalf of a project. It is intended to be used together with the project-specific source materials and the project scope statement supplied by the project representative.

For human-facing orientation to the overall process, see `START_HERE.md` and `Requirements_Collection_Overview.md`.

# I. Why Start with Requirements Collection

Before defining a shared SEPIO Covering Model or a set of reusable profiles, the consortium should first establish what each participating project actually needs to represent. A structured requirements-collection exercise provides the evidence base for deciding which SEPIO concepts and patterns are needed, which requirements recur across projects, and where project-specific differences must be preserved.

The requirements process should be artifact-centered and use-case-centered rather than asking project representatives to reason directly in SEPIO terms. Project representatives are usually best positioned to describe the claims they represent, the information they treat as evidence, how that evidence is assessed, and what provenance must be retained. The SEPIO/modeling group can then perform the second-stage semantic analysis: determining whether those requirements map to concepts such as DataItem, StudyResult, Statement, EvidenceLine, Contribution, or other SEPIO structures.

This separation also supports later implementation with LinkML and LinkML-Map. If the requirements effort captures the semantics of source fields, important distinctions in the source model, and what must survive transformation, those results can directly inform the design of SEPIO-based profiles and declarative mappings between project models.

## Recommended Overall Process

A practical path is to organize the consolidation effort into four phases:

- **Phase 1 — Project requirements collection.** Each project supplies representative evidence-bearing use cases and describes the claim, evidence, and provenance that must be retained.  
  **Agent-assisted execution:** A project representative defines the project scope and supplies schemas, documentation, representative data/examples, and other relevant materials. An AI agent uses these materials and this guidance to prepare a first-pass population of the forms. A project representative then reviews, corrects, and confirms the requirements.

- **Phase 2 — Cross-project semantic analysis.** The modeling group compares requirements across projects and asks which SEPIO concepts are involved, which needs recur, and which differences are semantic rather than merely structural.  
  **Agent-assisted execution:** After project requirements are confirmed, an agent can apply the Requirement → SEPIO Mapping Registry to identify direct mappings, partial coverage, implementation guidance, open questions, and recurrent requirements across projects.

- **Phase 3 — Model architecture.** Based on that analysis, determine what belongs in the Covering Model, how many Covering Models are useful, which reusable profiles are warranted, and which requirements may require extension of SEPIO. Mapping from elements in the requirements forms to specific features of the SEPIO model can help to automate some of this process.  
  **Agent-assisted execution:** During the current pilot phase, an AI agent may generate candidate covering-model content and associated review artifacts from the confirmed forms and mapping registry. These outputs remain candidates for modeler review.

- **Phase 4 — Mapping and validation.** Use real source examples from each project to demonstrate that required semantics can be represented in the chosen profile and mapped using LinkML-Map without unacceptable information loss.  
  **Agent-assisted execution:** Agents can help compare representative project records with the proposed SEPIO-based representation, identify information loss or ambiguity, and document issues for project and SEPIO modelers.

Real example records should be required throughout this process. Abstract descriptions alone often hide important distinctions—for example, whether something called “evidence” is actually source information, an interpretation of that information, a provenance activity, or a higher-order argument. Representative examples allow the modeling group to classify these objects correctly before assigning SEPIO classes or defining profile constraints.

## Role of AI Agents in Requirements Collection

The detailed guidance, documentation, and forms described below are designed with the expectation that AI agents will assist in preparing a first-pass set of project requirements. A project representative may task an AI agent with reviewing the project's available materials and preparing an initial population of the forms.

To do this effectively, the agent needs sufficiently detailed information about the project and its data. Relevant sources may include data-model and schema documentation, project documentation, representative datasets or records, example claims and evidence, provenance conventions, curation guidelines, software or pipeline documentation, meeting notes, and other materials that describe current practice or desired future capabilities.

The agent should use these sources to populate the forms only as far as the available evidence supports, clearly identify uncertainties or gaps, and leave final validation and refinement to project representatives. The goal is **not** for the agent to infer what the project *should* represent, but to document what the project currently represents and what its representatives want a future SEPIO-based model to support. In particular, the agent should distinguish information that may have been used during claim generation, curation, or validation from information that the project actually wants captured, exchanged, or exposed in its data.

AI agents completing the requirements forms should not attempt to assign SEPIO classes or slots on the project's behalf unless explicitly asked to perform the later mapping step. Respondent-facing answers should remain grounded in the project's own concepts, data structures, and requirements. Stable Requirement IDs provide the later machine-facing bridge from these project-centered descriptions to the Requirement → SEPIO Mapping Registry.

## Core Behavioral Rules for AI Agents

The following behavioral instructions apply when an AI agent prepares a first-pass population of the requirements forms (and may also be useful to human respondents).

- **Ground responses in project evidence, not plausibility.** Populate fields from project schemas, documentation, example records, publications, repositories, curation guides, meeting notes, or other supplied materials. Do not infer that a project has a requirement simply because that requirement would be sensible for a project of that type.

- **Distinguish current practice, process history, and desired/future representation requirements.** A source may describe what the project stores today, information that was used during curation but is not stored, something proposed in a design discussion, or what the project wants to support in the future. Do not collapse these into one answer. In particular, do not infer that information used to generate or validate a claim must therefore be represented in the project’s data. Where relevant, use language such as currently captured, used in workflow but not represented, desired capability, proposed, or future requirement.

- **Do not convert project terminology into SEPIO classes prematurely.** Describe the project's native information and requirements first. For example, report that a project stores publication excerpts and assesses whether they support a mechanism; do not decide on the project's behalf that these “must be DataItem and EvidenceLine objects.” Mapping to SEPIO is a later modeling task. Unless explicitly asked to perform the later modeling step, do not edit content in the **SEPIO Mapping Summary** columns or use those summaries to decide what the project's requirements should be. Do not edit predefined Requirement IDs. For any new project-specific row added under an “Other” option, assign a stable custom ID using the form-specific prefix shown in the guidance (for example EI.CUSTOM.001) so that the new requirement can later be added to the mapping registry.

- **Preserve semantic distinctions even when the source data do not.** In particular, keep separate: the information used as evidence; how that information was semantically aligned or grounded; how it was interpreted as evidence; confidence in extraction/alignment; scientific evidence strength; overall confidence in a claim; and downstream retrieval/encoding provenance. If a source field conflates several of these, say so rather than silently assigning it to one category.

- **Use real examples whenever available.** Prefer an actual claim, evidence record, publication excerpt, schema object, or provenance record from the project over a fabricated illustration. If no real example can be found, explicitly mark an example as *illustrative/hypothetical*.

- **Do not manufacture specificity.** Never invent identifiers, evidence types, workflows, agent names, confidence scales, interpretation rules, or provenance requirements to make a form look complete. Enter **Unknown**, **Not documented**, **Needs discussion**, or **Not applicable** where appropriate.

- **Treat absence of documentation as uncertainty, not as a negative requirement.** “I did not find evidence that the project records evidence strength” is different from “The project does not need evidence strength.” The latter requires explicit support or human confirmation.

- **Identify meaningful variation within the project.** Do not assume that one workflow applies everywhere. Look for differences among claim types, data sources, human versus automated curation, or production versus experimental pipelines. Conversely, do not create separate claim types merely because their predicates differ if their evidence/provenance requirements are essentially identical.

- **Use the minimum number of Claim Types needed to expose EPC differences.** When many claim types share the same Evidence, Provenance, and Confidence requirements, group them appropriately. Split them when their evidence sources, interpretation approaches, provenance needs, or confidence models materially differ.

- **For Evidence Item Types, describe what the information is—not how it was obtained.** An experimental result remains an experimental result whether it was entered manually or extracted by an LLM. Human/AI extraction belongs primarily in provenance unless the manner of extraction changes the semantic nature of the information artifact.

- **For Evidence Interpretation, determine the actual unit of judgment.** Do not assume one Evidence Line per snippet, paper, or study. Determine whether the project assesses each item independently, groups multiple items into one argument, or performs nested/higher-order assessments. If this is unclear, flag it as an open question.

- **For Semantic Alignment Provenance, distinguish mapping from evidentiary reasoning.** Extraction, entity/relation recognition, grounding, normalization, and mapping source semantics into a structured representation are alignment activities. Deciding whether that aligned information supports or disputes a target claim is Evidence Interpretation.

- **For Provenance, distinguish the five layers explicitly.** Ask separately: how did the evidence information come to exist; how was its meaning aligned to structured semantics; how was it interpreted/reasoned over to generate knowledge; how was the resulting artifact encoded; and how was that encoded artifact later retrieved or transformed between systems.

- **Record disagreements and ambiguity rather than resolving them silently.** If documentation or project representatives appear to use a term inconsistently, or two sources imply different requirements, note the discrepancy and identify it as something requiring human review.

- **Prioritize requirements, not implementation details.** Capture what information the project needs to represent and why. Do not overfocus on the exact YAML shape, property name, database column, or current technical implementation unless it reveals an important semantic requirement.

- **Make proposed additions obvious.** If the agent thinks a requirement may be useful but cannot find evidence that the project actually needs it, put it in a clearly labeled *Suggested follow-up / Possible requirement* note rather than filling it in as a project requirement.

- **Preserve traceability to source material.** For every substantive requirement in the first-pass draft, the agent should ideally be able to point back to the source that motivated it—a schema field, example record, documentation passage, issue, meeting note, or representative statement. This traceability does not necessarily have to appear in the final form, but should be retained during drafting so a human reviewer can verify the result.

- **End with unresolved questions for the project representative.** After populating the forms, generate a short list of the highest-value uncertainties that need human confirmation—for example, “Is evidence strength actually authored or intended to be derived?” or “Are multiple publication excerpts normally treated as independent arguments or grouped by study?”

- **Treat the completed form as a draft until a project representative validates it.** AI assistance should reduce the burden of requirements collection, but the agent should not present inferred requirements as authoritative project decisions.

**As a general rule, a partially completed form with clearly marked unknowns is preferable to a fully populated form containing inferred or invented project requirements.**

Finally, agentic respondents should produce **two outputs**:

1.  the populated forms

2.  a short **“Review Notes for Project Representative”** containing:

    1.  assumptions it made

    2.  fields it could not substantiate

    3.  conflicting information it encountered, and

    4.  the 5–10 questions whose answers would most improve the requirements record.

---

# II. Key Concepts and Terminology

Below we define and share preferred names for several foundational concepts where a shared understanding will be useful in this modeling requirements collection effort. Project representatives should understand the meaning of and distinctions between these concepts, and use the recommended terminology in describing their data and requirements.

### “Statements” (as “Claims” vs “Concept Definitions”)

> **Description:** An information artifact that expresses a proposition, hypothesis, or judgment about the world. A Statement may be an assertion which states a purported fact about our objective reality, or a more subjective judgement or definition that is offered from a particular point of view, but not grounded in an objective, provable reality.
>
> In our work we are concerned with **two high level kinds of Statements**: Claims and Concept Definitions. It is important to define and distinguish these two types of Statements because it represents a fundamental divide across the statements reported by projects in our consortium, which may ultimately use different models, and require different requirements collection forms.

- **“Claims”:** put forth propositions about how entities in the domain of discourse relate or behave, and that can in principle be evaluated for truth or validity.

  - **Examples:** “Variant X causes loss of function in Protein X”, “CFTR dysfunction contributes to the pathophysiology of cystic fibrosis.”

  - Claims are the types of things that have evidence and confidence, and are reported in Knowledgebases such as the Monarch KG, Translator, and DisMech.

  - Note that a particular claim is defined/identified by both its “proposition” (the inherent meaning of what it is putting forth as true), and the occasion on which it is made (when and by whom it was put forth). If two curators put forth the same proposition that “Variant X causes loss of function in Protein X”, these are separate Claims instances because they were made by different people on different occasions.

- **“Concept Definitions”**: characterize terms or concepts that refer to entities in the domain of discourse - e.g. assign names, definitions, identifiers, or synonyms to concepts, place them into a hierarchical classification, or provide mappings between terms representing them.

  - **Examples:** “The string xxx is the preferred name for the concept of yyy”, “The term xxx is defined as yyy”, “The name xxx is a synonym of the term yyy “, “The concept xxx is a subtype of the concept yyy.”

  - Such ‘definitions’ represent **expert** but ultimately **subjective** opinions about the best way to define or name a concept - they are given from a particular point of view but not grounded in an objective, provable reality.

  - Concept Definitions are most often reported in ontologies and other terminological artifacts such as Mondo. They typically have provenance and rationale describing why a particular naming, classification, or mapping decision was made. They are not usually supported or assessed using the same evidence-and-confidence framework applied to empirical Claims, because they represent terminological or modeling judgments rather than assertions about objective states of the world. For this reason. collect their modeling requirements separately in our effort.

  - In our work, we will use “**Concept**” to refer to the abstract notion of some thing that exists in reality, “**Name**” to refer to labels used to refer to concepts in speech or writing, and “**Term**” to refer to a formal characterization of a concept in a terminological artifact - which often provides things like identifiers, preferred and alternate names, synonyms, and mappings to other terms.)

### **“Evidence”** 

> **Description:** Evidence is information—such as data, observations, study results, text, images, or other knowledge—that is used by an agent in reasoning about the truth or validity of a claim; information plays the role of evidence only when it is interpreted as bearing on a particular claim.
>
> We call an individual piece of information that is used as evidence an “**Evidence Item”**.
>
> **Example 1:** Results from several in vitro and in vivo functional assays that are interpreted to support the conclusion that Variant X markedly reduces Protein X activity.
>
> **Example 2:** One or more passages from biomedical publications describing CFTR dysfunction, in Cystic Fibrosis (CF) together with the source publications or other structured information from which those passages were obtained - from which an AI Agent derives a structured claim purporting that CFTR dysfunction is causal for CF.
>
> Note that the notion of “**evidence**” is relevant for **Claims**, but not **Concept Definitions** - which are more subjective characterizations of concepts or terms rather than statements about the entities in reality that these terms reference.

### “Evidence Interpretation”

> **Description:** Evidence Interpretation is the act of evaluating one or more information artifacts and determining whether, in what direction, and with what strength they bear on the truth of a target claim.
>
> **Example 1:** A domain expert reviews the functional-assay results to assess if and how strongly they support that Variant X can cause loss of function in Protein X.
>
> **Example 2:** An AI-assisted DisMech curation workflow extracts and grounds concepts and relationships from publication text, then and assesses if and how strongly the extracted statements support the claim that CFTR dysfunction contributes to cystic-fibrosis pathophysiology.

### **“Evidence Line”** 

> **Description:** An Evidence Line is a single argument for or against the validity of a target claim, based on interpretation of a set of one or more evidence Items. Evidence Lines are the output of an Evidence Interpretation process - and typically report in what *direction*, and with what *strength* the assessed evidence bears on the truth of a target claim.
>
> **Example 1:** An argument based on functional assay results that determines they provide very strong (*strength*) evidence disputing (*direction*) the claim that Variant X causes loss of function in Protein X.
>
> **Example 2:** An argument based on structured statements extracted from text that determines them to *strongly* (strength) support (*direction*) the claim that CFTR dysfunction contributes to cystic-fibrosis pathophysiology.

### “Confidence”

> **Description:** The degree of certainty that an agent has in the accuracy of reported information. For a Claim, this may be confidence that the proposition put forth in a claim is true. For a semantic alignment output, this may be confidence that the agent mapped text strings to correct terms or codes. Confidence may be reported using a qualitative term (e.g.”high”, “medium”, “low”) or quantitative value (e.g. a probability between 0 and 1, or some custom score on bespoke scale)
>
> **Example 1:** A human curator reports “high” confidence that Variant X reduces the function of Protein X.
>
> **Example 2:** An AI-Agent reports a numerical score of 0.6 that indicates its confidence that it correctly identified and mapped a concept in text to a correct ontology term.
>
> Note that, like “evidence”, the notion of “**confidence**” is relevant for **Claims**, but not **Concept Definitions** - which are more subjective characterizations of concepts or terms, rather than statements about the entities in reality that these terms reference.

### “Agent”

> **Description:** An autonomous actor that participates in an activity or process, often in pursuit of an intended outcome. In this document, an Agent may be a person, organization, software program, or AI system. Where relevant, the specific type of Agent will be stated explicitly (for example, *human*, *organization*, *software agent*, or *AI agent*).
>
> **Example 1:** A clinical scientist or expert panel interpreting functional-assay results for a variant to determine whether they support its pathogenicity..
>
> **Example 2:** An AI curation agent extracting and interpreting mechanistic evidence from literature, and a human curator who reviews and validates the result.

### “Provenance”

> **Definition:** Information about the origins and history of data or knowledge artifacts, including the processes, inputs, agents, and transformations involved in their creation, interpretation, curation, retrieval, or modification.
>
> Note that, unlike “**evidence**” and “**confidence**”, the notion of “**provenance**” is relevant to both **Claims** and **Concept Definitions** - however the levels and kinds of provenance differ between them. In this document we focus on characterization of **Claim Provenance**.
>
> Below, we make an explicit distinction between five ‘levels’ of provenance relevant to Claims encoded in biomedical knowledgebases. It is important to understand these levels, as they **provide a framework for understanding and collecting EPC requirements** in the forms that follow.

#### Five Levels of Claim Provenance

1. **Evidence Item Provenance:** Describes how information items that may *later* be used as evidence for claims - such as experimental measurements or observations, derived statistical results, images, datasets, or prior claims - were originally generated, measured, extracted, curated, or otherwise produced - before they were used in evidence-based reasoning.

2. **Semantic Alignment Provenance:** Describes how a human or AI agent understands a claim representation encountered in a source text or record and maps the concepts, relationships, and contextual information expressed in the source to the normalized concepts and relationships used in a structured target representation. For human agents, this is usually an implicit and undocumented cognitive task, but for AI agents, each step in this process (extraction, grounding, normalization) may be recorded to allow provenance tracing and accuracy checking.

3. **Knowledge Provenance:** Describes the curation, interpretation, and reasoning processes involved in generating knowledge from evidence. This includes how information is selected, organized, evaluated, and interpreted as supporting or disputing a possible fact (**Evidence Interpretation Provenance**), and how multiple evidentiary arguments are subsequently combined and weighed to reach a final conclusion or assertion (**Assertion Provenance**).

4. **Encoding Provenance:** Describes how a claim, evidence item, or other information artifact is expressed or serialized in a concrete representation so that it can be stored, discovered, exchanged, or consumed - for example, as an English sentence in a publication, a Biolink-compliant edge in a Neo4j knowledge graph, an object in a JSON document, or a row in a table.

5. **Retrieval Provenance:** Describes downstream operations by which an existing encoded representation of knowledge or evidence is retrieved, transferred, transformed, normalized, aggregated, or otherwise passed between systems. It concerns the handling of an already encoded record, rather than the original generation of the knowledge or its initial serialization.

**In short:**

- **Evidence Item Provenance** → how the raw informational inputs came to exist (independent of and prior to their future use as evidence)
- **Semantic Alignment Provenance** → how one source’s representation of those inputs was understood and mapped into the concepts/relationships used by the target curator or system.
- **Knowledge Provenance** → how those aligned inputs were interpreted as evidence (*Evidence Interpretation Provenance*) and ultimately reasoned over to make a claim (*Assertion Provenance*)
- **Encoding Provenance** → how that claim was concretely serialized in a particular format or language
- **Retrieval Provenance** → how that serialization was subsequently moved/transformed between data systems

##### Illustrative Examples

**Variant functional-impact interpretation**

1. **Evidence Item Provenance:**  
   The Functional Genomics Laboratory at Redwood Biomedical Institute generated protein-activity measurements on March 12, 2026 using its FGX-17 cell-based assay protocol, and analyzed the results with BioQuant Analysis Suite v4.3.

2. **Semantic Alignment Provenance:** n/a - in this case as the agent is a human and semantic alignment is an implicit cognitive process that needs no documentation.

3. **Knowledge Provenance:**  
   Dr. Elena Marquez and the Redwood Variant Interpretation Panel reviewed the in vitro and mouse-model results on March 20, 2026 using Functional Evidence Guideline v2.1, judged them to provide very strong support for the proposition that Variant X causes loss of function in Protein X, and approved that conclusion by panel consensus.

4. **Encoding Provenance:**  
   On March 21, 2026, the approved conclusion was encoded by the Redwood Variant Curation System as a structured variant-functional-impact assertion in JSON, linking the normalized variant identifier, protein identifier, evidence lines, and the panel's strength assessment.

5. **Retrieval Provenance:**  
   On March 25, 2026, the variant-evidence-ingest pipeline retrieved that JSON record, normalized the gene and variant identifiers to HGNC and VRS identifiers, transformed the record into the Translational Genomics KG schema, and loaded it as a graph assertion.

**AI-assisted DisMech curation**

1. **Evidence Item Provenance:**  
   Nguyen and colleagues generated measurements of CFTR chloride transport in cultured airway epithelial cells and reported the finding that CFTR dysfunction contributes to cystic-fibrosis pathophysiology, as described in several key passages and figures in a 2024 publication.

2. **Semantic Alignment Provenance:** On May 10, 2026, the DisMech Curation Agent, running the mechanism-extraction-v3 workflow extracted and grounded the CFTR finding from a passage in this publication into a structured representation using the terms HGNC:1884 for CFTR and MONDO:0009061 for cystic fibrosis.

3. **Knowledge Provenance:**  
   On May 10, 2026, the DisMech Curation Agent, running model version MedCurator-3.2 interpreted the confidence in the semantic alignment, along with additional information about the location of the passage in the text, to determine the passage provides strong support for the claim that CFTR dysfunction contributes to cystic-fibrosis pathophysiology; curator Maya Patel reviewed and approved that interpretation on May 11.

4. **Encoding Provenance:**  
   After approval, the DisMech curation system serialized the mechanistic claim, supporting evidence items, evidence-line direction and strength, source references, and curation metadata into the corresponding DisMech YAML disorder record.

5. **Retrieval Provenance:**  
   On May 12, 2026, the dismech-to-monarch pipeline retrieved the YAML record, mapped its identifiers and relationships into the Monarch/Biolink representation, generated the corresponding knowledge-graph edge and provenance metadata, and loaded them into the Monarch KG.


# III. Populating Requirements Collection Forms

The bundled `Requirements_Collection_Forms.xlsx` workbook contains the following worksheets for collecting Evidence, Provenance, and Confidence (EPC) requirements for your project:

1.  **Project Overview Form:** reports on the scope and goals for your project

2.  **Claim Type Form:** enumerates the key kinds of claims your project reports (as context for understanding/enumerating the kinds of evidence and provenance that need to be represented)

3.  **Claim Representation Structure Form:** reports how claims are packaged or embedded in current project data, and what representation structures the project wants to preserve or support in future implementations

4.  **Reified Claim Semantics Form:** for projects requiring a reified Claim / Statement object, reports what semantic information that object must represent, including textual and structured proposition semantics, proposition placement, and qualifiers.

5.  **Evidence Item Type Form:** reports the kinds of information or artifacts the project currently represents, or wants to represent, as evidence for its claims

6.  **Evidence Interpretation Form:** reports what information about evidence interpretation and organization need to be captured in your project.

7.  **Provenance Types Form:** reports what types of provenance information you want to be able to capture about how information used as evidence is originally produced, how this evidence is organized and interpreted, and how claims are generated and encoded, and retrieved across systems.

Guidance and instructions for populating each form are provided below; complete the corresponding worksheet in `Requirements_Collection_Forms.xlsx`. Note that a separate set of requirements forms will be provided for Concept Definitions and related terminological statements that make up much of the content of ontologies and other terminological systems.

## General Requests for Populating Forms

- **Use Key Concepts and Terminology:** Respondents do not need to understand the SEPIO model. But please describe your project and data using terms from the “Key Concepts and Terminology” section above where possible. This will provide requirements with maximal clarity, consistency, and utility for data modelers.

- **Response conventions used across the forms:**
  - Y = Yes, N = No, and M = Maybe / Needs discussion.
  - For “current-state of your data” questions, do not treat absence of documentation as No; use M or explain that the answer is not documented when appropriate.
  - For “desired-state of your data” questions, answer Yes only when the project wants that information or structure represented in its data—not merely because it may have been used in generating, curating, or validating a claim.
  - “Desired in SEPIO-based Data” means desired support in the project’s future SEPIO-based representation; in this phase, these answers are used to determine what must be available in a project-level SEPIO Covering Model, not to define profile-level cardinality or requiredness constraints.
  - Agents should complete only respondent-facing fields. **Do not edit content in the SEPIO Mapping Summary columns, and do not use those summaries to decide what the project's requirements should be.**
  - Where a field provides a predefined set of permissible values, use the labels exactly as written rather than paraphrasing them. Multiple permitted values should be separated with semicolons. Free-text explanation and example fields provide context for mapping and validation, but should not by themselves be treated as deterministic mapping triggers unless a mapping rule explicitly says so.
  - **Required vs. optional fields:** Each respondent-facing question/field is marked as required (`r`) or optional (`o`). A few fields are marked (`r*`) - which indicates a conditional requirement that is described in the Dictionary for that form. Please complete optional fields whenever you reasonably can, as these details often provide important context for modeling and implementation. If an optional field cannot be completed or is not relevant, it is still helpful to say so briefly (for example, “n/a” “not available,” “not applicable,” or “not currently known”) and explain why when useful.
  - **“Used in Current Data?” vs. “Desired in SEPIO-based Data?”:** Most initial requirements will be derived from an AI agent’s review of current project schemas, documentation, datasets, and example records. These sources provide the primary basis for determining whether a feature is **Used in Current Data**. As a default for first-pass automated population, if a feature is clearly represented and meaningfully used in the project’s current data, the agent should normally also mark it as **Desired in SEPIO-based Data**, unless available project information indicates that the feature is legacy, incidental, being deprecated, intentionally excluded from the future representation, or otherwise not desired going forward. Conversely, the agent should not mark a feature as desired solely because it would be useful or seems appropriate for the project. Features not present in current data should be marked as desired only when there is affirmative evidence of a future requirement. Where the agent cannot determine the intended future state with reasonable confidence, use **M (Maybe / Needs discussion)** and explain the uncertainty. “Desired in SEPIO-based Data” responses produced by an AI agent should therefore be treated as provisional requirements that a project representative may confirm or revise during human review.


## 1. Project Overview Form (PO) 

**Purpose:** Use this form to provide enough high-level context for the modeling group to understand your project, the kinds of knowledge it manages, and why evidence/provenance representation matters for your use cases. Keep responses concise; detailed requirements are collected in the later forms.

**How to complete it:** Describe the project as it actually exists today, while noting important planned or desired capabilities where relevant. AI agents should rely on project documentation or other supplied sources rather than inferring requirements from what similar projects do. If something is uncertain, use “Unknown” or “Needs discussion.”
### **Dictionary**
- **Project Name (`r`)** is the name of the project or resource.

- **Representative(s) (`r`)** identifies the people contributing requirements on its behalf.

- **Description (`o`)** briefly summarizes the kinds and sources of knowledge the project contains, major workflows, and primary users/use cases.

- **Evidence/Provenance Needs (`o`):** briefly explains why the project needs evidence and provenance represented and the main use cases those representations need to support. Provides high level context/use cases for the more specific requirements captured in the remaining forms.

## 2. Claim Type Form (CT) 

**Purpose:** Use this form to identify the main kinds of claims for which your project needs evidence, provenance, or confidence represented. The goal is not necessarily to enumerate every predicate in your data, but to distinguish claim types where the underlying semantics or EPC requirements differ.

**How to complete it:** Define Claim Types using the categories of entities involved, the relationship asserted between them, and important qualifiers. See guidance below about the granularity at which to distinguish claim types when reporting them in the form. Use real project examples wherever possible. Claim Types with essentially the same evidence/provenance requirements may be grouped; separate them when their EPC requirements materially differ. Do not try to map these claims to SEPIO classes yet.

**Guidance for AI agents:** Do not create separate Claim Types simply because predicates differ if the project treats their evidence/provenance identically. Conversely, do not collapse claims that have materially different evidence or provenance requirements.

**Additional Resources**: See the Guidance below for How to Define/Distinguish Claim Types, as well as a Dictionary that defines and provides examples of values in each column/field in the form, as well as Populated Example of the form.

## How to Define / Distinguish Claim Types

A Claim Type is defined based on the category of things the claims connect (**subject** **category**, **object category**), and the type of relationship they assert to hold between them (**relationship**). Formally, Claim Type = S<sub>cat</sub> + Rel + O<sub>cat</sub>. Examples:

- **Drug** - treats - **Disease**

- **Disease** - characterized by - **Phenotype**

- **Chemical** - affects - **Gene/GeneProduct**

You can be as granular as you see fit in distinguishing types of claims defined in this way - depending on the number/diversity of claim types in your dataset, and the specific evidence and provenance requirements for each.

In selecting the subject and object categories to define a Claim Type, you can use very specific categories (e.g. “Drug”, “Pathological Process”), or broad categories / sets of categories (e.g. “Thing”, “Chemical Entity”, “Process”, “Gene Protein or Transcript”) as appropriate. *But try **NOT** to lump claim types together if they have different evidence/provenance modeling requirements.*

If your project deals in only a handful of claim types, it may be reasonable to list each separately even if they have the same types of E/P requirements.

If your project reports very many and diverse claim types, feel free to collapse them to a reasonable number by specifying many subject/object categories or relationship types in one Claim Type description - as long as the evidence and provenance modeling requirements for those claims are roughly the same.

For example, if your project uses NLP to extract several kinds of triples from text, and the EPC for all types of triples is the same, you can define your Claim Type as “**Thing** - related to - **Thing**”, or enumerate categories and say **“Gene/Chemical** - causes / interacts_with / affects - **Gene/Chemical”**.

The goal here is to distinguish as few Claim types as necessary to convey the diversity of knowledge in your datasets, while reporting areas where different types of claims may require different modeling.
### **Dictionary**
The data dictionary below describes the types of information to provide about each claim type (r= required, o = optional).

***NOTE** that the form includes **two example entries** for illustrative purposes. The second one shows a case where multiple subject and object types and predicates are grouped together into a single Claim Type entry for brevity/convenience - because claims of this type generally have the same kind and level of EPC metadata and modeling requirements. You can leave these examples in the form or delete and overwrite them.*

- **Identifier (`r`):** A numerical identifier of the form “C###” that serves as the project-level stable key for the Claim Type and can be used to reference that Claim Type from elsewhere in the requirements package. Claim Type identifiers are reference identifiers only; they are not Requirement IDs and do not directly trigger mappings to SEPIO model elements.

  - <u>Examples</u>: “C001”. “C002”, …

- **Descriptor (`r`)**: A short name by which we can reference the type of claim

  - <u>Examples</u>: “Causal Relationships”. “Disease Treatment” “Disease-Phenotype Association”, “Disease Pathophysiology”, “All Term-Level Relationships”.

- **Subject Categor(ies) (`r`):** The types of entities that are subjects of this type of claim (semi-colon separated list if more than one)

  - <u>Examples</u>: “Entity”, “Gene; Protein; Transcript”, "Chemical Entity”, “Biological Process; Molecular Function”, “Drug; Small Molecule; Molecular Mixture”, “Disease; Phenotype”

- **Object Categor(ies) (`r`):** The types of entities that are objects of this type of claim (semi-colon separated list if more than one)

  - <u>Examples</u>: “Entity”, “Gene; Protein; Transcript”, "Chemical Entity”, “Biological Process; Molecular Function”, “Drug; Small Molecule; Molecular Mixture”, “Disease; Phenotype”

- **Relationship Type(s) (`r`):** The types of relationships asserted to hold between entities in the subject and object categories (semi-colon separated list if more than one)

  - <u>Examples: “associated with”, “causes”, “treats”, “has phenotype”, “affects”, “acts upstream of”</u>

- **Qualifying Information (`o`):** types of additional information that refine, extend, or add context to the claim expressed by the subject–relationship–object structure.

  - <u>Examples</u>: “anatomical context”, “frequency; severity”, “disease context”, “relevant population”

- **Example Claim(s) from Your Data (`r`):** One or more concrete examples of an instance of this type of claim, to illustrate the nature of the subjects and objects and relationships reported and how they are encoded/framed.

  - <u>Examples</u>:

    - “Cystic fibrosis has phenotype chronic respiratory infection“,

    - “The EGFR V600E variant predicts sensitivity to afatinib in patients with Lung Carcinoma”;

- **Evidence/Provenance Notes (`o`):** Free-text description of the evidence, provenance, and confidence information the project wants represented for this Claim Type. Focus on information that should be captured, exchanged, or exposed in the data—not merely information that may have been used during claim generation.

  - <u>Examples</u>:

    - “We generally need to capture only the source from which the knowledge was retrieved, and any publications or evidence types reported by those sources.”;

    - “For all claims extracted from text by our AI agents, we need to capture detailed information about the extraction, grounding, and normalization of each concept in a claim the AI agent identifies in text and structures into a Statement in our data. We also need to capture the name and version of the agents and tools used, and the raw text that was used, the id and name of the publication, and the section of the publication it was found in.”

- **Additional Notes (`o`):** Additional descriptions or notes, as needed to convey additional useful nuances of considerations for this type of claim.

A Populated Example

An example of a few claim types described using these fields:

| **Identifier (`r`)** | **Descriptor (`r`)**            | **Subject Category(ies) (`r`)** | **Object Category(ies) (`r`)**           | **Relationship Type(s) (`r`)**      | **Qualifying Information (`o`)**       | **Example(s) (`r`)**                                                                       | **Evidence/Provenance Notes (`o`)**                                                                                                                                                                          |
|--------------------|-------------------------------|-------------------------------|----------------------------------------|-----------------------------------|--------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C001               | Disease-Phenotype Association | Disease                       | Phenotype                              | has phenotype                     | frequency; severity                  | Cystic fibrosis has phenotype chronic respiratory infection.                             | Capture the source from which the association was retrieved, relevant supporting publications, and any evidence type reported by the source.                                                               |
| C002               | Variant-Drug Response         | Genetic Variant               | Drug; Small Molecule                   | predicts sensitivity to           | disease context; relevant population | The EGFR V600E variant predicts sensitivity to afatinib in patients with Lung Carcinoma. | Capture supporting clinical or experimental evidence, the source publication, disease/population context, and provenance of any automated extraction or normalization.                                     |
| C003               | Causal Relationships          | Gene; Protein; Transcript     | Biological Process; Molecular Function | affects; causes; acts upstream of | anatomical context                   | Loss of CFTR function causes impaired chloride transport in airway epithelium.           | For claims extracted from text by AI agents, capture the raw text and publication location; the agent/model and version; extraction, grounding, and normalization steps; and any human review or approval. |

## 3. Claim Representation Structure Form (CRS) 

**Purpose**: Use this form to describe how claims are packaged or embedded in your project’s data, both in the current implementation and in the future project representation you want to support. This form focuses on representation structure—for example, whether a claim appears as a slot/value on a parent record, a nested object, a first-class claim/association object, or a direct graph edge. It does not ask where the semantic components of the claim itself (such as subject, relationship, object, and qualifiers) should live; those requirements are collected separately in the Claim Semantics Form.

The structures reported here are important for understanding project architecture, transformation requirements, and later profile or serialization design. They generally do not directly select SEPIO classes or slots for a Covering Model. A source structure may be transformed into a different SEPIO-based representation as long as the required claim semantics are preserved. If preserving a particular structural pattern is itself important to the project, say so explicitly in Explanation / Considerations.

A project may use or require more than one representation structure. For example, one class of claims may be represented as direct graph edges while another is represented as reified Association objects. Review each row independently and indicate whether the structure is used now and whether the project wants it supported in its future representation.
### **When completing the form**
- Select all structures that apply to any claim type in your data; these options are not mutually exclusive.

- Base responses on real project data, schemas, documentation, or examples wherever possible.

- Distinguish current implementation from desired future representation.

- For source-specific structures such as parent slot/value representations, nested objects, and direct graph edges, do not assume that the future SEPIO-based representation must preserve the same structural shape. Use Explanation / Considerations to state whether the structure must be preserved, may be transformed into a semantically equivalent representation, or is still undecided.

- If different Claim Types use different structures, list the relevant Claim Type reference IDs (for example C001, C002) where feasible.

- If you are unsure, use M / Needs discussion rather than guessing.

- AI agents completing a first pass should not invent project requirements or examples. Where possible, retain a traceable source for substantive conclusions and flag uncertain items for human review.

- Focus on the organization or packaging of claim records, rather than the semantic fields that express what the claim means or the evidence/provenance represented around it.
### **Dictionary**
**Pre-populated:**

- **Requirement ID:** a stable identifier for the predefined representation-structure row (prefix CS.). These identifiers support cross-reference, traceability, and transformation/profile analysis; they are not Requirement IDs that directly trigger SEPIO class/slot mappings. Do not edit these values. If a genuinely new structure is added under Other, assign a stable custom identifier such as CS.CUSTOM.001.

- **Claim Representation Structure:** a predefined pattern describing how a claim is packaged or embedded in project data. Review the provided options rather than editing these values unless the project requires an additional structure.

- **Description:** defines what the representation structure means and what aspects of a claim are explicit versus supplied by surrounding context.

- **Illustrative Example(s):** illustrates what the structure might look like in actual data. These examples are for orientation and do not prescribe a particular syntax, schema, identifier system, or implementation.

- **General Utility / Transformation Implications:** summarizes practical consequences of the structure, including compactness, ability to attach metadata, dependence on surrounding context, and likely transformation considerations.

**To be completed by respondent:**

- **\[F1\] Used in Current Data? (Y / N / M):** Enter Y if the project currently uses this representation structure for any relevant claims; N if it does not; or M if the answer is uncertain / needs discussion.

- **\[F2\] Desired in SEPIO-based Data? (Y / N / M):** Enter Y if the project wants a future SEPIO-based representation to support this structural pattern; N if the pattern does not need to be supported; or M if the requirement is unresolved. This is a structural or implementation preference and does not by itself determine which SEPIO classes or slots belong in the Covering Model.

- **\[F3\] Explanation / Considerations (`o`):** provide important additional details, especially whether the structure must be preserved in a SEPIO-based implementation, may be transformed into another structure as long as its semantics are retained, applies only to particular workflows or data sources, or raises unresolved transformation questions. Provide project examples where useful.

- **Relevant Claim Type IDs (`o`):** list the project-level Claim Type reference IDs (for example C001, C002) for which this structure is relevant.

## 4. Reified Claim Semantics Form (RCS) 

**Purpose:** This is a **conditional follow-on form** for projects that need to represent one or more **Reified Claim / Statement Objects** in their future data model. This includes reified objects used to represent the project’s own primary claims, as indicated in the **Claim Representation Structure Form**, as well as reified prior claims that are represented as evidence. Complete the RCS form whenever the project needs any such first-class Claim / Statement object represented in its SEPIO-based data.

A reified claim is represented as a first-class information object that can be independently identified, referenced, and annotated—for example with evidence, provenance, confidence, or other metadata. This form identifies what semantic information that first-class claim object must be able to represent.

If the project does **not** require a Reified Claim / Statement Object in its future representation, this form may be skipped. If the need for a reified representation is unresolved (M) in the Claim Representation Structure Form, this form may either be deferred until that question is resolved or completed provisionally with the uncertainty clearly noted. If only some Claim Types use a reified representation, complete the form with respect to those Claim Types and identify their Claim Type reference IDs where useful.

The form asks whether the reified claim representation must support:

- a human-readable textual expression of the claim;

- structured subject–predicate–object semantics represented directly on the Statement;

- structured subject–predicate–object semantics represented in a separate Proposition object referenced by the Statement; and

- additional qualifying or contextual information that extends or refines the core subject–predicate–object proposition.

These requirements directly inform generation of a project-specific SEPIO Covering Model because they determine which Statement and Proposition capabilities must be available.

In the current SEPIO model, a reified Statement can represent the structured meaning of the proposition it puts forth in either of two supported ways:

- **SPO Semantics on Statement:** the subject, predicate, object, and any qualifiers are represented directly on the Statement.

- **SPO Semantics in nested Proposition:** the Statement references a separate Proposition object, and the subject, predicate, object, and any qualifiers are represented on that Proposition.

These alternatives are represented as separate rows in the form rather than as a single choice. A project may therefore indicate that it needs the Statement pattern, the Proposition pattern, both patterns, or neither. If the project needs only a human-readable claim expression and no structured proposition semantics, it may select only the Human-Readable Claim Text requirement.

The **Reified Claim Semantics Form** should be interpreted together with, but kept distinct from, the **Claim Representation Structure Form**. The Claim Representation Structure Form determines whether a first-class reified claim object is needed at all. The RCS form is used only after that structural requirement is established, to determine what semantic capabilities that object must provide.
### **When completing the form**
- Complete this form only if **Reified Claim / Statement Object = Y** under **Desired in Future Project Representation** in the Claim Representation Structure Form.

- If **Reified Claim / Statement Object = M**, either defer this form or complete it provisionally and clearly flag unresolved questions.

- Answer each row based on what the project currently represents and what it wants its future SEPIO-based reified claim representation to support.

- Human-readable text and structured SPO semantics are not mutually exclusive. Mark both as desired if the project needs both a natural-language expression and a machine-computable structured representation of the claim.

- **SPO Semantics on Statement** and **SPO Semantics in nested Proposition** are also not necessarily mutually exclusive. Mark both as desired if the Covering Model must support both patterns.

- Do not select both structured patterns merely because both are available in SEPIO. Select only the pattern or patterns the project actually needs.

- Treat **Qualifying / Contextual Information** as a separate requirement from the core subject–predicate–object representation. Mark it as desired only if the project needs to represent information that refines, constrains, or adds context to the proposition.

- If qualifiers are needed, they should be supported on whichever semantic carrier is required by the project: the Statement, the nested Proposition, or both if both structured patterns are needed.

- If different Claim Types require different semantic patterns, identify the relevant Claim Type reference IDs and explain the distinction.

- If a requirement is unresolved, use M and explain the uncertainty rather than selecting a pattern simply because it appears more expressive.

- AI agents should report the project’s actual semantic requirements and should not choose among alternative SEPIO-supported patterns unless project documentation or a project representative supports that choice.
### **Dictionary**
**Pre-populated:**

- **Requirement ID:** a stable machine-facing identifier for the predefined reified-claim semantic requirement row (prefix RCS.). These IDs may be used by the Requirement → SEPIO Mapping Registry to select SEPIO classes, slots, or supported modeling patterns. Do not edit these values.

- **Reified Claim Semantic Requirement:** a short name for the semantic capability being assessed.

- **Description:** defines the information-content requirement for the reified claim representation.

- **Illustrative Example(s):** provides examples of the semantic information that may need to be represented. Examples are illustrative and should not be treated as prescribing a particular syntax, schema, or identifier system.

- **General Utility / Modeling Implications:** summarizes why the distinction matters and how it may affect the generated SEPIO Covering Model.


**To be completed by respondent:**

- **\[F1\] Represented in Current Data? (Y / N / M):** enter Y if the project currently represents this semantic capability explicitly in any relevant reified claim objects; N if it does not; or M if the answer is uncertain / needs discussion. If the project does not currently use reified claim objects, N may be appropriate even when the capability is desired in the future.

- **\[F2\] Desired in SEPIO-based Data? (Y / N / M):** enter Y if the future SEPIO-based reified claim representation must support this semantic capability; N if it is not required; or M if the requirement is unresolved. A Y in this field can act as a trigger for inclusion of mapped SEPIO elements in the generated Covering Model.

- **\[F3\] Explanation / Considerations (`o`):** provide additional project-specific details, examples, exceptions, unresolved questions, or distinctions among workflows. Use this field especially when different Claim Types require different semantic patterns or when both structured representation patterns are needed for different reasons.

- **\[F4\] Relevant Claim Type IDs (`o`):** list the project-level Claim Type reference IDs for which the semantic requirement applies when it does not apply uniformly across all reified Claim Types.

Interpretation of the predefined rows:

- **RCS.FREE_TEXT — Human-Readable Claim Text:** select when the project needs the reified claim object to carry a natural-language expression of what the claim asserts. This may be used alone or in addition to structured proposition semantics.

- **RCS.STRUCTURED_STATEMENT — SPO Semantics on Statement:** select when the core proposition expressed by the reified claim must be represented directly on the Statement using explicit subject, predicate/relationship, and object fields.

- **RCS.STRUCTURED_PROPOSITION — SPO Semantics in nested Proposition:** select when the Statement should reference a separate Proposition object that carries the structured subject, predicate/relationship, and object semantics.

- **RCS.QUALIFIERS — Qualifying / Contextual Information:** select when the project needs the proposition meaning to include additional information that extends, refines, constrains, or contextualizes its core subject–predicate–object semantics—for example disease context, anatomical context, population, frequency, severity, or another claim-specific qualifier. Qualifier support should be applied to the Statement and/or Proposition pattern selected by the project.

## 5. Evidence Item Type Form (EIT) 

**Purpose:** Use this form to identify the kinds of information or artifacts your project needs to represent as evidence for its claims, and to describe requirements for representing them.

**How to complete it:** Review each inventoried evidence item type and indicate whether your project needs to represent it as evidence for at least one claim type. Add project-specific examples and relevant details where useful. If an important evidence type is missing, add it under Other or create an additional row. A project may capture multiple levels of the same evidence chain—for example, a publication, a passage within it, a structured statement extracted from that passage, and a study result reported by the publication.

Note that the listed categories are intended as a **practical, respondent-facing framework for requirements collection, not a complete taxonomy of evidence or a proposed SEPIO class hierarchy**. They intentionally include evidence artifacts at different levels of granularity—for example individual measurements, study results, prior claims, database records, publication passages, and whole documents—because projects may represent and reference evidence at different levels. A given evidence item in a project may reasonably correspond to more than one category in this inventory; for example, a ClinVar record used as evidence might be classified both as an **External Data Record** and, if the relevant content is a specific pathogenicity assertion, as a **Directly Corresponding Prior Claim — Structured Data**. In such cases, select all applicable types and explain the overlap or distinction in the Explanations field. Additional types may be added as new use cases emerge, and later semantic modeling will determine how these requirements map to formal SEPIO classes, relationships, and profiles.
### **Dictionary**
**Pre-populated:**

- **Requirement ID:** a stable machine-facing identifier for the predefined evidence requirement row (prefix EI.). Do not edit these values. Category/grouping rows also have IDs for organization but are not respondent mapping triggers. For a new project-specific evidence type added under Other, assign a custom identifier such as EI.CUSTOM.001, EI.CUSTOM.002, et**c.**

- **Evidence Item Category / Type:** names the respondent-facing evidence category or specific evidence type represented by the row.

- **Description:** defines what the category represents.

- **Illustrative Example(s):** provides illustrative examples for orienting the respondent.

**To be completed by respondent:**

- **\[F1\] Represented in Current Data? (`r`):** whether this type of evidence information is currently represented explicitly in your project’s data for at least one Claim Type. Answer **Yes** only if the evidence item itself is captured or referenced in the project data—not merely because it was used informally or externally when generating the claim.

- **\[F2\] Desired in SEPIO-based Data? (`r`):** whether your project wants the future SEPIO-based model to support explicit representation of this type of evidence information for at least one Claim Type. This should reflect what the project wants to be able to store, exchange, or expose in its data, regardless of whether that evidence type was involved in generating the claim.

> **Conditional completion:** If Desired in SEPIO-based Data = No, the desired-location, local-representation, addressability, and attribute columns can usually be left blank. If Desired = Yes or Maybe, complete those columns as far as the available project requirements support.

- **\[F3\] Desired Evidence Item Location:** Where should instances of this evidence type be represented or maintained? Select all that apply, using the stable option codes exactly as written:

  - **LOCAL** — In project data ecosystem: the evidence item has some representation within a dataset or resource controlled by the project.

  - **EXTERNAL** — Referenced by external ID/URL: the authoritative or fuller representation exists in an external resource and is referenced using a resolvable identifier or URL.

> Select both where a local representation is maintained together with a link to an external source.

- **\[F4\] Desired Local Representation Form (required when F3 includes’ In project data ecosystem’):** If this evidence type is represented within the project’s data ecosystem, indicate how much of the evidence item itself should be represented. Select all that apply where appropriate, using the stable option codes exactly as written.

  - **FREE_TEXT** — Free-text representation: information about or from the evidence item is present only in free-text content and is not separately structured.

    - Example: a DisMech evidence snippet contains the statement that chloride transport was reduced by 42%, but the measurement itself is not separately modeled.

  - **STRUCTURED_METADATA** — Structured metadata / proxy record: a structured object describes or identifies the evidence item, but does not itself encode the evidentiary content carried by that item.

    - Example: a local Figure record stores figure_number, caption, publication, and url, but does not contain the image or the data shown in it.

    - Example: a Dataset record stores title, accession, creator, and URL, but not the dataset contents.

  - **STRUCTURED_CONTENT —** Structured evidence content: the evidentiary information or value carried by the item is explicitly represented in structured fields.

    - Example: an experimental measurement stores value: 42, unit: percent reduction, and confidence_interval.

    - Example: a Prior Claim object stores its subject, relationship, object, qualifiers, and other claim content.

  - **STORED_ARTIFACT —** Evidence artifact itself stored separately: the actual evidence artifact is stored separately within or directly managed by the project.

    - Example: an image file, figure image, PDF, or data table is stored as part of the project’s data resource.

- **\[F5\] Individual Addressability Needed?:** Does the project need individual instances of this evidence type to be represented as separately identifiable/addressable items, so that provenance, evidence interpretation, confidence, or other metadata can be attached specifically to them? Use one of the stable values YES, NO, or NO_SPECIFIC_REQUIREMENT.

  - Values:

    - **Yes** = individual instances needed

    - **No** = the item need only be represented/referenced as part of a larger object/container (e.g. a specific figure referenced from within a publication object)

    - **No specific requiremen**t = not sure or neither of these (explain as possible)

  - Example: a publication may currently be cited only by PMID at the claim level, whereas a particular figure within that publication may need its own identifier if a project wants to assert that the figure specifically supports the claim.

- **\[F6\] Evidence Item Attributes to Represent (`o`):** What non-provenance-related info about this type of evidence item do you want to capture in the data explicitly? Focus on attributes intrinsic to the evidence item itself, especially those not already covered by the Provenance Type Form (you may want to complete that form first, then return here to add things it did not cover). e.g.

  - for a **Scientific Publication**: title, publication year, journal, authors;

  - for an **Experimental Measurement**: measured value, unit, reference range, confidence interval, detection limit;

  - for a **Statistical Metric**: metric type, value, confidence interval, p-value threshold or significance interpretation;

  - for a **Computational Prediction / Score**: score/value, categorical classification, scale/range, threshold used for interpretation;

  - for a **Figure**: figure number/label, caption, panel identifier;

> *Do not repeat provenance information here unless it is necessary to understand the evidence item itself. For example, “journal” may reasonably be treated as an attribute of a publication, whereas the software version used to generate a result belongs under provenance.*

- **\[F7\] Specific Kinds of this Item Type (`r`):** List the specific kinds or subtypes of this high-level Evidence Item Type that occur in your data or that you want the future model to support. Use the terminology your project normally uses; a formal controlled vocabulary or taxonomy is not required. Be as specific as is useful for understanding modeling needs.

  - For example, if you selected **Experimental or Observational Data Items**, you might list “in vitro and ex vivo measurements,” “cell counts,” “FACS measurements,” “protein-expression measurements,” or “cell-line survival times.” If you selected **Statistical Metrics**, you might list “p-values,” “z-scores,” “odds ratios,” “confidence intervals,” or “chi-square statistics for concept co-occurrence in medical records.” If you selected **Computational Predictions / Scores**, identify the kinds of predictions or scores represented, such as “variant pathogenicity scores,” “drug-sensitivity predictions,” or “protein-structure confidence scores.” If you selected **External Data Record**, describe the kinds of records and their source systems, such as “ClinVar variation records,” “DrugCentral drug records,” or “dbGaP study/phenotype records.” For **Documents, Images, Datasets, Study Results,** or other broad categories, similarly describe the concrete kinds relevant to your project.

  - This field is intended to reveal distinctions that may affect modeling—for example, whether different subtypes require different attributes, provenance, representation patterns, or SEPIO specializations. Do not list every individual instance; describe the meaningful kinds represented across your data.

- **\[F7\] Example(s) from Your Data (`o`):** where possible, provide one or two concrete examples of this evidence item type from the project’s current data. If the evidence type is desired but not currently represented, an illustrative future example may be provided and clearly labeled as such.

- **\[F8\] Explanation / Considerations (`o`):** provide project-specific details about how this evidence type is or should be represented. Note any distinctions in granularity, overlap with other evidence types, important qualifiers, limitations of the current representation, or reasons why the project does or does not want to capture it.

- **\[F9\] Relevant Claim Types (`o`):** optional, but helpful where possible; list the IDs of specific Claim Types from the Claim Type Form for which this evidence type is relevant.

**Guidance for AI agents:** Describe what evidence information the project explicitly represents or wants to represent in its data. Do not infer a requirement simply because a type of evidence was used by a curator, algorithm, or external workflow to generate a claim. Evidence may influence claim generation without being part of the project’s desired data representation. Base selections on project data, documentation, examples, or explicit requirements, and flag uncertainty rather than assuming support is needed.

**Complete respondent fields for the specific evidence-type rows, not the higher-level category/grouping rows.** Do not edit the **SEPIO Mapping Summary** column, and do not use its content when describing the project's requirements.

These questions intentionally separate several downstream modeling concerns: where an evidence item is maintained; how it is represented locally; whether individual instances must be separately addressable; and what intrinsic attributes the representation must carry.

> where does it live? → what representation is needed? → must it be first-class/addressable? → what properties must it carry?

## 6. Evidence Interpretation Form (EINT) 

This form is concerned with how evidence is attached to and interpreted as bearing on a target claim. It includes both lightweight evidence-linking requirements and richer Evidence Line requirements so that downstream mapping can determine whether the Covering Model needs direct Statement-to-evidence shortcuts, EvidenceLine structures, or both.

**Purpose:** Use this form to describe whether and how your project evaluates information as evidence for or against claims, including evidence direction, strength, grouping, contradictory evidence, and aggregation.

**Background Information:**

- There is an important distinction between an **Evidence Item**—the information being considered—and an **Evidence Interpretation**—the judgment about how that information bears on a particular claim. The outcome of such interpretation is an argument for or against the claim - which we call an **Evidence Line**.

- An Evidence Line may assess a single text snippet, observation, measurement, study result, or prior claim; several pieces of information of these types that come from one or many studies or publications; or even other lower-level Evidence Lines.

- The types of and granularity at which evidence is assessed to produce an Evidence Line is up to the data provider - and matches the level at which they wish to assess the direction and strength of support evidence items have for the target claim.

- For example, consider two projects that use LLM-agents to extract structured statements from literature to support Disease-Phenotype association claims: one project may wish to assess the direction and strength of evidence provided by each distinct snippet, while the other might want to assess all snippets from a single pub together. The SEPIO model supports both.

- Notably, some projects aim to collect evidence that may argue against claims of interest (direction = disputes), in addition to evidence that argues for it (direction = supports) - which can provide a more complete picture of the evidence landscape.

**How to complete the form:** For each topic, indicate whether the capability needs to be captured and explain the project-specific requirement where necessary. The first two rows ask about lightweight linking patterns: direct links from a claim to specific evidence items, and direct links from a claim to source resources that provided evidence when the specific evidence items are not represented. Subsequent rows concern explicit Evidence Interpretation / Evidence Line structures. Base answers on the level at which your project actually makes evidentiary judgments. Do not assume that there must be one Evidence Line per snippet, publication, or study; multiple items may contribute to a single argument, or a project may assess each individually.

Note that for projects with simpler needs around representation of evidence interpretation and provenance, most of the questions in this form may not be relevant. But it is useful to review them in case it sparks ideas for future development.
### **Dictionary**
**Pre-populated:**

- **Requirement ID:** a stable machine-facing identifier for the predefined evidence-linking or interpretation requirement (prefix EINT.). Do not edit these values.

- **Topic:** identifies the interpretation feature being considered.

- **Question:** describes the requirement to assess.

- **Example Response/Explanation:** illustrates the kind of answer expected but is not a recommended design.

> ***Note** that if you answer “No” to the first question (“Do you need to capture information about how evidence items are interpreted as bearing on a target claim?”) you may still want to review the subsequent questions to be sure that none of the features they describe are important - but likely do not need to complete the rest of this form.*

**To be completed by respondent:**

- **\[F1\] Represented in Current Data? (`r`):** whether this type of information is currently represented explicitly in your project’s data for at least one Claim Type. Answer **Yes** only if the information is captured or referenced in the project data—not merely because it was performed informally or externally when generating a claim.

- **\[F2\] Desired in SEPIO-based Data? (`r`):** whether your project wants the future SEPIO-based model to support explicit representation of this type of information for at least one Claim Type. This should reflect what the project wants to be able to store, exchange, or expose in its data, regardless of whether that evidence interpretation process was involved in generating the claim.

- **\[F3\] Explanation / Considerations (`o`):** describe how the requirement works in your project, including relevant scales, grouping rules, examples, exceptions, or unresolved questions.

- **\[F4\] Example(s) from Your Data (`o`):** where possible, provide one or two concrete examples of this type of information from the project’s current data. If the feature is desired but not currently represented, an illustrative future example may be provided and clearly labeled as such.

Projects can also choose if they want to focus only on interpreting evidence that supports their claims, or also consider evidence that may argue against claims when determining if and with what degree of confidence they put forth a claim as true or false.

The questions in the **Evidence Interpretation Form** collect requirements related to these types of characteristics of the evidence interpretation and synthesis task. It will be relevant for projects that need to capture how evidence is interpreted as bearing on claims; the modeling group will later determine whether and how this maps to SEPIO Evidence Lines.”

## 7. Provenance Types Form (PROV) 

**Purpose:** Use this form to identify what provenance information your project currently represents, and what provenance information it wants a future SEPIO-based model to support for evidence items, semantic alignment, evidence interpretation, assertions, encoding, and retrieval. It is organized according to the provenance levels described above:

- **Evidence Item Provenance**: relevant only for projects that want to describe how info used as evidence was generated

- **Semantic Alignment Provenance:** relevant when a project wants to represent how source semantics were interpreted, extracted, grounded, normalized, or mapped into a structured target representation. In principle, this can apply to human curation or mappings from structured source records; however, in practice this level of detailed provenance is expected to be needed primarily for automated or AI-assisted extraction and semantic alignment from text, where the intermediate extraction, grounding, and normalization steps may need to be recorded and audited.

- **Evidence Interpretation Provenance:** relevant only for projects that want to capture details of how specific kinds/pieces of evidence are interpreted in support of claims

- **Assertion Provenance**: relevant for all projects to some degree - as this is the provenance of how claims are made. But some may want to track provenance here in more detail than others.

- **Encoding Provenance** : relevant only if your project is concerned with how a claim was concretely serialized in a particular format or language

- **Retrieval Provenance**: relevant only if your project is concerned with how data representing claims is moved/transformed between data systems

Not every project needs every provenance level. A lightweight knowledge resource may need only source and assertion level provenance. Projects following detailed evidence interpretation frameworks may require more granular provenance at the level of evidence organization and interpretation. And projects that utilize AI-assisted curation may require detailed provenance at the level of semantic-alignment and interpretation.

**How to complete it:** Review each provenance type independently. Indicate whether it is represented in current project data and whether the project wants it represented in future SEPIO-based data. Provide concrete project examples where possible, and use the Explanation / Considerations column to record required granularity, value distinctions, exceptions, or other project-specific requirements. Do not mark a provenance type as desired merely because it may have been involved in generating a claim; mark it as desired only when the project wants that provenance information represented in its data.
### **Dictionary**
**Pre-populated:**

- **Requirement ID:** a stable machine-facing identifier for each provenance requirement row (prefix PROV.). Do not edit these values.

- **Provenance Level:** identifies the type of artifact or task for which provenance is described, according to the Provenance Level Framework above (i.e. provenance of an evidence item, an assertion, an interpretation process, a semantic alignment task, etc)

- **Provenance Area:** identifies the kind of provenance information being considered for the indicated artifact or task—for example Agent, Methods, Resources, Date, Confidence, or Review Level.

- **Provenance Type / Question:** provides a short respondent-facing formulation of what the Provenance Attribute is asking about. Description explains the attribute in more detail at the indicated provenance level.

- **Illustrative Example(s):** provides example values to orient the respondent. **SEPIO Mapping Summary** content is provided for downstream modeling context. Project respondents and AI agents should **not edit it or use it to determine the project's requirements.**

**To be completed by respondent:**

- **\[F1\] Represented in Current Data? (`r`):** whether this type of information is currently represented explicitly in your project’s data for at least one type of Claim or other artifact. Answer **Yes** only if the information is captured or referenced in the project data—not merely because it was relevant to generating the claim.

- **\[F2\] Desired in SEPIO-based Data? (`r`):** whether your project wants the future SEPIO-based model to support explicit representation of this type of information for at least one type of Claim or other artifact. This should reflect what the project wants to be able to store, exchange, or expose in its data.

- **\[F3\] Example(s) from Your Data (`o`):** where possible, provide one or two concrete examples of this type of information from the project’s current data. If the feature is desired but not currently represented, an illustrative future example may be provided and clearly labeled as such.

- **\[F4\] Explanation / Considerations (`o`)**: Where helpful, provide additional details about this requirement as relevant to your specific project / dataset.

## 8. Claim–Evidence Matrix Form (CEM) — optional/conditional

The CEM worksheet is already included in `Requirements_Collection_Forms.xlsx`. It is intended as a follow-on step after the project's Claim Types and Evidence Item Types have been defined.

**Purpose:** This worksheet indicates which Evidence Item Types are relevant to which Claim Types, offering a compact view of the relationships identified separately in the Claim Type and Evidence Item Type forms. An AI agent may populate a first pass from the completed requirements and supporting project materials. Ambiguous cells should be flagged for human review rather than silently filled.

Example of what this might look like:

|                            | **Supporting Pubs** | **Evidence Type** | **Text Passage** | **Prior Claims** | **Expert Opinion** |
|----------------------------|---------------------|-------------------|------------------|------------------|--------------------|
| **Drug-Disease**           | X                   |                   |                  | X                |                    |
| **Disease-Phenotype**      | X                   |                   |                  |                  |                    |
| **Causal Chemical Gene**   | X                   | X                 |                  |                  |                    |
| **Disease-Anatomy**        | X                   |                   |                  |                  |                    |
| **Protein Interaction**    | X                   |                   | X                |                  |                    |
| **Model System - Disease** | X                   |                   | X                |                  | X                  |

**How to complete it:** Each row represents one Claim Type from the Claim Type Form. Each column represents one Evidence Item Type from the Evidence Item Type Form. Enter an X where that type of evidence is used or expected to be used for that Claim Type. Leave the cell blank where it is not relevant. Mark actual project requirements rather than every evidence type that could theoretically be useful. The generated matrix should preserve the **Claim Type reference ID** for each row and the **Evidence Item Requirement ID** for each column so that each marked cell can be interpreted as a machine-addressable pairwise requirement. A separate **generated matrix-cell Requirement ID** may be assigned to each marked relationship; this is distinct from the Claim Type reference ID and should not be edited.

If an AI agent generates the initial matrix, it should derive relationships from the completed requirements and supporting project materials rather than assuming common biomedical evidence patterns. Ambiguous cells should be flagged for human review rather than silently filled.

---

# IV. Completeness and Consistency Check Before Submission

Before returning the completed workbook to the project representative, the agent should:

- check every required respondent-facing field;
- verify that controlled values use the labels defined in the workbook/guidance;
- compare answers across forms for internal consistency;
- identify contradictions between project sources or between current-state and desired-state answers;
- identify required questions that remain unsupported or unresolved;
- make sure free-text explanations do not imply uncaptured requirements;
- verify that richer upstream-source information has not been incorrectly attributed to the project itself;
- verify that downstream/API/UI enrichments have not been treated as canonical project requirements unless the project scope says otherwise;
- retain traceability to the project sources supporting non-obvious conclusions; and
- prepare the short Review Notes for the Project Representative described in the Core Behavioral Rules above.

A partially completed workbook with clearly marked unknowns is preferable to a fully populated workbook containing inferred or invented requirements.

# V. What Happens After the Requirements Are Confirmed?

After a project representative reviews and confirms the completed requirements workbook, the requirements-to-model workflow applies the maintained Requirement → SEPIO Mapping Registry against the controlled responses and stable Requirement IDs. That later stage can generate a candidate SEPIO covering model and associated summary, traceability, follow-up, gap/extension, implementation-guidance, form-feedback, and generation-manifest artifacts.

During the current pilot phase, an AI agent may perform this later analysis and generation step. The completed requirements forms should nevertheless remain requirements-first: **do not use the SEPIO Mapping Summary columns to decide what the project needs.**

Detailed downstream mapping, routing, and output-generation behavior is documented separately in the Requirement → SEPIO Mapping Registry/README and the Requirements-to-Model Report Specification.
