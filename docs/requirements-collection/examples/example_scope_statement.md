# Example Project Scope Statements

A good scope statement tells the agent exactly what data product or model is being assessed and what nearby systems are out of scope.

## Example 1 — canonical knowledge graph output

> The project is the canonical MonarchKG data model and KG build output. Requirements should reflect what MonarchKG itself stores and represents, not richer evidence/provenance/confidence information available only in upstream source databases and not downstream API or display enrichments unless they are part of the canonical KG output.

## Example 2 — native knowledge model

> The project is the native DisMech knowledge model and disorder YAML dataset. Requirements should reflect information represented in the native schema and canonical disorder records, including the project's evidence-bearing mechanistic statements and provenance.

## Example 3 — a specific export

> The project is the canonical public JSON export produced by [PROJECT]. Internal curation objects that are not included in that export are out of scope unless the project documentation explicitly identifies them as required future capabilities.

## Example 4 — an ingest/adapter

> The project is the [SOURCE] ingest into [TARGET KG], specifically the normalized associations emitted by that ingest. Requirements should describe what the ingest output preserves, not the full source database model.

## Template

> The project is [EXACT PROJECT / MODEL / DATA PRODUCT]. Requirements should reflect [WHAT IS INCLUDED]. [UPSTREAM / DOWNSTREAM / INTERNAL SYSTEMS] are out of scope except where [EXPLICIT EXCEPTION].
