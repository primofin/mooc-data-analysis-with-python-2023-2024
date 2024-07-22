#!/usr/bin/env python3

import pandas as pd

def special_missing_values():
    # Read the data set
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    
    # Replace "New" and "Re" with None
    df['LW'].replace({'New': None, 'Re': None}, inplace=True)
    
    # Convert 'LW' column to numeric
    df['LW'] = pd.to_numeric(df['LW'], errors='coerce')
    
    # Filter rows where position dropped compared to last week's position
    dropped_positions = df[df['Pos'] > df['LW']]
    
    return dropped_positions


def main():
    result_df = special_missing_values()
    print(result_df)

if __name__ == "__main__":
    main()


