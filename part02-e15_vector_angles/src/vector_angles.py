#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    # Compute the inner product of corresponding vectors
    dot_products = np.einsum('ij,ij->i', X, Y)
    
    # Compute the Euclidean norms of the vectors
    norms_X = np.linalg.norm(X, axis=1)
    norms_Y = np.linalg.norm(Y, axis=1)
    
    # Compute the cosine of the angles
    cos_angles = dot_products / (norms_X * norms_Y)
    
    # Clip the cosine values to the range [-1.0, 1.0] to avoid numerical issues
    cos_angles = np.clip(cos_angles, -1.0, 1.0)
    
    # Compute the angles in radians
    angles_radians = np.arccos(cos_angles)
    
    # Convert the angles to degrees
    angles_degrees = np.degrees(angles_radians)
    
    return angles_degrees

def main():
    X = np.array([[1, 0], [0, 1], [1, 1], [1, -1]])
    Y = np.array([[0, 1], [1, 0], [1, -1], [-1, -1]])
    vector_angles(X, Y)
if __name__ == "__main__":
    main()
