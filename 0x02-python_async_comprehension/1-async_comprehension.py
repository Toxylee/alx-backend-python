#!/usr/bin/env python3
'''Module - Task 1
'''
from typing import List
from importlib import import_module as impmod


async_generator = impmod('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator.
    '''
    return [num async for num in async_generator()]
