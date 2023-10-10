#!/usr/bin/env python3
'''Module - Task 2
'''
import asyncio
import time
from importlib import import_module as impmod


async_comprehension = impmod('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
