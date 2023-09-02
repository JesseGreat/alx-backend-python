#!/usr/bin/env python3
"""Defines a function sum_list,
returns args sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum og input list as float
    """
    sum: float = 0.0
    for item in input_list:
        sum += item
    return sum
