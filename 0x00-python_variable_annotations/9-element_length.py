#!/usr/bin/env python3

"""
This module defines a function for calculating the length of
elements in an iterable.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in an iterable.

    Args:
        lst: An iterable object containing sequences.

    Returns:
        A list of tuples, where each tuple consists of a sequence
        and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
