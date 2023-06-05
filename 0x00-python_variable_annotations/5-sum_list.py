#!/usr/bin/env python3

"""
This module defines a function for summing a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats and returns the result as a float.

    Args:
        input_list: The list of floats.

    Returns:
        The sum of the floats in the input list, as a float.
    """
    return sum(input_list)
