#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    
    triangle.hypotenuse(12, 12)
    triangle.area(12, 12)

if __name__ == "__main__":
    main()
