#!/usr/bin/env python3
"""The basics of asynchronous programming in Python"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Coroutine that waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        The delay time in seconds.
    """

    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time

