import pandas as pd
import numpy as np

def cleaning_data():
    # Read the TSV file into a DataFrame
    file_path = "src/presidents.tsv"
    df = pd.read_csv(file_path, sep='\t')
    
    # Replace '-' with NaN in the 'Last' column
    df['Last'] = df['Last'].replace('-', np.nan).astype(float)

    # Replace '<NA>' with NaN
    df.replace('<NA>', np.nan, inplace=True)
    
    # Clean President column
    df['President'] = df['President'].str.replace('"', '').str.split(',').apply(lambda x: ' '.join(x[::-1])).str.strip().str.title().astype('object')

    # Clean Start and Last columns
    df['Start'] = df['Start'].str.extract('(\d{4})').astype(int)
    
    # Clean Seasons column
    df['Seasons'] = df['Seasons'].replace({'two': 2, 'three': 3})
    df['Seasons'] = pd.to_numeric(df['Seasons'], errors='coerce')

    # Clean Vice-president column
    df['Vice-president'] = df['Vice-president'].str.replace('"', '').str.split(',').apply(lambda x: ' '.join(x[::-1])).str.strip().str.title().astype('object')
    
    return df

def main():
    cleaned_data = cleaning_data()
    print(cleaned_data)

if __name__ == "__main__":
    main()
