#!/usr/bin/env python3

def detect_ranges(L):
    sorted_list = sorted(L)
    result = []
    i = 0
    while i < len(sorted_list):
        start = sorted_list[i]
        print("start", start)
        if i == len(sorted_list) -1:
            result.append(start)
            break
        end = sorted_list[i + 1]
        if start + 1 == end:
            print("end", end)
            while end in sorted_list:
                end = end + 1
            result.append((start, end))
            i = sorted_list.index(end -1)
        else:
            result.append(start)
        i += 1
    return result
                

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(result)

if __name__ == "__main__":
    main()
