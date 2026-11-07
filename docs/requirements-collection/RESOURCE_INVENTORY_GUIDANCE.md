# Resource Inventory — Guidance for SEPIO Requirements Collection

A **Resource Inventory** is a structured catalog of project materials used to establish the scope and supporting basis for a SEPIO requirements review. It is more than a list of files: it records which resources are authoritative, how they may be used, which versions and examples should be inspected, and what uncertainty remains.

The inventory may be assembled by a project representative, another human facilitator, an AI agent, or a human–AI team. The guidance applies to all these approaches. **AI assistance is recommended but optional**; `RESOURCE_INVENTORY_PROMPT.md` can help generate a first draft for human review.

A useful inventory makes clear:

- which exact source(s) control **current-state** responses ([F1]);
- which additional sources may support **desired-state** responses ([F2]);
- which sources are context only and must not determine requirement responses;
- which versions, releases, and commits are in scope;
- which real example records best demonstrate the project's claim, evidence, provenance, and confidence semantics;
- what conflicts, missing information, or access limitations remain.

**The selected project scope statement governs source use.** The Resource Inventory documents and supports that choice, but an inventory entry does not by itself authorize use of a resource for [F1] or [F2]. An authorized project representative should review and confirm the selected scope before the requirements are treated as authoritative.

---

## 1. Start with the canonical current-state source

Identify the exact source, dataset, distribution, schema, or release that should control answers to the forms' **[F1] current-state** questions (such as *Used in Current Data?* or *Represented in Current Data?*).

Examples:

- a specific version of `indications.xlsx`;
- a current LinkML schema release plus designated canonical records;
- a particular knowledge-graph build/export;
- a database schema plus one named production distribution.

Prefer version-pinned resources where possible. If several artifacts must be interpreted together—for example, a data table and its authoritative data dictionary—identify the additional resources explicitly as **canonical companion artifacts**.

Do not automatically include intermediate files, alternate releases, upstream databases, downstream APIs or user interfaces, or papers in the current-state source set. These may supply context or desired-state support, but they control [F1] only if the selected scope explicitly includes them as canonical sources or canonical companions.

Be precise about what the designated artifact actually represents. Documentation that a process exists does not establish that provenance about that process is stored in canonical data; information available in an upstream system does not establish that the scoped project retains it.

---

## 2. Identify sources that may inform desired state

**[F2] desired-state** requirements may draw on a broader set of project-specific materials when the selected scope allows it. The goal is to capture a *maximal but source-supported* account of the capabilities the project wants in a future SEPIO-based representation—not an inventory of potentially useful features proposed by the facilitator or agent.

Useful sources may include:

- explicit future requirements, approved roadmaps, or decisions;
- current project papers, model descriptions, and documentation;
- curation, evidence interpretation, review, or scoring guidance;
- intermediate curation or analysis artifacts;
- fields captured by a project pipeline but omitted from the canonical export;
- alternate or earlier project distributions;
- competency questions;
- implementation and design documents;
- project-representative statements obtained during collaborative elicitation, with their status and rationale recorded.

Where useful, classify desired-state support by the following types:

### `EXPLICIT_FUTURE_REQUIREMENT`

An authoritative project source expressly says that a capability is wanted or needed.

Examples: an approved roadmap item, a GitHub issue expressing an accepted requirement, a requirements document, or an approved competency question.

### `EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT`

The project already captures or uses information somewhere in its own ecosystem, but that information is absent from the selected canonical current-state distribution.

Examples: semantic-alignment intermediates retained in curation files but dropped from a compact export; provenance in an internal curation record that is not emitted publicly.

### `DOCUMENTED_MODEL_INTENT`

Authoritative project materials describe a capability as part of the intended model or product even though the selected canonical distribution does not yet represent it.

Examples: a current project paper describing intended qualifiers not present in the selected release; a modeling guide describing proposed evidence structures.

Do not treat every proposed idea, undocumented possibility, or feature available in SEPIO as a project requirement. A resource explicitly describing a capability as out of scope, rejected, intentionally excluded, or deprecated does not support a positive desired-state requirement unless a later authoritative decision reverses that position.

**For every [F2] `Y` or `M`, there must be identifiable project-specific support.** A response of `M` must indicate both an affirmative basis for considering the capability and what remains unresolved; it should not merely mean “this might be useful.” Record source IDs and relevant decisions so that the basis can later be summarized in **[F4] Basis for F2 Response** and **[F5] Explanation / Considerations**.

---

## 3. Gather representative examples

Real examples are essential because schemas and prose documentation may not reveal how fields are actually populated or what implicit conventions mean. Select a **small but diverse** set of concrete records that illustrates important semantic and workflow patterns, for example:

- a typical empirical claim or concept-definition statement;
- a statement with qualifiers or contextual information;
- a statement linked to a source or Evidence Item;
- a record with richer provenance, review, or confidence information;
- a record illustrating interpretation of evidence relative to a target statement;
- a record showing normalization, semantic alignment, encoding, or retrieval;
- a case where an intermediate artifact contains information omitted from the canonical export;
- an alternate distribution exposing a capability absent from the canonical one;
- an unusual but important edge case.

Concept-definition statements—including synonyms, classifications, mappings, and naming or definition assertions—are **within scope when the project has relevant evidence, provenance, interpretation, or confidence requirements**. Do not exclude them categorically.

Assign stable example IDs such as `E01`, `E02`, and `E03`. For each example, record:

- source ID, release/version, and exact record locator or link;
- claim/record type and relevant original field names;
- what requirement pattern or semantic distinction it demonstrates;
- why it was selected;
- whether it comes from the canonical current-state set or a broader desired-state source.

Prefer accessible record-specific URLs, dataset-and-record identifiers, API queries, or stable file/line pointers. A project homepage is not a substitute for a record locator. Identify whether a link resolves to an actual record, documentation, or a general resource page.

If examples combine data from multiple tables, label them **DENORMALIZED** and identify the contributing records. If examples combine different sources or illustrate a proposed future shape, label them **COMPOSITE/ILLUSTRATIVE** or **SCHEMATIC**, respectively. Such examples are useful for discussion but do **not** establish what is represented in the canonical [F1] source set.

Where source semantics are implicit—for instance, several distinct meanings encoded in one free-text or provenance slot—it may be necessary to inspect actual values, develop a codebook, and discuss their meanings with a project representative **before** completing the forms. Document those decisions or uncertainties alongside the inventory.

---

## 4. Useful source categories

Depending on the project, useful resources may include:

### Schemas and formal models

- LinkML, JSON Schema, SQL schemas, SHACL, or UML/class models;
- data dictionaries, field descriptions, controlled vocabularies;
- export or serialization specifications.

### Canonical distributions

- release spreadsheets;
- JSON/YAML datasets;
- KGX/RDF exports;
- database dumps;
- versioned API payload specifications **when explicitly designated as canonical**.

### Documentation

- model overviews and README files;
- architecture/design documents;
- semantic conventions or source field codebooks;
- project papers.

### Curation and evidence materials

- curation SOPs;
- evidence classification or interpretation rules;
- scoring, confidence, and quality guidance;
- review, approval, or decision workflows.

### Pipeline and provenance materials

- ingestion/transformation documentation;
- normalization and grounding procedures;
- intermediate curation artifacts;
- source-attribution and encoding rules;
- logs or outputs showing relevant information generated or intentionally retained by the project.

### Requirements and future intent

- roadmaps and issue trackers;
- requirements documents and user stories;
- competency questions;
- approved design proposals;
- documented decisions from project-representative interviews.

A project does not need every source category. The goal is sufficient **relevant, traceable support** for accurate requirements assessment, not a comprehensive archive of everything related to the project.

---

## 5. Distinguish neighboring resources from project requirements

Resources closely associated with the project may not be part of its selected current-state source set. Examples include:

- upstream source databases or curated knowledge resources;
- regulatory or scientific documents from which the project extracts information;
- external ontologies used for terminology normalization;
- downstream knowledge graphs;
- APIs and user interfaces that add derived or display-only information;
- historical or superseded releases.

These may help explain what the project does, but should not automatically determine [F1] answers. They may inform [F2] only if allowed by the selected scope **and** if they establish a project-specific requirement rather than just a capability of an adjacent system.

Maintain distinctions among:

- **scientific evidence**: information evaluated as supporting or disputing a claim or concept-definition statement;
- **provenance**: information about origins, activities, decisions, agents, and transformations;
- **requirements support**: sources and rationale justifying why a form response is `Y`, `N`, or `M`.

A copied external assertion may establish *where a record came from* without independently corroborating its truth. The same external source can play different roles in different workflows; explain its actual role rather than treating the resource name alone as sufficient.

---

## 6. Record versions and conflicts

For every important resource, record the most specific reproducible identifier available:

- version or release number;
- release tag;
- commit SHA;
- DOI/archive version;
- retrieval date if the source is mutable or lacks an immutable version identifier.

If two resources disagree:

1. describe the conflict and the relevant source IDs;
2. identify which scoped source controls [F1];
3. explain whether the other source is permitted to support [F2];
4. record unresolved interpretation or authority questions for human review;
5. do not silently merge or reconcile the accounts.

**Example:** Release v1.3 lacks qualifier fields, but a current project paper explicitly describes intended contextual hyperrelations. Release v1.3 controls current state; the paper may support desired state under a scope that permits it.

If a later curator discussion or project decision changes an earlier interpretation, retain a traceable decision note rather than silently replacing the old rationale. The inventory need not become a full decision-management system, but it should point to a separate decision log or review memo when that is where the rationale is maintained.

---

## 7. Recommended Resource Inventory fields

A useful inventory table includes:

| Field | What to record |
|---|---|
| **Source ID** | Stable identifier for citing this resource in forms and review materials |
| **Name** | Descriptive resource title |
| **Type** | Dataset, schema, data dictionary, documentation, guideline, issue, record collection, etc. |
| **URL / repository path** | Direct, usable locator, preferably version-pinned |
| **Version / release / commit** | Reproducible version information and retrieval date as appropriate |
| **Authority level** | Whether the resource is canonical, authoritative for future intent, supporting, or contextual |
| **Requirements role** | Permitted use for current-state, desired-state, or context only |
| **Desired-state support type** | Nature of any affirmative future-requirement support |
| **Requirement dimensions supported** | Claim types/semantics, Evidence Items, interpretation, confidence, provenance, etc. |
| **Important directly observed facts** | Concise findings, distinguished from interpretation or inference |
| **Example record link(s)** | Actual representative record IDs/URLs and what they illustrate |
| **Access status** | Accessible, restricted, missing, broken link, unverified, etc. |
| **Retrieval / human-assistance guidance** | What may be fetched directly and what needs provision or confirmation |
| **Notes / cautions** | Conflicts, scope restrictions, limitations, unresolved interpretations |

Suggested requirements-role values:

- `CURRENT_STATE_CANONICAL`
- `CURRENT_STATE_CANONICAL_COMPANION`
- `DESIRED_STATE_SUPPORT`
- `CURRENT_AND_DESIRED`
- `CONTEXT_ONLY`

Suggested desired-state support values:

- `EXPLICIT_FUTURE_REQUIREMENT`
- `EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT`
- `DOCUMENTED_MODEL_INTENT`
- `N/A`

If using `CURRENT_AND_DESIRED`, be explicit about the source's **canonical authority for [F1]**; a general dual-role label must not silently broaden the current-state source set. The selected scope remains the controlling authority.

A single markdown table, spreadsheet, or other structured inventory is acceptable if it preserves these distinctions. For complex projects, companion sections for example records, scope alternatives, access problems, and unresolved decisions may be easier to review than extremely long table cells.

---

## 8. Access and retrieval guidance

When AI assistance is used, the agent should normally attempt to retrieve **publicly accessible** materials directly, including specified source files and versioned examples, rather than requiring a representative to upload everything in advance.

Human assistance may be needed when:

- public retrieval fails;
- authentication or private access is required;
- a resource exists only locally;
- several plausible versions or files exist and the canonical one is unclear;
- a project representative must decide the authoritative scope or interpretation.

For each blocker, record:

- the exact file/resource and attempted locator;
- why it matters and what question it would resolve;
- the access problem or required decision;
- whether the review can proceed provisionally without it.

Human-led inventory creation can use the same access-status and provenance conventions; no AI agent or automated retrieval capability is required. Never assume that a link has been inspected merely because it appears in the inventory.

---

## 9. Candidate scope statements

A Resource Inventory should support selection of a **project scope statement** before definitive requirements completion. If the appropriate scope is already known, it may simply document that selected scope; if not, prepare and compare reasonable alternatives.

### Minimal / canonical-distribution-only

Use the designated canonical source set for [F1] and limit [F2] to requirements supported by that same set.

Best when the goal is a conservative description of one concrete release or distribution. Do not infer broad future requirements merely from what the release makes technically possible.

### Maximal / canonical current state + broad desired state

Use only the named canonical source(s) and explicitly designated companions for [F1], while allowing a broader, approved set of project-specific sources for [F2].

Best when the goal is to identify the broadest **supported** requirements set for subsequent project-representative review and refinement.

Additional scope alternatives may be appropriate for projects with multiple canonical products, domain subsets, or significantly different publication/curation pathways. Separate reviews may be preferable when the products have materially different EPC requirements.

The project representative should review, select, and, if necessary, refine the scope. **Do not silently combine alternative scopes.** Record the final selected statement and which sources have authority under it.

---

## 10. Final handoff

Before the inventory is used to complete the requirements forms, confirm that it answers:

- What exact resources control [F1] current-state responses?
- What additional resources may support [F2] desired-state responses?
- Which scope has been selected, and who confirmed it?
- Which sources are context only?
- Which representative records should be inspected, and where can they be accessed?
- What versions or immutable identifiers should be used?
- Which resources are accessible, and which are not yet inspected?
- What materials must a human provide or what decisions require representative input?
- What conflicts, implicit data conventions, or unanswered questions remain?

If these questions are adequately addressed, the inventory is ready for use with `REQUIREMENTS_FORM_PROMPT.md` and `Requirements_Instructions_and_Guidance_for_Agents.md`.

The forms may then be populated through **human-led work, independent AI drafting followed by review, or collaborative interview-style elicitation**. In the collaborative approach, a facilitator or AI agent can present each requirement, examine real examples with the representative, propose responses, and record decisions or open questions. This is particularly useful where a source's semantics are implicit in curation conventions or expert practice.

**The completed requirements remain provisional until an authorized project representative confirms them.** Mapping those requirements to SEPIO and deriving a candidate Covering Model are separate downstream activities; neither should determine the project's requirement responses during elicitation.
