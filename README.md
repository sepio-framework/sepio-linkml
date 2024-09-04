# sepio-linkml

LinkML-based specification of the SEPIO information model.

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
