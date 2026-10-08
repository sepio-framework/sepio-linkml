# Source Discovery Prompt — Assemble a Project Evidence Package

Use this prompt when the project representative has **not already assembled a complete set of project sources** for requirements elicitation.

This is an **optional preliminary step**. Its purpose is to help identify and organize the best evidence about the scoped project/data/model **before** the agent begins completing the SEPIO Requirements Forms.

Do **not** begin requirements elicitation or Requirement→SEPIO mapping during this step.

Copy the prompt below into your AI agent's interface and replace the bracketed text.

```text
You are acting as a source-discovery and evidence-preparation agent for the SEPIO requirements-collection workflow.

Your task is to identify and organize the best available sources for understanding the following project/data/model:

PROJECT
[PROJECT NAME]

PROJECT SCOPE
[Insert the one- or two-sentence project scope statement here.]

GOAL

Assemble a proposed Source Inventory / Evidence Package that another AI agent can later use to complete the SEPIO Requirements Forms accurately.

Do not complete the requirements forms yet.
Do not map project concepts to SEPIO yet.
Do not infer project requirements from what SEPIO supports.

SOURCE-DISCOVERY RULES

1. Respect the project scope statement.
   Distinguish the scoped project/data product from:
   - upstream source databases;
   - internal systems that are outside scope;
   - downstream APIs;
   - user-interface/display enrichments;
   - derived exports that are outside scope.

2. Prefer current, authoritative sources.

   In general, prioritize:
   a. current authoritative schema/data model;
   b. current model/design documentation;
   c. current representative data/examples;
   d. current curation/evidence/provenance guidance;
   e. current ingest/transformation/pipeline documentation;
   f. explicit requirements, competency questions, or roadmap documents;
   g. older papers or historical documentation for background only.

3. Look for sources that can answer questions about:
   - the kinds of claims/associations/statements represented;
   - how claims are structurally packaged;
   - whether claims are represented as reified objects, direct graph edges, slot/value pairs, or other forms;
   - how subject, relationship/predicate, object, and qualifiers are represented;
   - what kinds of evidence items are retained or referenced;
   - whether evidence items are represented locally, externally, or both;
   - whether evidence direction, strength, grouping, or higher-order synthesis is represented;
   - confidence or scoring information;
   - provenance about agents, methods, resources, dates, review, extraction, grounding, normalization, encoding, retrieval, or ingest;
   - what information is retained from upstream sources versus discarded or transformed;
   - current capabilities versus documented future requirements.

4. Include representative data/examples.
   When possible, identify a small but diverse set of current examples that covers the major claim or evidence patterns in the scoped project.
   Do not collect large datasets when a small representative sample will establish the relevant structure and semantics.

5. Record precise source locations.
   For each source, provide:
   - source title/name;
   - source type;
   - URL or repository path;
   - repository/release/tag/commit/version when available;
   - whether it appears current/authoritative;
   - what questions it helps answer;
   - any cautions about interpretation.

6. Identify source conflicts or version issues.
   If older papers/docs disagree with the current schema or implementation, flag this explicitly.
   Do not silently reconcile conflicts.

7. Distinguish direct evidence from inference.
   State what the source explicitly shows versus what you infer from it.
   If an important project behavior cannot be established confidently, mark it as unresolved.

8. Identify inaccessible or missing critical sources.
   If an important schema, dataset, generated build artifact, curation guide, or private document appears necessary but cannot be accessed, tell the project representative exactly what file or resource would be useful to provide.

9. Do not assume that richer upstream information is part of the scoped project.
   For aggregator/knowledge-graph projects, pay particular attention to which upstream fields are actually retained in the canonical project output.

10. Do not begin filling the SEPIO Requirements Forms until the source inventory has been reviewed or stabilized.

DELIVERABLE

Return a concise Source Inventory / Evidence Package with the following sections:

A. Project scope used

B. Recommended authoritative sources
For each source:
- Name
- Type
- URL/repository path
- Version/release/commit if available
- Why it matters
- Authority/currentness
- Notes/cautions

C. Representative data/examples to inspect
List a small, diverse set and explain what each helps test.

D. Upstream/downstream resources that should NOT be treated as canonical project evidence
List any important neighboring systems that could otherwise cause scope confusion.

E. Known source conflicts, ambiguities, or version concerns

F. Missing/inaccessible materials
State exactly what the project representative should provide, if anything.

G. Recommended source set for requirements elicitation
End with a compact list of the sources you recommend the requirements-completion agent actually use.
```

## How this fits into the workflow

Use this source-discovery prompt when the project representative wants the agent to help assemble the evidence base.

After the proposed Source Inventory / Evidence Package is reviewed, proceed with the main prompt in `AGENT_PROMPT.md` to populate `Requirements_Collection_Forms.xlsx`.

If the project representative already has a well-curated source package, this discovery step can be skipped.
