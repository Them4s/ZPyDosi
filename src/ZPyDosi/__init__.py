# src/ZPyDosi/__init__.py
__version__ = "0.0.1"

__all__ = [
    "Common",
    "DataInsta",
    "DataIrrad",
    "EfficiencyCalibration",
    "DosiFunctions",
    "Plots",
    "Prints",
    "Serpent2_utils",
    "Stats",
    "XSnFlux",
]

def __getattr__(name):
    if name in __all__:
        import importlib
        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
