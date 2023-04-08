#!/usr/bin/env python3
"""
    Task 3
"""


import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Takes two integers and returns the time it takes
    for the function to execute
    Args:
        int (int)
        max_delay (int)
    Returns:
        float
    """
    start = time.monotonic()
    await wait_n(n, max_delay)
    end = time.monotonic()
    return end - start


def measure_time_sync(n: int, max_delay: int) -> float:
    """
    Runs the `measure_time` function synchronously
    Args:
        int (int)
        max_delay (int)
    Returns:
        float
    """
    return asyncio.run(measure_time(n, max_delay))


async def measure_times_async(n_list: List[int], max_delay: int) -> List[float]:
    """
    Takes a list of integers and a max_delay integer and returns a list of
    floats representing the time it takes for the `measure_time`
    function to execute for each integer in the list.
    Args:
        n_list (List[int])
        max_delay (int)
    Returns:
        List[float]
    """
    tasks = [asyncio.create_task(measure_time(n, max_delay)) for n in n_list]
    times = await asyncio.gather(*tasks)
    return times


def measure_times_sync(n_list: List[int], max_delay: int) -> List[float]:
    """
    Runs the `measure_times_async` function synchronously
    Args:
        n_list (List[int])
        max_delay (int)
    Returns:
        List[float]
    """
    return asyncio.run(measure_times_async(n_list, max_delay))
