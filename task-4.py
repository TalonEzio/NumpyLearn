import numpy as np

def generate_array(width: int, height: int, borderValue=1, innerValue=0, dtype=int) -> np.array:
    arr = np.full((width, height), borderValue, dtype=dtype)

    arr[1:-1, 1:-1] = innerValue
    # arr[1:width - 1,1:height - 1] = innerValue
    # arr[1:arr.shape[0] - 1,1:arr.shape[1] - 1] = innerValue

    return arr

if __name__ == '__main__':
    width = 5
    height = 10

    print(generate_array(width, height, 5, 6, int))
