import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

train_data = pd.read_csv("data_train.csv", header=None)
test_data = pd.read_csv("data_test.csv", header=None)


train_X = train_data.iloc[:, :4]
train_y = train_data.iloc[:, 4]
test_X = test_data.iloc[:, :4]
test_y = test_data.iloc[:, 4]

scaler = StandardScaler()
train_X = scaler.fit_transform(train_X)
test_X = scaler.transform(test_X)

accuracy = []

for k in range(1, 16):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_X, train_y)
    test_predictions = knn.predict(test_X)
    accuracy.append(accuracy_score(test_y, test_predictions))

plt.plot(range(1, 16), accuracy)
plt.xlabel("k")
plt.ylabel("Dokładnośc")
plt.savefig("KNNpart1")
plt.show()

best_k = accuracy.index(max(accuracy)) + 1

knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(train_X, train_y)
test_predictions = knn.predict(test_X)

conf_matrix = confusion_matrix(test_y, test_predictions)
print(conf_matrix)


