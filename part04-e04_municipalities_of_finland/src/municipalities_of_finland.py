#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    # Load the dataset from the file, using the first column as the index
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    
    # Filter out rows corresponding to municipalities
    municipalities_df = df.loc['Akaa':'Äänekoski']
    
    return municipalities_df

def main():
    municipalities_df = municipalities_of_finland()
    print(municipalities_df)

if __name__ == "__main__":
    main()
