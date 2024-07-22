import pandas as pd

def inverse_series(series):
    inverted_series = pd.Series(series.index, index=series.values)
    return inverted_series

def main():
    # Test Series with unique values
    s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    inverted_s1 = inverse_series(s1)
    print("Original Series 1:")
    print(s1)
    print("Inverted Series 1:")
    print(inverted_s1)
    print()
    
    # Test Series with duplicate values
    s2 = pd.Series([1, 2, 2], index=['a', 'b', 'c'])
    inverted_s2 = inverse_series(s2)
    print("Original Series 2:")
    print(s2)
    print("Inverted Series 2:")
    print(inverted_s2)
    
if __name__ == "__main__":
    main()
