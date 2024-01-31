import numpy as np
def save_file_text(file_path: str, array: np.ndarray) -> bool:
    try:
        with open(file_path, 'w') as file:
            np.savetxt(file, array, fmt='%d', delimiter=' ', newline='\n')
        return True
    except Exception as e:
        print(f"Error saving text file: {e}")
        return False

def save_file_binary(file_path: str, array: np.ndarray) -> bool:
    try:
        np.save(file_path, array)
        return True
    except Exception as e:
        print(f"Error saving binary file: {e}")
        return False
if __name__ == '__main__':
    textPath = 'array_text.txt'
    binaryPath = 'array_binary'
    array = np.random.randint(1, 10, size=(3, 3))
    result = save_file_text(textPath, array)
    if result:
        print('File text saved')
    
    result = save_file_binary(binaryPath, array)
    if result:
        print('File binary saved')

