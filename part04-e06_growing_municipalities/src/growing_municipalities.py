import pandas as pd

def growing_municipalities(municipalities):
    # Filter municipalities with positive population change
    growing_municipalities = municipalities[municipalities["Population change from the previous year, %"] > 0]
    
    # Calculate the proportion
    proportion = (len(growing_municipalities) / len(municipalities)) 
    
    return proportion

def main():
    # Load the municipalities DataFrame from TSV file
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    
    # Calculate the proportion of growing municipalities
    proportion_growing = growing_municipalities(df)
    
    # Print the proportion as percentage with 1 decimal precision
    print(f"Proportion of growing municipalities: {proportion_growing * 100:.1f}%")

if __name__ == "__main__":
    main()
