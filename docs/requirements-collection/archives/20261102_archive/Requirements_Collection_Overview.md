# SEPIO Requirements Collection — Project Representative Overview

**Audience:** Project representatives who are asking an AI agent to complete the SEPIO Requirements Forms for their project

## 1. What this process is for

The SEPIO Requirements Forms describe what a biomedical knowledge project currently represents and what it should support about claims, evidence, interpretation, and provenance.

The goal is **not** to redesign your project or force it into SEPIO while the forms are being completed.

Instead, the process asks two related questions:

> **Current state:** What does the selected canonical source, dataset, distribution, or model actually represent now?

> **Desired state:** What broader capabilities does project-specific evidence support as requirements for a future SEPIO-based representation?

This distinction is important. Current-state answers should be conservative and reproducible: they are grounded only in the canonical source set explicitly selected for the review. Desired-state answers may use a broader set of project evidence to identify a **maximal, evidence-supported requirements set** that a human reviewer can later refine or narrow.

After the forms are reviewed and confirmed, a separate SEPIO requirements-to-model workflow can use them to:

- identify relevant SEPIO classes and attributes;
- generate a candidate project-specific SEPIO covering model;
- identify partial SEPIO coverage;
- identify model gaps or extension needs;
- generate implementation guidance; and
- identify questions requiring project or SEPIO modeler review.

The completed forms are therefore a description of **your project's requirements**, not a list of SEPIO features you have chosen.

---

## 2. What is in this starter package

This folder contains:

- `QUICK_START.md` — a short orientation and five-step entry point.
- `Requirements_Collection_Overview.md` — this comprehensive overview of the requirements-collection workflow.
- `Requirements_Collection_Forms.xlsx` — the authoritative requirements workbook the agent should complete.
- `Feedback_Log_Template.xlsx` — the separate post-completion feedback workbook for issues and suggested improvements to the forms and process.
- `Requirements_Instructions_and_Guidance_for_AI.md` — detailed semantic and field-by-field instructions intended primarily for the AI agent.
- `REQUIREMENTS_FORM_PROMPT.md` — the ready-to-copy prompt for tasking an agent to complete the requirements workbook.
- `RESOURCE_INVENTORY_PROMPT.md` — an optional agent prompt for discovering, classifying, and organizing project resources and proposing candidate scope statements.
- `RESOURCE_INVENTORY_GUIDANCE.md` — practical guidance for assembling and reviewing a Resource Inventory.
- `RESOURCE_INVENTORY_GUIDANCE.md` — guidance for gathering and reviewing project schemas, documentation, examples, and other evidence.
- `examples/example_scope_statement.md` — example project scope statements.
- `examples/example_completed_requirements_review.md` — an example Requirements Review Memo.
- `CONTENTS.md` — a list of files included in the package.

These files are designed to stay together in one directory in the repository.

---

## 3. The five-step workflow

At a high level:

1. **Define the scope.** Decide what canonical source(s) control current-state answers and what broader evidence may inform desired-state requirements.
2. **Create a Resource Inventory.** Identify the best sources, examples, versions, conflicts, access needs, and candidate scope statements.
3. **Give the agent the scope, inventory, forms, guidance, feedback template, and needed resources; have it complete the Requirements Forms, Review Memo, and Feedback Log.**
4. **Inspect the completed workbook and Requirements Review Memo; separately triage the Feedback Log.** Resolve uncertainties and correct anything that does not accurately reflect the project.
5. **Move to SEPIO mapping.** Once confirmed, use the requirements record as input to the separate requirements-to-model workflow.

The remainder of this document explains each part in more detail.

---

## 4. Step 1 — Define the project scope

Before asking the requirements agent to populate the forms, define a **project scope statement**.

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

Without an explicit scope, an agent can easily mix these together and produce answers that are neither reproducible nor clearly interpretable.

A useful scope statement identifies two evidence sets.

### 4.1 Current-state canonical source set

This is the exact source, dataset, distribution, release, schema, or explicitly designated companion artifact that controls the workbook's **current-state / “Used in Current Data?”** answers.

The requirements agent should **strictly use only this source set** when populating current-state columns.

Examples include:

- one versioned `indications.xlsx` distribution;
- one current LinkML schema release plus designated canonical example records;
- one KG release/export;
- one production database schema plus its canonical data dictionary.

The fact that richer information exists elsewhere in the project does not make it part of current state unless the scope explicitly includes that resource in the canonical source set.

### 4.2 Desired-state evidence set

This is the broader set of project-specific resources the agent is allowed to use when deciding what the future SEPIO-based representation should support.

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

The desired-state evidence set supports a **maximal but evidence-supported** first-pass requirements record. “Maximal” does not mean speculative: every desired-state Y/M answer should still have project-specific support.

### 4.3 Minimal versus maximal scope

The Resource Inventory workflow is designed to propose at least two reasonable scope choices.

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
> **Desired-state evidence:** additional MeDIC-maintained intermediate curation artifacts, alternate distributions, the MeDIC paper and project documentation, and explicit project requirements may be used to identify a broader, evidence-supported desired-state requirements set. Where desired state differs from current state, the supporting source must be named in `Explanation / Considerations`.

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

If not, use `RESOURCE_INVENTORY_PROMPT.md`. The resource-discovery agent should produce:

- a minimal scope;
- a maximal scope;
- additional reasonable alternatives when appropriate; and
- a recommended scope with tradeoffs.

The project representative should review or refine the proposed scope and place the selected statement into the `SELECTED PROJECT SCOPE` section of `REQUIREMENTS_FORM_PROMPT.md`.

---

## 5. Step 2 — Create a Resource Inventory

A **Resource Inventory** is a structured evidence package for the requirements review.

It is more than a list of files. It should tell the later requirements agent:

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

The agent-generated Resource Inventory should be reviewed before requirements completion.

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

Public resources are retrieval tasks for the AI agent, not preemptive upload tasks for the project representative.

The requirements agent should first try to retrieve public materials itself.

Human assistance is appropriate when:

- public retrieval fails;
- authentication/private access is required;
- a source exists only locally;
- multiple plausible versions/files exist and the canonical one cannot be identified confidently;
- a human scope or canonical-version decision is required.

If human help is needed, the agent should say exactly what resource is needed, why it matters, and whether the review can proceed provisionally without it.

---

## 6. Step 3 — Give the agent what it needs and populate the forms

Give the requirements agent:

1. `REQUIREMENTS_FORM_PROMPT.md`
2. the selected project scope statement
3. `Requirements_Collection_Forms.xlsx`
4. `Requirements_Instructions_and_Guidance_for_AI.md`
5. the reviewed `[PROJECT]_Resource_Inventory.md`
6. any private/local materials identified as necessary

For the forms and guidance, you may either upload the files or provide links/pointers to the exact versions you want used.

For project evidence, you may:

- upload local files;
- provide public repository/documentation/DOI links;
- provide a manifest or Resource Inventory with precise pointers;
- point to specific files/directories rather than entire repositories.

For large datasets, representative records plus structural documentation may be enough unless the agent needs the full dataset to answer a specific requirement.

### 6.1 Current-state rule

For every current-state/F1 answer, the agent should ask:

> Is this capability represented in the **selected current-state canonical source set**?

It should not mark something current merely because it appears in:

- an intermediate artifact;
- a historical or alternate distribution;
- a paper;
- a roadmap;
- an upstream source;
- a downstream API/UI;
- process documentation;

unless the selected scope explicitly includes that resource in the current-state canonical source set.

### 6.2 Desired-state rule

For every desired-state/F2 answer, the agent should ask:

> Is this capability supported as a project requirement by one or more resources allowed in the selected desired-state evidence set?

The initial desired-state pass should generally be **maximal but evidence-supported**.

When desired state differs from current state, the agent should identify the supporting source in `Explanation / Considerations`.

A useful pattern is:

> **Current state:** [brief observation from canonical source].  
> **Desired-state support:** [SUPPORT TYPE] — [Source ID/title/version]: [brief evidence and rationale].

### 6.3 How the agent should reason

The agent should triangulate across:

```text
Selected project scope
        +
Current-state canonical source set
        +
Broader desired-state evidence set
        +
Representative records/examples
        +
Curation / pipeline / provenance documentation
        +
Known requirements / use cases
```

For each substantive answer, it should be able to answer:

> What project evidence supports this answer, and is that source allowed to support current state, desired state, or both?

If that cannot be answered, the response should be marked uncertain rather than guessed.

### 6.4 Important distinctions to preserve

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

### 6.5 Requirements-first rule

The Requirement→SEPIO mapping registry should not be used to decide what the project's requirements are.

The agent should determine project requirements independently of current SEPIO coverage.

---

## 7. Step 4 — Inspect the deliverables

The agent should return **three distinct deliverables**: the completed requirements workbook, the Requirements Review Memo, and a project-specific copy of `Feedback_Log_Template.xlsx`. The Feedback Log captures suggestions about the collection process and is reviewed separately from the substantive project requirements. Feedback does not automatically change the authoritative forms or instructions.

The requirements agent should return two primary artifacts.

### A. Completed Requirements Workbook

The agent should populate the provided `Requirements_Collection_Forms.xlsx` template while preserving its existing structure and formatting.

The output filename should include project name, version, date, and 24-hour time, for example:

`MeDIC_Requirements_v0.2_20261013_1643.xlsx`

The `HHMM` form avoids filename problems caused by colons on some operating systems.

### B. Requirements Review Memo

The memo filename should follow the same version/date/time convention, for example:

`MeDIC_Requirements_Review_Memo_v0.2_20261013_1643.md`

The memo should include:

- the selected project scope;
- the exact **current-state canonical source set**;
- the broader **desired-state evidence set**;
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

### 7.2 Human review checklist

Focus review on:

| Review question | What to check |
|---|---|
| Scope | Did the agent use the selected project/data product and correct canonical source set? |
| Current state | Is every F1/current-state Y/M answer supported by the allowed canonical source set? |
| Desired state | Is every broader F2/desired-state Y/M answer supported by an allowed project source? |
| Source traceability | When F2 differs from F1, does `Explanation / Considerations` identify the supporting desired-state source and rationale? |
| Claims | Are the major kinds of assertions represented by the project captured? |
| Evidence | Are important evidence item categories and relationships represented? |
| Interpretation | Did the agent distinguish evidence from interpreted evidence, direction/strength, grouping, and higher-level synthesis? |
| Provenance | Are source, authorship, method, process, semantic alignment, encoding, retrieval, and other provenance requirements captured at the right level? |
| Upstream EPC | Did the agent avoid treating richer upstream content as current project representation? |
| Intermediate artifacts | If used for desired state, were they kept separate from current-state claims? |
| Downstream enrichment | Did the agent avoid treating API/UI enrichment as canonical current-state representation? |
| Uncertainty | Did it flag unsupported or ambiguous answers rather than guessing? |
| Consistency | Do responses across worksheets and the memo tell a coherent story? |
| Examples | Are current-state and desired-state examples accurate, sourced, and useful? |

Correct anything that does not accurately reflect the project.

Once you are comfortable with the workbook, treat it as the **confirmed project requirements input**.

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

During the current AI-first pilot phase, an AI agent can generate these artifacts with transparent provenance. A future production workflow can move exact schema extraction, dependency closure, validation, traceability, and manifest generation into deterministic code.

The project representative does **not** need to perform these mappings manually.

---

## 9. Evidence hierarchy and conflict handling

A single global evidence hierarchy is no longer sufficient because **current state and desired state intentionally use different source sets**.

### For current-state answers

The selected scope controls.

Within the allowed current-state source set, prefer:

1. explicitly designated canonical release/distribution;
2. canonical schema/data model;
3. canonical companion data dictionary/specification;
4. representative records from the same release;
5. other explicitly designated canonical companion artifacts.

A noncanonical paper, intermediate artifact, or alternate distribution should not override current state.

### For desired-state answers

Use the broader evidence set allowed by the selected scope.

Prefer the strongest project-specific evidence, such as:

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
3. **accurate project requirements**.

---

## 11. Minimum evidence standard

Before considering a requirements workbook ready for confirmation, the workflow should ideally have:

- a selected project scope statement;
- a clearly named current-state canonical source set;
- at least one authoritative structural source;
- representative examples from the canonical source;
- enough information to distinguish current project content from upstream/downstream information;
- one or more sources supporting desired-state requirements when F2 goes beyond F1;
- source/version information sufficient to reproduce the review;
- explicit review flags for questions the available evidence cannot answer.

Projects lacking one or more of these can still participate, but the resulting workbook should contain more uncertainty/review flags.

---

## 12. Key principle

The requirements process is **requirements-first, not SEPIO-first**.

The project representative and agent should first answer:

> **What does the selected canonical source currently represent, and what broader capabilities does project evidence support as desired requirements?**

Only after those requirements are reviewed should the SEPIO mapping workflow ask:

> **How well does SEPIO represent those needs?**
