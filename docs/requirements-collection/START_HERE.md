# START HERE — SEPIO Requirements Collection

This folder contains the resources you need to ask an AI agent to complete the SEPIO Requirements Forms for your biomedical knowledge project.

The goal is to capture **what your project currently represents and what it should support**, with a clean separation between:

- **current-state requirements**, grounded strictly in a defined canonical source/dataset/distribution; and
- **desired-state requirements**, which may draw on a broader evidence base to capture a maximal, evidence-supported requirements set for later human review.

At this stage, the agent should describe the project in its own terms rather than trying to choose SEPIO classes or properties.

After you review and confirm the completed forms, a separate SEPIO requirements-to-model step can determine which SEPIO model elements are relevant, where current SEPIO provides only partial coverage, and where follow-up or model extensions may be needed.

---

## What is in this folder

- `Requirements_Collection_Forms.xlsx` — the empty workbook your agent should complete.
- `Requirements_Instructions_and_Guidance_for_AI.md` — detailed semantic and field-by-field instructions intended primarily for the AI agent.
- `REQUIREMENTS_FORM_PROMPT.md` — the ready-to-copy prompt for asking an AI agent to complete the forms.
- `RESOURCE_INVENTORY_PROMPT.md` — an optional prompt that asks an AI agent to discover, classify, and organize project resources and propose candidate scope statements.
- `RESOURCE_INVENTORY_GUIDANCE.md` — practical guidance for assembling and reviewing a Resource Inventory.
- `PROJECT_SOURCE_CHECKLIST.md` — a checklist for gathering useful project schemas, documentation, examples, and other evidence.
- `Requirements_Collection_Overview.md` — the comprehensive human-facing overview of the requirements-collection workflow.
- `examples/example_scope_statement.md` — examples of project scope statements.
- `examples/example_completed_requirements_review.md` — an example Requirements Review Memo.
- `CONTENTS.md` — a list of files included in this package.

---

## Process at a glance

1. **Define the scope.** Decide exactly which canonical source(s) control current-state answers and which broader sources may inform desired-state requirements.
2. **Create a Resource Inventory.** Identify the best evidence, examples, versions, conflicts, and candidate scope statements.
3. **Give the inventory and materials to the agent.**
4. **Have the agent populate the Requirements Forms.**
5. **Inspect the workbook and review memo.** Resolve uncertainties and correct anything that does not reflect the project.
6. **Move to SEPIO mapping.** Once confirmed, use the requirements record as input to the separate requirements-to-model workflow.

---

# Step 1 — Define the Scope Statement

Before the requirements agent starts, define a **project scope statement**.

The scope statement is important because biomedical projects often have several different representations around them: internal curation data, canonical public distributions, intermediate pipeline artifacts, alternate releases, APIs, downstream knowledge graphs, and user-interface representations.

The scope statement tells the agent **which of these resources control current-state answers** and **which additional resources may inform desired-state answers**.

## Minimal vs maximal scope

A **minimal scope** describes only the canonical source/dataset/distribution selected for the review.

Example:

> **Current-state canonical source:** MeDIC `matrix_indication_list.xlsx`, version 1.3.0.  
> Current-state and desired-state requirements should both be limited to information represented in this canonical distribution.

This produces a conservative requirements record describing that specific distribution.

A **maximal scope** still defines a strict canonical source set for current state, but allows a broader evidence base for desired-state requirements.

Example:

> **Current-state canonical source:** MeDIC `matrix_indication_list.xlsx`, version 1.3.0. Current-state answers must be based only on this distribution.  
> **Desired-state evidence:** additional MeDIC-maintained intermediate curation artifacts, alternate distributions, the MeDIC paper and project documentation, and explicit project requirements may be used to identify a broader, evidence-supported desired-state requirements set. Where desired state differs from current state, the supporting source must be named in `Explanation / Considerations`.

This keeps the current-state answers reproducible while allowing the first-pass desired-state requirements to be intentionally broad. A human reviewer can later narrow that maximal set.

## How to create the scope statement

If the appropriate scope is already obvious, write it yourself.

If not, use `RESOURCE_INVENTORY_PROMPT.md`. The resource-discovery agent will propose:

- a **minimal / canonical-distribution-only** scope;
- a **maximal / canonical current state + broad desired state** scope;
- additional alternatives when justified;
- a recommended scope.

Review or refine one of those candidate statements, then paste the finished scope statement into the `SELECTED PROJECT SCOPE` section of `REQUIREMENTS_FORM_PROMPT.md`.

If the project has genuinely different canonical products with different evidence/provenance behavior, consider completing separate requirements reviews.

---

# Step 2 — Create a Resource Inventory

A **Resource Inventory** is a structured list of the project materials that can support the requirements review.

It is useful because it tells the requirements agent:

- which resources are canonical for current state;
- which additional resources may inform desired state;
- which examples to inspect;
- which sources are historical, upstream, downstream, or context only;
- which versions should be used;
- what conflicts or uncertainties exist;
- what the agent should retrieve itself versus what a human may need to provide.

You can assemble the inventory yourself, or use `RESOURCE_INVENTORY_PROMPT.md` to have an AI agent take a first pass.

If you use the agent-generated inventory, review its source roles, versions, proposed scopes, and exclusions before proceeding.

For detailed instructions, source categories, examples, and inventory structure, see:

**`RESOURCE_INVENTORY_GUIDANCE.md`**

---

# Step 3 — Give the Resource Inventory and Project Materials to the Agent

How you provide the evidence depends on how you created the inventory.

## If you assembled the inventory yourself

You can:

- upload the relevant files directly;
- provide public repository, DOI, or documentation links;
- provide a manifest/inventory containing precise pointers to the relevant resources;
- point to specific files or directories rather than an entire repository when appropriate.

For large datasets, representative records plus the schema/data dictionary may be enough unless the agent needs the full data to answer a specific question.

## If you are using an AI-generated Resource Inventory

Upload or link the reviewed `[PROJECT]_Resource_Inventory.md` along with the requirements prompt.

The inventory should tell the requirements agent which public resources it should retrieve itself. Do not manually upload every public file unless direct retrieval fails or human access/clarification is genuinely required.

---

# Step 4 — Have the Agent Populate the Requirements Forms

Give the agent:

1. `REQUIREMENTS_FORM_PROMPT.md`
2. the selected project scope statement
3. `Requirements_Collection_Forms.xlsx`
4. `Requirements_Instructions_and_Guidance_for_AI.md`
5. the reviewed Resource Inventory
6. any private/local files that the inventory identified as necessary

You can either:

- upload the form and guidance files directly; or
- put links/pointers to the exact versions you want the agent to use into `REQUIREMENTS_FORM_PROMPT.md`.

The agent should follow these principles:

- **Current-state answers must come only from the canonical source set named in the selected scope.**
- **Desired-state answers may use the broader evidence set allowed by the selected scope.**
- Desired state should be **maximal but evidence-supported**, not speculative.
- When desired state differs from current state, the agent should say what source supports the broader requirement in `Explanation / Considerations`.
- The agent should distinguish:
  - canonical project data from upstream or downstream representations;
  - current representation from desired capability;
  - evidence items from evidence interpretation;
  - evidence strength from confidence in extraction/alignment;
  - stored provenance from process documentation.
- If the available information does not support a confident answer, the agent should use **M / Maybe / Needs discussion** or otherwise flag uncertainty rather than guessing.
- The agent should not use SEPIO mappings to decide what the project requirements are. Requirements come first; mapping comes later.

---

# Step 5 — Inspect the Deliverables

The requirements agent should return two main deliverables.

## 1. Completed Requirements Workbook

The completed workbook should preserve the original template formatting and contain the project's current-state and desired-state responses.

The filename should include project name, version, date, and time, for example:

`MeDIC_Requirements_v0.2_20261013_1643.xlsx`

## 2. Requirements Review Memo

The memo should summarize:

- the selected project scope;
- the exact sources used for **current-state** answers;
- the broader sources used for **desired-state** answers;
- source versions/releases/commits where relevant;
- high-confidence conclusions;
- answers that need human review;
- conflicts, assumptions, and missing information;
- inaccessible resources, if any;
- observations about the forms/guidance;
- a small set of representative data examples.

The memo should include:

- a few examples directly from the canonical current-state source; and
- a few broader/maximal examples from desired-state sources when they reveal additional requirements.

Examples should be represented as close to the source structure as practical—for example, table rows for tabular data, JSON/YAML for structured documents, or triples/edges for graph data.

## What to review

Focus especially on places where the agent had to interpret ambiguous evidence or infer desired-state intent.

Ask:

- Did it assess the **right canonical current-state source**?
- Did it use only that source set for current-state answers?
- Did it use the broader desired-state sources only where the selected scope allowed them?
- When current and desired state differ, did it identify the supporting desired-state source?
- Did it capture the major **claim types**?
- Did it correctly identify what the project treats as **evidence**?
- Did it distinguish evidence items from evidence interpretation?
- Did it capture provenance at the correct level?
- Did it avoid importing rich information that exists only in upstream sources unless the selected scope explicitly allows it as desired-state evidence?
- Did it avoid treating downstream API/display enrichments as canonical current-state requirements?
- Did it flag unsupported answers instead of guessing?
- Do the worksheets and memo tell a coherent story?

Correct anything that does not accurately reflect the project.

Once you are comfortable with the workbook, treat it as the **confirmed project requirements input**.

---

# Step 6 — What Can Happen Next

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

The requirements-collection workflow should first answer:

> What does the selected canonical source currently represent, and what broader capabilities does the project evidence support as desired requirements?

Only after those requirements are reviewed should the mapping workflow ask:

> How well does SEPIO represent those needs?

---

## More detailed guidance

A more comprehensive overview of the workflow and tasks can be found in `Requirements_Collection_Overview.md`.

Detailed guidance for building and reviewing the project evidence set can be found in `RESOURCE_INVENTORY.md`.
