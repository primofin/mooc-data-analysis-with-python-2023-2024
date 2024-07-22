#!/usr/bin/env python3

def find_matching(L, pattern):
    result = []
    for i, x in enumerate(L):
        if pattern in x: 
            result.append(i)
    return result

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")

if __name__ == "__main__":
    main()
