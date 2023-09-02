#!/usr/bin/env python3
"""Defines a function make_multiplier
returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    """
    return lambda f: f * multiplier
