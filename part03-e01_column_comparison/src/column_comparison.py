#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    # return np.array([])
    mask = [row[1] > row[-2] for row in a]
    # mask = a[:,1] > a[:,-2]
    return a[mask]
    # return c
    
def main():
    a = column_comparison(np.array([[1, 9, 2, 23, 12, 2], [2, 30, 22, 3, 2, 5]]))
    print(a)
if __name__ == "__main__":
    main()
