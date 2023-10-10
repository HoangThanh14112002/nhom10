import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Tạo tập giá trị x và y
x = np.linspace(0, 50, 50)
y = np.linspace(0, 50, 50)

# Cộng thêm nhiễu cho tập x và y để có tập dữ liệu ngẫu nhiên
x += np.random.uniform(-4, 4, 50)
y += np.random.uniform(-4, 4, 50)
n = len(x)  # Số lượng dữ liệu

# Plot dữ liệu huấn luyện
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Dữ liệu Huấn luyện")
plt.show()

# Tạo model cho tập dữ liệu
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# Khởi tạo biến w và b
W = tf.Variable(tf.random.normal([1]), name="W")
b = tf.Variable(tf.random.normal([1]), name="b")

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

# Starting the TensorFlow Session
with tf.Session() as sess:
    # Khởi tạo các biến
    sess.run(tf.global_variables_initializer())

    # Iterating through all the epochs
    for epoch in range(training_epochs):
        # Feeding each data point into the optimizer using Feed Dictionary
        for (_x, _y) in zip(x, y):
            sess.run(optimizer, feed_dict={X: _x, Y: _y})

        # Displaying the result after every 50 epochs
        if (epoch + 1) % 50 == 0:
            # Calculating the cost at every epoch
            c = sess.run(cost, feed_dict={X: x, Y: y})
            print("Epoch", (epoch + 1), ": cost =", c, "W =", sess.run(W), "b =", sess.run(b))

    # Lấy các giá trị cần thiết để sử dụng ngoài Session
    training_cost = sess.run(cost, feed_dict={X: x, Y: y})
    weight = sess.run(W)[0]
    bias = sess.run(b)[0]

# Lưu mô hình đã huấn luyện bằng Pickle
model = {'weight': weight, 'bias': bias}
with open('linear_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Đọc mô hình từ tệp và sử dụng nó để dự đoán dữ liệu mới
with open('linear_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

new_x = np.array([55, 60, 65, 70])  # Dữ liệu mới
new_predictions = loaded_model['weight'] * new_x + loaded_model['bias']
print("Dự đoán cho dữ liệu mới:", new_predictions)

# Plot kết quả
plt.plot(x, y, 'ro', label='Dữ liệu gốc')
plt.plot(new_x, new_predictions, 'bo', label='Dự đoán cho dữ liệu mới')
plt.title('Kết quả Hồi quy Tuyến tính')
plt.legend()
plt.show()
