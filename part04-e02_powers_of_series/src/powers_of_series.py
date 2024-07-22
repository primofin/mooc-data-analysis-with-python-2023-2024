#!/usr/bin/env python3

import pandas as pd

def powers_of_series(series, k):
    data = {}
    for i in range(1, k+1):
        data[i] = series ** i
    return pd.DataFrame(data, index=series.index)

def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 3))

if __name__ == "__main__":
    main()
