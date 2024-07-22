import pandas as pd

def read_series():
    data = {}
    while True:
        line = input("Enter index and value separated by whitespace (empty line to end): ")
        if not line:  # Empty line signals the end of Series
            break
        parts = line.split()
        if len(parts) != 2:
            raise ValueError("Malformed input: Each line should contain index and value separated by whitespace")
        index, value = parts
        data[index] = value
    return pd.Series(data, dtype=object)

def main():
    try:
        series = read_series()
        print("\nSeries created:")
        print(series)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
