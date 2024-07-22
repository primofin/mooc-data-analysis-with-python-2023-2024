#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    if a.shape[1] < 4:
        raise ValueError("Input array must have at least four columns")

    x = a[:, 0]
    y = a[:, 1]
    colors = a[:, 2]
    sizes = a[:, 3]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.plot(x, y)
    ax1.set_title("Line Plot")

    scatter = ax2.scatter(x, y, c=colors, s=sizes, alpha=0.5)
    ax2.set_title("Scatter Plot")

    plt.show()

def main():
    a = np.array([
        [1, 2, 10, 100],
        [2, 3, 20, 200],
        [3, 4, 30, 300],
        [4, 5, 40, 400],
        [5, 6, 50, 500]
    ])
    
    subfigures(a)

if __name__ == "__main__":
    main()
