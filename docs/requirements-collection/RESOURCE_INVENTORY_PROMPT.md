# Resource Inventory Prompt

Use this prompt as the preliminary evidence-discovery and scope-definition step before completing the SEPIO Requirements Forms when the authoritative project evidence base or appropriate requirements-review scope is not already obvious.

The purpose of this task is to:

1. identify, evaluate, and organize the project resources that can inform requirements elicitation;
2. distinguish resources that should control **current-state** requirements from broader resources that may inform **desired-state** requirements; and
3. propose multiple provisional project scope statements for human selection before the requirements forms are completed.

The discovery agent should not complete the requirements forms and should not map requirements to SEPIO.

## Copyable prompt

```text
You are acting as a resource-discovery, scope-definition, and evidence-preparation agent for the SEPIO requirements-collection workflow.

Your task is to identify, evaluate, and organize the best available resources for understanding the following project/data/model and to recommend one or more reasonable scopes for a subsequent requirements review.

PROJECT
[PROJECT NAME]

INITIAL PROJECT CONTEXT / SCOPE NOTES
[Optional. Insert any initial scope statement, project description, known canonical distribution, exclusions, or questions from the project representative. If nothing is supplied, discover and propose the scope from the available project resources.]

GOAL

Assemble a proposed Resource Inventory / Evidence Package that another AI agent can later use to complete the SEPIO Requirements Forms accurately and reproducibly.

Do not complete the requirements forms yet.
Do not map project concepts to SEPIO yet.
Do not infer project requirements from what SEPIO supports.

A central output of this task is one or more PROVISIONAL SCOPE STATEMENTS that the project representative can review and select before requirements elicitation.

The Resource Inventory should make explicit:

- which exact source(s), dataset(s), distribution(s), release(s), or companion artifacts should control CURRENT-STATE requirements answers;
- which broader project resources may be used to identify DESIRED-STATE requirements;
- what resources are context only and must not be used as requirements evidence;
- which materials are publicly accessible and should normally be retrieved directly by the later requirements agent;
- which materials, if any, require a human project representative to download, upload, or clarify.

SCOPE-DESIGN PRINCIPLES

1. Separate current-state scope from desired-state evidence.

The subsequent requirements forms contain two distinct concepts:

CURRENT STATE:
What is represented in the selected canonical project source(s) for this review?

DESIRED STATE:
What should the SEPIO-based representation support, based on the broader, evidence-supported project requirements allowed by the selected scope?

Do not assume the same source set must control both.

2. The scope statement must identify the CURRENT-STATE CANONICAL SOURCE SET.

This is the exact set of source(s), dataset(s), distribution(s), release(s), or explicitly designated companion artifacts that the later requirements agent must use to populate current-state / "Used in Current Data?" columns.

The later agent should strictly stick to this set for current-state answers.

Examples:
- one versioned `indications.xlsx` distribution;
- one current LinkML schema release plus explicitly designated canonical example data;
- one KG release artifact;
- one database export and its required schema/data dictionary.

Do not broaden current state simply because richer information exists elsewhere in the project.

3. The scope statement should separately identify the DESIRED-STATE EVIDENCE SET.

Desired-state evidence may be broader than the canonical current-state distribution.

When relevant and not explicitly out of scope, it may include:
- explicit future requirements or roadmaps;
- current project/model documentation and papers;
- intermediate curation/analysis artifacts;
- data captured elsewhere in the project pipeline but dropped from the canonical export;
- alternate or earlier project distributions;
- other project-maintained representations;
- competency questions;
- curation guidance;
- implementation/design documents.

The purpose is to support an initial MAXIMAL EVIDENCE-SUPPORTED requirements set that a human reviewer can later narrow.

"Maximal" does not mean speculative. Every desired-state capability must be supported by project-specific evidence.

4. Classify desired-state support where useful.

Use these labels when characterizing why a noncanonical resource is informative for desired state:

- EXPLICIT_FUTURE_REQUIREMENT
  A roadmap, issue, requirements document, competency question, or explicit statement says the project wants/needs the capability.

- EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT
  The project already captures or uses the information in an intermediate artifact, alternate distribution, curation workflow, analysis product, or other project-maintained representation, but it is absent from the proposed canonical current-state distribution.

- DOCUMENTED_MODEL_INTENT
  A paper, model/design document, curation guide, or other authoritative project document describes the capability as part of the intended project model/data product, even if absent from the proposed canonical current-state source.

5. Do not use a source as desired-state evidence when it explicitly says the capability is out of scope, rejected, deprecated, or intentionally excluded, unless another authoritative project source explicitly reverses that decision.

SOURCE-DISCOVERY RULES

6. Respect supplied project context and discover scope boundaries.

Distinguish the scoped project/data product from:
- upstream source databases;
- internal systems that are outside scope;
- downstream APIs;
- user-interface/display enrichments;
- unrelated derived exports;
- historical/superseded project versions.

For every source, consider whether it describes:
- the canonical project/data model itself;
- a candidate canonical current-state distribution;
- an alternate or historical project representation;
- an intermediate curation/analysis artifact;
- an upstream source;
- a downstream representation;
- an implementation detail;
- future/project intent.

7. Prefer current, authoritative sources, but do not discard older/alternate/intermediate project artifacts that may legitimately inform desired state.

For CURRENT-STATE canonical-source recommendations, prioritize:
a. current authoritative schema/data model;
b. current canonical distribution/release;
c. current authoritative data dictionary;
d. current representative data/examples;
e. explicitly designated canonical companion artifacts.

For DESIRED-STATE evidence, also consider:
f. current model/design documentation and papers;
g. current curation/evidence/provenance guidance;
h. current ingest/transformation/pipeline artifacts;
i. explicit requirements, competency questions, roadmap documents, or issues;
j. intermediate curation/analysis artifacts;
k. alternate or earlier project distributions that expose project capabilities or intent.

When sources conflict:
- identify the conflict;
- state which source should control current state;
- explain whether the conflicting resource remains useful for desired-state evidence;
- do not silently reconcile the difference.

8. Look for sources that can answer questions about:

- the kinds of claims/associations/statements represented;
- how claims are structurally packaged;
- whether claims are represented as reified objects, direct graph edges, slot/value pairs, tabular records, or other forms;
- how subject, relationship/predicate, object, and qualifiers are represented;
- what kinds of evidence items are retained or referenced;
- whether evidence items are represented locally, externally, or both;
- whether evidence direction, strength, grouping, or higher-order synthesis is represented;
- confidence or scoring information;
- provenance about agents, methods, resources, dates, review, extraction, grounding, normalization, encoding, retrieval, or ingest;
- what information is retained from upstream sources versus discarded or transformed;
- what richer information is captured in intermediate project artifacts but lost in the canonical distribution;
- current capabilities versus documented future/intended requirements.

9. Include representative data/examples.

When possible, identify a small but diverse set of examples that covers the major claim and EPC patterns.

Include examples from:
- candidate canonical current-state sources; and
- broader desired-state sources when they reveal additional project requirements.

Prefer examples that collectively test different situations, such as:
- a claim with publication or regulatory support;
- a claim with structured evidence metadata;
- a claim with qualifiers/context;
- a claim with source/provenance but little explicit evidence;
- a case where richer project-internal EPC is dropped from the canonical export;
- a case involving normalization/transformation;
- an alternate distribution exposing a capability absent from the canonical one;
- any unusual but important pattern.

Do not collect large datasets when a small representative sample will establish the relevant structure and semantics.

Assign stable IDs such as E01, E02, E03.

10. Record precise source locations and source roles.

Assign each source a stable ID such as S01, S02, S03.

For each source, record:
- Source ID
- Source title/name
- Source type
- URL or repository path
- Repository/release/tag/commit/version when available
- Authority level
- Requirements role
- Desired-state support type, when applicable
- Scope relevance
- Requirement dimensions supported
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

Use these REQUIREMENTS ROLE labels:
- CURRENT_STATE_CANONICAL
- CURRENT_STATE_CANONICAL_COMPANION
- DESIRED_STATE_SUPPORT
- CURRENT_AND_DESIRED
- CONTEXT_ONLY

A source should receive CURRENT_STATE_CANONICAL or CURRENT_STATE_CANONICAL_COMPANION only if you recommend that the later requirements agent be allowed to use it for current-state answers under at least one proposed scope.

11. Capture directly observed facts from key sources.

For each major authoritative source, record concise facts explicitly supported by the source.

Examples:
- "The canonical table contains subject ID, object ID, and a source-text field."
- "The canonical record does not contain evidence-direction or evidence-strength fields."
- "Intermediate curation records retain Name Resolver candidates and LLM QC outcomes, but the final export drops them."
- "The project paper describes hyperrelations absent from the selected release."

Distinguish direct observation from interpretation.

Use labels where helpful:
- DIRECT
- INFERRED
- UNRESOLVED

12. Retrieve publicly accessible materials before asking the human to provide them.

When a potentially important source is publicly accessible:
- first attempt to access/download it yourself;
- follow GitHub, DOI/archive, release, and direct-download links;
- inspect actual files/artifacts when record-level or schema-level details matter.

Human assistance is a fallback, not the default.

13. Identify inaccessible, ambiguous, or human-supplied materials precisely.

Human intervention may be needed when:
- the agent cannot access/download the resource;
- authentication, institutional permission, or a private repository is required;
- the source exists only locally/internally;
- multiple plausible files/versions exist and the canonical one cannot be identified confidently;
- the public copy is stale/incomplete and the representative may have a better copy;
- a human decision is required to choose the canonical source/version or scope.

If human assistance is needed:
- identify the exact file/resource;
- provide the URL/path when known;
- explain why it matters;
- state what question it is needed to answer;
- state whether discovery/requirements elicitation can proceed provisionally without it;
- tell the project representative exactly what to download, upload, or clarify.

14. Distinguish process documentation from stored project content.

A project may document curation, extraction, review, normalization, mapping, evidence assessment, encoding, or transformation.

For each such source, determine whether it shows:
- information actually stored in the proposed canonical current-state source;
- information captured elsewhere by the project but omitted from the canonical export;
- only an implementation process with no evidence that its outputs are retained.

This distinction is especially important for desired-state scope design.

15. Do not begin filling the SEPIO Requirements Forms until the Resource Inventory and one project scope statement have been reviewed/selected or the project representative explicitly authorizes the agent to use the recommended scope.

PROVISIONAL SCOPE STATEMENTS

16. Author multiple reasonable provisional scope statements for human selection.

At minimum, provide:

SCOPE A — MINIMAL / CANONICAL-DISTRIBUTION-ONLY

This scope should:
- identify the narrowest defensible CURRENT-STATE CANONICAL SOURCE SET;
- restrict current-state answers to those canonical source(s);
- normally restrict desired-state answers to the same canonical source(s), unless a small number of explicitly inseparable canonical companion artifacts are required;
- produce a conservative requirements record describing the canonical distribution itself.

SCOPE B — MAXIMAL / CANONICAL CURRENT STATE + BROAD DESIRED STATE

This scope should:
- identify the exact CURRENT-STATE CANONICAL SOURCE SET;
- require the later agent to use only that set for current-state/F1 answers;
- identify a broader DESIRED-STATE EVIDENCE SET;
- allow desired-state/F2 answers to draw on project-specific evidence such as:
  - intermediate curation/analysis artifacts;
  - alternate/earlier project distributions;
  - other maintained project outputs;
  - authoritative papers/documentation;
  - curation/modeling guidance;
  - roadmaps/issues/explicit requirements;
- aim for a maximal evidence-supported desired-state requirements set that the human reviewer can later whittle down;
- require the requirements agent to name the desired-state supporting source in `Explanation / Considerations` whenever F2 differs from F1.

If other reasonable project scopes emerge, provide additional alternatives such as:
- CURRENT RELEASE + CURRENT PIPELINE ARTIFACTS;
- CORE PRODUCT + DESIGNATED COMPANION DATASETS;
- DOMAIN-SPECIFIC SUBSET;
- STRICT HISTORICAL RELEASE;
- CURRENT PRODUCT FAMILY / MULTI-DISTRIBUTION SCOPE.

17. Recommend one scope.

After presenting alternatives:
- identify the scope you recommend for the initial requirements exercise;
- explain why;
- state the tradeoff between reproducibility/conservatism and broader requirements discovery.

Unless project context argues otherwise, prefer recommending the MAXIMAL scope for the initial requirements pass because it preserves a strict canonical basis for current state while surfacing a broader evidence-supported desired-state requirements set for human review.

DELIVERABLE

Return a Markdown document named:

[PROJECT_NAME]_Resource_Inventory.md

Use the following sections.

A. Project context used

Restate the supplied project context/scope notes and any important assumptions used during discovery.

B. Provisional scope statements

Provide:

### Scope A — Minimal / canonical-distribution-only

Include:
- Scope statement text ready to paste into `REQUIREMENTS_FORM_PROMPT.md`
- CURRENT-STATE CANONICAL SOURCE SET
- DESIRED-STATE EVIDENCE SET
- Key exclusions
- Strengths / tradeoffs

### Scope B — Maximal / canonical current state + broad desired state

Include:
- Scope statement text ready to paste into `REQUIREMENTS_FORM_PROMPT.md`
- CURRENT-STATE CANONICAL SOURCE SET
- DESIRED-STATE EVIDENCE SET
- Desired-state support categories represented
- Key exclusions
- Strengths / tradeoffs

### Additional reasonable scope alternatives

Include only when justified.

### Recommended scope

State which scope you recommend and why.

C. Resource inventory

Provide a table with these columns:

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

For Desired-state support type, use when applicable:
- EXPLICIT_FUTURE_REQUIREMENT
- EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT
- DOCUMENTED_MODEL_INTENT
- N/A

For Access status, use concise values where possible:
- PUBLIC_ACCESSIBLE
- PUBLIC_DOWNLOADABLE
- ACCESS_NOT_VERIFIED
- ACCESS_FAILED
- AUTHENTICATION_REQUIRED
- PRIVATE_OR_LOCAL
- CANONICAL_FILE_AMBIGUOUS

For Retrieval / human-assistance guidance, use:
- AGENT_RETRIEVE
- HUMAN_PROVIDE_IF_AGENT_ACCESS_FAILS
- HUMAN_PROVIDE_REQUIRED
- HUMAN_CONFIRM_CANONICAL_VERSION
- HUMAN_CONFIRM_SCOPE
- CONTEXT_ONLY_NO_DOWNLOAD_NEEDED

D. Recommended authoritative source set

Separate this into:

### D1. Recommended current-state canonical source set

Identify the exact sources that should control F1/current-state answers under the recommended scope.

For each source:
- explain why it is canonical;
- specify version/release;
- identify any canonical companion artifact that must be interpreted together with it.

### D2. Recommended desired-state evidence set

Identify broader sources allowed to inform F2/desired-state requirements under the recommended maximal scope.

For each:
- state why it is relevant;
- assign a desired-state support type;
- note any limitations.

E. Representative data/examples

List selected examples using stable IDs.

For each:
- Example ID
- Current-state or desired-state example
- Source
- Claim/record type
- EPC/model pattern demonstrated
- Why selected
- Whether directly inspected or still needs retrieval

Prefer examples from both:
- canonical current-state sources;
- broader desired-state sources that reveal additional requirements.

F. Upstream/downstream/context resources that should NOT be treated as canonical requirements evidence

List neighboring systems/resources that could cause scope confusion.

Explain whether each is:
- context only;
- allowed only as desired-state evidence under a specific scope;
- fully out of scope.

G. Known source conflicts, ambiguities, or version concerns

Document:
- conflicting sources;
- stale documentation;
- unclear implementation behavior;
- unresolved version questions;
- differences between canonical distribution and richer intermediate/alternate representations;
- uncertainty about which release/file is canonical.

For each conflict:
- state what controls current state;
- state whether another source may still inform desired state.

H. Materials the requirements agent should retrieve vs. materials a human may need to provide

Start with this rule:

The requirements-completion agent should first attempt to retrieve all publicly accessible materials itself. The project representative should not need to manually download and upload public resources merely because they are listed in the Resource Inventory.

Then provide:

### H1. Materials the requirements agent should retrieve directly

For each:
- Source ID
- exact resource/file
- URL/path
- why needed
- what should be inspected

### H2. Materials a human may need to provide only if agent retrieval fails

For each:
- exact resource
- why it matters
- what the human should upload if requested

Do not ask the human to provide these preemptively.

### H3. Materials that genuinely require human provision or clarification

List only resources that:
- are private/local;
- require authentication;
- cannot be publicly accessed;
- require a human canonical-version decision;
- require a human scope-selection decision.

If none:
"None identified at this stage."

I. Evidence gaps / unresolved questions

For each unresolved question, indicate whether it:
- can likely be resolved by retrieving a public source;
- requires human-provided material;
- requires a human semantic/project decision;
- requires scope selection;
- can remain unresolved during preliminary requirements elicitation.

J. Recommended handoff for requirements elicitation

End with a compact machine-readable block.

Use this structure:

RECOMMENDED SCOPE:
- Scope B — Maximal / canonical current state + broad desired state

CURRENT-STATE CANONICAL SOURCES:
- S01
- S02

CURRENT-STATE CANONICAL COMPANIONS:
- S03

DESIRED-STATE SUPPORT SOURCES:
- S04: EXISTING_PROJECT_CAPABILITY_NOT_IN_CANONICAL_EXPORT
- S05: DOCUMENTED_MODEL_INTENT
- S06: EXPLICIT_FUTURE_REQUIREMENT

REPRESENTATIVE EXAMPLES:
- E01
- E02
- E03

CONTEXT ONLY / DO NOT USE AS REQUIREMENTS EVIDENCE:
- S08
- S09

AGENT SHOULD RETRIEVE DURING REQUIREMENTS REVIEW:
- S02: [specific file]
- S04: [specific file]

HUMAN PROVIDE ONLY IF AGENT RETRIEVAL FAILS:
- S07: [specific file]

HUMAN-PROVIDED MATERIAL REQUIRED:
- NONE
or
- [specific resource and why]

HUMAN CONFIRMATION REQUIRED:
- Select/approve one provisional scope before final requirements completion
- [other issue]

UNRESOLVED:
- [brief issue]

HANDOFF INSTRUCTION:
Use only CURRENT-STATE CANONICAL SOURCES and explicitly designated CURRENT-STATE CANONICAL COMPANIONS to populate F1/current-state requirements.
Use the DESIRED-STATE SUPPORT SOURCES allowed by the selected scope to populate an evidence-supported maximal F2/desired-state requirements set.
When F2 differs from F1, identify the supporting source and desired-state support type in the form's Explanation / Considerations field.
Do not use CONTEXT ONLY sources as requirements evidence.
Attempt to retrieve public resources before asking the project representative to upload them.
Flag unresolved issues for human review rather than guessing.

K. Short resource-discovery summary

Conclude with 5–10 bullets summarizing:
- the canonical model/data product identified;
- the recommended current-state canonical source set;
- the broader desired-state evidence set;
- the recommended scope;
- the main EPC patterns observed;
- important scope exclusions;
- critical source/version conflicts;
- additional public materials the requirements agent should retrieve;
- whether any material currently requires human provision;
- whether the package is ready for scope selection and requirements elicitation.
```

## Human handoff principle

The Resource Inventory should make the division of responsibility explicit:

1. **Public and accessible:** the requirements agent retrieves it.
2. **Public but retrieval may fail:** the human provides it only if the agent asks.
3. **Private/local/authenticated:** the human provides access or uploads it.
4. **Canonical version ambiguous:** the human decides which version is authoritative.
5. **Scope alternatives remain:** the human selects/approves the scope before final requirements completion.

## Scope-selection principle

The discovery agent proposes the scope; the project representative owns the scope decision.

For most initial requirements exercises, the recommended default is:

**strict canonical current state + maximal evidence-supported desired state**

This gives the modeling workflow a conservative, reproducible account of what the selected canonical distribution represents today while exposing a broader set of project-supported capabilities for human review before SEPIO modeling.

## Relationship to the requirements-form workflow

The completed `[PROJECT_NAME]_Resource_Inventory.md` is intended to be provided to the requirements-completion agent alongside:

- `Requirements_Collection_Forms.xlsx`
- `Requirements_Instructions_and_Guidance_for_AI.md`
- the selected project scope statement
- any materials explicitly identified as genuinely requiring human provision

The later requirements agent should attempt to retrieve all other publicly accessible resources itself.

The Requirement→SEPIO mapping registry is intentionally not used during resource discovery or requirements elicitation.
