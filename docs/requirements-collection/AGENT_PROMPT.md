# Agent Prompt — Complete the SEPIO Requirements Forms

Use this prompt after the project scope has been defined and, ideally, after a Source Inventory / Evidence Package has been prepared using `SOURCE_DISCOVERY_PROMPT.md`.

The agent may receive the workflow materials and project evidence as **attached files, public repository links, direct-download URLs, or version-pinned URLs**. Publicly accessible files do not need to be downloaded and re-uploaded by the human project representative unless the agent cannot retrieve them itself.

## Copyable prompt

Copy the prompt below into your AI agent's interface and replace the bracketed text.

```text
You are acting as a requirements analyst and as a knowledgeable representative of [PROJECT NAME].

Your task is to populate the SEPIO Requirements Forms workbook based on the project materials and workflow resources I provide.

PROJECT

[PROJECT NAME]

PROJECT SCOPE

[Insert the one- or two-sentence project scope statement here.]

REQUIREMENTS-COLLECTION MATERIALS

You will be provided access to the materials needed for this task. They may be supplied as:

- files attached directly to this prompt;
- public GitHub repository links;
- direct-download URLs;
- version-pinned GitHub URLs identifying a specific commit, tag, or release;
- other public project URLs or repository paths;
- a reviewed Source Inventory / Evidence Package produced using `SOURCE_DISCOVERY_PROMPT.md`.

The core requirements-collection materials are:

1. `Requirements_Collection_Forms.xlsx`
2. `Requirements_Instructions_and_Guidance_for_AI.md`

Additionally, a Source inventory / supporting information package may be provided (if available)

These may be supplied as attachments or as repository links.

REQUIREMENTS MATERIAL LOCATIONS

Requirements forms:
[ATTACHMENT OR URL TO Requirements_Collection_Forms.xlsx]

Instructions and guidance:
[ATTACHMENT OR URL TO Requirements_Instructions_and_Guidance_for_AI.md]

Source inventory / supporting information package, if available:
[ATTACHMENT OR URL TO PROJECT_Source_Inventory.md]

Additional project materials, if any:
[ATTACHMENTS, URLS, OR REPOSITORY PATHS]

MATERIAL ACCESS RULES

1. If a public GitHub or other repository URL is provided, retrieve and use the referenced material directly.

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
   - follow the version explicitly designated for the requirements run;
   - note any materially relevant differences you discover.

12. Record enough source-version information in the Requirements Review Memo that another agent could reproduce the review later.

SOURCE INVENTORY / EVIDENCE PACKAGE

13. When a reviewed Source Inventory / Evidence Package is supplied:
   - use its PRIMARY SOURCES as the authoritative evidence base;
   - use SUPPORTING SOURCES to clarify semantics or implementation;
   - use REPRESENTATIVE EXAMPLES to verify actual data usage;
   - do not treat sources marked CONTEXT ONLY / DO NOT TREAT AS CANONICAL as evidence of project requirements;
   - preserve its UNRESOLVED issues for human review rather than guessing.

14. If the Source Inventory identifies public files that should be inspected during requirements elicitation, attempt to retrieve those files yourself before asking the project representative to upload them.

15. If the Source Inventory and a directly inspected canonical source disagree, flag the conflict. Do not silently overwrite or reconcile the inventory.

16. If the Source Inventory identifies material that a human may need to provide, first determine whether you can retrieve it yourself. Human upload is a fallback, not the default.

Use `Requirements_Instructions_and_Guidance_for_AI.md` to understand each form, question, controlled value, and response convention.

IMPORTANT REQUIREMENTS-ELICITATION RULES

17. Answer the forms based on what this project actually represents or explicitly requires. Do not choose answers because they map conveniently to SEPIO.

18. Respect the project scope statement. Distinguish the scoped project/data product from:
   - upstream source systems;
   - internal systems outside scope;
   - downstream APIs;
   - user-interface/display enrichments;
   - derived products outside scope.

19. Distinguish:
   - information the project currently represents;
   - information the project explicitly requires but may not yet represent;
   - information available only in upstream sources;
   - information created or enriched only downstream.

20. Prefer current authoritative sources. In general, use this evidence hierarchy:
   a. the explicit project scope statement;
   b. the current authoritative schema/data model or canonical data product;
   c. current project/model documentation and curation rules;
   d. representative current data/examples;
   e. implementation, ingest, or transformation documentation;
   f. explicit future requirements, competency questions, or roadmap materials;
   g. older papers or historical documentation.

21. Use representative data/examples to confirm how the model is actually used, but do not infer a project-wide requirement from a single unusual record unless other evidence supports it.

22. Ground answers in the supplied or discovered evidence. Distinguish what a source explicitly establishes from what you infer.

23. Do not invent missing requirements. If the available project materials do not provide enough information to answer confidently:
   - use the form's uncertainty/review mechanism where available;
   - preserve the uncertainty;
   - flag the issue clearly for human review.

24. Preserve project-specific terminology and examples in explanatory fields where useful.

25. For each non-obvious answer, keep track of the source evidence that supports it so that the answer can be reviewed and traced back to its source.

26. Assess the project comprehensively across:
   - claim/assertion types;
   - claim representation structure;
   - semantic structure of reified claims;
   - evidence item types and representations;
   - evidence interpretation, grouping, direction, strength, and stacking;
   - provenance about information artifacts, agents, methods, processes, semantic alignment, encoding, and retrieval;
   - relationships between claim types and evidence types.

27. Do not use the Requirement→SEPIO mapping registry to decide what the project's requirements should be unless explicitly instructed to do so. Requirements elicitation must remain independent of current SEPIO coverage.

28. Do not proceed to Requirement→SEPIO mapping or generate a SEPIO covering model unless explicitly asked.

WORKBOOK HANDLING RULES

29. Populate the provided `Requirements_Collection_Forms.xlsx` workbook itself rather than recreating the forms from scratch.

30. Preserve the workbook's existing visual formatting and structure, including:
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

31. Change only the cells needed to enter project responses, explanations, examples, or explicitly requested review notes.

32. Do not redesign, restyle, normalize, or rebuild the workbook.

33. If technical limitations prevent safe editing of the workbook without altering its formatting, stop and report the limitation rather than silently rebuilding the workbook in a different style.

34. The returned XLSX should open normally in Excel without triggering a repair/recovery warning. Do not "fix" workbook internals by reconstructing the workbook if doing so changes the visible template formatting. If an Excel-integrity problem cannot be corrected without risking formatting changes, report it for human review.

COMPLETENESS AND CONSISTENCY REVIEW

35. Before finalizing the workbook, perform a completeness and consistency pass:
   - check every applicable field;
   - compare answers across forms;
   - identify contradictions;
   - identify unanswered or weakly supported questions;
   - identify places where free text implies a requirement not captured by a structured response;
   - make sure upstream evidence/provenance capabilities were not incorrectly attributed to the scoped project;
   - make sure current-state and desired-state answers are not conflated;
   - make sure process provenance described in documentation is not automatically treated as provenance stored in canonical records;
   - make sure downstream transformations are not treated as native project representation.

36. Preserve unresolved issues rather than forcing a Y/N answer when the evidence supports uncertainty.

DELIVERABLES

A. Completed requirements workbook

Return a completed copy of:

`Requirements_Collection_Forms.xlsx`

Preserve the original workbook formatting and structure.

B. Requirements Review Memo

Return a short Markdown memo containing:

- Project scope used
- Requirements-workflow materials used
- Project/source materials consulted
- Exact versions, releases, commits, DOI/archive versions, or retrieval dates where relevant
- High-confidence conclusions
- Answers requiring human review
- Apparent conflicts or missing information
- Files/resources the agent was unable to access, if any
- Form/guidance questions that were difficult to interpret
- Important assumptions made
- Any project observations that suggest improvements to the requirements forms or guidance

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
- the project scope statement
- the reviewed `[PROJECT]_Source_Inventory.md`, when available
- any private or local project materials identified as necessary

These materials may be supplied as attachments or public repository links.

For publicly accessible materials, **linking is preferred over manually downloading and attaching a copy**. The agent should retrieve public resources itself and should ask for a human-provided upload only when direct access fails, authentication/private access is required, or the canonical file/version cannot be identified confidently.

For the XLSX workbook, provide a URL from which the actual `.xlsx` file can be downloaded. A normal GitHub `blob/...` page may be useful for navigation, but the agent should retrieve the underlying workbook rather than treating the HTML preview as the workbook.

## Recommended GitHub-link pattern

During active development, links to `main` are acceptable:

```text
Requirements forms:
https://github.com/sepio-framework/sepio-linkml/blob/main/docs/requirements-collection/Requirements_Collection_Forms.xlsx

Instructions and guidance:
https://github.com/sepio-framework/sepio-linkml/blob/main/docs/requirements-collection/Requirements_Instructions_and_Guidance_for_AI.md
```

For a reproducible requirements run, prefer links pinned to an exact commit or release:

```text
Requirements forms:
https://github.com/sepio-framework/sepio-linkml/blob/<COMMIT_SHA>/docs/requirements-collection/Requirements_Collection_Forms.xlsx

Instructions and guidance:
https://github.com/sepio-framework/sepio-linkml/blob/<COMMIT_SHA>/docs/requirements-collection/Requirements_Instructions_and_Guidance_for_AI.md
```

A direct/raw URL for the XLSX may also be supplied when convenient:

```text
https://raw.githubusercontent.com/sepio-framework/sepio-linkml/<COMMIT_SHA>/docs/requirements-collection/Requirements_Collection_Forms.xlsx
```

When using a moving branch such as `main`, the agent should record the commit SHA or retrieval date actually used.

## Recommended project-specific invocation

A project representative can invoke the workflow with a compact wrapper like:

```text
Complete the SEPIO Requirements Forms for the following project using the instructions in AGENT_PROMPT.md.

PROJECT:
[PROJECT NAME]

PROJECT SCOPE:
[PROJECT SCOPE STATEMENT]

AGENT PROMPT:
[URL TO AGENT_PROMPT.md]

REQUIREMENTS FORMS:
[URL TO Requirements_Collection_Forms.xlsx]

REQUIREMENTS GUIDANCE:
[URL TO Requirements_Instructions_and_Guidance_for_AI.md]

SOURCE INVENTORY:
[URL OR ATTACHMENT FOR PROJECT_Source_Inventory.md]

Use the linked public materials directly. If a required public file cannot be accessed or downloaded, tell me exactly which file you need me to upload and why before substituting another source.
```

## Relationship to source discovery

For projects where the authoritative evidence base is not already obvious, run `SOURCE_DISCOVERY_PROMPT.md` first.

The resulting Source Inventory / Evidence Package should tell the requirements-completion agent:

- which sources are primary;
- which sources are supporting only;
- which representative examples to inspect;
- which neighboring resources are context only;
- which questions remain unresolved;
- which public files the agent should retrieve during the review;
- whether any material may require human upload if direct access fails.

The project representative should not be expected to manually download every source listed in the inventory.

## What not to provide for this stage

The Requirement→SEPIO mapping registry is intentionally **not** part of the requirements-elicitation task.

The requirements agent should determine what the project represents and requires independently of what SEPIO currently supports. Mapping to SEPIO occurs only after the requirements record has been reviewed and stabilized.
