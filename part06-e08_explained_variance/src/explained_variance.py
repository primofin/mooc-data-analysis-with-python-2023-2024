import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def explained_variance():
    # Read the data from the file
    df = pd.read_csv("src/data.tsv", sep="\t")
    
    # Check if the DataFrame has 10 columns
    if len(df.columns) != 10:
        raise ValueError("Expected 10 columns in the DataFrame!")
    
    # Fit PCA to the data
    pca = PCA()
    pca.fit(df)
    
    # Get the variances of all features
    variances = df.var(axis=0)
    
    # Get the explained variances after PCA
    explained_variances = pca.explained_variance_
    
    return variances, explained_variances

def plot_cumulative_explained_variance(explained_variances):
    # Calculate cumulative explained variances
    cumulative_variance = np.cumsum(explained_variances)
    
    # Plot cumulative explained variances
    plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o')
    plt.xlabel('Number of Principal Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('Cumulative Explained Variance Plot')
    plt.grid(True)
    plt.show()


def main():
    variances, explained_variances = explained_variance()
    
    # Print the variances
    print("The variances are:", " ".join("{:.3f}".format(var) for var in variances))
    
    # Print the explained variances after PCA
    print("The explained variances after PCA are:", " ".join("{:.3f}".format(var) for var in explained_variances))
    
    plot_cumulative_explained_variance(explained_variances)

if __name__ == "__main__":
    main()

