# Project Source Checklist

Use this checklist before asking an AI agent to complete the SEPIO Requirements Forms.

You do not need every item below. The goal is to provide enough authoritative evidence for the agent to understand what the project actually represents and requires.

If you do not already know where all of these materials are, use `SOURCE_DISCOVERY_PROMPT.md`. An AI agent can assemble a proposed source inventory, identify authoritative/current materials, and flag anything important that it cannot access.

## 1. Project scope statement — required

Write one or two sentences defining exactly what is being assessed.

**Project/data product:**  
`[name]`

**Scope statement:**  
`[what is included and what is explicitly out of scope]`

Examples are in `examples/example_scope_statement.md`.

## 2. Structural sources — strongly recommended

Gather at least one authoritative description of the project's structure.

- [ ] LinkML schema
- [ ] JSON Schema
- [ ] SHACL shapes
- [ ] SQL/database schema
- [ ] UML/class diagram
- [ ] data dictionary
- [ ] API object model
- [ ] canonical export specification
- [ ] other: ______________________

**Best/current source:**  
`[file or URL]`

## 3. Model and design documentation — strongly recommended

Gather documentation that explains the intended meaning of the model, not just field names.

- [ ] model overview
- [ ] design decisions
- [ ] architecture documentation
- [ ] semantic conventions
- [ ] modeling guidelines
- [ ] project overview/paper
- [ ] other: ______________________

**Best/current source(s):**  
`[files or URLs]`

## 4. Representative data/examples — strongly recommended

Provide enough real examples to see how the model is used.

- [ ] example records
- [ ] example claims/associations
- [ ] example evidence records
- [ ] example provenance
- [ ] example exports
- [ ] small representative dataset
- [ ] other: ______________________

Try to include examples that cover different major claim or evidence types, not many nearly identical records.

**Examples provided:**  
`[files or URLs]`

## 5. Evidence, curation, and interpretation documentation — provide when relevant

- [ ] curation SOP
- [ ] evidence coding guidelines
- [ ] evidence type definitions
- [ ] assertion/claim review rules
- [ ] confidence or scoring rules
- [ ] evidence direction/strength rules
- [ ] contradiction handling
- [ ] expert review workflow
- [ ] other: ______________________

**Sources:**  
`[files or URLs]`

## 6. Provenance and ingest documentation — especially important for aggregators/KGs

- [ ] source/ingest documentation
- [ ] provenance model
- [ ] source attribution rules
- [ ] primary vs aggregator knowledge-source rules
- [ ] retrieval/processing pipeline documentation
- [ ] transformations applied during ingest
- [ ] documentation of source fields retained/discarded
- [ ] other: ______________________

**Sources:**  
`[files or URLs]`

## 7. Requirements/use-case documentation — useful when current implementation is incomplete

- [ ] formal requirements
- [ ] competency questions
- [ ] user stories
- [ ] roadmap/model requirements
- [ ] documented capabilities not yet implemented
- [ ] other: ______________________

**Sources:**  
`[files or URLs]`

## 8. Downstream/API/UI materials — optional, but useful for scoping

Provide these when they help distinguish canonical model content from downstream enrichment.

- [ ] API documentation
- [ ] UI/display documentation
- [ ] expanded/derived objects
- [ ] query service behavior
- [ ] other: ______________________

**Sources:**  
`[files or URLs]`

## 9. Source quality check

Before starting, ask:

- [ ] Is the project scope explicit?
- [ ] Do we have at least one authoritative structural source?
- [ ] Do we have documentation explaining model intent?
- [ ] Do we have representative examples?
- [ ] Can we distinguish canonical project content from upstream source content?
- [ ] Can we distinguish canonical project content from downstream/API enrichment?
- [ ] Are the sources current?
- [ ] Are important source conflicts known?

If several answers are "no," the forms can still be completed, but the agent should produce more uncertainty/review flags.

## 10. What not to provide as a requirements source

Do not use the Requirement→SEPIO mapping registry to determine what the project requires during the initial elicitation step.

The mapping registry is applied later, after the project requirements have been reviewed and confirmed.
