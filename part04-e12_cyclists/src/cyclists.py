#!/usr/bin/env python3

import pandas as pd

def cyclists():
    # Load the Helsinki bicycle data set from the src folder
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    
    # Remove empty rows at the end
    df = df.dropna(how='all')
    
    # Remove columns that contain only missing values
    df = df.dropna(axis=1, how='all')
    
    return df


def main():
    cleaned_data = cyclists()
    print(cleaned_data.head())

    
if __name__ == "__main__":
    main()
