#!/usr/bin/env python3
'''Annotating the below function parameters and return
values with the appropriate types
'''
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotating the function parameters
    Returns a tuple of sequence and int types.
    """
    return [(i, len(i)) for i in lst]
