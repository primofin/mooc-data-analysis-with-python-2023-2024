#!/usr/bin/env python3

def transform(s1, s2):
    l1 = s1.split()
    l2 = s2.split()
    combine = list(zip(l1, l2))
    return list(map(lambda x: int(x[0]) * int(x[1]), combine))
    
# def transform(s1, s2):
#     return [ a*b for (a, b) in zip(map(int, s1.split()), map(int, s2.split())) ]
def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
