#!/usr/bin/env python3

"""
This module provides a function to zoom in an array.
"""


from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in an array by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]):
            The array to zoom in.
        factor (int, optional):
            The number of times to repeat each element. Default is 2.

    Returns:
        Tuple[int, ...]:
            The zoomed-in array.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)