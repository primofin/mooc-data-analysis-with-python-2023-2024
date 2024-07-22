#!/usr/bin/env python3

import numpy as np

def diamond(n):
    a = np.eye(n, dtype=int)
    print('a', a)
    b = a[:, ::-1]
    
    upper = np.concatenate((b, a[:, 1:]), axis=1)
    print(upper)
    lower = np.concatenate((a, b[:, 1:]), axis=1)
    
    # Combine the upper and lower parts
    diamond_matrix = np.concatenate((upper, lower[1:, :]), axis=0)
    
    return diamond_matrix

    # e=np.eye(n, dtype=int)
    # a=np.concatenate([e[::-1], e[:,1:]], axis=1)
    # result = np.concatenate([a[:-1], a[::-1]], axis=0)
    # return result
def main():
    print(diamond(4))

if __name__ == "__main__":
    main()
