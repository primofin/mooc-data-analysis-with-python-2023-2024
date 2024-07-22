#!/usr/bin/env python3

import pandas as pd

def main():
    # Load the dataset from the file
    df = pd.read_csv('src/municipal.tsv', sep='\t')

    # Print the shape of the DataFrame
    print(f"Shape: {df.shape[0]},{df.shape[1]}")

    # Print the column names
    print("Columns:")
    for col in df.columns:
        print(col)

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
