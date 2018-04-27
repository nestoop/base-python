#!/usr/bin/python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import numpy as np
import graphviz
import os

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)

print("Accuracy train set : {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy test set : {:.3f}".format(tree.score(X_test, y_test)))
print("Features importance : {}".format(tree.feature_importances_))

tree4 = DecisionTreeClassifier(max_depth=4, random_state=0)
tree4.fit(X_train, y_train)

print("Accuracy max_depth= 4 train set : {:.3f}".format(tree4.score(X_train, y_train)))
print("Accuracy max_depth= 4 test set : {:.3f}".format(tree4.score(X_test, y_test)))

# show tree picture

export_graphviz(tree, out_file="tree.dot", class_names=["malignant", "benign"], feature_names=cancer.feature_names,
                impurity=False, filled=True)

export_graphviz(tree4, out_file="tree4.dot", class_names=["malignant", "benign"], feature_names=cancer.feature_names,
                impurity=False, filled=True)

with open("tree.dot") as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)

with open("tree4.dot") as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)

os.system("dot -Tpng tree.dot -o tree.png")
os.system("dot -Tpng tree4.dot -o tree4.png")

n_features = cancer.data.shape[1]
plt.barh(range(n_features), tree.feature_importances_, align="center")
plt.yticks(np.arange(n_features), cancer.feature_names)
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
