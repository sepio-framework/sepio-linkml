# Requirements Form Prompt — Complete the SEPIO Requirements Forms

Use this prompt after the project evidence base has been reviewed and, ideally, after a Resource Inventory / Evidence Package has been prepared using `RESOURCE_INVENTORY_PROMPT.md`.

The requirements workflow deliberately distinguishes **current-state requirements** from **desired-state requirements**:

- **Current state** is controlled by the canonical source(s), dataset(s), distribution(s), release(s), or explicitly designated companion artifacts named in the selected project scope statement.
- **Desired state** may be informed by a broader, evidence-supported set of project resources identified in the selected scope statement and Resource Inventory.

This separation is intentional. The current-state columns should remain conservative and reproducible, while the desired-state columns may capture a broader **maximal evidence-supported requirements set** for later human review and refinement.

Publicly accessible resources may be supplied as attachments, GitHub links, direct-download URLs, DOI/archive links, or version-pinned URLs. The agent should retrieve public resources itself whenever possible; human upload is a fallback.

## Copyable prompt

Copy the prompt below into your AI agent's interface and replace the bracketed text.

```text
You are acting as a requirements analyst and as a knowledgeable representative of [PROJECT NAME].

Your task is to populate the SEPIO Requirements Forms workbook based on the selected project scope and the project materials and workflow resources I provide.

PROJECT

[PROJECT NAME]

SELECTED PROJECT SCOPE

[Paste the selected scope statement here. Prefer a scope statement produced by RESOURCE_INVENTORY_PROMPT.md and reviewed/selected/refined by the project representative.]

The selected scope statement must identify, explicitly or by reference to the Resource Inventory:

1. CURRENT-STATE CANONICAL SOURCE SET
   The exact source(s), dataset(s), distribution(s), release(s), or explicitly designated companion artifacts that control answers in the "Used in Current Data?" / current-state columns.

2. DESIRED-STATE EVIDENCE SET
   The broader set of project resources that may be used to identify desired/future requirements.

If the selected scope statement does not make these two source sets clear enough to apply reproducibly, stop and ask the project representative to clarify the scope before completing the forms.

REQUIREMENTS-COLLECTION MATERIALS

You will be provided access to the materials needed for this task. They may be supplied as:

- files attached directly to this prompt;
- public GitHub repository links;
- direct-download URLs;
- version-pinned GitHub URLs identifying a specific commit, tag, or release;
- DOI/archive links;
- other public project URLs or repository paths;
- a reviewed Resource Inventory / Evidence Package produced using `RESOURCE_INVENTORY_PROMPT.md`-  which may contain pointers/links to the types of resources above.

The core requirements-collection materials are:

1. `Requirements_Collection_Forms.xlsx`
2. `Requirements_Instructions_and_Guidance_for_AI.md`

A project Resource Inventory / Evidence Package should also be supplied when available.

REQUIREMENTS MATERIAL LOCATIONS

Requirements forms:
[ATTACHMENT OR URL TO Requirements_Collection_Forms.xlsx]

Instructions and guidance:
[ATTACHMENT OR URL TO Requirements_Instructions_and_Guidance_for_AI.md]

Resource inventory / evidence package, if available:
[ATTACHMENT OR URL TO PROJECT_Resource_Inventory.md]

Additional project materials, if any:
[ATTACHMENTS, URLS, DOI LINKS, OR REPOSITORY PATHS]

MATERIAL ACCESS RULES

1. If a public GitHub, DOI/archive, or other repository URL is provided, retrieve and use the referenced material directly.

2. For Markdown, YAML, JSON, CSV, text, schema, or similar files:
   - read the repository file directly when possible;
   - prefer the exact referenced version when the URL is version-pinned.

3. For `Requirements_Collection_Forms.xlsx` or any other binary spreadsheet:
   - retrieve/download the actual XLSX file;
   - do not rely on a rendered GitHub preview as a substitute for the workbook;
   - use the downloaded workbook itself as the template to populate.

4. If both a repository page URL and a direct/raw download URL are available for an XLSX file, prefer the direct downloadable file for workbook processing.

5. Do not require the project representative to manually download and re-upload a publicly accessible file unless you are unable to retrieve it yourself.

6. If a required file cannot be accessed:
   - identify the exact file/resource you could not retrieve;
   - provide the URL/path you attempted to use;
   - explain why the file is needed;
   - state whether the requirements review can proceed provisionally without it;
   - ask the project representative to upload that specific file only when necessary.

7. If a repository, DOI landing page, release page, or archive contains multiple plausible files, versions, or artifacts and the canonical one cannot be identified confidently, do not guess. Flag the ambiguity and ask for confirmation.

VERSION AND REPRODUCIBILITY RULES

8. Prefer version-pinned URLs when they are provided.

A version-pinned source may identify:
- a Git commit;
- a release tag;
- a versioned release;
- a DOI/archive version;
- another immutable version identifier.

9. If a version-pinned URL is provided, treat that exact version as authoritative for this requirements run unless explicitly instructed otherwise.

10. If only a moving branch such as `main` or `master` is provided:
   - use the current version available at the time of the review;
   - record the repository path and, when possible, the commit SHA, release identifier, or retrieval date used;
   - do not silently substitute an older cached or historical version.

11. If both a version-pinned source and a newer unpinned source are supplied:
   - do not silently merge them;
   - follow the source-role rules in the selected scope statement;
   - record materially relevant differences.

12. Record enough source-version information in the Requirements Review Memo that another agent could reproduce the review later.

RESOURCE INVENTORY / EVIDENCE PACKAGE

13. When a reviewed Resource Inventory / Evidence Package is supplied:
   - use the selected scope statement as the controlling rule for current-state and desired-state evidence;
   - use sources classified as CURRENT_STATE_CANONICAL only for current-state answers unless the scope statement explicitly designates additional canonical companion artifacts;
   - use DESIRED_STATE_SUPPORT sources only for desired-state reasoning, unless they are also designated CURRENT_STATE_CANONICAL;
   - use REPRESENTATIVE EXAMPLES to verify actual data usage;
   - do not treat sources marked CONTEXT_ONLY / DO NOT TREAT AS CANONICAL as evidence of requirements;
   - preserve unresolved issues for human review rather than guessing.

14. If the Resource Inventory identifies public files that should be inspected during requirements elicitation, attempt to retrieve those files yourself before asking the project representative to upload them.

15. If the Resource Inventory and a directly inspected canonical source disagree:
   - the selected canonical current-state source controls the current-state answer;
   - flag the discrepancy;
   - do not silently alter the current-state answer based on a noncanonical source.

16. If the Resource Inventory identifies material that a human may need to provide, first determine whether you can retrieve it yourself. Human upload is a fallback, not the default.

Use `Requirements_Instructions_and_Guidance_for_AI.md` to understand each form, question, controlled value, and response convention.

CURRENT-STATE VS DESIRED-STATE RULES

17. Treat the two requirements columns as answering different questions.

CURRENT STATE / F1:
"What is represented in the canonical current-state source set selected for this review?"

DESIRED STATE / F2:
"What should the SEPIO-based representation support, based on the maximal evidence-supported project requirements allowed by the selected scope?"

18. Populate CURRENT STATE strictly from the selected CURRENT-STATE CANONICAL SOURCE SET.

Do not mark a requirement as currently represented merely because it appears in:
- an intermediate curation artifact;
- an earlier or alternate release;
- a different distribution;
- a paper or documentation page;
- a roadmap;
- an upstream source;
- a downstream application;
unless that resource is explicitly included in the selected current-state canonical source set.

19. Populate DESIRED STATE from the broader DESIRED-STATE EVIDENCE SET permitted by the selected scope statement.

This may include, when relevant and not explicitly out of scope:
- explicit future requirements or roadmaps;
- current project documentation and papers;
- intermediate curation/analysis artifacts;
- information captured elsewhere in the project's own pipeline but dropped from the canonical export;
- alternate or earlier project distributions;
- other project-maintained representations;
- project examples, competency questions, or implementation guidance.

20. For the initial requirements pass, prefer a MAXIMAL EVIDENCE-SUPPORTED desired-state requirements set when the selected scope authorizes it.

"Maximal" does NOT mean speculative. Every desired-state Y/M answer must be supported by project-specific evidence.

The human reviewer may later narrow or remove desired-state requirements.

21. When a desired-state answer differs from the current-state answer, explicitly document the supporting source in the form's `Explanation / Considerations` field.

When useful, classify the desired-state support using one of these labels:

- EXPLICIT_FUTURE_REQUIREMENT
  A roadmap, issue, requirements document, competency question, or explicit statement says the project wants/needs the capability.

- EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT
  The project already captures or uses the information in an intermediate artifact, alternate distribution, curation workflow, analysis product, or other project-maintained representation, but it is absent from the selected canonical current-state distribution.

- DOCUMENTED_MODEL_INTENT
  A paper, model/design document, curation guide, or other authoritative project documentation describes the capability as part of the intended project model or data product, even if it is absent from the selected canonical current-state source.

Recommended explanation format when F1 and F2 differ:

"Current state: [brief canonical-source observation].
Desired-state support: [SUPPORT TYPE] — [Source ID/title/version]: [brief evidence and rationale]."

22. If several desired-state sources support the same requirement, cite the strongest and most direct source(s) rather than listing everything.

23. A source that explicitly says a capability is out of scope, rejected, deprecated, or intentionally excluded should not be used to justify a desired-state requirement unless another authoritative source explicitly reverses that decision.

IMPORTANT REQUIREMENTS-ELICITATION RULES

24. Answer the forms based on what this project actually represents or explicitly requires. Do not choose answers because they map conveniently to SEPIO.

25. Respect the selected project scope statement. Distinguish the scoped project/data product from:
   - upstream source systems;
   - internal systems outside scope;
   - downstream APIs;
   - user-interface/display enrichments;
   - derived products outside scope, unless explicitly admitted as desired-state evidence.

26. Distinguish:
   - information represented by the selected canonical current-state source;
   - information supported only as a desired-state requirement;
   - information available only in upstream sources;
   - information created or enriched only downstream;
   - process metadata that documents how data were generated but is not itself represented in the canonical source.

27. Use representative data/examples to confirm how the model is actually used, but do not infer a project-wide requirement from a single unusual record unless other evidence supports it.

28. Ground answers in supplied or discovered evidence. Distinguish what a source explicitly establishes from what you infer.

29. Do not invent missing requirements. If available project materials do not provide enough information to answer confidently:
   - use the form's uncertainty/review mechanism where available;
   - preserve the uncertainty;
   - flag the issue clearly for human review.

30. Preserve project-specific terminology and examples in explanatory fields where useful.

31. For each non-obvious answer, keep track of the source evidence that supports it so that the answer can be reviewed and traced back to its source.

32. Assess the project comprehensively across:
   - claim/assertion types;
   - claim representation structure;
   - semantic structure of reified claims;
   - evidence item types and representations;
   - evidence interpretation, grouping, direction, strength, and stacking;
   - provenance about information artifacts, agents, methods, processes, semantic alignment, encoding, and retrieval;
   - relationships between claim types and evidence types.

33. Do not use the Requirement→SEPIO mapping registry to decide what the project's requirements should be unless explicitly instructed to do so. Requirements elicitation must remain independent of current SEPIO coverage.

34. Do not proceed to Requirement→SEPIO mapping or generate a SEPIO covering model unless explicitly asked.

WORKBOOK HANDLING RULES

35. Populate the provided `Requirements_Collection_Forms.xlsx` workbook itself rather than recreating the forms from scratch.

36. Preserve the workbook's existing visual formatting and structure, including:
   - sheet names;
   - row and column positions;
   - fills/shading;
   - fonts;
   - borders;
   - alignment;
   - word wrapping;
   - row heights;
   - column widths;
   - data validation;
   - other template formatting.

37. Change only the cells needed to enter project responses, explanations, examples, or explicitly requested review notes.

38. Do not redesign, restyle, normalize, or rebuild the workbook.

39. If technical limitations prevent safe editing of the workbook without altering its formatting, stop and report the limitation rather than silently rebuilding the workbook in a different style.

40. The returned XLSX should open normally in Excel without triggering a repair/recovery warning. Do not "fix" workbook internals by reconstructing the workbook if doing so changes the visible template formatting. If an Excel-integrity problem cannot be corrected without risking formatting changes, report it for human review.

COMPLETENESS AND CONSISTENCY REVIEW

41. Before finalizing the workbook, perform a completeness and consistency pass:
   - check every applicable field;
   - compare answers across forms;
   - identify contradictions;
   - identify unanswered or weakly supported questions;
   - identify places where free text implies a requirement not captured by a structured response;
   - verify that every F1/current-state Y/M answer is supported by the selected current-state canonical source set;
   - verify that every broader F2/desired-state Y/M answer is supported by an allowed desired-state source;
   - verify that F1 and F2 were not conflated;
   - make sure upstream evidence/provenance capabilities were not incorrectly attributed to the canonical project source;
   - make sure process provenance described in documentation is not automatically treated as provenance stored in canonical records;
   - make sure downstream transformations are not treated as native current-state representation unless the selected scope says otherwise;
   - verify that the Explanation / Considerations field names the desired-state supporting source whenever F2 differs materially from F1.

42. Preserve unresolved issues rather than forcing a Y/N answer when the evidence supports uncertainty.

DELIVERABLES

A. Completed requirements workbook

Return a completed copy of the supplied workbook.

FILE NAMING:
Use:

[PROJECT]_Requirements_v[VERSION]_[YYYYMMDD]_[HHMM].xlsx

Example:
MeDIC_Requirements_v0.2_20261013_1643.xlsx

Use 24-hour/military time. Use `HHMM` without a colon for cross-platform filename compatibility.

If a prior requirements version is supplied, increment or retain the version according to the project representative's instruction. If no version is specified, use `v0.1`.

Preserve the original workbook formatting and structure.

B. Requirements Review Memo

Return a Markdown memo named:

[PROJECT]_Requirements_Review_Memo_v[VERSION]_[YYYYMMDD]_[HHMM].md

The memo must contain:

1. Project scope used
   - reproduce or precisely summarize the selected scope statement;
   - explicitly identify the CURRENT-STATE CANONICAL SOURCE SET;
   - explicitly identify the DESIRED-STATE EVIDENCE SET.

2. Requirements-workflow materials used

3. Sources used for CURRENT-STATE requirements
   - list the exact datasets/distributions/schema artifacts that controlled F1/current-state responses;
   - record exact versions/releases/commits/DOI/archive versions/retrieval dates as applicable;
   - explain any explicitly designated canonical companion artifacts.

4. Sources used for DESIRED-STATE requirements
   - list the broader sources actually used to populate F2/desired-state responses;
   - group or annotate them where useful as:
     EXPLICIT_FUTURE_REQUIREMENT,
     EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT,
     DOCUMENTED_MODEL_INTENT;
   - identify sources considered but excluded from desired-state reasoning and why.

5. High-confidence conclusions

6. Answers requiring human review

7. Apparent conflicts or missing information

8. Files/resources the agent was unable to access, if any

9. Form/guidance questions that were difficult to interpret

10. Important assumptions made

11. Project observations that suggest improvements to the requirements forms or guidance

12. Diverse representative data examples

Include a small but diverse set of concrete examples that make the requirements tangible.

Provide:
- a few CURRENT-STATE examples directly from the selected canonical source set; and
- a few broader/maximal DESIRED-STATE examples drawn from allowed desired-state sources when these reveal additional requirements.

For each example, record:
- Example ID
- Current-state or desired-state example
- Source ID/title/version
- What requirement pattern it demonstrates

Represent the example as close to its source representation as practical:

- tabular/database source:
  show the example as a row/table with the original field/column names where possible.
  If a complete logical record is distributed across multiple tables, it is acceptable to denormalize the relevant fields into a single illustrative row, but label it as DENORMALIZED and identify the contributing source tables.

- JSON/YAML document:
  show a compact JSON/YAML object preserving source field names and nesting.

- RDF/graph data:
  show triples/quads/edge properties as appropriate.

- free text/document source:
  show only the minimal relevant excerpt/fields necessary to demonstrate the requirement; do not reproduce unnecessary copyrighted text.

- composite/maximal example assembled from several project sources:
  label it COMPOSITE/ILLUSTRATIVE, identify every contributing source, and do not present the assembled record as if it existed verbatim in one source.

Do not fabricate values to make examples look complete.

C. Source-access status

Include a concise statement confirming:

- which linked resources were successfully retrieved;
- which attached files were used;
- whether any fallback human uploads were required;
- whether the review used version-pinned or moving-source URLs;
- any public resources that could not be retrieved.

Do not proceed to Requirement→SEPIO mapping or generate a SEPIO covering model unless I explicitly ask you to do so.
```

## What to provide to the agent

Provide access to:

- `Requirements_Collection_Forms.xlsx`
- `Requirements_Instructions_and_Guidance_for_AI.md`
- the **selected project scope statement**
- the reviewed `[PROJECT]_Resource_Inventory.md`, when available
- any private or local project materials identified as necessary

The selected scope statement should clearly identify:

1. the canonical current-state source set controlling current-state answers; and
2. the broader evidence set allowed to inform desired-state answers.

If the Resource Inventory provides multiple provisional scope alternatives, the project representative should normally select one before requirements completion.

## Recommended GitHub-link pattern

During active development, links to `main` are acceptable:

```text
Requirements forms:
https://github.com/sepio-framework/sepio-linkml/blob/main/docs/requirements-collection/Requirements_Collection_Forms.xlsx

Instructions and guidance:
https://github.com/sepio-framework/sepio-linkml/blob/main/docs/requirements-collection/Requirements_Instructions_and_Guidance_for_AI.md
```

For a reproducible requirements run, prefer links pinned to an exact commit or release.

A direct/raw URL for the XLSX may also be supplied when convenient.

## Recommended project-specific invocation

```text
Complete the SEPIO Requirements Forms for the following project using REQUIREMENTS_FORM_PROMPT.md.

PROJECT:
[PROJECT NAME]

SELECTED PROJECT SCOPE:
[PASTE THE SELECTED SCOPE STATEMENT]

REQUIREMENTS FORM PROMPT:
[URL TO REQUIREMENTS_FORM_PROMPT.md]

REQUIREMENTS FORMS:
[URL TO Requirements_Collection_Forms.xlsx]

REQUIREMENTS GUIDANCE:
[URL TO Requirements_Instructions_and_Guidance_for_AI.md]

RESOURCE INVENTORY:
[URL OR ATTACHMENT FOR PROJECT_Resource_Inventory.md]

Use the selected current-state canonical source set strictly for F1/current-state answers.
Use the broader desired-state source set allowed by the selected scope to build an evidence-supported maximal F2/desired-state requirements set.
If F2 differs from F1, name the desired-state supporting source and support type in Explanation / Considerations.
```

## Relationship to resource discovery

For projects where the evidence base or appropriate review scope is not already obvious, run `RESOURCE_INVENTORY_PROMPT.md` first.

The resulting Resource Inventory should provide:
- candidate canonical current-state sources;
- broader desired-state evidence sources;
- multiple provisional scope statements;
- a recommended scope;
- representative examples;
- access/retrieval guidance;
- unresolved questions.

## What not to provide for this stage

The Requirement→SEPIO mapping registry is intentionally **not** part of the requirements-elicitation task.

Requirements elicitation should determine what the project currently represents and what it should support independently of current SEPIO coverage. Mapping to SEPIO occurs only after the requirements record has been reviewed and stabilized.
