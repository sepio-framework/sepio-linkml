"""sepio-linkml.

LinkML-based specification of the SEPIO information model.
"""

try:
    from sepio_linkml._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
