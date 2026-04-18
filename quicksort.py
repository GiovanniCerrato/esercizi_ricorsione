import random
from time import time


def quick_sort(sequenza):
    # caso terminale
    if len(sequenza) <= 1:
        return sequenza
    # caso ricorsivo
    else:
        #1. scelta pivot
        pivot = sequenza[0]
        #2. dividere sequenza secondo il pivot


        sequenza_smaller = [n for n in sequenza if n < pivot]
        sequenza_pivot = [n for n in sequenza if n == pivot]
        sequenza_larger = [n for n in sequenza if n > pivot]

        return quick_sort(sequenza_smaller) + sequenza_pivot + quick_sort(sequenza_larger)





if __name__ == '__main__':
    sequenza = [random.randint(1, 10000) for _ in range(10000)]

    start_time = time()
    sequenza.sort()
    print(sequenza)
    end_time = time()
    print(f"Elapsed time - {end_time - start_time}")

    start_time = time()
    print(quick_sort(sequenza))
    end_time = time()
    print(f"Elapsed time - {end_time - start_time}")
