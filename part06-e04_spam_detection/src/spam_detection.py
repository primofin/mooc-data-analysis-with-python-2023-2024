import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def spam_detection(random_state=0, fraction=1.0):
    # Read lines from ham.txt.gz
    with gzip.open('src/ham.txt.gz', 'rt') as f:
        ham_lines = f.readlines()

    # Read lines from spam.txt.gz
    with gzip.open('src/spam.txt.gz', 'rt') as f:
        spam_lines = f.readlines()

    # Take only fraction of lines
    ham_lines = ham_lines[:int(len(ham_lines) * fraction)]
    spam_lines = spam_lines[:int(len(spam_lines) * fraction)]

    # Combine ham and spam lines
    all_lines = ham_lines + spam_lines

    # Create labels
    labels = [0] * len(ham_lines) + [1] * len(spam_lines)

    # Vectorize the text data
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_lines)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=random_state)

    # Train MultinomialNB model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Predict labels for test set
    y_pred = model.predict(X_test)

    # Calculate accuracy score
    accuracy = accuracy_score(y_test, y_pred)

    # Get size of test sample
    test_sample_size = len(y_test)

    # Count number of misclassified samples
    misclassified_samples = (y_test != y_pred).sum()

    return accuracy, test_sample_size, misclassified_samples



def main():
# Example usage:
    acc, test_size, misclassified = spam_detection()
    print("Accuracy:", acc)
    print("Test sample size:", test_size)
    print("Misclassified samples:", misclassified)

if __name__ == "__main__":
    main()