#!/usr/bin/env python3

import sys

def file_count(filename):
    L = []
    words = 0
    characters = 0
    with open(filename, 'r') as f:
        for line in f:
            try:
                L.append(line)
                words_of_line = line.split()
                words += len(words_of_line)
                for word in line:
                    characters += len(word)
                    
            except ValueError:
                continue
            print(len(L))       
            print("words", words)       
            print("characters", characters)       
    return (len(L), words, characters)

def main():
    for file_name in sys.argv[1:]:
        length, words, characters = file_count(file_name)
        print(f"{length}\t{words}\t{characters}\t{file_name}")

if __name__ == "__main__":
    main()
