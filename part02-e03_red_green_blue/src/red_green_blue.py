#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            matches = re.findall(r'(\d+)\s+(\d+)\s+(\d+)\s+([\w\s]+)', line)
            for match in matches:
                r = int(match[0])
                g = int(match[1])
                b = int(match[2])
                color_name = match[3].strip()
                string = f"{r}\t{g}\t{b}\t{color_name}"
                result.append(string)
            
    return result


def main():
    print(red_green_blue()[1])

if __name__ == "__main__":
    main()
