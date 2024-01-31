import numpy as np


def generate_array(min: int, max: int,condition) -> np.ndarray:
    array =  np.arange(min, max + 1)
    return array[condition(array)]

def generate_array_range(min: int, max: int,condition) -> np.ndarray:
    array =  np.array(range(min, max + 1))
    return array[condition(array)]

def generate_array_for_loop(min: int, max: int,condition) -> np.ndarray:
    array = np.empty(max - min + 1)
    for i in range(min, max + 1):
        array[i - min] = i
    return array[condition(array)]


if __name__ == '__main__':
    min= 10
    max= 101

    print(generate_array(min,max,lambda  x : x % 2 ==0))
    print(generate_array_range(min,max,lambda  x : x % 2 ==0))
    print(generate_array_for_loop(min,max,lambda  x : x % 2 ==0))
