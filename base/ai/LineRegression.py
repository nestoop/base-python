#!/usr/bin/python

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

X_boson, y_boson = load_boston(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X_boson, y_boson, random_state=0)

lr = LinearRegression().fit(X_train, y_train)

print("LinearRegression Train set score: {:.2f}".format(lr.score(X_train, y_train)))
print("LinearRegression Test set score: {:.2f}".format(lr.score(X_test, y_test)))

ridge = Ridge().fit(X_train, y_train)

print("LinearRegression Ridge Train set score: {:.2f}".format(ridge.score(X_train, y_train)))
print("LinearRegression Ridge Test set score: {:.2f}".format(ridge.score(X_test, y_test)))

ridge_01 = Ridge(alpha=0.1).fit(X_train, y_train)

print("LinearRegression  Ridge alpha=0.1 ,Train set score: {:.2f}".format(ridge_01.score(X_train, y_train)))
print("LinearRegression Ridge alpha=0.1 ,Test set score: {:.2f}".format(ridge_01.score(X_test, y_test)))

ridge_1 = Ridge(alpha=1).fit(X_train, y_train)

print("LinearRegression Ridge ,alpha=1 Train set score: {:.2f}".format(ridge_1.score(X_train, y_train)))
print("LinearRegression Ridge ,alpha=1, Test set score: {:.2f}".format(ridge_1.score(X_test, y_test)))

ridge_10 = Ridge(alpha=10).fit(X_train, y_train)

print("LinearRegression Ridge alpha=10 Train set score: {:.2f}".format(ridge_10.score(X_train, y_train)))
print("LinearRegression Ridge alpha=10,Test set score: {:.2f}".format(ridge_10.score(X_test, y_test)))
