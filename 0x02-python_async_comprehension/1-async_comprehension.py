#!/usr/bin/env python3
'''Defines a coroutine called async_comprehension,
Import async_generator from the previous task and
then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
'''

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Returns a list of random numbers using async comprehension
    '''
    rand_nums = [i async for i in async_generator()]

    return rand_nums

if __name__ == '__main__':
    print(asyncio.run(async_comprehension()))