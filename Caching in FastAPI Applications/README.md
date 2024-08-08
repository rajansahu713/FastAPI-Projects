# This project demonstrates how to implement caching in a FastAPI application using disk caching and an LRU cache.

## Project Structure

- **decorators.py**: Contains the `cache_decorator` function for caching data using disk caching with a customizable expiration time.
- **functools_caching.py**: Implements an asynchronous function `get_factorial` that computes the factorial of a number using an LRU cache.
- **main.py**: The main FastAPI application that provides endpoints to demonstrate caching in action.



## Disk Caching
The cache_decorator in decorators.py uses the diskcache library to cache function results on disk. The cache key is generated based on the function name and its parameters, ensuring unique keys for different calls.

## LRU Caching
The get_factorial function in functools_caching.py uses the lru_cache decorator from Python's functools module. This is particularly useful for caching the results of expensive recursive calls like calculating factorials.

## Requirements

* Python 3.8+
* FastAPI
* diskcache



