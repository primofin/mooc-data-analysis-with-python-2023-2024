import pandas as pd

def cities():
    data = {
        'Population': [643272, 279044, 231853, 223027, 201810],
        'Total area': [715.48, 528.03, 689.59, 240.35, 3817.52]
    }
    index = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']
    df = pd.DataFrame(data, index=index)
    return df

def main():
    cities_df = cities()
    print(cities_df)

if __name__ == "__main__":
    main()
