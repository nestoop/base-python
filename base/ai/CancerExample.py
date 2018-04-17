#!/usr/bin/python
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer


cancer = load_breast_cancer()
X_train, Y_train, x_test, y_test = train_test_split(cancer.data, cancer.target, cancer.target, 66)



training_accuracy = []

test_accuracy = []

neighbors_setting = range(1, 10)

for n_neighbors in neighbors_setting:
    clf = KNeighborsClassifier(n_neighbors)
    clf.fit(X_train, Y_train)
    training_accuracy.append(clf.score(X_train, Y_train))
    test_accuracy.append(clf.score(x_test, y_test))


plt.plot(n_neighbors, training_accuracy, "train accuracy")
plt.plot(n_neighbors, test_accuracy, "test accuracy")
plt.xlabel("Accuracy")
plt.ylabel("n_neighbors")
plt.legend()



