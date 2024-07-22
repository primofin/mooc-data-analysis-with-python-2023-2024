#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(arr):
    return np.sqrt(np.sum(arr**2, axis=1))

def main():
    vectors = np.array([[3, 4], [1, 2], [0, 0], [5, 12]])
    print(vector_lengths(vectors))
if __name__ == "__main__":
    main()
