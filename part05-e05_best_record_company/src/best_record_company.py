#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    return df[df["Publisher"]== df.groupby("Publisher")["WoC"].sum().idxmax()]

def main():
    df = best_record_company()
    print(df)
    
if __name__ == "__main__":
    main()