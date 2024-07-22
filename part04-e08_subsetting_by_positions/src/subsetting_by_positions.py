#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    # Read the data set of the top forty singles from the beginning of the year 1964
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    
    # Subset the DataFrame to select the top 10 entries and the columns Title and Artist by their positions
    subset_df = df.iloc[:10, [1, 2]]  # Assuming Title is in the 2nd column and Artist is in the 3rd column
    
    # Rename the columns to match the expected output
    subset_df.columns = ['Title', 'Artist']
    
    return subset_df


def main():
    result_df = subsetting_by_positions()
    print(result_df)

if __name__ == "__main__":
    main()
