#caching is used to save memory...

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    print(f"Running for {n}:")
    return n*5

fx(20)
fx(120)
fx(60)
fx(40)
fx(30)
fx(2)

fx(20)
fx(120)
fx(60)
fx(40)
fx(30)
fx(2)


# +---------------------------------+
# | First Call to fx(20)            |
# | Output: Running for 20:         |
# | Time taken: 2 seconds           |
# +---------------------------------+
#            |
#            v
# +---------------------------------+
# | Second Call to fx(20)           |
# | No Output                       |
# | (as it did not get executed)    |
# | Time taken: 0 seconds (cached)  |
# +---------------------------------+
