"""
OpenClaw Identity Mini-Framework

A lightweight identity management framework for Aethel.
"""

__version__ = "0.1.0"
__author__ = "Molten"

from .core.identity import Identity
from .core.auth import AuthProvider

__all__ = ["Identity", "AuthProvider"]
