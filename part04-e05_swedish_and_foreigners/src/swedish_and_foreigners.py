import pandas as pd

def swedish_and_foreigners():
    # Load the dataset from the file, using the first column as the index
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    
    # Filter out rows corresponding to municipalities
    municipalities_df = df.loc['Akaa':'Äänekoski']
    
    # Further filter rows with proportion of Swedish speaking people and foreigners above 5%
    filtered_df = municipalities_df[(municipalities_df['Share of Swedish-speakers of the population, %'] > 5) &
                                     (municipalities_df['Share of foreign citizens of the population, %'] > 5)]
    
    # Select only columns about population, proportion of Swedish speaking people, and foreigners
    final_df = filtered_df[['Population', 'Share of Swedish-speakers of the population, %', 
                            'Share of foreign citizens of the population, %']]
    
    return final_df

def main():
    final_df = swedish_and_foreigners()
    print(final_df)
    
    # Check correlation
    correlation = final_df.corr()
    print("\nCorrelation between columns:")
    print(correlation)

if __name__ == "__main__":
    main()
