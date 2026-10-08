# START HERE — SEPIO Requirements Collection

This folder contains the resources you need to ask an AI agent to complete the SEPIO Requirements Forms for your biomedical knowledge project.

The goal is to capture **what your project actually represents and requires** about claims, evidence, interpretation, and provenance. At this stage, the agent should describe the project in its own terms rather than trying to choose SEPIO classes or properties.

After you review and confirm the completed forms, a separate SEPIO requirements-to-model step can determine which SEPIO model elements are relevant, where current SEPIO provides only partial coverage, and where follow-up or model extensions may be needed.

---

## What is in this folder

- `SEPIO_Requirements_Forms.xlsx` — the empty workbook your agent should complete.
- `SEPIO_Requirements_Instructions_and_Guidance.md` — detailed semantic and field-by-field instructions intended primarily for the AI agent.
- `AGENT_PROMPT.md` — a ready-to-copy prompt for tasking the agent.
- `PROJECT_SOURCE_CHECKLIST.md` — a checklist for gathering useful project schemas, documentation, examples, and other evidence.
- `SEPIO_Requirements_Collection_Quick_Start.md` — the full human-facing guide to the requirements-collection workflow.
- `examples/example_scope_statement.md` — examples of how to define exactly what project, model, or data product is being assessed.
- `examples/example_completed_requirements_review.md` — an example of the short review memo the agent should return with the completed forms.
- `BUNDLE_CONTENTS.md` — a list of the files included in this package.

---

# Step 1 — Define exactly what “the project” means

Before the agent starts, write a short **project scope statement**—usually one or two sentences.

This matters because a biomedical resource may have several different representations around it:

- an internal curation model;
- a canonical public data model;
- one or more source databases that feed it;
- an ingest/transformation pipeline;
- an API representation;
- a user-interface representation;
- exports in different formats.

The requirements forms should describe **one clearly defined target**.

A good scope statement says what is in scope and, where useful, what is out of scope.

### Example — canonical knowledge graph

> The project is the canonical MonarchKG data model and KG build output. Requirements should reflect what MonarchKG itself stores and represents, not richer evidence/provenance/confidence information available only in upstream source databases and not downstream API or display enrichments unless they are part of the canonical KG output.

### Example — native project model

> The project is the native DisMech knowledge model and disorder YAML dataset. Requirements should reflect information represented in the native schema and canonical disorder records, including the project's evidence-bearing mechanistic statements and provenance.

### Example — one ingest into a larger KG

> The project is the CTD chemical–disease ingest into Translator. Requirements should describe the normalized associations emitted by that ingest and the evidence/provenance retained in the ingest output, rather than the full CTD source model or Translator as a whole.

More examples are available in `examples/example_scope_statement.md`.

If your project has two substantially different data products with different evidence/provenance behavior, consider completing separate requirements forms for each.

---

# Step 2 — Gather the best project materials you can

Your agent should not guess what the project does based on its name or on what similar resources usually do. Give it the strongest available evidence.

You do **not** need every type of source below, but try to provide enough material for the agent to understand both the structure of the data and the intended meaning of that structure.

Useful materials include:

### Authoritative schemas and data models

These are often the most important sources.

Examples:

- LinkML schema
- JSON Schema
- SHACL shapes
- SQL/database schema
- UML/class diagrams
- data dictionaries
- canonical API object models
- formal export specifications

These help the agent answer questions such as:

> Is a claim a direct graph edge, a reified object, or a field on another record?

> Are supporting publications represented explicitly?

> Is evidence represented as its own object?

### Model and design documentation

Provide documents that explain **why** the model is structured as it is.

Examples:

- model overview
- architecture documentation
- modeling/design decisions
- semantic conventions
- project README files
- data-model documentation
- project papers describing the resource

These are especially important when the schema alone does not explain intended semantics.

### Representative records or datasets

Give the agent real examples of how the model is used.

Examples:

- several representative YAML/JSON records
- example KG edges
- example curated assertions
- example evidence records
- example exports
- a small representative subset of a dataset

Try to provide examples covering the major kinds of claims/evidence in the project rather than hundreds of nearly identical records.

### Evidence and curation guidance

If the project evaluates or curates evidence, include materials such as:

- curation SOPs
- evidence classification rules
- evidence type definitions
- confidence/scoring guidance
- interpretation guidelines
- review/approval workflows
- documentation of evidence strength or direction

### Provenance and ingest documentation

This is particularly important for knowledge graphs and aggregators.

Examples:

- ingest documentation
- source-attribution rules
- primary vs aggregator source conventions
- ETL/transformation documentation
- normalization/grounding procedures
- documentation describing which source fields are retained or discarded
- retrieval or processing pipeline descriptions

This helps the agent distinguish what an upstream source knows from what **your project actually preserves**.

### Requirements and use cases

If the desired future model is richer than today's implementation, also provide:

- formal requirements
- competency questions
- user stories
- roadmap/design documents
- documented planned capabilities

These can justify marking something as **Desired in SEPIO-based Data = Y** even when it is not yet present in current data.

Use `PROJECT_SOURCE_CHECKLIST.md` for a fuller checklist.

---

# Step 3 — Give those materials to your AI agent

Give the agent, at minimum:

1. `SEPIO_Requirements_Forms.xlsx`
2. `SEPIO_Requirements_Instructions_and_Guidance.md`
3. your project scope statement
4. the project materials you gathered in Step 2

Then copy the prompt from `AGENT_PROMPT.md`, replace the bracketed project name/scope text, and send it to the agent.

### How to provide project materials

Use whatever mechanism your agent supports best:

- **Upload files directly** when you have local schemas, documentation, spreadsheets, PDFs, YAML/JSON examples, or small datasets.
- **Provide repository or documentation links** when the authoritative materials are publicly available online.
- **Point to specific files/directories in a repository** when only part of a repo is relevant.
- **Provide several representative records rather than an entire large dataset** when the full dataset is unnecessary for understanding the model.
- **Tell the agent which sources are authoritative/current** if multiple versions exist.
- **Call out known conflicts** between old papers, current schemas, documentation, or implementation behavior.

A useful message might look like:

> The current LinkML schema and model documentation are authoritative. The 2023 paper is useful for background but is older than the current implementation. I have also attached five representative records. Please use the schema/docs to establish requirements and use the records to verify how the fields are actually populated.

If the project is spread across many web pages or repository files, ask the agent to first make a short inventory of the sources it plans to use so you can confirm it is looking at the right materials.

---

# Step 4 — Have the agent populate the forms

The prompt in `AGENT_PROMPT.md` tells the agent to complete the workbook using the detailed guidance.

The agent should work from project evidence, not plausibility.

In particular, it should distinguish:

- **currently represented** vs **desired in future SEPIO-based data**;
- **upstream source capability** vs **what the project actually retains**;
- **canonical project data** vs **downstream API/UI enrichment**;
- **evidence information** vs **evidence interpretation**;
- **scientific evidence strength** vs **confidence in a claim or extraction/alignment**;
- **knowledge-generation provenance** vs **encoding/retrieval provenance**.

If the available information does not support a confident answer, the agent should use **M / Maybe / Needs discussion** or otherwise flag the uncertainty rather than guessing.

The agent should also **not edit or use the SEPIO Mapping Summary columns to decide what the project's requirements should be**. Those mappings are downstream modeling information, not inputs to requirements elicitation.

---

# Step 5 — Ask for the two deliverables

The agent should return:

### 1. A completed requirements workbook

A completed copy of `SEPIO_Requirements_Forms.xlsx`.

### 2. A short Requirements Review Memo

The memo should summarize:

- the project scope used;
- the main project materials consulted;
- high-confidence conclusions;
- answers that need human review;
- apparent conflicts or missing information;
- difficult form/guidance questions;
- important assumptions.

See `examples/example_completed_requirements_review.md` for the expected style.

This memo is useful because you should not have to inspect every workbook cell equally closely. It tells you where your attention is most needed.

---

# Step 6 — Review the agent's work

Focus especially on places where the agent had to interpret ambiguous documentation or infer future intent.

Ask:

- Did it assess the **right project/data product**?
- Did it capture the major **claim types**?
- Did it correctly identify what the project treats as **evidence**?
- Did it distinguish flat publication/evidence-code metadata from richer evidence-item or EvidenceLine-style models?
- Did it capture provenance at the right level?
- Did it avoid importing rich EPC information that exists only in upstream sources?
- Did it avoid treating downstream API/display enrichments as canonical project requirements?
- Did it correctly distinguish **current** from **desired** capabilities?
- Did it flag unsupported answers instead of guessing?
- Do answers across the different worksheets tell a coherent story?

Correct anything that does not accurately reflect the project.

Once you are comfortable with the workbook, treat it as the **confirmed project requirements input**.

---

# Step 7 — What happens after the requirements are confirmed

The confirmed forms can then be passed into the separate SEPIO requirements-to-model workflow:

```text
Confirmed Requirements Forms
        +
Requirement→SEPIO Mapping Registry
        +
SEPIO source schema
        ↓
Requirements-to-Model Output Package
```

That downstream package can include:

1. Candidate SEPIO Covering Model
2. Requirements Summary
3. Requirements-to-Model Traceability
4. Requirements Follow-Up & Modeling Decisions
5. Gap & Extension Analysis
6. Implementation Guidance
7. Requirements Collection & Form Feedback
8. Generation Manifest

During the current pilot phase, an AI agent can generate these outputs with transparent provenance. Later, deterministic code can take over schema extraction, dependency closure, validation, traceability, and manifest generation.

The project representative does **not** need to perform these mappings manually.

---

# Key principle

> **Requirements first, SEPIO mapping second.**

The requirements-collection agent should first answer:

> What does this project currently represent, and what does it actually need to represent?

Only after those requirements are reviewed should the mapping workflow ask:

> How well does SEPIO represent those needs?

---

## More detailed guidance

A more comprehensive overview of the workflow and tasks can be found in `SEPIO_Requirements_Collection_Quick_Start.md` in this folder.
