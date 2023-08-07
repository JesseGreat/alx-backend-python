#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async """
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create coroutines and await their completion upon which
    they will be added to the list to be returned"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]