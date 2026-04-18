from time import time

from networkx.algorithms.planar_drawing import triangulate_embedding
import random

def dichotomy(input_list, val):
    # caso terminale
    if len(input_list) == 1:
        if input_list[0] == val:
            return True
        else:
            return False

    # caso ricorsivo
    else:
        index = len(input_list)//2
        return dichotomy(input_list[:index], val) or dichotomy(input_list[index:], val)

if __name__ == '__main__':
    sequenza = [x for x in range(100000)]
    start_time = time()
    print(dichotomy(sequenza, random.randint(1, 100000)))
    end_time = time()
    print(end_time - start_time)

    start_time = time()
    print(dichotomy(sequenza, 100001))
    end_time = time()
    print(end_time - start_time)

