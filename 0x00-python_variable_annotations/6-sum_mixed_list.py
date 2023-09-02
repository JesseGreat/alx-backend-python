#!/usr/bin/env python3
"""Defines a function sum_mixed_list,
takes a list mxd_lst of integers and floats and
returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of mxd_lst items as float.
    """
    return sum(mxd_lst)
