#!/usr/bin/env python3
 
import math
 
 
def main():
    userInput = "hi"
    triangle = 'triangle'
    rectangle="rectangle"
    circle="circle"
    # enter you solution here
    while(len(userInput)):
        userInput = input('Choose a shape (triangle, rectangle, circle): ')
        if len(userInput) == 0: 
            break
        elif userInput != triangle and userInput != rectangle and userInput != circle and len(userInput) != 0:
            print("Unknown shape!")
        elif userInput == triangle:
            base = input("Give base of the triangle: ")
            height = input("Give height of the triangle: ")
            area = 1/2 * int(base) * int(height)
            print(f"The area is {str(area)}")
        elif userInput == rectangle:
            width = input("Give width of the triangle: ")
            height = input("Give height of the triangle: ")
            area = int(width) * int(height)
            print(f"The area is {str(area)}")
        elif userInput == circle:
            radius = input("Give radius of the circle: ")
            area = math.pi * int(radius) * int(radius)
            print(f"The area is {str(area)}")
 
 
if __name__ == "__main__":
    main()