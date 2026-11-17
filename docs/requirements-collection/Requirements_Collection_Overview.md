# SEPIO Requirements Collection — Project Representative Overview

**Audience:** Project representatives, human facilitators, and others participating in SEPIO requirements collection, whether working independently or with AI agents.

**How to use this overview:** Requirements collection is a general project-led process. The starter kit supports human-led collection, AI-generated drafts reviewed by humans, and collaborative interviews in which an agent and project representative develop responses together. AI assistance is recommended but optional; an authorized project representative confirms the requirements before they are used for SEPIO mapping.

## 1. What this process is for

The SEPIO Requirements Forms describe what a biomedical knowledge project currently represents and what it should support about claims and concept-definition statements, evidence, evidence interpretation, provenance, and confidence.

The goal is **not** to redesign your project or force it into SEPIO while the forms are being completed.

Instead, the process asks two related questions:

> **Current state:** What does the selected canonical source, dataset, distribution, or model actually represent now?

> **Desired state:** What broader capabilities does project-specific sources support as requirements for a future SEPIO-based representation?

This distinction is important. Current-state answers should be conservative and reproducible: they are grounded only in the canonical source set explicitly selected for the review. Desired-state answers may use a broader set of project-specific sources to identify a **maximal, source-supported requirements set** for representative review. This can include requirements for concept-definition statements, such as synonym, mapping, and subclass assertions, when the project needs to represent their evidence, provenance, or confidence.

### How requirements collection fits into the larger SEPIO process

Requirements collection is **Phase 1** of a broader four-phase workflow:

1. **Project Requirements Collection:** Establish the project's current and desired representational needs, grounded in source materials and confirmed by its representative.
2. **Requirements-to-SEPIO Mapping:** Map confirmed requirements to the SEPIO Core Model using the maintained Requirement → SEPIO Mapping Registry and identify direct coverage, partial coverage, modeling alternatives, and gaps.
3. **Covering Model Derivation and Review:** Systematically derive a candidate SEPIO Covering Model from the approved requirement mappings, then have SEPIO modelers and participating projects review and refine it. The Covering Model identifies shared representational capabilities; it is **not** a project-specific implementation profile with dataset-level constraints or cardinalities.
4. **Project Data Mapping and Validation:** Transform representative records into the candidate SEPIO-based representation, assess whether required semantics are preserved, and feed findings back into the model and mappings.

AI assistance may be used in any phase, but is not required. The detailed four-phase explanation is in `Requirements_Instructions_and_Guidance_for_Agents.md`.

**This Overview and its five practical steps focus on Phase 1.** The completed forms describe **your project's requirements**, not a selection of SEPIO features. Requirements mapping and model derivation come after project confirmation.

---

## 2. What is in this starter package

This folder contains:

- `QUICK_START.md` — a short orientation and five-step entry point.
- `Requirements_Collection_Overview.md` — this comprehensive overview of the requirements-collection workflow.
- `Requirements_Collection_Forms.xlsx` — the authoritative requirements workbook to complete and confirm.
- `Feedback_Log_Template.xlsx` — a separate template for documenting feedback on the forms and collection process, particularly useful in AI-assisted workflows.
- `Requirements_Instructions_and_Guidance_for_Agents.md` — detailed semantic and field-by-field guidance for human and AI participants, written with sufficient specificity for AI-assisted execution.
- `REQUIREMENTS_FORM_PROMPT.md` — a ready-to-copy AI prompt for preparing a requirements draft; collaborative interviewing is also a valid approach.
- `RESOURCE_INVENTORY_PROMPT.md` — an optional agent prompt for discovering, classifying, and organizing project resources and proposing candidate scope statements.
- `RESOURCE_INVENTORY_GUIDANCE.md` — practical guidance for assembling and reviewing a Resource Inventory.
- `examples/example_scope_statement.md` — example project scope statements.
- `examples/example_completed_requirements_review.md` — an example Requirements Review Memo.
- `CONTENTS.md` — a list of files included in the package.

These files are designed to stay together in one directory in the repository.

---

## 3. The five-step workflow

At a high level:

1. **Discover resources and establish scope.** Identify relevant project sources and representative examples, select the authoritative canonical current-state set, and define broader sources that may support desired-state requirements. A Resource Inventory can be assembled before or alongside scope selection.
2. **Finalize a Resource Inventory.** Record source roles, versions, example records, conflicts, access needs, and the approved scope; review any agent-generated inventory.
3. **Complete the forms and Review Memo.** Use human-led work, an AI-generated draft, or a facilitated interview in which an agent and project representative discuss questions and agree on responses. Record substantive bases and examples; use the Feedback Log separately for process-improvement observations when helpful.
4. **Review and confirm the results.** An authorized project representative validates the workbook and Review Memo, resolves uncertainties, and reviews process feedback separately.
5. **Move to SEPIO mapping.** Use the confirmed requirements as input to the separate requirements-to-model workflow.

The remainder of this document explains each part in more detail.

---

## 4. Step 1 — Define the project scope

Before completing the forms, define a **project scope statement**. A human participant or an AI agent may help discover resources and propose the scope, but the project representative should confirm it.

Biomedical projects often have several related representations:

- an internal curation model;
- a canonical public distribution;
- intermediate curation or analysis artifacts;
- one or more source databases;
- an ingest/transformation pipeline;
- alternate or historical releases;
- an API representation;
- a knowledge-graph export;
- a user-interface representation.

Without an explicit scope, anyone preparing the forms can inadvertently mix these together and produce answers that are neither reproducible nor clearly interpretable.

A useful scope statement identifies two source sets for requirements assessment.

### 4.1 Current-state canonical source set

This is the exact source, dataset, distribution, release, schema, or explicitly designated companion artifact that controls the workbook's **current-state / “Used in Current Data?”** answers.

Whoever prepares the forms should **strictly use only this source set** when populating current-state [F1] columns.

Examples include:

- one versioned `indications.xlsx` distribution;
- one current LinkML schema release plus designated canonical example records;
- one KG release/export;
- one production database schema plus its canonical data dictionary.

The fact that richer information exists elsewhere in the project does not make it part of current state unless the scope explicitly includes that resource in the canonical source set.

### 4.2 Desired-state supporting-source set

This is the broader set of project-specific resources permitted for use when deciding what the future SEPIO-based representation should support.

Depending on the selected scope, this can include:

- explicit future requirements or roadmap items;
- current papers and project documentation;
- model/design documentation;
- intermediate curation or analysis artifacts;
- information captured elsewhere in the project pipeline but dropped from the canonical export;
- alternate or earlier project distributions;
- competency questions;
- curation guidance;
- implementation/design documents.

The desired-state source set supports a **maximal but source-supported** first-pass requirements record. “Maximal” does not mean speculative: every desired-state [F2] `Y` or `M` response should still have identifiable project-specific support.

### 4.3 Minimal versus maximal scope

When alternatives are useful, the Resource Inventory workflow can identify at least two reasonable scope choices.

#### Minimal / canonical-distribution-only

A minimal scope limits the review to one canonical source set.

Example:

> **Current-state canonical source:** MeDIC `matrix_indication_list.xlsx`, version 1.3.0.  
> Current-state and desired-state requirements should both be limited to information represented in this canonical distribution.

This produces a conservative description of one concrete release.

#### Maximal / canonical current state + broad desired state

A maximal scope preserves a strict current-state source while allowing broader project evidence to inform desired state.

Example:

> **Current-state canonical source:** MeDIC `matrix_indication_list.xlsx`, version 1.3.0. Current-state answers must be based only on this distribution.  
> **Desired-state evidence:** additional MeDIC-maintained intermediate curation artifacts, alternate distributions, the MeDIC paper and project documentation, and explicit project requirements may be used to identify a broader, source-supported desired-state requirements set. Where desired state differs from current state, the supporting source must be named in `Explanation / Considerations`.

This is often the preferred starting point because it gives a reproducible account of current representation while surfacing a broader set of requirements for human review.

### 4.4 Other reasonable scopes

Some projects may justify additional alternatives, for example:

- current release + current pipeline artifacts;
- core product + designated companion datasets;
- domain-specific subset;
- strict historical release;
- current product family / multi-distribution scope.

If substantially different products have different evidence/provenance behavior, separate requirements reviews may be clearer.

### 4.5 How to obtain a scope statement

If the scope is already obvious, write it directly.

If not, the scope can be developed through discussion and source review, optionally using `RESOURCE_INVENTORY_PROMPT.md`. When used, the resource-discovery agent should propose:

- a minimal scope;
- a maximal scope;
- additional reasonable alternatives when appropriate; and
- a recommended scope with tradeoffs.

The project representative should review and confirm the selected scope. For AI-assisted completion, place it into the `SELECTED PROJECT SCOPE` section of `REQUIREMENTS_FORM_PROMPT.md`.

---

## 5. Step 2 — Create a Resource Inventory

A **Resource Inventory** is a structured catalog of source materials supporting the requirements review. It documents the *basis* for requirements assessments; this is distinct from the scientific evidence that a project may represent about its claims.

It is more than a list of files. It should tell anyone preparing the forms:

- which resources are canonical for current state;
- which resources may inform desired state;
- which examples should be inspected;
- which sources are historical, upstream, downstream, or context only;
- which versions/releases should be used;
- what source conflicts or uncertainties exist;
- which public resources the agent should retrieve itself;
- which materials may require human provision or clarification.

Use `RESOURCE_INVENTORY_GUIDANCE.md` for detailed guidance.

### 5.1 Two ways to create the inventory

**Option A — Assemble it yourself.**  
If you already know the key schema, canonical distribution, documentation, examples, curation guidance, and provenance materials, create a simple inventory or manifest with precise pointers to them.

**Option B — Ask an AI agent to take a first pass.**  
Use `RESOURCE_INVENTORY_PROMPT.md` when project evidence is distributed across repositories, documentation sites, papers, DOI archives, generated artifacts, or multiple versions.

Whether drafted by a human or generated by an agent, the Resource Inventory and its source-role assignments should be reviewed before requirements completion.

### 5.2 Resource roles

The inventory should distinguish source roles such as:

- `CURRENT_STATE_CANONICAL`
- `CURRENT_STATE_CANONICAL_COMPANION`
- `DESIRED_STATE_SUPPORT`
- `CURRENT_AND_DESIRED`
- `CONTEXT_ONLY`

Only sources designated as current-state canonical or canonical companions should control current-state answers under the selected scope.

### 5.3 Desired-state support types

When a broader source supports desired state, it is useful to distinguish why:

#### `EXPLICIT_FUTURE_REQUIREMENT`

A roadmap, issue, requirements document, competency question, or explicit project statement says the capability is wanted or needed.

#### `EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT`

The project already captures or uses the information in an intermediate artifact, alternate distribution, curation workflow, analysis product, or other project-maintained representation, but the selected canonical distribution does not expose it.

#### `DOCUMENTED_MODEL_INTENT`

A paper, model/design document, curation guide, or other authoritative project document describes the capability as part of the intended project model or data product, even though it is absent from the selected canonical source.

A source that explicitly says a capability is out of scope, rejected, deprecated, or intentionally excluded should not normally be used to justify desired state unless another authoritative project source explicitly reverses that decision.

### 5.4 Useful resources

Typical resources include:

| Resource type | Why it helps |
|---|---|
| Canonical dataset/distribution | Establishes what is actually represented in current state. |
| Authoritative schema or data model | Shows entities, relationships, fields, structure, and constraints. |
| Data dictionary / field documentation | Explains field meaning, allowed values, cardinality, and intended use. |
| Model/design documentation | Explains why structures exist and what the project intends to represent. |
| Representative example records | Shows how the model is actually used in practice. |
| Intermediate curation/analysis artifacts | May reveal existing project capabilities omitted from the canonical export. |
| Source/ingest documentation | Shows which upstream information is retained, transformed, or discarded. |
| Curation guidelines / SOPs | Helps interpret claims, evidence evaluation, confidence, review, and provenance. |
| Pipeline / normalization documentation | Helps identify semantic-alignment and process provenance. |
| Project papers / overview documents | Provides project goals, intended semantics, and model intent. |
| Requirements / competency questions / roadmap | Captures desired capabilities not yet fully implemented. |

You do not need every resource type. The goal is to assemble enough evidence to answer each form question responsibly.

### 5.5 Representative examples

The inventory should identify a small, diverse set of examples rather than hundreds of repetitive records.

Useful examples may include:

- a typical claim;
- a claim with qualifiers/context;
- a claim with source or evidence support;
- a claim with richer provenance;
- a normalization or transformation example;
- a case where intermediate information is dropped from the canonical export;
- an alternate distribution that exposes a capability absent from the canonical one.

Assign stable IDs such as `E01`, `E02`, and `E03`.

### 5.6 Public resources and human uploads

**For AI-assisted work**, the agent should ordinarily attempt to retrieve publicly accessible materials itself, rather than requiring the project representative to upload them in advance. In human-led work, project participants may instead gather or link directly to the relevant materials.

Human assistance is appropriate when:

- public retrieval fails;
- authentication/private access is required;
- a source exists only locally;
- multiple plausible versions/files exist and the canonical one cannot be identified confidently;
- a human scope or canonical-version decision is required.

If an AI agent needs human help, it should identify the precise resource, why it matters, and whether the review can proceed provisionally without it. In any execution mode, record unavailable sources and their consequences for the assessments.

---

## 6. Step 3 — Complete the requirements forms

The forms may be completed directly by a project representative, by a human facilitator, by an AI agent preparing a draft for subsequent review, or collaboratively in a structured interview. **AI assistance is recommended but optional**; the same source rules, documentation expectations, and confirmation requirement apply in every mode.

### 6.1 AI-assisted preparation (when used)

For an independent agent draft or a collaborative AI-assisted interview, provide:

1. `REQUIREMENTS_FORM_PROMPT.md`
2. the selected project scope statement
3. `Requirements_Collection_Forms.xlsx`
4. `Requirements_Instructions_and_Guidance_for_Agents.md`
5. the reviewed `[PROJECT]_Resource_Inventory.md`
6. any private/local materials identified as necessary

For the forms and guidance, you may either upload the files or provide links/pointers to the exact versions you want used.

For project source materials, you may:

- upload local files;
- provide public repository/documentation/DOI links;
- provide a manifest or Resource Inventory with precise pointers;
- point to specific files/directories rather than entire repositories.

For large datasets, representative records plus structural documentation may be enough unless a specific assessment requires the full dataset.

**Two valid AI-assisted modes:**

- **Agent-generated draft:** The agent inspects the permitted sources, fills the forms and Review Memo, and flags unresolved questions for human validation.
- **Collaborative elicitation/interview:** The agent presents each form question to a project representative, proposes a source-grounded answer or asks for a concrete record, and collaborates with the representative to clarify and document the answer. This is especially useful where important requirements live in source-data conventions or expert knowledge rather than written documentation, as in the MONDO pilot. Record decisions and provisional assumptions so later answers can be revised consistently.

In either case, the project representative must confirm the final responses. Human-led collection can use the same forms, dictionaries, and review practices without using the AI prompt.

### 6.2 Current-state rule

For every current-state [F1] answer, ask:

> Is this capability represented in the **selected current-state canonical source set**?

Do not mark something current merely because it appears in:

- an intermediate artifact;
- a historical or alternate distribution;
- a paper;
- a roadmap;
- an upstream source;
- a downstream API/UI;
- process documentation;

unless the selected scope explicitly includes that resource in the current-state canonical source set.

### 6.3 Desired-state rule

For every desired-state [F2] answer, ask:

> Is this capability supported as a project requirement by one or more resources allowed in the selected desired-state source set?

The initial desired-state pass should generally be **maximal but source-supported**.

When desired state differs from current state, cite the supporting source in [F4] Basis for F2 Response and summarize the rationale in [F5] Explanation / Considerations.

A useful pattern is:

> **Current state:** [brief observation from canonical source].  
> **Desired-state support:** [SUPPORT TYPE] — [Source ID/title/version]: [brief source basis and rationale].

### 6.4 Assessing support for answers

The preparer should consider:

```text
Selected project scope
        +
Current-state canonical source set
        +
Broader desired-state source set
        +
Representative records/examples
        +
Curation / pipeline / provenance documentation
        +
Known requirements / use cases
```

For each substantive answer, the preparer should be able to answer:

> What project source supports this assessment, and is it permitted to support current state, desired state, or both?

If that cannot be answered, the response should be marked uncertain rather than guessed.

### 6.5 Important distinctions to preserve

#### Current representation vs desired requirement

A capability may be absent from the canonical current-state distribution but still be a valid desired-state requirement.

#### Upstream source capability vs project capability

If an upstream source contains rich EPC information that the project neither stores nor explicitly requires, it should not automatically become a project requirement.

#### Canonical distribution vs intermediate project capability

An intermediate project artifact may contain information omitted from the canonical export. Under a maximal scope, this can support desired state as `EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT` without changing the current-state answer.

#### Canonical model vs downstream API/UI enrichment

Downstream computation or display enrichment should not be treated as current canonical representation unless explicitly included in scope.

#### Claim semantics vs evidence/provenance

A project may support many biomedical claim types while using one relatively simple evidence/provenance envelope. Assess these dimensions separately.

#### Evidence item vs evidence interpretation

A publication, source passage, dataset, or experimental result is not the same thing as an interpreted argument about whether evidence supports or disputes a proposition.

#### Scientific evidence strength vs extraction/alignment confidence

A score indicating confidence in entity normalization or extraction should not be treated as scientific evidence strength unless project semantics explicitly say so.

#### Process documentation vs stored provenance

Documentation that an LLM, normalization service, curator, or pipeline step was used does not prove that provenance about that process is stored in the canonical data.

#### Missing information vs negative requirement

Silence is not automatically “N.” Use **M / Maybe / Needs discussion** or another review flag when evidence is insufficient.

### 6.6 Requirements-first rule

The Requirement→SEPIO mapping registry should not be used to decide what the project's requirements are.

Determine project requirements independently of current SEPIO coverage, whether the forms are completed by a person or an AI agent.

---

## 7. Step 4 — Review and confirm the deliverables

Requirements collection should produce **two primary artifacts**: a completed Requirements Workbook and a Requirements Review Memo. For AI-assisted collection, a project-specific Feedback Log is also recommended as a **separate process-improvement artifact**; human-led efforts may use the same template. Feedback should be reviewed separately and does not automatically change authoritative forms or guidance.

### A. Completed Requirements Workbook

Complete the provided `Requirements_Collection_Forms.xlsx` template while preserving its existing structure and formatting.

The output filename should include project name, version, date, and 24-hour time, for example:

`MeDIC_Requirements_v0.2_20261013_1643.xlsx`

The `HHMM` form avoids filename problems caused by colons on some operating systems.

### B. Requirements Review Memo

The memo filename should follow the same version/date/time convention, for example:

`MeDIC_Requirements_Review_Memo_v0.2_20261013_1643.md`

The memo should include:

- the selected project scope;
- the exact **current-state canonical source set**;
- the broader **desired-state source set**;
- exact versions/releases/commits/DOI archive versions/retrieval dates where relevant;
- high-confidence conclusions;
- answers requiring human review;
- source conflicts or missing information;
- inaccessible resources;
- important assumptions;
- difficult form/guidance questions;
- observations that may improve the workflow;
- representative data examples.

### 7.1 Representative examples in the memo

The memo should include a small, diverse set of concrete examples:

- a few **current-state examples** directly from the selected canonical source; and
- a few broader **desired-state/maximal examples** when noncanonical project evidence reveals additional requirements.

Represent examples as close to their source representation as practical:

- **tabular/database source:** show rows/tables using source column names where possible;
- **JSON/YAML:** show compact objects preserving source field names and nesting;
- **RDF/graph:** show triples/quads/edge properties;
- **free text:** show only the minimal excerpt needed;
- **multi-source example:** label it `COMPOSITE/ILLUSTRATIVE`;
- **record assembled across tables:** label it `DENORMALIZED` and identify contributing tables.

Do not fabricate values to create a complete-looking example.

### 7.2 Feedback on the tools and process

When AI assistance is used, complete a project-specific copy of `Feedback_Log_Template.xlsx` following its `Agent Instructions` and `Controlled Vocabularies` tabs. Human-led collections may also use this template. Keep feedback about ambiguous form rows, instructions, process difficulties, and suggested improvements **separate** from substantive project requirements and unresolved project-specific questions in the Review Memo. Review and approve changes before modifying the starter-kit templates.

### 7.3 Project review and confirmation checklist

Focus review on:

| Review question | What to check |
|---|---|
| Scope | Did the preparer use the selected project/data product and correct canonical source set? |
| Current state | Is every [F1] current-state `Y`/`M` answer supported by the allowed canonical source set? |
| Desired state | Is every broader [F2] desired-state `Y`/`M` answer supported by an allowed project source? |
| Source traceability | When [F2] differs from [F1], do [F4] Basis for F2 Response and [F5] Explanation / Considerations identify the supporting desired-state source and rationale? |
| Claims | Are the major kinds of assertions represented by the project captured? |
| Evidence | Are important evidence item categories and relationships represented? |
| Interpretation | Did the preparer distinguish evidence from interpreted evidence, direction/strength, grouping, and higher-level synthesis? |
| Provenance | Are source, authorship, method, process, semantic alignment, encoding, retrieval, and other provenance requirements captured at the right level? |
| Upstream EPC | Did the preparer avoid treating richer upstream content as current project representation? |
| Intermediate artifacts | If used for desired state, were they kept separate from current-state claims? |
| Downstream enrichment | Did the preparer avoid treating API/UI enrichment as canonical current-state representation? |
| Uncertainty | Were unsupported or ambiguous answers flagged rather than guessing? |
| Consistency | Do responses across worksheets and the memo tell a coherent story? |
| Examples | Are current-state and desired-state examples accurate, sourced, and useful? |

Correct anything that does not accurately reflect the project.

An **authorized project representative** should review, correct, and confirm the workbook and Review Memo before they are treated as the **authoritative project requirements input** for SEPIO mapping and Covering Model derivation.

---

## 8. Step 5 — What happens after the forms are confirmed

The confirmed workbook becomes the project requirements input for the later SEPIO requirements-to-model workflow.

That later workflow uses:

```text
Confirmed Requirements Forms
        +
Requirement→SEPIO Mapping Registry
        +
SEPIO source schema
        ↓
Requirements-to-Model Output Package
```

That package can include:

1. Candidate SEPIO Covering Model
2. Requirements Summary
3. Requirements-to-Model Traceability
4. Requirements Follow-Up & Modeling Decisions
5. Gap & Extension Analysis
6. Implementation Guidance
7. Requirements Collection & Form Feedback (downstream mapping artifact, not the Starter Kit agent Feedback Log)
8. Generation Manifest

The mapping and candidate-model generation stages may be assisted by AI agents, deterministic tools, or human modeling work. The maintained Requirement → SEPIO Mapping Registry and authoritative SEPIO Core Model provide the basis for systematic candidate derivation; SEPIO modelers and participating projects review and refine the results. A candidate Covering Model is distinct from a project-specific implementation profile, which may subsequently add dataset-level constraints or cardinalities.

Project representatives need not perform the detailed mappings themselves; their central role is confirming requirements and reviewing the proposed representations for fidelity to their needs.

---

## 9. Evidence hierarchy and conflict handling

A single global evidence hierarchy is no longer sufficient because **current state and desired state intentionally use different source sets**.

### For current-state answers

The selected scope controls the answer.

Within the allowed current-state source set, prefer:

1. explicitly designated canonical release/distribution;
2. canonical schema/data model;
3. canonical companion data dictionary/specification;
4. representative records from the same release;
5. other explicitly designated canonical companion artifacts.

A noncanonical paper, intermediate artifact, or alternate distribution should not override current state.

### For desired-state answers

Use the broader source set allowed by the selected scope.

Prefer the strongest project-specific sources or documented bases, such as:

1. explicit future requirements / approved roadmap / competency questions;
2. current authoritative project/model documentation;
3. existing project-maintained intermediate or alternate artifacts that demonstrate a capability;
4. current curation/modeling guidance;
5. current implementation/design documentation;
6. older or historical project sources when they remain relevant and are not contradicted by authoritative current sources.

When sources disagree:

- identify the conflict;
- state which source controls current state;
- state whether the conflicting resource may still inform desired state;
- do not silently reconcile them.

---

## 10. What project representatives are not expected to do

Project representatives do not need to:

- learn the complete SEPIO model before filling out the forms;
- manually map project fields to SEPIO classes and slots;
- decide whether a SEPIO gap exists;
- design SEPIO extensions;
- understand dependency closure; or
- create the Candidate Covering Model themselves.

Their responsibility is to help establish:

1. a defensible scope;
2. an accurate evidence base; and
3. **accurate, confirmed project requirements**.

---

## 11. Minimum evidence standard

Before considering a requirements workbook ready for confirmation, the workflow should ideally have:

- a selected project scope statement;
- a clearly named current-state canonical source set;
- at least one authoritative structural source;
- representative examples from the canonical source;
- enough information to distinguish current project content from upstream/downstream information;
- one or more project sources supporting desired-state requirements when [F2] goes beyond [F1];
- source/version information sufficient to reproduce the review;
- explicit review flags for questions the available evidence cannot answer.

Projects lacking one or more of these can still participate, but the resulting workbook should contain more uncertainty/review flags.

---

## 12. Key principle

The requirements process is **requirements-first, not SEPIO-first**.

The requirements-collection participants should first answer:

> **What does the selected canonical source currently represent, and what broader capabilities does project evidence support as desired requirements?**

Only after those requirements are reviewed should the SEPIO mapping workflow ask:

> **How well does SEPIO represent those needs?**
