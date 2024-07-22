#!/usr/bin/env python3

def file_extensions(filename):
    no_extensions = []
    dic = {}
    with open(filename, 'r') as f:
        for file_name in f:
            splitted_name = file_name.strip().split('.')
            name = splitted_name[0]
            if len(splitted_name) > 1:
                extension = splitted_name[-1]
                if extension in dic:
                    dic[extension].append(file_name.strip())
                else:
                    dic[extension] = [file_name.strip()]
            else:
                no_extensions.append(name)

            
    return (no_extensions, dic)

def main():
    no_extensions, dic = file_extensions("src/filenames.txt")
    sorted_dic = dict(sorted(dic.items(), key = lambda x: x))
    print(f"{len(no_extensions)} files with no extension")
    for key, values in sorted_dic.items():
        print(f"{key} {len(values)}")
    

if __name__ == "__main__":
    main()
