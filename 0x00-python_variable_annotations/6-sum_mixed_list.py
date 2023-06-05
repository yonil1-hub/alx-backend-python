#!/usr/bin/env python3

"""
This module defines a function for summing a list of mixed integers and floats
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of mixed integers and floats and returns the
    result as a float.

    Args:
        mxd_lst: The list of mixed integers and floats.

    Returns:
        The sum of the integers and floats in the input list, as a float.
    """
    return sum(mxd_lst)
