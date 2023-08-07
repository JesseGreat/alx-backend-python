#!/usr/bin/env python3
"""Create task for <wait random>"""
from asyncio import create_task, Task
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """Creates a new task"""
    return create_task(wait_random(max_delay))