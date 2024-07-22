#!/usr/bin/env python3

import pandas as pd

def below_zero():
    # Read the weather DataFrame from the src folder
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    
    # Filter the DataFrame to include only days when the temperature was below zero
    below_zero_df = df[df['Air temperature (degC)'] < 0]
    
    # Get the number of days when the temperature was below zero
    num_days_below_zero = below_zero_df.shape[0]
    
    return num_days_below_zero

def main():
    num_days_below_zero = below_zero()
    print(f"Number of days below zero: {num_days_below_zero}")

if __name__ == "__main__":
    main()

