#!/usr/bin/env python3
import pandas as pd

def average_temperature():
    # Read the weather DataFrame from the src folder
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    
    # Filter the DataFrame to include only data for the month of July
    df_july = df[df['m'] == 7]
    
    # Calculate the average temperature in July
    avg_temp_july = df_july['Air temperature (degC)'].mean()
    
    return avg_temp_july

def main():
    avg_temp_july = average_temperature()
    print(f"Average temperature in July: {avg_temp_july:.1f} °C")

if __name__ == "__main__":
    main()
