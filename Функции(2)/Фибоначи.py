import functools
from functools import lru_cache


@functools.lru_cache
def fib(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 1000):
    print(fib(i))

# ЕГЭшная классика...
