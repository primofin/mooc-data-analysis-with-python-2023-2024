#!/usr/bin/env python3

def merge(L1, L2):
    merged_list = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged_list.append(L1[i])
            i += 1
        else:
            merged_list.append(L2[j])
            j += 1
    while i < len(L1):
        merged_list.append(L1[i])
        i += 1
    while j < len(L2):
        merged_list.append(L2[j])
        j += 1
    return merged_list
def main():
    pass

if __name__ == "__main__":
    main()
