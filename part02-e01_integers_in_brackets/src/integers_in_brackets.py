#!/usr/bin/env python3
import re


def integers_in_brackets(s):
    return [int(num) for num in re.findall(r'\[\s*([+-]?\d+)\s*\]', s)]

def main():
    pass

if __name__ == "__main__":
    main()
