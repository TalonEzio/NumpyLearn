import numpy as np

def generate_array(size:int,start:int,step:int, dtype=int) -> np.array:
    arr = np.zeros((size,size),dtype=dtype)
    current_diagonal_value = start
    for i in range(size):
        arr[i][i] = current_diagonal_value
        current_diagonal_value += step

    return arr
def generate_array_with_support_method(size:int,start:int,step:int) ->np.array:
    end = start + (size-1) * step + 1
    diagonal_values = range(start,end,step)
    diagonal_type = 0
    array = np.diag(diagonal_values,  k = diagonal_type)
    return array

if __name__ == '__main__':

    size = 7
    start = 1
    step = 2
    print(generate_array(size,start,step,int))
    print(generate_array_with_support_method(size,start,step))
