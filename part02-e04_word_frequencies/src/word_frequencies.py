#!/usr/bin/env python3

def word_frequencies(filename):
    with open(filename, 'r') as f:
        dic = {}
        for i, line in enumerate(f):
            transformed_line = line.strip()
            word_list = transformed_line.split(' ')
            for word in word_list:
                stripped_word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if stripped_word in dic:
                    dic[stripped_word] = int(dic[stripped_word]) + 1
                else: dic[stripped_word] = 1
                if i == 3:
                    print(dic)
            
    return dic

def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
