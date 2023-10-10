import numpy as np
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import tkinter as tk

tf.disable_v2_behavior()

# Tạo tập giá trị x và y
x = np.linspace(0, 50, 50)
y = np.linspace(0, 50, 50)

# Cộng thêm nhiễu cho tập x và y để có tập dữ liệu ngẫu nhiên
x += np.random.uniform(-4, 4, 50)
y += np.random.uniform(-4, 4, 50)
n = len(x)  # Số lượng dữ liệu

# Tạo biến để lưu kết quả dự đoán mới
new_predictions = None

# Hàm để vẽ biểu đồ dữ liệu huấn luyện
def plot_training_data():
    plt.scatter(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Dữ liệu Huấn luyện")
    plt.show()

# Hàm để vẽ biểu đồ dự đoán cho dữ liệu mới
def plot_predictions():
    if new_predictions is not None:
        plt.plot(np.array([55, 60, 65, 70]), new_predictions, 'bo', label='Dự đoán cho dữ liệu mới')
        plt.title('Kết quả Dự đoán')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()
    else:
        print("Bạn cần dự đoán trước khi hiển thị biểu đồ dự đoán.")

# Hàm để tính và hiển thị kết quả dự đoán cho dữ liệu mới
def predict_new_data():
    global new_predictions
    new_x = np.array([55, 60, 65, 70])  # Dữ liệu mới
    new_predictions = loaded_model['weight'] * new_x + loaded_model['bias']
    print("Dự đoán cho dữ liệu mới:", new_predictions)
    print("R-squared:", r2)
    print("RMSE:", rmse)
    plot_predictions()

# Hàm để tạo giao diện người dùng
def create_ui():
    root = tk.Tk()
    root.title("Ứng dụng Hồi quy Tuyến tính")

    # Tạo nút để hiển thị biểu đồ dữ liệu huấn luyện
    plot_training_button = tk.Button(root, text="Biểu đồ Dữ liệu Huấn luyện", command=plot_training_data)
    plot_training_button.pack()

    # Tạo nút để dự đoán và hiển thị biểu đồ dự đoán
    predict_button = tk.Button(root, text="Dự đoán cho dữ liệu mới", command=predict_new_data)
    predict_button.pack()

    # Tạo nút để hiển thị biểu đồ dự đoán
    plot_predictions_button = tk.Button(root, text="Biểu đồ Dự đoán", command=plot_predictions)
    plot_predictions_button.pack()

    root.mainloop()

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra (80% huấn luyện, 20% kiểm tra)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Tạo model cho tập dữ liệu
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Khởi tạo biến w và b
W = tf.Variable(np.random.randn(), name="W")
b = tf.Variable(np.random.randn(), name="b")

# Thiết lập tốc độ học
learning_rate = 0.01

# Số vòng lặp
training_epochs = 100

# Hàm tuyến tính
y_pred = tf.add(tf.multiply(X, W), b)

# Mean Squared Error Cost Function
cost = tf.reduce_sum(tf.pow(y_pred - Y, 2)) / (2 * n)

# Tối ưu bằng Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Thiết lập Global Variables
init = tf.global_variables_initializer()

# Starting the Tensorflow Session
with tf.Session() as sess:
    # Initializing the Variables
    sess.run(init)

    # Iterating through all the epochs
    for epoch in range(training_epochs):
        # Feeding each data point into the optimizer using Feed Dictionary
        for (_x, _y) in zip(x_train, y_train):
            sess.run(optimizer, feed_dict={X: _x, Y: _y})

        # Displaying the result after every 50 epochs
        if (epoch + 1) % 50 == 0:
            # Calculating the cost at every epoch
            c = sess.run(cost, feed_dict={X: x_train, Y: y_train})
            print("Epoch", (epoch + 1), ": cost =", c, "W =", sess.run(W), "b =", sess.run(b))

            # Storing necessary values to be used outside the Session
        training_cost = sess.run(cost, feed_dict={X: x_train, Y: y_train})
        weight = sess.run(W)
        bias = sess.run(b)

    # Lưu mô hình đã huấn luyện bằng Pickle
    model = {'weight': weight, 'bias': bias}
    with open('linear_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

    # Đọc mô hình từ tệp và sử dụng nó để dự đoán dữ liệu mới
    with open('linear_model.pkl', 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    # Tạo giao diện người dùng
    create_ui()
