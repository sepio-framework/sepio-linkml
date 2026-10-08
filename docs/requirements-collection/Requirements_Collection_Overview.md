# SEPIO Requirements Collection — Project Representative Overview

**Audience:** Project representatives who are asking an AI agent to complete the SEPIO Requirements Forms for their project

## 1. What this process is for

The SEPIO Requirements Forms describe what a biomedical knowledge project needs to represent about claims, evidence, interpretation, and provenance.

The goal is **not** to redesign your project or force it into SEPIO while the forms are being completed.

Instead, the process asks:

> What kinds of knowledge does your project represent, what evidence or provenance does it preserve, and what capabilities does the project actually need?

After the forms are reviewed and confirmed, a separate SEPIO requirements-to-model workflow can use them to:

- identify relevant SEPIO classes and attributes;
- generate a candidate project-specific SEPIO covering model;
- identify partial SEPIO coverage;
- identify model gaps or extension needs;
- generate implementation guidance; and
- identify questions requiring project or SEPIO modeler review.

The completed forms are therefore a description of **your project's requirements**, not a list of SEPIO features you have chosen.

## 2. What is in this starter package

This folder contains:

- `START_HERE.md` — a short orientation and step-by-step entry point.
- `Requirements_Collection_Overview.md` — this comprehensive overview of the requirements-collection workflow.
- `Requirements_Collection_Forms.xlsx` — the empty requirements workbook the agent should complete.
- `Requirements_Instructions_and_Guidance_for_AI.md` — detailed form instructions intended primarily for the AI agent.
- `AGENT_PROMPT.md` — a ready-to-copy prompt for tasking the agent.
- `PROJECT_SOURCE_CHECKLIST.md` — a checklist for gathering project schemas, documentation, examples, and other evidence.
- `SOURCE_DISCOVERY_PROMPT.md` — an optional agent prompt for discovering and organizing project sources before form completion.
- `examples/example_scope_statement.md` — example project scope statements.
- `examples/example_completed_requirements_review.md` — an example of the short review memo the agent should return with the completed forms.

These files are designed to stay together in one directory in the repository.

## 3. Your role

As project representative, you should:

1. define clearly what project/data product the requirements apply to;
2. gather the best available project documentation and examples;
3. provide those sources plus the bundled forms and detailed guidance to an AI agent;
4. use the prompt in `AGENT_PROMPT.md` to task the agent;
5. review the completed workbook and accompanying review memo;
6. correct answers that do not accurately reflect the project; and
7. confirm the workbook as the project's requirements input.

You do **not** need to understand the SEPIO model in detail to complete this process.

## 4. Define the project scope first

Before asking the agent to populate the forms, write a one- or two-sentence scope statement.

Be explicit about what counts as the project whose requirements are being elicited.

For example:

> The project is the canonical MonarchKG data model and KG build output. Requirements should reflect what MonarchKG itself stores and represents, not richer evidence/provenance/confidence information available only in upstream source databases and not downstream API or display enrichments unless they are part of the canonical KG output.

More examples are provided in `examples/example_scope_statement.md`.

If a project has several substantially different products or representations, consider completing separate requirements forms for each.

## 5. Gather project evidence

Use `PROJECT_SOURCE_CHECKLIST.md`.

The most useful resources include:

| Resource type | Why it helps |
|---|---|
| Authoritative schema or data model | Shows what entities, relationships, fields, and structures the project actually represents. |
| Data dictionary / field documentation | Explains field meaning, allowed values, cardinality, and intended use. |
| Model/design documentation | Explains why structures exist and what the project intends to represent. |
| Representative example records | Shows how the model is actually used in practice. |
| Source/ingest documentation | Shows which upstream information is retained, transformed, or discarded. |
| Curation guidelines / SOPs | Helps interpret claims, evidence evaluation, confidence, review, and provenance. |
| User/API documentation | May reveal required capabilities not obvious from the schema. |
| Project papers / overview documents | Provides project goals and knowledge scope. |
| Requirements / competency questions | Captures intended capabilities that may not yet be fully implemented. |

You do not need every resource type. The agent needs enough evidence to answer each form question responsibly.

### Optional agent-assisted source discovery

A project representative does not need to identify every relevant source manually.

If the important materials are distributed across repositories, documentation sites, generated model documentation, papers, APIs, or example data, use `SOURCE_DISCOVERY_PROMPT.md` before beginning form completion.

That prompt asks an agent to:

- start from the project scope statement;
- identify current authoritative model/schema sources;
- identify useful design, curation, ingest, and provenance documentation;
- select a small, diverse set of representative data/examples;
- record precise URLs/repository paths and version information where available;
- distinguish canonical project sources from upstream and downstream systems;
- flag stale/conflicting sources;
- identify inaccessible materials that the project representative may need to provide; and
- recommend the source set the requirements-completion agent should actually use.

The result is a proposed **Source Inventory / Evidence Package**. Review or stabilize that source inventory before requirements elicitation begins.

If the project representative already has a well-curated source package, this step can be skipped.

## 6. Evidence hierarchy

When project sources disagree, the agent should generally prioritize:

1. the explicit project scope statement;
2. the current authoritative schema/data model;
3. current project/model documentation and curation rules;
4. current representative data/examples;
5. implementation or ingest documentation;
6. older papers or historical documentation.

A source can describe information available upstream without implying that the assessed project itself represents it.

The agent should distinguish:

- information the project currently represents;
- information the project explicitly requires but may not yet represent;
- information available only in upstream sources;
- information created or enriched only downstream.

## 7. Give the agent the bundled resources

At minimum, provide the agent:

- `Requirements_Collection_Forms.xlsx`
- `Requirements_Instructions_and_Guidance_for_AI.md`
- your project scope statement
- the relevant project source materials, or the reviewed source set produced using `SOURCE_DISCOVERY_PROMPT.md`

Then use the prompt in `AGENT_PROMPT.md`.

The Requirement→SEPIO mapping registry is intentionally **not** included in this starter package. Initial requirements elicitation should be requirements-first, not SEPIO-first.

The later mapping step can use the confirmed requirements workbook together with the mapping registry and SEPIO schema.

## 8. How the agent should reason

The agent should triangulate across:

```text
Project intent
        +
Authoritative schema/model
        +
Field documentation
        +
Representative records
        +
Curation/ingest rules
        +
Known requirements/use cases
```

For each substantive requirement, it should be able to answer:

> What project evidence supports this answer?

If that cannot be answered, the response should be marked uncertain rather than guessed.

## 9. Important distinctions to preserve

### Current representation vs desired requirement

A project may require information that is not yet represented in its current schema.

When documentation clearly establishes the requirement, the forms should capture that requirement and note the implementation gap.

### Upstream source capability vs project capability

If an upstream source contains rich evidence metadata but the project discards it during ingest, that metadata is not automatically a requirement of the assessed project.

### Canonical model vs API/UI enrichment

If an API or UI computes or enriches information that is not part of the canonical project data model, do not automatically treat it as a canonical model requirement.

### Claim semantics vs evidence/provenance

A project may support many biomedical claim types while using the same relatively simple evidence/provenance envelope for all of them.

Assess these dimensions separately.

### Missing information vs negative requirement

Silence in the documentation is not automatically equivalent to "the project does not need it."

Use uncertainty/review mechanisms when appropriate.

## 10. What the agent returns

The prompt asks the agent for two deliverables:

### A. Completed requirements workbook

A completed copy of `Requirements_Collection_Forms.xlsx`.

### B. Requirements Review Memo

A short memo containing:

- project scope used;
- project materials consulted;
- high-confidence conclusions;
- answers requiring human review;
- apparent conflicts or missing information;
- form/guidance questions that were difficult to interpret;
- important assumptions.

An example is provided in `examples/example_completed_requirements_review.md`.

## 11. Human review checklist

When the agent returns the forms, focus review on:

| Review question | What to check |
|---|---|
| Scope | Did the agent assess the intended project/data product rather than upstream/downstream systems? |
| Claims | Are the major kinds of assertions represented by the project captured? |
| Evidence | Are important evidence item categories and evidence relationships represented? |
| Interpretation | Did the agent correctly distinguish evidence from interpreted evidence, direction/strength, grouping, and higher-level synthesis? |
| Provenance | Are source, authorship, method, process, retrieval, and other provenance requirements captured at the right level? |
| Current vs desired | Did the agent avoid equating current implementation limitations with project requirements? |
| Upstream EPC | Did the agent avoid importing evidence/provenance/confidence capabilities that exist only upstream? |
| Uncertainty | Did the agent flag unsupported or ambiguous answers rather than guessing? |
| Consistency | Do responses across forms tell a coherent story? |
| Examples | Are representative examples accurate and useful? |

The immediate goal is to confirm that the forms accurately describe the project.

## 12. What happens after the forms are confirmed

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
7. Requirements Collection & Form Feedback
8. Generation Manifest

During the current AI-first pilot phase, an AI agent can generate these artifacts with transparent provenance. A future production workflow can move exact schema extraction, dependency closure, validation, traceability, and manifest generation into deterministic code.

## 13. What project representatives are not expected to do

Project representatives do not need to:

- learn the complete SEPIO model before filling out the forms;
- manually map project fields to SEPIO classes and slots;
- decide whether a SEPIO gap exists;
- design SEPIO extensions;
- understand dependency closure; or
- create the Candidate Covering Model themselves.

Their responsibility is to help establish **accurate project requirements**.

## 14. Minimum evidence standard

Before considering a requirements workbook ready for confirmation, the agent should ideally have:

- a clear project scope statement;
- at least one authoritative structural source;
- at least one source explaining project/model intent;
- representative examples of actual data or records;
- enough information to distinguish project content from upstream/downstream information; and
- explicit review flags for questions the available sources cannot answer.

Projects lacking one or more of these can still participate, but the resulting workbook should contain more uncertainty/review flags.

## 15. Key principle

The requirements process is **requirements-first, not SEPIO-first**.

The project representative and agent should answer:

> What does this project need to represent?

Only after those requirements are reviewed should the SEPIO mapping workflow ask:

> How well does SEPIO represent those needs?
