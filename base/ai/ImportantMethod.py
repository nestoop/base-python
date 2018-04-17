import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split


# Define the sigmoid function
def sigmoid(z):
    a = 1 / (1 + np.exp(-z))
    return a


# Initialize
def initialize(dim):
    w = np.zeros(dim).reshape(dim, 1)
    b = 0
    return w


# Compute the loss
def computeLoss(numTraining, Y, A):
    loss = -1 / numTraining * np.sum(Y * np.log(A) + (1 - Y) * (np.log(1 - A)))
    return (loss)


# Execute the forward propagation
def forwardPropagation(w, b, X, Y):
    # Compute Z
    Z = np.dot(w.T, X) + b
    # Determine the number of training samples
    numTraining = float(len(X))
    # Compute the output of the sigmoid activation function
    A = sigmoid(Z)
    # Compute the loss
    loss = computeLoss(numTraining, Y, A)
    # Compute the gradients dZ, dw and db
    dZ = A - Y
    dw = 1 / numTraining * np.dot(X, dZ.T)
    db = 1 / numTraining * np.sum(dZ)

    # Return the results as a dictionary
    gradients = {"dw": dw,
                 "db": db}
    loss = np.squeeze(loss)
    return gradients, loss


# Compute Gradient Descent
def gradientDescent(w, b, X, Y, numIerations, learningRate):
    losses = []
    idx = []
    # Iterate
    for i in range(numIerations):
        gradients, loss = forwardPropagation(w, b, X, Y)
        # Get the derivates
        dw = gradients["dw"]
        db = gradients["db"]
        w = w - learningRate * dw
        b = b - learningRate * db

        # Store the loss
        if i % 100 == 0:
            idx.append(i)
            losses.append(loss)
            # Set params and grads
        params = {"w": w,
                  "b": b}
        grads = {"dw": dw,
                 "db": db}

    return params, grads, losses, idx


# Predict the output for a training set
def predict(w, b, X):
    size = X.shape[1]
    yPredicted = np.zeros((1, size))
    Z = np.dot(w.T, X)
    # Compute the sigmoid
    A = sigmoid(Z)
    for i in range(A.shape[1]):
        # If the value is > 0.5 then set as 1
        if (A[0][i] > 0.5):
            yPredicted[0][i] = 1
        else:
            # Else set as 0
            yPredicted[0][i] = 0

    return yPredicted


# Normalize the data
def normalize(x):
    x_norm = None
    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    x = x / x_norm
    return x


# Run the 2 layer Neural Network on the cancer data set

from sklearn.datasets import load_breast_cancer

# Load the cancer data
(X_cancer, y_cancer) = load_breast_cancer(return_X_y=True)
# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer,
                                                    random_state=0)
# Normalize the data for better performance
X_train1 = normalize(X_train)

# Create weight vectors of zeros. The size is the number of features in the data set=30
w = np.zeros((X_train.shape[1], 1))
# w=np.zeros((30,1))
b = 0

# Normalize the training data so that gradient descent performs better
X_train1 = normalize(X_train)
# Transpose X_train so that we have a matrix as (features, numSamples)
X_train2 = X_train1.T

# Reshape to remove the rank 1 array and then transpose
y_train1 = y_train.reshape(len(y_train), 1)
y_train2 = y_train1.T

# Run gradient descent for 4000 times and compute the weights
parameters, grads, costs, idx = gradientDescent(w, b, X_train2, y_train2, numIerations=4000, learningRate=0.75)
w = parameters["w"]
b = parameters["b"]

# Normalize X_test
X_test1 = normalize(X_test)
# Transpose X_train so that we have a matrix as (features, numSamples)
X_test2 = X_test1.T

# Reshape y_test
y_test1 = y_test.reshape(len(y_test), 1)
y_test2 = y_test1.T

# Predict the values for
yPredictionTest = predict(w, b, X_test2)
yPredictionTrain = predict(w, b, X_train2)

# Print the accuracy
print("train accuracy: {} %".format(100 - np.mean(np.abs(yPredictionTrain - y_train2)) * 100))
print("test accuracy: {} %".format(100 - np.mean(np.abs(yPredictionTest - y_test)) * 100))

# Plot the Costs vs the number of iterations
fig1 = plt.plot(idx, costs)
fig1 = plt.title("Gradient descent-Cost vs No of iterations")
fig1 = plt.xlabel("No of iterations")
fig1 = plt.ylabel("Cost")
fig1.figure.savefig("fig1", bbox_inches='tight')