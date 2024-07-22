#!/usr/bin/env python3

import numpy as np
from scipy import stats
from sklearn.datasets import load_iris

def load():
    iris = load_iris()
    return iris.data

def lengths():
    data = load()
    
    sepal_length = data[:, 0]
    petal_length = data[:, 2]
    
    correlation, _ = stats.pearsonr(sepal_length, petal_length)
    
    return correlation

def correlations():
    data = load()
    
    correlation_matrix = np.corrcoef(data, rowvar=False)
    
    return correlation_matrix

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
