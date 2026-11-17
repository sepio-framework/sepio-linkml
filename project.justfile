## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

sheet_id := env_var_or_default("LINKML_SCHEMA_GOOGLE_SHEET_ID", "")
sheet_tabs := env_var_or_default("LINKML_SCHEMA_GOOGLE_SHEET_TABS", "")
sheet_module_path := source_schema_dir / "sepio_classes.yaml"

# Regenerate the sepio_classes schema module from the Google Sheet
[group('model development - extended')]
compile-sheets:
  uv run sheets2linkml --gsheet-id {{sheet_id}} {{sheet_tabs}} > {{sheet_module_path}}.tmp
  mv {{sheet_module_path}}.tmp {{sheet_module_path}}
