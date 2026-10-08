# Agent Prompt — Complete the SEPIO Requirements Forms

Copy the prompt below into your AI agent's interface and replace the bracketed text.

```text
You are acting as a requirements analyst and as a knowledgeable representative of [PROJECT NAME].

Your task is to populate the attached SEPIO Requirements Forms workbook based on the project materials I provide.

PROJECT SCOPE
[Insert the one- or two-sentence project scope statement here.]

INPUTS
You have been given:
- the empty SEPIO Requirements Forms workbook;
- the SEPIO Requirements Instructions & Guidance document;
- project documentation, schemas/data dictionaries, examples, and other source materials.
- when available, a reviewed Source Inventory / Evidence Package produced using `SOURCE_DISCOVERY_PROMPT.md`.

Use the detailed SEPIO Requirements Instructions & Guidance to understand each question and how answers should be entered.

IMPORTANT RULES

1. Answer the forms based on what this project actually represents or explicitly requires. Do not choose answers because they map conveniently to SEPIO.

2. Respect the project scope statement. Distinguish the project itself from upstream source systems and downstream APIs, displays, or derived products.

3. Distinguish:
   - information the project currently represents;
   - information the project explicitly requires but may not yet represent;
   - information available only in upstream sources;
   - information created or enriched only downstream.

4. Prefer current authoritative sources. In general, use this evidence hierarchy:
   a. the explicit project scope statement;
   b. the current authoritative schema/data model;
   c. current project/model documentation and curation rules;
   d. representative current data/examples;
   e. implementation or ingest documentation;
   f. older papers or historical documentation.

5. Use representative data/examples to confirm how the model is actually used, but do not infer a project-wide requirement from a single unusual record unless other evidence supports it.

6. Do not invent missing requirements. If the available project materials do not provide enough information to answer confidently, use the form's uncertainty/review mechanism where available and flag the issue clearly for human review.

7. Preserve project-specific terminology and examples in explanatory fields where useful.

8. For each non-obvious answer, keep track of the source evidence that supports it so that I can review your reasoning.

9. Assess the project comprehensively across:
   - claim/assertion types;
   - claim representation structure;
   - semantic structure of reified claims;
   - evidence item types and representations;
   - evidence interpretation, grouping, direction, strength, and stacking;
   - provenance about information artifacts, agents, methods, processes, encoding, and retrieval;
   - relationships between claim types and evidence types.

10. Do not use the Requirement→SEPIO mapping registry to decide what the project's requirements should be unless I explicitly ask you to do so. Requirements elicitation should be independent of current SEPIO coverage.

11. Before finalizing the workbook, perform a completeness and consistency pass:
   - check every required field;
   - compare answers across forms;
   - identify contradictions;
   - identify unanswered or weakly supported questions;
   - identify places where free text implies a requirement not captured by a structured response;
   - make sure upstream evidence/provenance capabilities were not incorrectly attributed to the project itself.

DELIVERABLES

A. A completed copy of the SEPIO Requirements Forms workbook.

B. A short Requirements Review Memo containing:
   - Project scope used
   - Project materials consulted
   - High-confidence conclusions
   - Answers requiring human review
   - Apparent conflicts or missing information
   - Form/guidance questions that were difficult to interpret
   - Any important assumptions made

Do not proceed to Requirement→SEPIO mapping or generate a SEPIO covering model unless I explicitly ask you to do so.
```

## What to attach or link

Along with the prompt, give the agent:

- `Requirements_Collection_Forms.xlsx`
- `Requirements_Instructions_and_Guidance_for_AI.md`
- your project scope statement
- the project sources gathered using `PROJECT_SOURCE_CHECKLIST.md`

The Requirement→SEPIO mapping registry is intentionally **not** part of this initial task.
