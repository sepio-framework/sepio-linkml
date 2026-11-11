"""Data model package for sepio-linkml."""

from pathlib import Path
from .sepio_linkml import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "sepio_linkml.yaml"
