import numpy as np
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import pandas as pd
from numpy import array
import datetime

tf.disable_v2_behavior()

# Generating random linear data
# There will be 50 data points ranging from 0 to 50
x = np.linspace(0, 50, 50)
y = np.linspace(0, 50, 50)

# Add random noise to the x and y data to create random dataset
x += np.random.uniform(-4, 4, 50)
y += np.random.uniform(-4, 4, 50)
n = len(x)  # Number data points

# Plot of Training Data
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Training Data")
plt.show()

# Creating model for the dataset
X = tf.placeholder("float")
Y = tf.placeholder("float")
W = tf.Variable(np.random.randn(), name="W")
b = tf.Variable(np.random.randn(), name="b")

learning_rate = 0.01
training_epochs = 100

y_pred = tf.add(tf.multiply(X, W), b)
cost = tf.reduce_sum(tf.pow(y_pred - Y, 2)) / (2 * n)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        for (_x, _y) in zip(x, y):
            sess.run(optimizer, feed_dict={X: _x, Y: _y})

        if (epoch + 1) % 50 == 0:
            c = sess.run(cost, feed_dict={X: x, Y: y})
            print("Epoch", (epoch + 1), ": cost =", c, "W =", sess.run(W), "b =", sess.run(b))

    training_cost = sess.run(cost, feed_dict={X: x, Y: y})
    weight = sess.run(W)
    bias = sess.run(b)

    # Calculating the predictions
    predictions = weight * x + bias
    print("Training cost =", training_cost, "Weight =", weight, "bias =", bias, '\n')

    # Calculate Mean Squared Error (MSE)
    mse = np.mean((predictions - y) ** 2)
    print("Mean Squared Error (MSE) =", mse)

    # Plotting the Results
    plt.scatter(x, y, label='Original data')
    plt.plot(x, predictions, label='Fitted line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Regression Result')
    plt.legend()
    plt.show()

# Generating random linear test data
# There will be 20 data points ranging from 0 to 50
x_test = np.linspace(0, 50, 20)
y_test = np.linspace(0, 50, 20)

# Add random noise to the x and y test data to create random dataset
x_test += np.random.uniform(-4, 4, 20)
y_test += np.random.uniform(-4, 4, 20)

# Calculate predictions for test data
predictions_test = weight * x_test + bias

# Plotting the Results for test data
plt.scatter(x_test, y_test, label='Original test data')
plt.plot(x_test, predictions_test, label='Fitted line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Test Result')
plt.legend()
plt.show()

# Print current date and time for prediction
now = datetime.datetime.now()
print("Current date and time is:", now)

# Predict for new values
x_new = np.array([10, 20, 30, 40, 50])
predictions_new = weight * x_new + bias
print("Predictions for new values:", predictions_new)
