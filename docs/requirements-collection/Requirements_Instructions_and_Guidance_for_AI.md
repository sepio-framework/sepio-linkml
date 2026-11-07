# Evidence, Provenance, Confidence (EPC) Requirements Collection


**Detailed Instructions & Guidance for Agents Completing the SEPIO Requirements Forms**

This document provides the detailed semantic and field-level guidance an agent should use when completing `Requirements_Collection_Forms.xlsx` on behalf of a project. It is written with sufficient detail to guide AI agents in performing this work, but is also useful for human agents. It is intended to be used together with `REQUIREMENTS_FORM_PROMPT.md`, the selected project scope statement, the reviewed project Resource Inventory, and the project-specific source materials identified there.

For more focused human-facing orientation to the overall process, see `QUICK_START.md` and `Requirements_Collection_Overview.md`. For guidance on assembling and classifying the evidence base before requirements completion, see `RESOURCE_INVENTORY_GUIDANCE.md` and `RESOURCE_INVENTORY_PROMPT.md`.

# I. Why Start with Requirements Collection

Before defining a shared SEPIO Covering Model or a set of reusable profiles, the consortium should first establish what each participating project actually needs to represent. A structured requirements-collection exercise provides the evidence base for deciding which SEPIO concepts and patterns are needed, which requirements recur across projects, and where project-specific differences must be preserved.

The requirements process should be artifact-centered and use-case-centered rather than asking project representatives to reason directly in SEPIO terms. Project representatives are usually best positioned to describe the claims they represent, the information they treat as evidence, how that evidence is assessed, and what provenance must be retained. The SEPIO/modeling group can then perform the second-stage semantic analysis: determining whether those requirements map to concepts such as DataItem, StudyResult, Statement, EvidenceLine, Contribution, or other SEPIO structures.

This separation also supports later implementation with LinkML and LinkML-Map. If the requirements effort captures the semantics of source fields, important distinctions in the source model, and what must survive transformation, those results can directly inform the design of SEPIO-based profiles and declarative mappings between project models.

## Recommended Overall Process

The SEPIO modeling effort follows a four-phase workflow that progresses from project-specific requirements collection through semantic mapping, model derivation, and validation. The process is designed to be **requirements-driven and grounded in real project data**, with project representatives and SEPIO modelers providing review and oversight at appropriate stages.

The requirements collection tools, guidance documents, and associated workflows have been designed to facilitate **AI-assisted execution**, which is a recommended but optional approach. AI agents can help inspect project resources, elicit and document requirements, propose mappings to the SEPIO Core Model, and generate candidate Covering Models and related artifacts. These activities may also be performed manually or through a combination of human and AI-assisted work.

### Phase 1 — Project Requirements Collection

**Objective:** Establish what each participating project currently represents, and what it needs to represent in a future SEPIO-based data model, with respect to claims, evidence, evidence interpretation, provenance, and confidence.

**General approach:** Identify and review relevant project resources, establish the scope of the requirements collection effort, and complete the Requirements Collection Forms to characterize both current-state and desired-state representational needs. Document the basis for important requirements, provide concrete examples from project data, and identify uncertainties requiring further discussion. Project representatives review and confirm the resulting requirements.

**Recommended AI-assisted execution:**

- **Resource discovery and scoping:** An AI agent examines project materials and prepares a Resource Inventory identifying authoritative current-state sources, additional resources supporting desired-state requirements, and representative data records. A project representative reviews the inventory and confirms the scope of the effort.
- **Requirements form completion:** An agent uses the selected scope, Resource Inventory, project source materials, and starter-kit guidance to prepare responses to the Requirements Collection Forms. It independently assesses current-state ([F1]) and desired-state ([F2]) requirements, documents the basis for these responses, and provides concrete examples.
- **Collaborative elicitation as an alternative:** Rather than completing an initial draft independently, the agent may work interactively with a project representative to populate the forms through a structured discussion or interview. The agent presents each requirement question, proposes an initial interpretation or response based on available project materials, and works with the representative to clarify the project's needs and agree on an appropriate answer. This approach can be particularly valuable when important requirements are implicit in existing data conventions, curation practices, or expert knowledge rather than explicitly documented. It was successfully used in the MONDO ontology-curation pilot.
- **Supporting outputs and review:** The agent can generate project-specific Claim–Evidence Matrices and a Requirements Review Memo summarizing the project's data landscape, principal requirements, current-versus-desired distinctions, and unresolved questions. The project representative reviews, refines, and confirms the results.

**Primary outcome:** A reviewed, project-specific requirements package describing the project's representational needs independently of the SEPIO modeling constructs that may ultimately satisfy them.

### Phase 2 — Requirements-to-SEPIO Mapping and Analysis

**Objective:** Determine how the collected project requirements correspond to capabilities of the SEPIO Core Model, and identify requirements that are directly supported, require particular modeling patterns, are only partially supported, or reveal potential model gaps.

**General approach:** Analyze the confirmed requirements against the authoritative SEPIO Core Model to identify relevant classes, properties, relationships, and modeling patterns. Document the mappings, their rationale, any conditions governing their applicability, and areas where requirements are not fully supported. As requirements from multiple projects become available, compare their mappings to identify recurring capabilities, common modeling patterns, and project-specific differences.

**Recommended AI-assisted execution:**

- Apply the maintained **Requirement → SEPIO Mapping Registry** and associated specifications to the confirmed requirements.
- Identify the SEPIO classes, properties, relationships, and supported modeling patterns corresponding to the requirements, including any conditions or constraints governing their use.
- Generate traceable mapping results and review artifacts that document direct coverage, alternative approaches, partial matches, unresolved questions, and potential gaps or extension needs.
- Support cross-project comparison of mapped requirements to identify common capabilities and project-specific distinctions.

**Primary outcome:** A reviewed set of traceable Requirement → SEPIO mappings, including any unresolved mapping questions or identified gaps in the SEPIO Core Model.

### Phase 3 — SEPIO Covering Model Derivation and Review

**Objective:** Derive candidate SEPIO Covering Models that collectively provide the representational capabilities needed to satisfy the mapped requirements of participating projects.

**General approach:** Use the confirmed requirements and their mappings to the SEPIO Core Model as the basis for deriving an initial candidate Covering Model. Evaluate the proposed model for completeness, semantic coherence, unnecessary complexity, and compatibility with the SEPIO Core Model. Review and refine the candidate through collaboration among SEPIO modelers and participating project representatives.

The initial derivation of a candidate Covering Model is intended to be **systematic and driven by the approved requirement mappings**, rather than beginning with a manually designed model architecture. Human review then focuses on evaluating the generated model, resolving modeling alternatives, addressing gaps, and refining its structure.

**Recommended AI-assisted execution:**

- Generate an initial candidate Covering Model from the confirmed project requirements and their mappings to SEPIO.
- Produce supporting artifacts identifying which requirements are satisfied by each model element, how they are represented, and where important modeling choices or unresolved gaps remain.
- Check the candidate model for consistency with the authoritative SEPIO Core Model, completeness relative to the mapped requirements, and potential redundancies or unnecessary complexity.
- Support iterative review and refinement by SEPIO modelers and project representatives, including analysis of potential extensions where existing SEPIO capabilities are insufficient.

**Covering Models versus project-specific profiles:** The purpose of a SEPIO Covering Model is to assemble the shared representational capabilities needed to satisfy a set of project requirements. It is distinct from a project-specific implementation profile, which may subsequently impose additional constraints, cardinalities, controlled vocabularies, or structural conventions appropriate to a particular dataset or application. Defining such profiles may be a useful follow-on activity, but is not a required output of this phase.

**Primary outcome:** A reviewed candidate SEPIO Covering Model, with traceability to the requirements it addresses and documentation of any unresolved modeling decisions or extension needs.

### Phase 4 — Project Data Mapping and Validation

**Objective:** Demonstrate that representative project data can be transformed into SEPIO-based representations using the proposed Covering Model without losing information or semantic distinctions required by the project.

**General approach:** Develop mappings from project-specific data structures to the relevant SEPIO classes, properties, and modeling patterns. Apply these mappings to representative source records, including important variations and edge cases. Evaluate whether the resulting representations preserve the required information and support the project's intended uses. Use the findings to refine the mappings, Covering Model, or original requirements where necessary.

**Recommended AI-assisted execution:**

- Develop or propose mappings from project-specific source models into the proposed SEPIO-based representation, using tools such as LinkML-Map where appropriate.
- Apply these mappings to representative records spanning different Claim Types, Evidence Item Types, evidence interpretation patterns, provenance structures, and important edge cases.
- Evaluate the transformed representations for semantic fidelity, completeness, and consistency with the confirmed requirements.
- Identify information loss, ambiguous mappings, unsupported requirements, or missing modeling capabilities, and document proposed corrections for review.

**Primary outcome:** A validated approach for representing project knowledge and its associated evidence, provenance, and confidence information using SEPIO-based models, together with any outstanding implementation or modeling issues.

### Role of Representative Data Throughout the Process

Concrete source records are important throughout all four phases. They help establish what information a project actually represents, reveal implicit semantics and distinctions that abstract requirements may miss, support evaluation of proposed SEPIO mappings, and demonstrate whether the candidate Covering Model can adequately represent the project's information.

Representative records should therefore be identified early in the requirements collection process, referenced in the completed forms where useful, and reused during mapping and validation. When examples are illustrative rather than drawn from actual project data, they should be clearly labeled as such.


## Role of AI Agents in Requirements Collection

The detailed guidance, documentation, and forms described below are designed with the expectation that AI agents will assist in preparing a first-pass set of project requirements. A project representative may task an AI agent with reviewing the project's available materials and preparing an initial population of the forms.

To do this effectively, the agent needs a reviewed **Resource Inventory** and a selected **project scope statement**. The Resource Inventory is the supporting-source catalog: it assigns stable Source IDs, records versions and roles, identifies representative examples, and distinguishes canonical current-state sources from broader desired-state support. Relevant resources may include data-model and schema documentation, canonical datasets or distributions, representative records, project documentation, provenance conventions, curation guidelines, software or pipeline artifacts, papers, requirements, issues, competency questions, and other project-specific materials.

The selected scope determines how those resources may be used. **[F1]/current-state answers must be based only on the sources explicitly designated as CURRENT_STATE_CANONICAL or CURRENT_STATE_CANONICAL_COMPANION in the selected scope.** Richer information found elsewhere in the project must not be used to broaden [F1]. **[F2]/desired-state answers may draw on the broader DESIRED_STATE_SUPPORT sources allowed by the selected scope**, but only where those sources provide affirmative project-specific support. The agent should clearly identify uncertainties or gaps and leave final validation and refinement to project representatives.

AI agents completing the requirements forms should not attempt to assign SEPIO classes or slots on the project's behalf unless explicitly asked to perform the later mapping step. Respondent-facing answers should remain grounded in the project's own concepts, data structures, and requirements. Stable Requirement IDs provide the later machine-facing bridge from these project-centered descriptions to the Requirement → SEPIO Mapping Registry.

## Core Behavioral Rules for AI Agents

The following behavioral instructions apply when an AI agent prepares a first-pass population of the requirements forms (and may also be useful to human respondents).

- **Ground responses in project sources, not plausibility.** Populate fields from project schemas, documentation, example records, publications, repositories, curation guides, meeting notes, or other supplied materials. Do not infer that a project has a requirement simply because that requirement would be sensible for a project of that type.

- **Treat the Resource Inventory as the supporting-source catalog and the selected scope as the authority for source use.** Refer to sources by their Resource Inventory Source IDs where useful. Do not silently expand the allowed source set during form completion. If a source appears important but is not permitted by the selected scope, flag it for human review rather than using it.

- **Classify broader desired-state support when [F2] goes beyond [F1].** Where useful, use the Resource Inventory support labels: `EXPLICIT_FUTURE_REQUIREMENT`, `EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT`, or `DOCUMENTED_MODEL_INTENT`. If no project-specific supporting source justifies a desired-state capability, do not mark it Y or M simply because it seems useful.

- **When [F2] differs from [F1], make the support for that difference explicit.** In [F4] Basis for F2 Response, identify the supporting Source ID + source name/version and, where relevant, the desired-state support type. Summarize the same basis in the self-contained [F5] Explanation / Considerations field. A useful pattern is: `Current state: [canonical observation]. Desired-state support: [SUPPORT TYPE] — [Source ID — source name/version]: [brief rationale].`

- **Apply the selected scope literally when distinguishing current and desired state.** For [F1]/current-state questions, use only the exact canonical source set named in the selected scope. A capability found only in an intermediate artifact, alternate release, paper, roadmap, upstream source, downstream representation, or process description must not be marked current unless that resource is explicitly included in the current-state canonical source set. For [F2]/desired-state questions, use the broader source set allowed by the selected scope and capture a **maximal but source-supported** requirement set rather than a speculative one.

- **Do not convert project terminology into SEPIO classes prematurely.** Describe the project's native information and requirements first. For example, report that a project stores publication excerpts and assesses whether they support a mechanism; do not decide on the project's behalf that these “must be DataItem and EvidenceLine objects.” Mapping to SEPIO is a later modeling task. Unless explicitly asked to perform the later modeling step, do not edit content in the **SEPIO Mapping Summary** columns or use those summaries to decide what the project's requirements should be. Do not edit predefined Requirement IDs. For any new project-specific row added under an “Other” option, assign a stable custom ID using the form-specific prefix shown in the guidance (for example EI.CUSTOM.001) so that the new requirement can later be added to the mapping registry.

- **Preserve semantic distinctions even when the source data do not.** In particular, keep separate: the information used as evidence; how that information was semantically aligned or grounded; how it was interpreted as evidence; confidence in extraction/alignment; scientific evidence strength; overall confidence in a claim; and downstream retrieval/encoding provenance. If a source field conflates several of these, say so rather than silently assigning it to one category.

- **Use real examples whenever available.** For current-state examples, prefer actual records from the selected canonical source set. For desired-state capabilities that are absent from current canonical data, prefer real examples from allowed desired-state support sources. Preserve the source's native representation as closely as practical (for example, a table row, JSON/YAML object, or RDF triple). If an example is assembled across records/tables, label it **DENORMALIZED**; if it combines information from multiple sources, label it **COMPOSITE/ILLUSTRATIVE**. Do not fabricate values to make an example look complete.

- **Do not manufacture specificity.** Never invent identifiers, evidence types, workflows, agent names, confidence scales, interpretation rules, or provenance requirements to make a form look complete. Enter **Unknown**, **Not documented**, **Needs discussion**, or **Not applicable** where appropriate.

- **Treat lack of support carefully.** For [F1], if the relevant canonical artifact has been directly inspected and a capability is demonstrably absent, `N` may be appropriate. If the canonical source was not fully inspected or the documentation is incomplete, use `M` / Needs discussion rather than assuming `N`. For [F2], absence from current data does not imply the capability is undesired; use the allowed desired-state source set to determine whether there is affirmative support.

- **Identify meaningful variation within the project.** Do not assume that one workflow applies everywhere. Look for differences among claim types, data sources, human versus automated curation, or production versus experimental pipelines. Conversely, do not create separate claim types merely because their predicates differ if their evidence/provenance requirements are essentially identical.

- **Use the minimum number of Claim Types needed to expose EPC differences.** When many claim types share the same Evidence, Provenance, and Confidence requirements, group them appropriately. Split them when their evidence sources, interpretation approaches, provenance needs, or confidence models materially differ.

- **For Evidence Item Types, describe what the information is—not how it was obtained.** An experimental result remains an experimental result whether it was entered manually or extracted by an LLM. Human/AI extraction belongs primarily in provenance unless the manner of extraction changes the semantic nature of the information artifact.

- **For Evidence Interpretation, determine the actual unit of judgment.** Do not assume one Evidence Line per snippet, paper, or study. Determine whether the project assesses each item independently, groups multiple items into one argument, or performs nested/higher-order assessments. If this is unclear, flag it as an open question.

- **For Semantic Alignment Provenance, distinguish mapping from evidentiary reasoning.** Extraction, entity/relation recognition, grounding, normalization, and mapping source semantics into a structured representation are alignment activities. Deciding whether that aligned information supports or disputes a target claim is Evidence Interpretation.

- **For Provenance, distinguish the five layers explicitly.** Ask separately: how did the evidence information come to exist; how was its meaning aligned to structured semantics; how was it interpreted/reasoned over to generate knowledge; how was the resulting artifact encoded; and how was that encoded artifact later retrieved or transformed between systems.

- **Record disagreements and ambiguity rather than resolving them silently.** If documentation or project representatives appear to use a term inconsistently, or two sources imply different requirements, note the discrepancy and identify it as something requiring human review.

- **Prioritize requirements, not implementation details.** Capture what information the project needs to represent and why. Do not overfocus on the exact YAML shape, property name, database column, or current technical implementation unless it reveals an important semantic requirement.

- **Make proposed additions obvious.** If the agent thinks a requirement may be useful but cannot find evidence that the project actually needs it, put it in a clearly labeled *Suggested follow-up / Possible requirement* note rather than filling it in as a project requirement.

- **Preserve traceability to source material.** For every substantive requirement, retain the relevant Resource Inventory Source ID(s) and, where useful, representative Example ID(s). [F1] conclusions should trace to the selected current-state canonical source set. Broader [F2] conclusions should trace to allowed desired-state support sources. [F1]/[F2] support should be captured in [F3] Basis for F1 Response and [F4] Basis for F2 Response **and** summarized in the self-contained [F5] Explanation / Considerations field, not merely in private drafting notes.

- **End with unresolved questions for the project representative.** After populating the forms, generate a short list of the highest-value uncertainties that need human confirmation—for example, “Is evidence strength actually authored or intended to be derived?” or “Are multiple publication excerpts normally treated as independent arguments or grouped by study?”

- **Treat the completed form as a draft until a project representative validates it.** AI assistance should reduce the burden of requirements collection, but the agent should not present inferred requirements as authoritative project decisions.

**As a general rule, a partially completed form with clearly marked unknowns is preferable to a fully populated form containing inferred or invented project requirements.**

Finally, requirements-completion agents should produce **two outputs**:

1. **The populated requirements workbook**, preserving the supplied workbook structure and formatting. Use a filename of the form `[PROJECT]_Requirements_v[VERSION]_[YYYYMMDD]_[HHMM].xlsx` (24-hour `HHMM`, with no colon).

2. **A Requirements Review Memo**, named `[PROJECT]_Requirements_Review_Memo_v[VERSION]_[YYYYMMDD]_[HHMM].md`, containing:
   - the selected project scope;
   - the exact current-state canonical source set used for [F1];
   - the broader desired-state supporting-source set used for [F2];
   - relevant source versions/releases/commits;
   - high-confidence conclusions;
   - fields or answers requiring human review;
   - conflicting or missing information;
   - inaccessible resources, if any;
   - important assumptions;
   - the highest-value unresolved questions; and
   - a small set of representative examples from both canonical current-state sources and, where they reveal additional requirements, broader desired-state sources.

The memo should make it possible for the project representative to see **why** current-state and desired-state answers differ without auditing every workbook cell.

---

# II. Key Concepts and Terminology

Below we define and share preferred names for several foundational concepts where a shared understanding will be useful in this modeling requirements collection effort. Project representatives should understand the meaning of and distinctions between these concepts, and use the recommended terminology in describing their data and requirements.

### “Statements” (as “Claims” vs “Concept Definitions”)

> **Description:** An information artifact that expresses a proposition, hypothesis, or judgment about the world. A Statement may be an assertion which states a purported fact about our objective reality, or a more subjective judgement or definition that is offered from a particular point of view, but not grounded in an objective, provable reality.
>
> In our work we are concerned with **two high level kinds of Statements**: Claims and Concept Definitions. It is important to define and distinguish these two types of Statements because it represents a fundamental divide across the statements reported by projects in our consortium, which may require different handling or levels of representation. Both may be assessed using these EPC requirements forms when evidence, provenance, interpretation, or confidence is applicable.

- **“Claims”:** put forth propositions about how entities in the domain of discourse relate or behave, and that can in principle be evaluated for truth or validity.

  - **Examples:** “Variant X causes loss of function in Protein X”, “CFTR dysfunction contributes to the pathophysiology of cystic fibrosis.”

  - Claims of this kind commonly have associated evidence and confidence assessments in resources such as the Monarch KG, Translator, and DisMech. Concept-definition statements can also be assessed when a project treats names, definitions, synonyms, classifications, or mappings as claims supported by source information or subject to confidence judgments.

  - Note that a particular claim is defined/identified by both its “proposition” (the inherent meaning of what it is putting forth as true), and the occasion on which it is made (when and by whom it was put forth). If two curators put forth the same proposition that “Variant X causes loss of function in Protein X”, these are separate Claims instances because they were made by different people on different occasions.

- **“Concept Definitions”**: characterize terms or concepts that refer to entities in the domain of discourse - e.g. assign names, definitions, identifiers, or synonyms to concepts, place them into a hierarchical classification, or provide mappings between terms representing them.

  - **Examples:** “The string xxx is the preferred name for the concept of yyy”, “The term xxx is defined as yyy”, “The name xxx is a synonym of the term yyy “, “The concept xxx is a subtype of the concept yyy.”

  - Such ‘definitions’ represent **expert** but ultimately **subjective** opinions about the best way to define or name a concept - they are given from a particular point of view but not grounded in an objective, provable reality.

  - Concept Definitions are most often reported in ontologies and other terminological artifacts such as Mondo. They typically have provenance and rationale describing why a particular naming, classification, or mapping decision was made. Their assessment can differ from empirical claims, but they are **not excluded** from EPC requirements collection. Use the Claim Type, EIT, EINT, and PROV forms to capture applicable evidentiary support, curation provenance, confidence, review, and interpretation requirements for names, synonyms, definitions, classification, and mappings. Preserve the project’s actual semantics; do not presume that every terminological judgment has an EvidenceLine.

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
> Evidence can also be relevant to concept-definition statements—for example, an external terminology record that corroborates a synonym or a classification source used to evaluate a subclass placement. Whether a source is evidence, origin provenance, or both depends on how it is used in the particular judgment.

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
> Confidence may apply to empirical claims **and** concept-definition statements, such as confidence in an equivalence mapping, synonym assignment, or subclass placement. Distinguish confidence in semantic alignment from confidence in the statement being asserted.

### “Agent”

> **Description:** An autonomous actor that participates in an activity or process, often in pursuit of an intended outcome. In this document, an Agent may be a person, organization, software program, or AI system. Where relevant, the specific type of Agent will be stated explicitly (for example, *human*, *organization*, *software agent*, or *AI agent*).
>
> **Example 1:** A clinical scientist or expert panel interpreting functional-assay results for a variant to determine whether they support its pathogenicity..
>
> **Example 2:** An AI curation agent extracting and interpreting mechanistic evidence from literature, and a human curator who reviews and validates the result.

### “Provenance”

> **Definition:** Information about the origins and history of data or knowledge artifacts, including the processes, inputs, agents, and transformations involved in their creation, interpretation, curation, retrieval, or modification.
>
> Provenance applies to both empirical claims and concept-definition statements. The applicable provenance layers depend on the record and workflow; use the same framework to elicit the types needed for a given project without assuming every layer applies.
>
> Below, we make an explicit distinction between five ‘levels’ of provenance relevant to Claims encoded in biomedical knowledgebases. It is important to understand these levels, as they **provide a framework for understanding and collecting EPC requirements** in the forms that follow.

#### Five Levels of Provenance

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

The `Requirements_Collection_Forms.xlsx` workbook contains **Project Overview (PO), Claim Type (CT), Claim Representation Structure (CRS), Reified Claim Semantics (RCS), Evidence Item Types (EIT), Evidence Interpretation (EINT), Provenance Types (PROV), and Claim–Evidence Matrix (CEM)** worksheets. Work within the selected project scope and reviewed Resource Inventory. The respondent-facing definitions below reflect the worksheet’s field order; every numbered field is shown with its bracketed identifier.

## General conventions for completing every form

- **Y / N / M:** `Y` = Yes, `N` = No / not established in the assessed scope, `M` = Maybe / needs discussion. For an [F1] `N`, say whether absence was demonstrated or the capability was not established from the inspected canonical set; do not claim definite absence from an incomplete inspection. For [F2], `Y` and `M` require project-specific support from allowed desired-state resources. An `M` must identify both the affirmative indication and the unresolved issue. A desired capability is not established simply because an agent thinks it useful.
- **[F1] and [F2] are independent.** An existing feature is not automatically a desired feature, and a missing [F1] feature is not automatically desired. A target redesign may intentionally retire current features. Distinguish documented intent from conjecture.
- **Support versus scientific evidence:** use *support*, *basis*, *source*, *rationale*, and *justification* for what substantiates form assessments; reserve *evidence* for the domain information bearing on claims or concept-definition statements.
- **Source citations:** identify Resource Inventory Source IDs, release/commit, document section or record key, and relevant access limitations. The chosen canonical [F1] source set must be verified. Never silently upgrade a live website, intermediate artifact, or external documentation example to canonical current-state data.
- **Basis fields:** In the assessment sheets, [F3] Basis for F1 Response gives a concise, traceable [F1] rationale. [F4] Basis for F2 Response gives the corresponding [F2] rationale, with maturity/commitment and uncertainty when relevant. For [F2] `Y` or `M`, start with the applicable maturity designation where a controlled vocabulary has been defined (for example *Exploratory*, *Proposed*, or *Established*), then give source support; for `M`, explain what prevents `Y`. The column header itself does not impose a new controlled vocabulary.
- **Complete explanations:** [F5] Explanation / Considerations must be sufficiently detailed and self-contained to explain both [F1] and [F2] judgments, applicability, source fields, semantic distinctions, qualifiers, limitations, process granularity and unresolved questions. It is fine—and often helpful—to repeat supporting information already summarized in [F3], [F4], or other columns.
- **Concrete examples:** where a worksheet asks for examples from your data, give a short explanation, a minimal snippet of actual source-native fields and values when available, and a source/record reference. Clearly label schematic examples; invented or composite values are never proof of [F1]. Link to a larger memo example (EX01, EX02, etc.) for a complex record.
- **Required and optional:** `(r)` is required and `(o)` is optional; `(r*)` is conditionally required according to the corresponding definition. Complete optional fields when relevant; do not fill them with speculative mappings.
- **Preserve forms and downstream boundaries:** Do not change predefined Requirement IDs or the informational `SEPIO Mapping Summary` cells. Use stable IDs for any allowed `Other` rows. The later Requirements → SEPIO mapping stage is separate from requirements elicitation.

## 1. Project Overview Form (PO)

**Purpose.** Provide concise project-level context: the project’s scope, its main data and use cases, and why representing evidence, provenance and confidence matters. Use canonical sources for current-state descriptions and approved project materials for future goals; distinguish them clearly.

### Field dictionary (worksheet order)

- **Project Name (r):** The official name of the project/resource.
- **Representative(s) (r):** People contributing or validating the requirements on the project’s behalf; do not invent names.
- **Description (o):** The project’s purposes, major datasets, kinds of claims or concept-definition statements, workflows, consumers, and known current/future distinctions. Keep this an orientation, not a substitute for the detailed form rows.
- **Evidence/Provenance Needs (o):** Why EPC representation is needed, the primary use cases, and important known limitations. Include concept definitions, synonyms, classification and mapping judgments when they are in project scope.

## 2. Claim Type Form (CT)

**Purpose.** Identify the main kinds of statements whose semantics or EPC needs differ. These may include empirical/domain claims **or** concept-definition statements (such as synonym, subclass, mapping, and naming assertions) when the project evaluates, supports, or curates them. The goal is a useful number of Claim Types, not exhaustive enumeration of every predicate.

**Defining a Claim Type.** Describe its **subject category → relationship type → object category**, with contextual qualifiers as needed. For example, `Drug — treats — Disease`, `Disease — has phenotype — Phenotype`, or `Ontology term — is subclass of — Ontology term`. Combine related types only when their EPC requirements are substantially the same; split them where evidence sources, interpretation, provenance, or confidence differ. A small project may list closely related types separately for clarity, while a project with many predicates may group several subject/object categories or relationships under one Claim Type when their EPC needs are similar. For example, an NLP resource might group `Gene/Chemical — causes/interacts_with/affects — Gene/Chemical` statements if they share the same evidence and provenance patterns. Avoid both one-row-per-predicate proliferation and broad groupings that conceal genuine EPC differences. Preserve source vocabulary, even if a relationship is expressed by multiple domain-specific fields. The form includes removable example Claim Types; replace them with project types.

### Field dictionary (worksheet column order)

- **Identifier (r):** Stable project Claim Type reference, usually `C001`, `C002`, etc. These are **not** requirement IDs and do not directly trigger SEPIO mappings.
- **Descriptor (r):** Short, interpretable name, e.g., `Disease–Phenotype Association`, `Synonym Assignment`, `Variant–Drug Response`.
- **Subject Category(ies) (r):** One or more source-relevant subject categories; separate multiple categories with semicolons. Use the narrowest useful distinctions without gratuitous fragmentation.
- **Relationship Type(s) (r):** The relationship(s) asserted (e.g., `has phenotype`, `causes`, `is synonym of`, `subclass of`). Semicolon-separate multiple values; distinguish proposition semantics from record encoding.
- **Object Category(ies) (r):** Object categories for this type, with the same granularity guidance as subjects.
- **Qualifying Information (o):** Context that refines the proposition, such as disease context, population, anatomy, severity, frequency, evidence modality, or validity interval. Do not confuse a qualifier with the object merely because a project stores both in adjacent fields.
- **Example Claim(s) from Your Data (r):** Actual human-readable example statements, ideally drawn from canonical project records. Include a source-native phrase and, where helpful, indicate how domain fields encode the assertion. Keep examples representative rather than invented.
- **Link(s) to Example Record(s) (o):** One or more labeled, traceable references to records of the type: `Web UI: …`, `API/query: …`, `Dataset/release: …; record ID: …`, `Documentation: …`. Prefer records corresponding to the preceding example claims, but another type-matched record is acceptable. A general portal link is not a substitute for a specific record pointer; do not invent endpoints.
- **Evidence/Provenance Notes (o):** State the evidence, interpretation, provenance, and confidence information the project wants represented *for this Claim Type*, explaining meaningful type-specific differences. This is not just the information a curator might have consulted internally.
- **Additional Notes (o):** Other limitations, terminology nuances, differences across subtypes, decision questions, or future intentions.

### Short populated example (column order)

| Identifier | Descriptor | Subject Category(ies) | Relationship Type(s) | Object Category(ies) | Qualifying Information | Example Claim(s) from Your Data | Link(s) to Example Record(s) | Evidence/Provenance Notes | Additional Notes |
|---|---|---|---|---|---|---|---|---|---|
| C001 | Disease–Phenotype Association | Disease | has phenotype | Phenotype | Frequency; severity | Cystic fibrosis has phenotype chronic respiratory infection | Dataset/release and record ID to be supplied for the actual project | Capture authoritative source and relevant support; specify whether frequency is a proposition qualifier | Illustrative pattern only, not a verified record |

When claim types span several categories, additional semicolon-separated subject, relationship and object values are appropriate provided EPC requirements remain similar.

## 3. Claim Representation Structure Form (CRS)

**Purpose.** Record **how claims are packaged or embedded** in project data, separately from what the propositions mean. A project may represent some claims as parent-record slot/value pairs, others as nested records, reified Statement objects, or graph edges. Several rows may be selected. The source structure need not be preserved in the desired SEPIO-based representation unless the project actually requires that form; document this in [F5].

### Field dictionary (worksheet column order)

**Prepopulated informational fields**

- **Requirement ID:** Fixed `CS.*` identifier for each structural pattern; do not change. If an `Other` structure is needed, create a stable project-specific ID such as `CS.CUSTOM.001`.
- **Claim Representation Structure:** Names the predefined packaging pattern being evaluated.
- **Description:** Defines what the representation physically/structurally looks like and what surrounding context supplies.
- **Illustrative Example(s):** Schematic examples to orient the respondent, not mandatory syntax.
- **General Utility / Implications of this Structure:** Explains typical addressability, metadata, and transformation implications; not itself a project requirement.

**Respondent fields**

- **[F1] Used in Current Data? (r):** Enter `Y`, `N`, or `M` for the specified structure in the canonical source. Assess every row independently; give [F3] support.
- **[F2] Desired in SEPIO-based Data? (r):** Enter `Y`, `N`, or `M` for genuinely desired representation. A current parent slot/value may be transformed to a reified Statement if project support favors that design. Do not select an approach merely because SEPIO supports it.
- **[F3] Basis for F1 Response (o):** Give concise canonical schema/record examples, identifiers, locations, and inspection limits that justify [F1].
- **[F4] Basis for F2 Response (o):** State the project-specific basis for [F2], relevant maturity or design status, and, for `M`, the unresolved choice about preserving versus transforming the source structure. Cite sources.
- **[F5] Explanation / Considerations (o):** Provide a self-contained account of which Claim Types use the structure, what is implicit in parent context, whether qualifiers and metadata can be attached, and the rationale for both judgments. Explicitly state whether the original packaging **must be preserved** in the SEPIO-based representation or **may be transformed** into a different structure that preserves the proposition semantics. For example, a direct knowledge-graph edge might become a reified Statement so evidence and provenance can be attached; if retaining an edge-based shape is itself required, explain the project-specific basis. Distinguish a source implementation convention from a genuine future representation requirement.
- **SEPIO Mapping Summary (informational):** A downstream reference only. Do not populate or use it to justify a requirement.

**Pattern examples.** A parent record property (`disease: {phenotype: ...}`) differs from a nested claim object with its own fields, a first-class association with its own identifier, and an RDF subject–predicate–object edge. More than one pattern may apply to different Claim Types. Select `M` rather than guessing when the intended future packaging is unresolved.

## 4. Reified Claim Semantics Form (RCS)

**Purpose.** Use this conditional form when the project represents or may need first-class **reified Claim/Statement objects**—including reified prior claims that serve as Evidence Items. A reified Statement can carry text, explicit structured proposition semantics, qualifiers, evidence, provenance and confidence. If [F2] for reified claim structure is `M` in CRS, complete this form provisionally or defer it, explaining the dependency. RCS describes *semantic content*; CRS describes *packaging*.

Two direct-on-Statement patterns are distinguished **by how semantic roles are identified by attributes**: domain-specific attribute names versus generic SPO role names. A third pattern places structured SPO information in a separate Proposition object. The patterns are independently assessable; do not select them merely because the model permits them.

### Field dictionary (worksheet column order)

**Prepopulated informational fields**

- **Requirement ID:** Stable predefined `RCS.*` semantic requirement ID; do not modify.
- **Claim Semantic Requirement:** The particular semantic capability to assess.
- **Description:** Definition of that capability, including where the core proposition is represented.
- **Illustrative Example(s):** Source-independent example of the capability, not a requirement to adopt the example’s vocabulary.
- **General Utility / Modeling Implications:** Describes why the pattern matters and possible later modeling consequences, not a substitute for project-specific need.

**Respondent fields**

- **[F1] Used in Current Data? (r):** Judge whether current canonical records actually represent this semantic capability, including implicit domain conventions. Cite support in [F3].
- **[F2] Desired in SEPIO-based Data? (r):** Independently judge the supported future need. Generic SPO representation is **not automatically required** when existing domain-specific fields can be interpreted as SPO.
- **[F3] Basis for F1 Response (o):** Refer to source-native attributes, record types or documentation supporting the current assessment, including necessary inference rules.
- **[F4] Basis for F2 Response (o):** State documentary/design support for future representation, its maturity, and what is unresolved for an `M` judgment.
- **[F5] Explanation / Considerations (o):** Explain comprehensively which direct or nested semantic carrier applies, how the proposition is reconstructed, qualifiers, constraints, and differences between [F1] and [F2]. Explicitly mention relevant project claim types.
- **[F6] Relevant Claim Type IDs (o):** List CT identifiers such as `C001; C004` to define applicability; no SEPIO class IDs here.
- **SEPIO Mapping Summary (informational):** Read-only for requirements collection; later modeling use only.

### Interpretation of the predefined rows

- **`RCS.FREE_TEXT` — Human-Readable Claim Text:** A natural-language statement, alone or alongside structured semantics.
- **`RCS.STRUCTURED_STATEMENT_DOMAIN_ATTRIBUTE_NAMES` — Structured Claim Semantics using Domain-Specific Attribute Names:** Proposition held directly on a Statement through domain-specific fields. The subject/object roles follow attribute meanings; the relationship can appear in a dedicated attribute or be derived from several fields and their values.
- **`RCS.STRUCTURED_STATEMENT_SPO_ATTRIBUTE_NAMES` — Structured Claim Semantics using Generic SPO Attribute Names:** Proposition held directly on a Statement using attributes explicitly designating subject, predicate and object roles, regardless of domain. The names need not literally be `subject`, `predicate`, `object` if the generic roles are clearly designated.
- **`RCS.STRUCTURED_PROPOSITION` — SPO Semantics in Nested Proposition:** The Statement references a separate Proposition object that carries the structured meaning.
- **`RCS.QUALIFIERS` — Qualifying / Contextual Information:** Context added to the selected semantic carrier(s), such as disease, anatomical location, population or frequency.

**Paired examples representing the same proposition (schematic):**

```yaml
# Domain-specific Statement attributes
Statement:
  gene: HGNC:1884              # Subject role inferred from attribute meaning
  association_type: causal     # Relationship encoded via domain-specific attribute
  disease: MONDO:0009061      # Object role inferred from attribute meaning
```

```yaml
# Generic SPO Statement attributes
Statement:
  subject: HGNC:1884
  predicate: biolink:causes
  object: MONDO:0009061
```

A more complex predictive clinical relationship can be encoded via `molecular_profile_id`, `therapy_id`, `disease_id`, `evidence_type` and `clinical_significance`; translating that example to generic SPO may produce `subject: MP123`, `predicate: predicts_sensitivity_to`, `object: CIViC-T123`, with `disease_context: DOID:3908`. This is schematic: the relationship is inferred from **multiple** fields and disease serves as context *for this claim formulation*, not universally.

## 5. Evidence Item Type Form (EIT)

**Purpose.** Identify information artifacts and source content represented or desired **as evidence** for target statements—including concept-definition statements when relevant. Assess individual **Evidence Item Type** rows, not group labels. The listed groups form a respondent-friendly inventory of different levels of granularity (measurements, statistical metrics, study results, publication passages, documents, structured prior claims, external records, etc.), **not** a proposed SEPIO class hierarchy. An external database record may also qualify as a structured prior claim; indicate such overlapping interpretations in [F5].

**Boundary:** An evidence item is information that may be assessed; an EvidenceLine is an interpretation of one or more items *relative to a proposition*. Do not treat every publication or database record as an EvidenceLine. Documents may be sources containing specific evidentiary information even where the project tracks them as coarse evidence references.

### Field dictionary (worksheet column order)

**Prepopulated informational fields**

- **Requirement ID:** Fixed `EI.*` identifier for the specific evidence item type. Do not edit. Use `EI.CUSTOM.001`, etc., for genuinely new project-specific rows.
- **Evidence Item Group:** Navigation/category label; not itself a requirement to answer.
- **Evidence Item Type:** Name of the specific type being assessed, e.g., experimental measurement, study result, text passage or external record.
- **Description:** Defines the item’s informational nature independently of how it was extracted or imported.
- **Illustrative Example(s):** Orientation examples, not evidence that the project represents the type.

**Respondent fields**

- **[F1] Represented in Current Data? (r):** `Y/N/M` for whether the canonical source actually represents or identifies this type as evidence-bearing information. Citation or use in an unrecorded internal workflow does not alone establish that it is represented in project data.
- **[F2] Desired in SEPIO-based Data? (r):** Independently assess supported desired representation of the item type; use broader project sources allowed for [F2], without presuming all potentially useful types are desired.
- **[F3] Basis for F1 Response (o):** Brief canonical source references, types, records, attribute names and inspection boundaries supporting [F1]; distinguish direct source records from source documentation.
- **[F4] Basis for F2 Response (o):** Brief source-based future requirement rationale, maturity and unresolved uncertainties where relevant. [F2] `Y` or `M` needs identifiable affirmative project support; an `M` also needs a specific open question.
- **[F5] Explanation / Considerations (o):** Give a detailed, self-contained explanation of how this item type is represented and used, the rationale for both [F1] and [F2], and why the project does or does not need to represent it. Describe important granularity distinctions, overlap with other Evidence Item Types, qualifiers, applicable claims, whether the item is retained locally or merely cited/referenced, limitations of current representations, and differences between current and desired forms. Include the meanings of relevant source fields where useful, even if repeated in [F3], [F4], [F6], or other focused fields. Do not shorten this field merely to avoid intentional duplication.
- **[F6] Relevant Source Data Elements (o):** Concise inventory of **existing [F1]** classes, fields, record types or concepts with brief source-native definitions. For example, `class: ClinicalEvidenceItem — interpreted publication-linked evidence record`; `attribute: rating — curator-assigned quality value`. Do not list speculative future fields. This identifies **existing** source elements; it is distinct from the desired attributes requested in [F11].
- **[F7] Example(s) from Your Data (o):** Briefly describe a relevant item and provide a compact source-native snippet with actual field values and a traceable source ID/record where possible; label schematic future examples. If the full record is large, reference an identified EX## example in the Review Memo. Explain what the snippet illustrates instead of providing raw syntax alone.
- **[F8] Desired Evidence Item Location (r):** Indicate **where instances of this Evidence Item Type need to be represented or maintained** in the project's desired data ecosystem. Select all applicable workbook codes, separated by semicolons:
  - **`LOCAL` — In project data ecosystem:** Some representation of the item is maintained in a project-controlled dataset or resource. It may be full structured content, free text, a metadata/proxy record, or a locally stored artifact.
  - **`EXTERNAL` — Referenced by external ID/URL:** The authoritative or fuller item representation exists outside the project and is referenced by a resolvable identifier or URL; the complete content need not be copied locally.
  - **`UNSURE` — Needs discussion:** The desired location or the division between local and external representations remains unsettled.
  Select both `LOCAL` and `EXTERNAL` when the project keeps a local summary/record and also links to its external source—for example, a structured account of publication findings linked to the publication by PMID or DOI. This field concerns **desired representation location**, not where a curator encountered the item or how it was retrieved; the latter are primarily provenance questions.
- **[F9] Desired Local Representation Form (r\*):** **Required when [F8] includes `LOCAL`.** Indicate **how the item should be represented within project-controlled data**. Select all applicable workbook codes, separated by semicolons:
  - **`FREE_TEXT` — Free-text representation:** Information about or from the item appears in natural-language text, without distinct structured fields for its substantive content. *Example:* A DisMech passage says chloride transport was reduced by 42%, but the measured property, value and unit are not encoded as separate attributes.
  - **`STRUCTURED_METADATA` — Structured metadata/proxy:** A structured record identifies, describes or links the item but does not itself encode the substantive evidentiary information it conveys. *Examples:* A Figure object contains `figure_number`, `caption`, `publication` and `url`, but not the image or results depicted; a Dataset catalog record contains `title`, `accession`, `creator` and `url`, but not the observations.
  - **`STRUCTURED_CONTENT` — Structured item content:** The substantive information or values in the item are separately modeled as structured fields. *Examples:* A measurement stores `value: 42`, `unit: percent_reduction` and `confidence_interval`; a structured prior claim stores subject, relationship, object and qualifiers.
  - **`STORED_ARTIFACT` — Artifact stored or managed locally:** The item itself (for example a figure image, PDF, data table or other file) is held by or directly managed within the project, rather than merely referenced or described.
  - **`UNSURE` — Needs discussion:** The intended local representation is not yet established; describe the question in [F4] and [F5].
  These options **can coexist**: a project may store image metadata plus the image itself, or a textual summary alongside structured content. In particular, **structured metadata describing an artifact does not necessarily structure the evidentiary content that artifact conveys**. Explain significant combinations or ambiguities in [F5].
- **[F10] Individual Addressability Needed? (r):** Decide whether **individual instances** need to be distinctly identifiable/addressable so they can be independently referenced or linked to provenance, confidence or evidence interpretation. Select one workbook value:
  - **`YES`:** Individual instances require separate identity/addressability; an interpretation or metadata record can point to that specific item.
  - **`NO`:** The item need only be present or referenced within a larger container; individual addressability is not required.
  - **`NO_SPECIFIC_REQUIREMENT`:** No explicit project requirement for separate addressability is established, or it remains unspecified.
  *Example:* A project may cite a publication by PMID without separately identifying its figures. If it needs to record that **Figure 3B specifically** supports a proposition, with figure-specific interpretation or provenance, the figure may need its own addressable identity. Addressability is a **logical modeling capability**, not a requirement for a separate database table or physical file. Explain subtype-dependent differences in [F5].
- **[F11] Evidence Item Attributes to Represent (o):** Identify **intrinsic, non-provenance properties** that the project's **desired** representation should capture explicitly. These describe the item's content, characteristics or informational meaning, especially information not already asked about in PROV. Typical examples by type:
  - **Scientific Publication:** title, publication year, journal, authors.
  - **Experimental Measurement:** measured value, unit, reference range, confidence interval, detection limit.
  - **Statistical Metric:** metric type, value, confidence interval, p-value threshold or significance interpretation.
  - **Computational Prediction / Score:** predicted outcome, score, classification, scale/range, interpretation threshold.
  - **Figure:** figure number/label, caption, panel identifier.
  - **Structured Prior Claim:** subject, predicate/relationship, object, qualifiers.
  Distinguish intrinsic information from **how an item was produced, extracted, curated, transformed or retrieved**, which typically belongs in PROV. For example, `journal` can be a bibliographic attribute of a publication, while the software version used to extract a result is provenance of the extraction activity. Some attributes have mixed significance; explain such cases in [F5] rather than forcing a false boundary. **[F11] specifies attributes desired in the future representation; [F6] names attributes already present in existing source data.**
- **[F12] Specific Kinds of this Item Type (o):** Describe meaningful subtypes of the broad Evidence Item Type that occur in the project's data **or** should be supported in its desired representation. Use familiar project terminology; a formal taxonomy is not required. For example:
  - **Experimental or Observational Data Items:** in vitro and ex vivo measurements, cell counts, flow-cytometry/FACS measurements, protein-expression measurements, cell-line survival times.
  - **Statistical Metrics:** p-values, z-scores, odds ratios, confidence intervals, chi-square statistics for concept co-occurrence in medical records.
  - **Computational Predictions / Scores:** variant-pathogenicity scores, drug-sensitivity predictions, protein-structure confidence scores.
  - **External Data Records:** ClinVar variation records, DrugCentral drug records, dbGaP study or phenotype records.
  - **Documents, Images, Datasets and Study Results:** project-specific kinds such as research publications, clinical reports, microscopy images, sequencing datasets or clinical-study outcomes.
  List **kinds, not individual instances or an exhaustive taxonomy**. Note distinctions that affect information content, attributes, provenance, representation or possible SEPIO modeling in [F5] and, where relevant, [F11].
- **[F13] Relevant Claim Types (o):** List relevant CT identifiers, separated by semicolons, e.g. `C001; C003`. An item type may be relevant only to particular claim types or may be interpreted differently depending on the target proposition; explain those differences in [F5]. Do not assume an Evidence Item Type applies to every Claim Type merely because it is present in project data.
- **SEPIO Mapping Summary (informational):** Do not edit or use to determine which evidence types the project requires. Informational text may be updated later through the separate registry workflow.

**Example of a suitable [F7] cell (schematic; not evidence of current [F1]):** “Curation quality attached to a literature-derived evidence record: `EvidenceItem: {rating: 4, evidence_level: B}`. Source: project evidence documentation, record/example ID if verified.” The actual completed form should use the source's real names and values whenever available.

## 6. Evidence Interpretation Form (EINT)

**Purpose.** Identify what the project represents or needs about **how one or more Evidence Items bear on a target proposition**: direct links, interpreted direction and strength, grouping/granularity, conflicting evidence, and higher-order synthesis. This can support empirical claims or concept-definition statements, depending on the project.

**Interpretation boundary.** A source publication or record is not automatically an interpreted EvidenceLine. An EvidenceLine is an argument assessing its inputs relative to a specific target proposition. One line might interpret one snippet or several evidence items; it may also refer to lower-level EvidenceLines. `EINT.GRANULARITY` includes how items are grouped **within** one line. Synthesis of several lines into a higher-level Assertion is different.

### Field dictionary (worksheet column order)

**Prepopulated informational fields**

- **Requirement ID:** Fixed `EINT.*` row identifier; do not modify.
- **Topic:** Names the evidence-linking or interpretation feature.
- **Question:** The exact respondent-facing requirement, including any conditional phrasing.
- **Illustrative Example Responses/Explanations:** Examples of the kinds of answers expected, not definitive modeling prescriptions.

**Respondent fields**

- **[F1] Represented in Current Data? (r):** Assess whether the specified linking, interpretation or synthesis information is present in canonical records, as opposed to an inferred internal curator activity with no stored representation.
- **[F2] Desired in SEPIO-based Data? (r):** Record the independently supported project need for the feature. `M` requires a credible project indication and a well-identified unresolved question.
- **[F3] Basis for F1 Response (o):** Reference the observed record structures, fields, source release and relevant examples that substantiate [F1]. Distinguish direct linking from actual interpreted direction or strength.
- **[F4] Basis for F2 Response (o):** Record the documented/proposed basis for [F2], maturity where relevant, and uncertainty or alternative patterns for an `M`.
- **[F5] Explanation / Considerations (o):** Explain, independently of other cells, the unit of judgment, applicable Claim Types and Evidence Item Types, how direction and strength are determined, grouping criteria, conflict handling, higher-order reasoning, and [F1]/[F2] rationale.
- **[F6] Relevant Source Data Elements (o):** Short source-native names and definitions of **existing** interpretation-related fields, entities or combinations; distinguish an explicit strength field from a score inferred from several fields.
- **[F7] Example(s) from Your Data (o):** A representative small source-data snippet showing a relationship between assessed items and target claim and, where present, direction/strength. Include source ID and record locator; label synthetic examples as schematic.
- **SEPIO Mapping Summary (informational):** Only for subsequent mapping; do not edit or use as input to EPC assessment.

### Guidance for the specific EINT requirements

- **`EINT.REQUIRED`:** Whether the project must capture interpretation of information relative to a target claim at all. Direct evidence links and richer explicit EvidenceLines need not be equivalent; examine downstream rows independently even if interpretation is lightweight.
- **`EINT.DIRECTION`:** Whether evidence supports, disputes or is neutral toward a specified claim; distinguish scientific direction from confidence in extraction quality.
- **`EINT.CATEGORICAL_STRENGTH`:** Qualitative or ranked strength **of an EvidenceLine relative to its target proposition**, rather than record-quality grades or final assertion confidence.
- **`EINT.NUMERICAL_STRENGTH`:** Numeric strength/score for the interpreted contribution of evidence to a proposition; do not automatically include an overall claim score or curation queue rank.
- **`EINT.GRANULARITY`:** Define whether an EvidenceLine assesses individual items, groups several items by study/publication/source/context, or uses other grouping rules, and state the **criteria** for each group. For example, consider two projects extracting disease–phenotype associations from publications: one assigns direction and strength separately to each extracted passage; the other combines passages from the same study into one EvidenceLine and assesses their joint contribution. Both are possible; report which occurs or is desired in the project. **Grouping items within one EvidenceLine is different from synthesizing multiple EvidenceLines into a higher-level Assertion.**
- **`EINT.CONTRADICTION`:** Representation of both supporting and disputing evidence in the project’s final interpretation; do not assume it includes every kind of incompatible alternative proposition.
- **`EINT.STACKING`:** Whether one EvidenceLine can be treated as input to a higher-order line and which distinct granularity/aggregation levels result.

**Application example (schematic):** A project reads two separate passages from one study and assigns one study-level EvidenceLine to evaluate their joint support for a synonym assertion. [F5] should explain why they are grouped (same underlying source/study), whereas [F7] can show the two passage IDs and the one interpreted conclusion. The same paper appearing in multiple databases does not automatically create independent lines.

## 7. Provenance Types Form (PROV)

**Purpose.** Identify provenance, method, review, quality and confidence information represented or desired at different levels of the workflow. Apply these to empirical and concept-definition statements where relevant. Do not assume a provenance type must be captured merely because a process occurred outside the project’s desired representation.

**Provenance layers.** Evidence Item (how source information came to exist); Semantic Alignment (extraction, grounding, normalization and semantic mapping); Evidence Interpretation (how items were judged relative to a proposition); Assertion (how claims were accepted or synthesized); Encoding (how records were serialized); Retrieval (how existing encoded representations were fetched/transferred/transformed). Layers are contextual, not automatically required everywhere. Provenance may be attached to individual records, datasets/releases, pipeline runs, activities, or retrieval events; identify which granularity is relevant.

**Semantic boundaries.** Evidence Item **quality** assesses reliability/quality of the input information; evidence **strength** concerns its contribution to a proposition (EINT); semantic-alignment **confidence** concerns whether extracted/grounded meaning is correct; assertion **confidence** concerns the claim or conclusion. A source record can be provenance for *where an item originated* and, separately, scientific evidence when its content is assessed as support for a proposition. The distinctions belong in [F5] even if native fields conflate them.

### Field dictionary (worksheet column order)

**Prepopulated informational fields**

- **Requirement ID:** Stable `PROV.*` identifier for each provenance requirement. Do not change or invent mapping triggers.
- **Provenance Level:** The level/entity/activity to which the provenance concept applies (Evidence Item, Semantic Alignment, Evidence Interpretation, Assertion, Encoding, Retrieval).
- **Provenance Area:** The topical category of provenance (e.g. Agent, Method, Resource, Date, Quality, Confidence, Review), not itself an F-numbered response.
- **Provenance Type / Question:** The particular question or item to evaluate at that level.
- **Description:** Defines the required information and distinctions; use this before interpreting an example.
- **Illustrative Example(s):** Sample values that orient the response; they do not establish the feature in the project.

**Respondent fields**

- **[F1] Represented in Current Data? (r):** Decide whether the canonical data explicitly stores or faithfully conveys the provenance/quality/confidence information. Distinguish dataset/release metadata from record-level or activity-level provenance, and observed fields from undocumented workflow practice.
- **[F2] Desired in SEPIO-based Data? (r):** Independently assess whether approved project materials show a need to represent this level/type. `M` needs some project-specific support, not just possible utility.
- **[F3] Basis for F1 Response (o):** Give concise source references, exact fields/events/record examples, applicable versions, and inspection caveats supporting the current-state judgment.
- **[F4] Basis for F2 Response (o):** Give project-specific future-design or requirements support, noting maturity, relevant uncertainty, and the precise resource basis; for `M`, explain the outstanding decision.
- **[F5] Explanation / Considerations (o):** Give a complete rationale for both judgments. Identify affected Claim Types, Evidence Item Types, datasets or processes; provenance granularity; method steps; agent roles; confidence/quality semantics; distinction between source and assessed evidence; and any limitations or unresolved issues. Do not presume applicability is universal. Repeat details from other fields when needed for a self-sufficient explanation.
- **[F6] Relevant Source Data Elements (o):** List actual [F1] classes/attributes/concepts and brief source-native definitions, e.g. `attribute: evidence_rating — curator-assigned 1–5-star assessment of quality of an Evidence Item summary`. Multiple fields may jointly encode a concept; do not propose target-model fields here.
- **[F7] Example(s) from Your Data (o):** Include a short contextual note, concrete source-native field/value snippet, and traceable record. Show the level where the provenance lives (item, claim, run, release, retrieval). Clearly label hypothetical illustrations and link to a full EX## memo example for complex chains.
- **SEPIO Mapping Summary (informational):** Not respondent-authored. Do not edit, or use old downstream mapping descriptions to infer the requirements.

### Interpretive notes for provenance areas

- **Evidence Item Provenance:** Describe creators, input resources, study/extraction methods, execution details, date/time, contextual location, and source-information quality when applicable. Keep upstream original-record provenance separate from a project-generated extraction artifact's creation provenance.
- **Semantic Alignment Provenance:** Describe extraction/recognition, grounding, normalization, correspondence method, target ontology or schema, agent and model versions, review, and alignment confidence; an accurate mapping does not by itself establish the truth of an asserted claim.
- **Evidence Interpretation Provenance:** Report who evaluated what information relative to which proposition, method/guideline, process, time, perspective, and assessment results. Do not mistake interpretation strength for information quality.
- **Assertion Provenance:** Describe how the final assertion was made or reviewed, using what rules or supporting arguments, by which agents, and at what time or version. Where a confidence score exists, distinguish authored/stated values from computed values. Project-specific policy/decision-history needs can be described in [F5] and flagged for later model mapping if the existing rows do not capture them.
- **Encoding Provenance:** Describe how an information artifact is expressed or serialized in a particular model, language or format when this is important to the project's representational requirements. Identify the encoding method or rules and their provenance **especially when an encoding decision changes the meaning, specificity or interpretation** of a statement (for example a cross-reference being emitted as an exact match). Different file formats alone do not automatically establish a requirement to preserve detailed encoding provenance.
- **Retrieval Provenance:** Describe movement of an **already encoded** record between systems: the immediate system it was retrieved from, the destination/consuming system, each system's role, the retrieval event/time, and transformations along the way. Distinguish the **original creator/source of the knowledge** from the **immediate provider of a retrieved representation**. A system may be an upstream source in one activity and a downstream target in another, so specify the particular retrieval event and direction. Describe any transformation or export rule that changes the meaning of the retrieved record, rather than treating transfer as a purely technical step.

**Cross-level example (schematic, not an observed record):** An AI agent extracts a quotation from a paper (Evidence Item creation and semantic-alignment provenance), resolves a disease term (alignment method/confidence), assesses whether the quote supports a subclass claim (Evidence Interpretation), and a curator accepts the assertion under a documented policy (Assertion Provenance). This illustrates why recording extraction confidence alone is not the same as recording confidence in the asserted subclass relationship.

## 8. Claim–Evidence Matrix Form (CEM)

**Purpose.** Produce **two project-specific matrices** on the existing CEM worksheet: one for **[F1]/current state**, one for **[F2]/desired state**. The matrices relate Claim Types (`C###`) to Evidence Item Types (`EI.*`) and complement—not replace—the detailed forms.

**How to complete.** Use the completed CT and EIT forms and project-specific source support. Determine relevant claim-type rows and evidence-type columns for **each** state before writing. Preserve all applicable identifiers, preferably in a comparable ordering across [F1] and [F2]. Populate `Y` for an established supported relationship, `M` where source-supported applicability requires discussion, and leave blank if no relevant relationship is identified. **Do not use `X`, `N`, or an unrelated illustrative matrix.** For negative or disputing evidence, explain the polarity in the associated forms or memo rather than inventing a new cell-value convention.

**Layout and validation.** The worksheet has designated [F1] and [F2] titles/areas, but no prepopulated example matrix. If more [F1] rows are needed than the allocated space (initially 24 Claim Type data rows), **insert rows above the [F2] title** to move the entire [F2] section safely; then size [F2] and the evidence-type columns as necessary. Preserve headings, cell content, styles, validations and any formulas. Confirm no rows/columns were truncated, no [F1] content overwrote [F2], and that every marked relationship has traceable project support. Do not mechanically copy [F1] cells to [F2]; assess the two separately.

# IV. Completeness and Consistency Check Before Submission

Before returning the completed workbook to the project representative, the agent should:

- check every required respondent-facing field;
- verify that controlled values use the labels defined in the workbook/guidance;
- verify that every [F1]/current-state conclusion is supported only by the current-state canonical sources/companions allowed by the selected scope;
- verify that every broader [F2]/desired-state conclusion is supported by an allowed desired-state source and not speculation;
- for each [F2] `Y` or `M`, verify [F4] Basis for F2 Response cites a project-specific source and explains the rationale; for each `M`, verify uncertainty is explicit;
- compare answers across forms for internal consistency;
- identify contradictions between project sources or between current-state and desired-state answers;
- identify required questions that remain unsupported or unresolved;
- make sure free-text explanations do not imply uncaptured requirements;
- verify that richer upstream-source information has not been incorrectly attributed to the project itself;
- verify that intermediate project artifacts have not been treated as current canonical data unless the selected scope explicitly includes them;
- verify that downstream/API/UI enrichments have not been treated as canonical project requirements unless the selected scope says otherwise;
- retain traceability to the Resource Inventory sources supporting non-obvious conclusions; and
- prepare the Requirements Review Memo described in the Core Behavioral Rules above, including its current-state project/dataset overview and form-by-form synthesis.

A partially completed workbook with clearly marked unknowns is preferable to a fully populated workbook containing inferred or invented requirements.

# V. What Happens After the Requirements Are Confirmed?

After a project representative reviews and confirms the completed requirements workbook, the requirements-to-model workflow applies the maintained Requirement → SEPIO Mapping Registry against the controlled responses and stable Requirement IDs. That later stage can generate a candidate SEPIO covering model and associated summary, traceability, follow-up, gap/extension, implementation-guidance, form-feedback, and generation-manifest artifacts.

During the current pilot phase, an AI agent may perform this later analysis and generation step. The confirmed workbook remains the formal project-requirements input; the selected scope and Resource Inventory provide traceable support for how those requirements were derived. The completed requirements forms should nevertheless remain requirements-first: **do not use the SEPIO Mapping Summary columns to decide what the project needs.**

Detailed downstream mapping, routing, and output-generation behavior is documented separately in the Requirement → SEPIO Mapping Registry/README and the Requirements-to-Model Report Specification.


## Agent feedback after requirements completion

After completing the requirements workbook and Review Memo, complete a project-specific copy of `Feedback_Log_Template.xlsx`. Record actionable observations about the forms, field wording, controlled responses, guidance, or workflow, using its `Agent Instructions` and `Controlled Vocabularies` tabs. This feedback is separate from the project requirements and from unresolved project-specific questions in the Review Memo. Do not modify the authoritative forms or guidance on the basis of feedback without review and approval.

---
