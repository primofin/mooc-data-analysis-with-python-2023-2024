#!/usr/bin/env python3

def sum_equation(L):
    result = 0
    sum_in_text = ""
    if len(L) == 0:
        return "0 = 0"

    for i, num in enumerate(L):
        result += num
        if i == 0:
            sum_in_text = sum_in_text + str(num)
        else:
            sum_in_text = sum_in_text + " + " + str(num) 
    return f"{sum_in_text} = {result}"

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
