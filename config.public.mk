# config.public.mk

# This file is public in git. No sensitive info allowed.

###### schema definition variables, used by justfile

# Note:
# - just works fine with quoted variables of dot-env files like this one
LINKML_SCHEMA_NAME="sepio_linkml"
LINKML_SCHEMA_AUTHOR="Corey Cox <corey@tislab.org>"
LINKML_SCHEMA_DESCRIPTION="LinkML-based specification of the SEPIO information model."
LINKML_SCHEMA_SOURCE_DIR="src/sepio_linkml/schema"

###### linkml generator variables, used by justfile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
## --subfolder-type-separation: classes/, slots/, types/ subfolders, so that e.g. the
## Proposition class and the proposition slot don't overwrite each other on
## case-insensitive filesystems (macOS)
LINKML_GENERATORS_DOC_ARGS="--template-directory docs/templates-linkml --subfolder-type-separation"

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile=rdfs)
# LINKML_GENERATORS_OWL_ARGS="--no-type-objects --no-metaclasses --metadata-profile=rdfs"
LINKML_GENERATORS_OWL_ARGS=

## pass args to pydantic generator which isn't supported by gen-project
## https://github.com/linkml/linkml/issues/2537
LINKML_GENERATORS_PYDANTIC_ARGS=
