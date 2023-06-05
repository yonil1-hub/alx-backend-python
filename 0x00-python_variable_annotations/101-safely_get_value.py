#!/usr/bin/env python3

"""
This module provides a function for safely retrieving a value from a dictionary.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping):
            The dictionary.
        key (Any):
            The key to retrieve the value for.
        default (Union[T, None], optional):
            The default value to return if the key is not found.

    Returns:
        Union[Any, T]:
            The value associated with the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default