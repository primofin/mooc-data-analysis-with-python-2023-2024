#!/usr/bin/env python3


def main():
    d = [ (i, j) for i in range(1,6) for j in range(1,6) if i + j == 5]
    for x in d:
        print(x)
    # for i in range (1, 6):
    #     for j in range (1, 6):
    #         sum = i + j
    #         if sum == 5:
    #             print((i, j))

if __name__ == "__main__":
    main()
