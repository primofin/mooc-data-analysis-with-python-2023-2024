#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    data = {
        'State': ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia'],
        'Year of independence': [np.nan, 1917, 1776, 1523, np.nan, 1992],
        'President': [np.nan, 'Niinistö', 'Trump', np.nan, 'Steinmeier', 'Putin']
    }
    df = pd.DataFrame(data)
    df = df.set_index('State')
    return df



def main():
    result_df = missing_value_types()
    print(result_df)

if __name__ == "__main__":
    main()
