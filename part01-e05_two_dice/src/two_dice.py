#!/usr/bin/env python3

def main():
    for i in range (1, 6):
        for j in range (1, 6):
            sum = i + j
            if sum == 5:
                print((i, j))

if __name__ == "__main__":
    main()
