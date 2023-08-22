# OreO


"""
Exceptions which can be raised by py-Oreo Itself.
"""


class pyOreoError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyOreoError):
    ...
