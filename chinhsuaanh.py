import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Define global variables
img = None
rows, cols = 0, 0
kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
kernel_5x5 = np.ones((5, 5), np.float32) / 25.0
effect_strength = 0.0  # Initial effect strength

def apply_effect(x, y):
    global img, effect_strength

    # Define a region around the clicked point
    x1, y1, x2, y2 = max(0, x - 25), max(0, y - 25), min(cols, x + 25), min(rows, y + 25)
    roi = img[y1:y2, x1:x2]

    blur_kernel = np.ones((9, 9), np.float32) / (9.0 + 80.0 * effect_strength)
    blurred_roi = cv2.filter2D(roi, -1, blur_kernel)
    img[y1:y2, x1:x2] = blurred_roi

    cv2.imshow('Original', img)

def open_image():
    global img, rows, cols
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    rows, cols = img.shape[:2]
    cv2.imshow('Original', img)

def update_effect_strength(value):
    global effect_strength
    effect_strength = float(value)

# Create the main window
root = tk.Tk()
root.title("Image Editor")

# Load button
load_button = tk.Button(root, text="Chọn ảnh", command=open_image)
load_button.pack()

# Slider for effect strength
slider_label = tk.Label(root, text="Mức độ mờ")
slider_label.pack()
effect_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.01, orient='horizontal', command=update_effect_strength)
effect_slider.set(0.0)
effect_slider.pack()

# Set up the OpenCV mouse callback to apply the effect on mouse click
cv2.namedWindow('Original')

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        apply_effect(x, y)

cv2.setMouseCallback('Original', on_mouse)

root.mainloop()
