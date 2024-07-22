#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    # Read the bicycle dataset
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    
    # Clean the dataset
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    
    # Split the 'Päivämäärä' column
    df['Weekday'] = df['Päivämäärä'].apply(lambda x: x.split()[0])
    df['Day'] = df['Päivämäärä'].apply(lambda x: int(x.split()[1]))
    df['Month'] = df['Päivämäärä'].apply(lambda x: x.split()[2])
    df['Year'] = df['Päivämäärä'].apply(lambda x: int(x.split()[3]))
    df['Hour'] = df['Päivämäärä'].apply(lambda x: int(x.split()[4].split(':')[0]))
    
    # Map the Weekday and Month columns
    weekdays_mapping = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    months_mapping = {'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5, 'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12}
    df['Weekday'] = df['Weekday'].map(weekdays_mapping)
    df['Month'] = df['Month'].map(months_mapping)
    
    # Reorder the columns
    df = df[['Weekday', 'Day', 'Month', 'Year', 'Hour']]
    
    return df

def main():
    df = split_date()
    print(df.head())

if __name__ == "__main__":
    main()
