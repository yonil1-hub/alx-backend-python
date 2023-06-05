#!/usr/bin/env python3

"""
This module defines a function for creating a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    Args:
        multiplier: The multiplier value.

    Returns:
        A function that takes a float argument and returns the product of
        the float and the multiplier.
    """
    def multiplier_function(num: float) -> float:
        return num * multiplier

    return multiplier_function
