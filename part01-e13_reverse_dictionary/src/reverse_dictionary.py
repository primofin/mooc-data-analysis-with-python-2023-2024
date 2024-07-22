#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
    for key, value in d.items():
        for meaning in value:
            if meaning in result:
                result[meaning].append(key)
            else:
                result[meaning] = [key]
            
        # print(f"For key '{key}' value {value} was stored")

    return result

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
