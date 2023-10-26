import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Define global variables
img = None
original_img = None  # This will hold the original image
rows, cols = 0, 0
kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
kernel_5x5 = np.ones((5, 5), np.float32) / 25.0
effect_strength = 0.0  # Initial effect strength

def hieu_ung_lam_mo(x, y):
    global img, effect_strength

    # Define a region around the clicked point
    x1, y1, x2, y2 = max(0, x - 25), max(0, y - 25), min(cols, x + 25), min(rows, y + 25)
    roi = img[y1:y2, x1:x2]

    blur_kernel = np.ones((9, 9), np.float32) / (9.0 + 80.0 * effect_strength)
    blurred_roi = cv2.filter2D(roi, -1, blur_kernel)
    img[y1:y2, x1:x2] = blurred_roi

    cv2.imshow('Original', img)

def chon_anh():
    global img, original_img, rows, cols
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    original_img = img.copy()  # Save a copy of the original image
    rows, cols = img.shape[:2]
    cv2.imshow('Original', img)

def muc_do_mo(value):
    global effect_strength
    effect_strength = float(value)

def lam_sac_net():
    global img
    kernel_sharpen = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel_sharpen)
    cv2.imshow('Original', img)

def thay_doi_do_sang_va_do_tuong_phan():
    global img
    brightness = 70
    contrast = 35
    img = cv2.convertScaleAbs(img, alpha=(1 + contrast / 100.0), beta=brightness)
    cv2.imshow('Original', img)

def Khoi_phuc_anh_goc():
    global img, original_img
    img = original_img.copy()  # Restore the original image
    cv2.imshow('Original', img)

# Create the main window
root = tk.Tk()
root.title("Chỉnh sửa ảnh")

# Load button
load_button = tk.Button(root, text="Chọn ảnh", command=open_image)
load_button.pack()

# Slider for effect strength
slider_label = tk.Label(root, text="Mức độ mờ")
slider_label.pack()
effect_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.01, orient='horizontal', command=update_effect_strength)
effect_slider.set(0.0)
effect_slider.pack()

# Add a button for the sharpen function
sharpen_button = tk.Button(root, text="Làm sắc nét", command=sharpen_image)
sharpen_button.pack()

# Add a button for the brightness/contrast function
brightness_contrast_button = tk.Button(root, text="Thay đổi độ sáng và độ tương phản", command=change_brightness_contrast)
brightness_contrast_button.pack()

# Add a button for the reset function
reset_button = tk.Button(root, text="Khôi phục ảnh gốc", command=reset_image)
reset_button.pack()

# Set up the OpenCV mouse callback to apply the effect on mouse click
cv2.namedWindow('Original')

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        apply_effect(x, y)

cv2.setMouseCallback('Original', on_mouse)

root.mainloop()
