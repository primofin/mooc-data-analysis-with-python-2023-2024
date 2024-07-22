#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    # Read the weather DataFrame from the src folder
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    
    # Filter the DataFrame to include only data from the year 2017
    df_2017 = df[df['Year'] == 2017]
    
    # Find the maximum amount of snow depth in 2017
    max_snow_depth = df_2017['Snow depth (cm)'].max()
    
    return max_snow_depth

def main():
    max_snow_depth = snow_depth()
    print(f"Max snow depth: {max_snow_depth} cm")

if __name__ == "__main__":
    main()
