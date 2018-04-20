#!/usr/bin/python

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
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

lasso = Lasso().fit(X_train, y_train)

print("LinearRegression Lasso Train set score: {:.2f}".format(lasso.score(X_train, y_train)))
print("LinearRegression Lasso Test set score: {:.2f}".format(lasso.score(X_test, y_test)))
print("LinearRegression Lasso Number of features used: {:.2f}".format(np.sum(lasso.coef_ != 0)))

lasso_01 = Lasso(alpha=0.1, max_iter=100000).fit(X_train, y_train)

print("LinearRegression Lasso alpha=0.1 Train set score: {:.2f}".format(lasso_01.score(X_train, y_train)))
print("LinearRegression Lasso alpha=0.1 Test set score: {:.2f}".format(lasso_01.score(X_test, y_test)))
print("LinearRegression Lasso alpha=0.1 Number of features used: {:.2f}".format(np.sum(lasso_01.coef_ != 0)))


lasso_001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)

print("LinearRegression Lasso alpha=0.01 Train set score: {:.2f}".format(lasso_001.score(X_train, y_train)))
print("LinearRegression Lasso alpha=0.01 Test set score: {:.2f}".format(lasso_001.score(X_test, y_test)))
print("LinearRegression Lasso alpha=0.01 Number of features used: {:.2f}".format(np.sum(lasso_001.coef_ != 0)))


lasso_0001 = Lasso(alpha=0.001, max_iter=100000).fit(X_train, y_train)

print("LinearRegression Lasso alpha=0.001 Train set score: {:.2f}".format(lasso_0001.score(X_train, y_train)))
print("LinearRegression Lasso alpha=0.001 Test set score: {:.2f}".format(lasso_0001.score(X_test, y_test)))
print("LinearRegression Lasso alpha=0.001 Number of features used: {:.2f}".format(np.sum(lasso_0001.coef_ != 0)))


lasso_00001 = Lasso(alpha=0.0001, max_iter=100000).fit(X_train, y_train)

print("LinearRegression Lasso alpha=0.0001 Train set score: {:.2f}".format(lasso_00001.score(X_train, y_train)))
print("LinearRegression Lasso alpha=0.0001 Test set score: {:.2f}".format(lasso_00001.score(X_test, y_test)))
print("LinearRegression Lasso alpha=0.0001 Number of features used: {:.2f}".format(np.sum(lasso_00001.coef_ != 0)))
