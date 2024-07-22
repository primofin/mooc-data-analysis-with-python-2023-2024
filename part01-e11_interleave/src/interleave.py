#!/usr/bin/env python3

def interleave(*lists):
    interleaved = []
    
    for items in zip(*lists):
        interleaved.extend(items)
    
    return interleaved

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()