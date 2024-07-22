#!/usr/bin/env python3

def extract_numbers(s):
    L = []
    print(L)
    for item in s.split():
        try:
            x = int(item)
            L.append(x)
        except ValueError:
            try:
                x = float(item)
                L.append(x)
            except ValueError:
                continue
    return L

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
