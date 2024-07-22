#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    elif n > 0:
        return reduce(np.matmul, (a for _ in range(n)))
    else:
        a_inv = np.linalg.inv(a)
        return reduce(np.matmul, (a_inv for _ in range(-n)))

def main():
    a = np.array([
        [2, 1],
        [1, 2]
    ])
    
    for n in [0, 1, 2, -1, -2]:
        result = matrix_power(a, n)
        print(f"Matrix a raised to the power {n}:\n{result}\n")

if __name__ == "__main__":
    main()
