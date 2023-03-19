import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load the Adult Income dataset
data = pd.read_csv("adult.csv", header=None,
                   names=["age", "workclass", "fnlwgt", "education", "education-num",
                          "marital-status", "occupation", "relationship", "race", "sex",
                          "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"])

# Preprocess the dataset by converting categorical variables into numerical variables
data = pd.get_dummies(data, columns=["workclass", "education", "marital-status",
                                     "occupation", "relationship", "race", "sex",
                                     "native-country"])

# Select the features to use for clustering
X = data.drop("income", axis=1)
y = data["income"]
knn = KNeighborsClassifier(n_neighbors=3)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
with ThreadPoolExecutor() as executor:
    batch_size = 10000
    for i in range(0, len(X_train), batch_size):
        X_batch = X_train[i:i+batch_size]
        y_batch = y_train[i:i+batch_size]
        knn.fit(X_batch, y_batch)


# Split the data into training and test sets

# Initialize the KNN classifier

# Use ThreadPoolExecutor to train the model concurrently
with ThreadPoolExecutor() as executor:
    future = executor.submit(knn.fit, X_train, y_train)
    print(future.result())

# Use ThreadPoolExecutor to predict concurrently
with ThreadPoolExecutor() as executor:
    future = executor.submit(knn.predict, X_test)
    predictions = future.result()
