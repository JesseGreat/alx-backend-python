#!/usr/bin/env python3
"""Defines a function to_kv, takes a string k and
an int OR float v as arguments
returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple
    The first element of the tuple is the string k
    The second element is the square of the int/float v
    """
    return ((k, v**2))
