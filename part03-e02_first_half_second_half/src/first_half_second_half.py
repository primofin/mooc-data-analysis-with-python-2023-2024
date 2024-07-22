
#!/usr/bin/env python3
import numpy as np

def first_half_second_half(a):
    num_columns = a.shape[1]
    
    half_size = num_columns // 2
    
    first_half = a[:, :half_size]
    second_half = a[:, half_size:]
    
    sum_first_half = np.sum(first_half, axis=1)
    sum_second_half = np.sum(second_half, axis=1)
    
    mask = sum_first_half > sum_second_half
    
    result = a[mask]
    
    return result

def main():
    first_half_second_half(np.array([[1, 2, 3, 4, 5, 6]]))

if __name__ == "__main__":
    main()
