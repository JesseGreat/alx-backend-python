#!/usr/bin/env python3
"""Defines a function to measure time"""
import asyncio
from typing import List
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the average time it takes for coroutines to complete"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n