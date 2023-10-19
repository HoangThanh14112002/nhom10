import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Hàm zoom ảnh với tỷ lệ scaleFactorX và scaleFactorY
def zoom_image(scaleFactorX, scaleFactorY):
    global original_image
    resized_image = cv2.resize(original_image, (0, 0), fx=scaleFactorX, fy=scaleFactorY)
    display_image(resized_image)

# Hàm hiển thị ảnh lên giao diện
def display_image(image):
    global photo_label
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image=image)
    photo_label.config(image=photo)
    photo_label.photo = photo

# Hàm reset ảnh về ban đầu
def reset_image():
    display_image(original_image)

# Đọc ảnh ban đầu
original_image = cv2.imread('aw.jpg')

# Tạo cửa sổ
window = tk.Tk()
window.title("Zoom Image")

# Tạo khung nhập tỷ lệ x và y
scale_factor_x_label = ttk.Label(window, text="Tỷ lệ X:")
scale_factor_x_label.grid(row=0, column=0)
scale_factor_x_entry = ttk.Entry(window)
scale_factor_x_entry.grid(row=0, column=1)

scale_factor_y_label = ttk.Label(window, text="Tỷ lệ Y:")
scale_factor_y_label.grid(row=1, column=0)
scale_factor_y_entry = ttk.Entry(window)
scale_factor_y_entry.grid(row=1, column=1)

zoom_button = ttk.Button(window, text="Zoom", command=lambda: zoom_button_clicked())
zoom_button.place(x=20, y=20)  # Điều chỉnh vị trí (x, y) của nút "Zoom" theo ý muốn

# Nút Reset
reset_button = ttk.Button(window, text="Reset", command=reset_image)
reset_button.place(x=100, y=20)  # Điều chỉnh vị trí (x, y) của nút "Reset" theo ý muốn

# Hiển thị ảnh ban đầu
photo_label = ttk.Label(window)
display_image(original_image)
photo_label.grid(row=2, columnspan=4)

# Hàm xử lý sự kiện khi nhấn nút Zoom
def zoom_button_clicked():
    scale_factor_x = float(scale_factor_x_entry.get())
    scale_factor_y = float(scale_factor_y_entry.get())
    zoom_image(scale_factor_x, scale_factor_y)

window.mainloop()
