# sepio-linkml

SEPIO was first developed as an ontology by the [Monarch Initiative](https://monarchinitiative.org/about) to support standardized RDF representations of evidence and provenance across integrated genotype-phenotype datasets (the Scientific Evidence and Provenance Information Ontology). The ontological model has since been abstracted into a generic **Core Information Model (IM)** that can be implemented in any language or format. The Core IM is domain-agnostic, and able to represent assertions and their evidence and provenance of any kind. Application of SEPIO to a specific data set or use case requires defining a **‘Profile’** that extends/customizes the generic core model for a particular domain or application.

The components of the SEPIO Framework include:

1. **A Domain Analysis Model (DAM)**: an informal description of the domain we are modeling (scientific assertions and their evidence/provenance)
2. **A Core Information Model (IM)**:  defines data structures that can represent information about this domain (for any type of assertion and evidence).
3. **A 'Profiling' Methodology**:  Implementations extend the core model with domain-specific content to define a “SEPIO Profile” - a custom schema for a particular application or use case.
4. **Ontology Support**: An ontological representation of the core model that can be used if desired to produce linked data with ontology-based semantics.

The modeling framework-based approach addresses challenges posed by the diversity of types, levels of complexity, and use cases for evidence and provenance across knowledge domains and application - which means there is no ‘one-size-fits-all’ solution. A framework allows custom models built on a common semantic foundation can provide a base level of understanding and interoperability, without restricting expressivity. While this approach may not always support out-of-the-box interoperability across all communities of use, it can significantly lower barriers to aggregating, harmonizing, and operating across disparate data.

The SEPIO Core-IM specified in this repository was written in a yaml format using the [LinkML modeling language](https://linkml.io/linkml/), and uses LinkML tooling to automatically generate formal json schema specification and Github pages web documentation found here. 

## Website

[https://sepio-framework.github.io/sepio-linkml](https://sepio-framework.github.io/sepio-linkml)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [sepio_linkml](src/sepio_linkml)
    * [schema](src/sepio_linkml/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/sepio_linkml/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
