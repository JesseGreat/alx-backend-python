#!/usr/bin/env python3
'''Defines a measure_runtime coroutine,
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds,
explain it to yourself.
'''

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Runs async comprehension four times in parallel
    and returns the total time
    '''
    start_time = time.time()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    return time.time() - start_time

if __name__ == '__main__':
    print(asyncio.run(measure_runtime()))
