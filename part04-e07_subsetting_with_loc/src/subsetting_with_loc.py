#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    subset_df = df.loc["Akaa":"Äänekoski", ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    return subset_df

def main():
    result_df = subsetting_with_loc()  # Pass the DataFrame df to the function
    print(result_df)

if __name__ == "__main__":
    main()
