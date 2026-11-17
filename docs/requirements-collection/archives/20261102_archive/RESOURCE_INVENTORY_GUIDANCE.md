# Resource Inventory — Guidance for SEPIO Requirements Collection

A Resource Inventory is the evidence package used to support a SEPIO requirements review.

Its purpose is not merely to list project files. It should make clear:

- which exact source(s) control **current-state** requirements;
- which additional sources may inform **desired-state** requirements;
- which sources are context only;
- which versions/releases should be used;
- what examples best demonstrate the project semantics;
- what conflicts, missing information, or access issues remain.

For many projects, the easiest way to create a first draft is to use `RESOURCE_INVENTORY_PROMPT.md`.

---

## 1. Start with the canonical current-state source

Identify the exact source, dataset, distribution, schema, or release that should control answers to:

> **Used in Current Data?**

Examples:

- a specific version of `indications.xlsx`;
- a current LinkML schema release plus designated canonical records;
- a particular KG build/export;
- a database schema plus one named production distribution.

Prefer a version-pinned source when possible.

If several artifacts must be interpreted together—for example a data table plus its canonical data dictionary—identify them as **canonical companion artifacts**.

Do not automatically include intermediate files, alternate releases, upstream sources, downstream APIs, or papers in the current-state source set.

---

## 2. Identify sources that may inform desired state

Desired-state requirements can use a broader project evidence base when the selected scope permits it.

Useful sources may include:

- explicit requirements or roadmaps;
- current papers or model documentation;
- curation/evidence guidance;
- intermediate curation or analysis artifacts;
- fields captured in the pipeline but dropped from the canonical export;
- alternate or earlier project distributions;
- competency questions;
- implementation/design documents.

When useful, classify these sources as:

### EXPLICIT_FUTURE_REQUIREMENT

The project explicitly says it wants or needs the capability.

Examples:
- roadmap item;
- GitHub issue;
- requirements document;
- approved competency question.

### EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT

The project already captures or uses the information somewhere, but it is absent from the chosen canonical current-state distribution.

Examples:
- semantic-alignment intermediates retained in curation files but dropped from a final compact export;
- provenance stored in an internal curation record but not emitted publicly.

### DOCUMENTED_MODEL_INTENT

Authoritative project documentation describes the capability as part of the intended model/product even though it is absent from the selected canonical distribution.

Examples:
- a current project paper describing qualifiers not present in the selected release;
- a modeling guide describing intended evidence structures.

Do not use a source to justify desired state if it explicitly says the feature is out of scope, rejected, or deprecated unless another authoritative source reverses that decision.

---

## 3. Gather representative examples

Real examples are essential because schemas and documentation may not show how fields are actually used.

Try to select a small but diverse set that covers important patterns, for example:

- a typical claim;
- a claim with qualifiers/context;
- a claim with a source/evidence reference;
- a claim with richer provenance;
- a record showing normalization or transformation;
- a case where information exists in an intermediate artifact but is dropped from the canonical export;
- an alternate distribution exposing a capability absent from the canonical one;
- an unusual but important edge case.

Assign stable IDs such as E01, E02, E03.

For each example, record:

- source;
- claim/record type;
- what requirement pattern it demonstrates;
- why it was selected.

---

## 4. Useful source categories

Depending on the project, useful resources may include:

### Schemas and formal models
- LinkML
- JSON Schema
- SQL schemas
- SHACL
- UML/class models
- data dictionaries
- export specifications

### Canonical distributions
- release spreadsheets
- JSON/YAML datasets
- KGX/RDF exports
- database dumps
- versioned API payload specifications

### Documentation
- model overview
- README files
- architecture/design documents
- semantic conventions
- project papers

### Curation/evidence materials
- curation SOPs
- evidence classification rules
- scoring/confidence guidance
- interpretation guidelines
- review/approval workflows

### Pipeline/provenance materials
- ingest/transformation documentation
- normalization/grounding procedures
- intermediate curation artifacts
- source-attribution rules
- logs or intermediate outputs when they reveal intentionally retained project information

### Requirements/future intent
- roadmaps
- GitHub issues
- requirements documents
- user stories
- competency questions
- approved design proposals

---

## 5. Distinguish neighboring resources from project requirements

Pay particular attention to resources that are nearby but not actually part of the scoped project.

Examples:

- upstream source databases;
- regulatory documents from which the project extracts information;
- external ontologies used for normalization;
- downstream KGs;
- APIs or user interfaces that add derived information;
- historical or superseded releases.

These may be useful for context, but they should not automatically control current-state answers.

They may inform desired state only when the selected scope explicitly permits them and the evidence is genuinely project-specific.

---

## 6. Record versions and conflicts

For every important resource, record:

- version;
- release;
- tag;
- commit SHA;
- DOI/archive version;
- retrieval date when no immutable version is available.

If two resources disagree:

1. identify the conflict;
2. identify which source controls current state;
3. state whether the other source may still inform desired state;
4. do not silently merge the two.

Example:

> Release v1.3 lacks qualifier fields, but the current project paper explicitly describes contextual hyperrelations. v1.3 controls current state; the paper may support desired state under a maximal scope.

---

## 7. Recommended Resource Inventory fields

A useful inventory table includes:

- Source ID
- Name
- Type
- URL / repository path
- Version / release / commit
- Authority level
- Requirements role
- Desired-state support type
- Requirement dimensions supported
- Important directly observed facts
- Access status
- Retrieval / human-assistance guidance
- Notes / cautions

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

---

## 8. Access and retrieval guidance

The requirements agent should normally retrieve public resources itself.

A human should need to intervene only when:

- public retrieval fails;
- authentication/private access is required;
- the file exists only locally;
- multiple plausible versions/files exist and the canonical one is unclear;
- the human must decide which scope/version is authoritative.

When human help is needed, the inventory should say:

- exactly what file/resource is needed;
- why it matters;
- what question it will resolve;
- whether the requirements review can proceed provisionally without it.

---

## 9. Candidate scope statements

A good Resource Inventory should end with candidate scope statements.

At minimum:

### Minimal / canonical-distribution-only

Use the canonical distribution as both the current-state and desired-state evidence base.

Best when the goal is to describe one concrete release conservatively.

### Maximal / canonical current state + broad desired state

Use only the named canonical source(s) for current-state answers, but allow broader project evidence for desired-state requirements.

Best when the goal is to discover the broadest evidence-supported requirements set before human review.

Additional scopes may be useful for projects with multiple legitimate products or distributions.

The project representative should review and select/refine one scope before final requirements completion.

---

## 10. Final handoff

Before giving the inventory to the requirements agent, make sure it clearly answers:

- What controls current-state answers?
- What may inform desired-state answers?
- Which scope was selected?
- Which sources are context only?
- Which examples should the agent inspect?
- What versions should it use?
- What public resources should it retrieve itself?
- Is any human-provided material genuinely required?
- What important questions remain unresolved?

If those questions are clear, the inventory is ready to accompany `REQUIREMENTS_FORM_PROMPT.md`.
