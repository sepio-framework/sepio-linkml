# Source Discovery Prompt

Use this prompt as an optional preliminary step before completing the SEPIO Requirements Forms when the authoritative project evidence base is not already obvious.

The purpose of this task is to identify, evaluate, and organize the sources that a later requirements-completion agent should use. The discovery agent should not complete the requirements forms and should not map requirements to SEPIO.

## Copyable prompt

```text
You are acting as a source-discovery and evidence-preparation agent for the SEPIO requirements-collection workflow.

Your task is to identify, evaluate, and organize the best available sources for understanding the following project/data/model:

PROJECT
[PROJECT NAME]

PROJECT SCOPE
[Insert the one- or two-sentence project scope statement here.]

GOAL

Assemble a proposed Source Inventory / Evidence Package that another AI agent can later use to complete the SEPIO Requirements Forms accurately and reproducibly.

Do not complete the requirements forms yet.
Do not map project concepts to SEPIO yet.
Do not infer project requirements from what SEPIO supports.

The output of this task should be suitable for direct handoff to the later requirements-completion agent.

The Source Inventory should also make clear:
- which materials are publicly accessible and should normally be retrieved directly by the later requirements agent;
- which materials, if any, require a human project representative to download, upload, or otherwise provide;
- when human assistance is needed and why.

SOURCE-DISCOVERY RULES

1. Respect the project scope statement.

Distinguish the scoped project/data product from:
- upstream source databases;
- internal systems that are outside scope;
- downstream APIs;
- user-interface/display enrichments;
- derived exports that are outside scope.

For every source, consider whether it describes:
- the canonical project/data model itself;
- an upstream source;
- a downstream representation;
- an implementation detail;
- a historical or superseded design.

2. Prefer current, authoritative sources.

In general, prioritize:
a. current authoritative schema/data model;
b. current model/design documentation;
c. current representative data/examples;
d. current curation/evidence/provenance guidance;
e. current ingest/transformation/pipeline documentation;
f. explicit requirements, competency questions, or roadmap documents;
g. older papers or historical documentation for background only.

When two sources conflict, identify which source should be treated as authoritative and explain why.

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

When possible, identify a small but diverse set of current examples that covers the major claim and EPC patterns in the scoped project.

Prefer examples that collectively test different situations, such as:
- a claim with publication support;
- a claim with structured evidence metadata;
- a claim with qualifiers or contextual information;
- a claim with source/provenance but little or no explicit evidence;
- a case where richer upstream EPC exists but is not retained;
- a case involving normalization or transformation of source identifiers/relationships;
- any unusual claim/evidence pattern that appears important to the project.

Do not collect large datasets when a small representative sample will establish the relevant structure and semantics.

Assign each representative example a stable ID such as E01, E02, E03.

5. Record precise source locations.

Assign each source a stable ID such as S01, S02, S03.

For each source, record:
- Source ID
- Source title/name
- Source type
- URL or repository path
- Repository/release/tag/commit/version when available
- Authority level
- Whether it supports current-state requirements, desired-state requirements, or both
- Scope relevance
- What requirement dimensions it can support
- Important directly observed facts
- Access status
- Whether the later requirements agent should retrieve it directly or human assistance may be required
- Notes/cautions

Use these authority labels where appropriate:
- PRIMARY_AUTHORITATIVE
- SUPPORTING_CURRENT
- REPRESENTATIVE_EXAMPLE
- HISTORICAL_BACKGROUND
- OUT_OF_SCOPE_CONTEXT

6. Capture directly observed facts from key sources.

For each major authoritative source, record a few concise model/data facts that the source explicitly supports.

Examples:
- "Association has subject, predicate, object, publications, and primary_knowledge_source."
- "The canonical record does not contain evidence-direction or evidence-strength fields."
- "The ingest drops upstream confidence scores."
- "The project stores publication identifiers but not publication text."

Distinguish these directly observed facts from your interpretation.

7. Identify source conflicts or version issues.

If older papers/docs disagree with the current schema or implementation:
- flag the conflict explicitly;
- state which source should control;
- explain why;
- do not silently reconcile the difference.

8. Distinguish direct evidence from inference.

State what the source explicitly shows versus what you infer from it.

If an important project behavior cannot be established confidently, mark it as unresolved.

Use labels where helpful:
- DIRECT
- INFERRED
- UNRESOLVED

9. Retrieve publicly accessible materials before asking the human to provide them.

When a potentially important source is publicly accessible:
- first attempt to access or download it yourself;
- follow public repository links, DOI/archive links, release pages, and direct-download links as needed;
- inspect the actual file or artifact when record-level or schema-level details matter.

Do not ask the project representative to manually download and re-upload a public resource merely because it is needed for the later requirements review.

Human assistance should be treated as a fallback, not the default.

10. Identify inaccessible, ambiguous, or human-supplied materials precisely.

Human intervention may be needed when:
- the agent cannot access or download the resource;
- access requires authentication, institutional permissions, or a private repository;
- the source exists only as a local/internal file;
- a DOI, release page, archive, or repository contains multiple plausible files and the canonical one cannot be identified confidently;
- the public copy appears stale or incomplete and the project representative may have a more authoritative version;
- a human decision is required to determine which source/version is canonical.

If human assistance is needed:
- identify the exact file or resource;
- provide the URL/path when known;
- explain why it matters;
- state what question(s) it is needed to answer;
- state whether requirements elicitation can proceed provisionally without it;
- tell the project representative exactly what they should download, upload, or clarify.

Do not simply say "more information is needed."

11. Do not assume that richer upstream information is part of the scoped project.

For aggregator/knowledge-graph projects, pay particular attention to which upstream fields are actually retained in the canonical project output.

Do not treat upstream evidence/provenance/confidence information as a project requirement merely because it exists in the source resource.

12. Distinguish current-state evidence from desired-state evidence.

For each source, indicate whether it can support conclusions about:
- what the project currently represents;
- what the project explicitly wants to represent in the future;
- both;
- neither.

A current schema may strongly support current-state answers but not future intent.
A roadmap or requirements document may support desired-state answers even if the feature is not yet implemented.

13. Distinguish process documentation from stored project content.

A project may document processes such as:
- curation;
- LLM extraction;
- review;
- normalization;
- mapping;
- evidence assessment;
- encoding;
- data transformation.

Do not assume that provenance about these processes is stored in the canonical project data merely because the process is documented.

The later requirements agent must determine whether such information is actually represented in the scoped data/model.

14. Do not begin filling the SEPIO Requirements Forms until the source inventory has been reviewed or stabilized.

DELIVERABLE

Return a Markdown document named:

[PROJECT_NAME]_Source_Inventory.md

Use the following sections.

A. Project scope used

Restate the exact project scope used for discovery.

B. Source inventory

Provide a table with these columns:

- Source ID
- Name
- Type
- URL / repository path
- Version / release / commit
- Authority level
- Supports current state / desired state / both
- Requirement dimensions supported
- Important directly observed facts
- Access status
- Retrieval / human-assistance guidance
- Notes / cautions

For Access status, use concise values where possible, such as:
- PUBLIC_ACCESSIBLE
- PUBLIC_DOWNLOADABLE
- ACCESS_NOT_VERIFIED
- ACCESS_FAILED
- AUTHENTICATION_REQUIRED
- PRIVATE_OR_LOCAL
- CANONICAL_FILE_AMBIGUOUS

For Retrieval / human-assistance guidance, indicate one of:
- AGENT_RETRIEVE
- HUMAN_PROVIDE_IF_AGENT_ACCESS_FAILS
- HUMAN_PROVIDE_REQUIRED
- HUMAN_CONFIRM_CANONICAL_VERSION
- CONTEXT_ONLY_NO_DOWNLOAD_NEEDED

C. Recommended authoritative source set

Identify the small set of sources that should serve as the primary evidence base for the requirements-completion agent.

For each, explain briefly why it belongs in the canonical source set.

Also indicate whether the later requirements agent should:
- retrieve it directly;
- use an already attached copy;
- ask the human for it only if retrieval fails;
- require the human to provide it.

D. Representative data/examples

List the selected examples using stable IDs such as E01, E02, etc.

For each example provide:
- Example ID
- Source
- Claim/record type
- What EPC/model pattern it demonstrates
- Why it was selected
- Whether the example was directly inspected or still needs to be retrieved during requirements elicitation

E. Upstream/downstream resources that should NOT be treated as canonical project evidence

List important neighboring systems or resources that could otherwise cause scope confusion.

Explain why each is contextual rather than authoritative for the scoped project.

F. Known source conflicts, ambiguities, or version concerns

Document:
- conflicting sources;
- stale documentation;
- unclear implementation behavior;
- unresolved version questions;
- uncertainty about which release/file is canonical.

State which source should control where possible.

G. Materials the requirements agent should retrieve vs. materials a human may need to provide

Start with this default rule:

The requirements-completion agent should first attempt to retrieve all publicly accessible materials itself. The project representative should not need to manually download and upload public resources merely because they are listed in the Source Inventory.

Then provide three subsections:

### G1. Materials the requirements agent should retrieve directly

List public sources/files that the later agent should download or inspect during requirements elicitation.

For each, provide:
- Source ID
- exact resource/file;
- URL or repository path;
- why it is needed;
- what should be inspected.

### G2. Materials a human may need to provide only if agent retrieval fails

List resources that appear publicly available but may present access/download issues.

For each, provide:
- exact resource;
- why it matters;
- what the human should download/upload if requested.

Do not ask the human to provide these preemptively.

### G3. Materials that genuinely require human provision or clarification

List only resources that:
- are private/local;
- require authentication;
- cannot be accessed publicly;
- or require a human decision about the canonical version.

If none are identified, state:

"None identified at this stage."

H. Evidence gaps / unresolved questions

List any important requirements dimensions for which the available sources do not provide a confident answer.

Do not try to fill these gaps with general knowledge.

For each unresolved question, indicate whether it:
- can probably be resolved by the later requirements agent retrieving an identified public source;
- requires human-provided material;
- requires a human semantic/project decision;
- can remain unresolved during preliminary requirements elicitation.

I. Recommended source set for requirements elicitation

End with a compact, machine-readable handoff block for the next agent.

Use this structure:

PRIMARY SOURCES:
- S01
- S02
- S05

SUPPORTING SOURCES:
- S03
- S07

REPRESENTATIVE EXAMPLES:
- E01
- E02
- E03

CONTEXT ONLY / DO NOT TREAT AS CANONICAL:
- S08
- S09

AGENT SHOULD RETRIEVE DURING REQUIREMENTS REVIEW:
- S05: [specific file/artifact]
- S06: [specific file/artifact]

HUMAN PROVIDE ONLY IF AGENT RETRIEVAL FAILS:
- S07: [specific file/artifact]

HUMAN-PROVIDED MATERIAL REQUIRED:
- NONE
or
- [specific resource and why]

HUMAN CONFIRMATION REQUIRED:
- [canonical-version question, if any]

UNRESOLVED:
- [brief issue]
- [brief issue]

HANDOFF INSTRUCTION:
Use the PRIMARY SOURCES as the authoritative basis for current-state requirements.
Use SUPPORTING SOURCES to clarify semantics or implementation.
Use REPRESENTATIVE EXAMPLES to verify actual data usage.
Attempt to retrieve all public sources and files listed under AGENT SHOULD RETRIEVE before asking the project representative to upload anything.
Ask the human to provide a public file only if direct retrieval fails or the canonical file/version cannot be identified confidently.
If human assistance is required, state exactly what resource is needed, why it is needed, and whether the review can continue provisionally without it.
Do not infer project requirements from CONTEXT ONLY sources.
Flag UNRESOLVED issues for human review rather than guessing.

J. Short source-discovery summary

Conclude with 5–10 bullets summarizing:
- the canonical model/data product identified;
- the strongest source(s);
- the main EPC pattern(s) observed;
- important scope exclusions;
- any critical uncertainties;
- which additional public materials the requirements agent should retrieve itself;
- whether any material currently requires human provision;
- whether the evidence package is ready for requirements elicitation.
```

## Human handoff principle

The Source Inventory should make the division of responsibility explicit:

1. **Public and accessible:** the requirements agent retrieves it.
2. **Public but retrieval may fail:** the human provides it only if the agent asks.
3. **Private/local/authenticated:** the human must provide access or upload it.
4. **Canonical version ambiguous:** the human may need to decide which version is authoritative.

The source-discovery agent should never leave the project representative guessing about whether a file must be supplied.

## Relationship to the requirements-agent workflow

The completed `[PROJECT_NAME]_Source_Inventory.md` is intended to be provided to the requirements-completion agent alongside:

- `Requirements_Collection_Forms.xlsx`
- `Requirements_Instructions_and_Guidance_for_AI.md`
- the project scope statement
- any materials explicitly identified in the Source Inventory as genuinely requiring human provision

The later requirements agent should attempt to retrieve all other publicly accessible sources itself.

The Requirement→SEPIO mapping registry is intentionally not used during source discovery or requirements elicitation.
