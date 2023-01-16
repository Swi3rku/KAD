import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Read train and test data using pandas
train_data = pd.read_csv("data_train.csv", header=None)
test_data = pd.read_csv("data_test.csv", header=None)


# Extract features and labels from the data
# train_X = train_data.iloc[:, :4]
# train_y = train_data.iloc[:, 4]
# test_X = test_data.iloc[:, :4]
# test_y = test_data.iloc[:, 4]
#
# # Normalize the data
# scaler = StandardScaler()
# train_X = scaler.fit_transform(train_X)
# test_X = scaler.transform(test_X)
#
# # Initialize an empty list to store accuracy results
# accuracy = []
#
# # Loop through different k values
# for k in range(1, 16):
#     # Create a KNeighborsClassifier object
#     knn = KNeighborsClassifier(n_neighbors=k)
#     # Fit the model on train data
#     knn.fit(train_X, train_y)
#     # Predict labels on test data
#     test_predictions = knn.predict(test_X)
#     # Calculate accuracy
#     accuracy.append(accuracy_score(test_y, test_predictions))
#
# # Plot the accuracy results
# plt.plot(range(1, 16), accuracy)
# plt.xlabel("k value")
# plt.ylabel("Accuracy")
# plt.show()
#
# # Find the best k value
# best_k = accuracy.index(max(accuracy)) + 1
#
# # Create a KNeighborsClassifier object with the best k value
# knn = KNeighborsClassifier(n_neighbors=best_k)
# # Fit the model on train data
# knn.fit(train_X, train_y)
# # Predict labels on test data
# test_predictions = knn.predict(test_X)
#
# # Calculate confusion matrix
# conf_matrix = confusion_matrix(test_y, test_predictions)
# print(conf_matrix)



# =================================

labels = ["DDK_SDK_KNN","DDK_DP_KNN","DDK_SP_KNN","SDK_DP_KNN","SDK_SP_KNN","DP_SP_KNN"]
pom=0
for i in range(4):
    for j in range(i+1,4):
        # Extract features and labels from the data
        train_X = train_data.iloc[:, :4]
        train_y = train_data.iloc[:, 4]
        test_X = test_data.iloc[:, :4]
        test_y = test_data.iloc[:, 4]

        train_X = train_data.iloc[:, [i,j]]
        test_X = test_data.iloc[:, [i,j]]


        # Normalize the data
        scaler = StandardScaler()
        train_X = scaler.fit_transform(train_X)
        test_X = scaler.transform(test_X)

        # Initialize an empty list to store accuracy results
        accuracy = []

        # Loop through different k values
        for k in range(1, 16):
            # Create a KNeighborsClassifier object
            knn = KNeighborsClassifier(n_neighbors=k)
            # Fit the model on train data
            knn.fit(train_X, train_y)
            # Predict labels on test data
            test_predictions = knn.predict(test_X)
            # Calculate accuracy
            accuracy.append(accuracy_score(test_y, test_predictions))

        # Plot the accuracy results
        plt.plot(range(1, 16), accuracy)
        plt.xlabel("k value")
        plt.ylabel("Accuracy")
        plt.savefig(labels[pom])
        pom+=1
        plt.show()

        # Find the best k value
        best_k = accuracy.index(max(accuracy)) + 1

        # Create a KNeighborsClassifier object with the best k value
        knn = KNeighborsClassifier(n_neighbors=best_k)
        # Fit the model on train data
        knn.fit(train_X, train_y)
        # Predict labels on test data
        test_predictions = knn.predict(test_X)

        # Calculate confusion matrix
        conf_matrix = confusion_matrix(test_y, test_predictions)
        print(conf_matrix)
