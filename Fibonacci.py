from functools import lru_cache
from time import time

class Fibonacci:
    def __init__(self):
        self.cache = {0:0, 1:1}

    def calcola_elemento_cache(self,n):
        #se ho già la soluzione per questo n la prendo dalla cache
        if self.cache.get(n) is not None:
            return self.cache[n]
        #altrimenti devo andare avanti con la ricorsione
        else:
            self.cache[n] = (self.calcola_elemento_cache(n-1) + self.calcola_elemento_cache(n-2))
            return self.cache[n]



    def calcola_elemento(self, n):
        #terminale
        if n == 0:
            return 0
        if n == 1:
            return 1
        #ricorsivo
        else:
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)

    @lru_cache(maxsize=None)
    def calcola_elemento_lru(self, n):
        # terminale
        if n == 0:
            return 0
        if n == 1:
            return 1
        # ricorsivo
        else:
            return self.calcola_elemento_lru(n - 1) + self.calcola_elemento_lru(n - 2)

if __name__ == '__main__':
    N = 37
    fib = Fibonacci()

    start_time = time()
    print(fib.calcola_elemento(N))
    end_time = time()
    print(f"Elapsed time - recursion: {end_time - start_time}")

    start_time = time()
    print(fib.calcola_elemento_cache(N))
    end_time = time()
    print(f"Elapsed time - cache: {end_time - start_time}")

    start_time = time()
    print(fib.calcola_elemento_lru(N))
    end_time = time()
    print(f"Elapsed time - lru: {end_time - start_time}")