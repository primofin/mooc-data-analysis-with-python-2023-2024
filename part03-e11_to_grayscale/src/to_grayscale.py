#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(rgb_image):
    weights = [0.2126, 0.7152, 0.0722]
    return np.dot(rgb_image[..., :3], weights)

def to_red(rgb_image):
    red_image = rgb_image.copy()
    red_image[:, :, 1:] = 0  # Zero out green and blue channels
    return red_image

def to_green(rgb_image):
    green_image = rgb_image.copy()
    green_image[:, :, [0, 2]] = 0  # Zero out red and blue channels
    return green_image

def to_blue(rgb_image):
    blue_image = rgb_image.copy()
    blue_image[:, :, :2] = 0  # Zero out red and green channels
    return blue_image

def main():
    # Load the RGB image
    rgb_image = plt.imread('src/painting.png')
    
    # Convert to grayscale
    grayscale_image = to_grayscale(rgb_image)
    
    # Display grayscale image
    plt.imshow(grayscale_image, cmap='gray')
    plt.axis('off')
    plt.show()
    
    
    # Load the RGB image
    rgb_image = plt.imread('src/painting.png')
    
    # Convert to red, green, and blue
    red_image = to_red(rgb_image)
    green_image = to_green(rgb_image)
    blue_image = to_blue(rgb_image)
    
    # Create a figure with three subplots
    fig, axes = plt.subplots(3, 1, figsize=(8, 10))
    titles = ['Red Image', 'Green Image', 'Blue Image']
    images = [red_image, green_image, blue_image]
    
    for ax, title, image in zip(axes, titles, images):
        ax.imshow(image)
        ax.set_title(title)
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
