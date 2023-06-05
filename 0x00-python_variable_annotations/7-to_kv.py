#!/usr/bin/env python3

"""
This module defines a function for converting a string and an
int/float to a tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and an int/float to a tuple.

    The first element of the tuple is the input string `k`.
    The second element is the square of the input int/float `v`,
    represented as a float.

    Args:
        k: The input string.
        v: The input int or float.

    Returns:
        A tuple containing the input string `k` and the square
        of `v` as a float.
    """
    return (k, v ** 2)
