#!/usr/bin/env python3
 
def triple(number):
    return number * 3
def square(number):
    return number * number
def main():
    for i in range(1, 10):
        tempTriple = triple(i)
        tempSquare = square(i)
        if tempTriple < tempSquare:
            break
        print(f"triple({i})=={tempTriple} square({i})=={tempSquare}")
 
if __name__ == "__main__":
    main()