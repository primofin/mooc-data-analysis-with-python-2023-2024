#!/usr/bin/env python3

import re


def file_listing(file_path="src/listing.txt"):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\S+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\S+\s+\d+\s+\d+:\d+)\s+(.*)', line)
            if match:
                size = int(match.group(5))
                date_str = match.group(6)
                filename = match.group(7)
                
                # Extract month, day, hour, and minute from the date string
                month, day, time = date_str.split()
                hour, minute = map(int, time.split(':'))
                
                result.append((size, month, int(day), hour, minute, filename))
    return result

def main():
    # print(file_listing())
    file_listing()

if __name__ == "__main__":
    main()
