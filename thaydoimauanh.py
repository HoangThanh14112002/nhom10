import cv2
import tkinter as tk
from tkinter import filedialog, Entry, Button, Label, Scale, messagebox
import matplotlib.pyplot as plt

combined_image = None

def change_color_map():
    global combined_image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path, 1)
        if image is not None:
            color_map_index = scale.get()
            if 0 <= color_map_index <= 21:
                color_mapped_image = cv2.applyColorMap(image, color_map_index)
                height, width, _ = image.shape
                desired_size = (width, height)
                image = cv2.resize(image, desired_size)
                color_mapped_image = cv2.resize(color_mapped_image, desired_size)
                alpha = scale_alpha.get()
                if 0 <= alpha <= 1:
                    combined_image = cv2.addWeighted(image, 1 - alpha, color_mapped_image, alpha, 0)
                else:
                    messagebox.showerror("Lỗi", "Hệ số alpha phải nằm trong khoảng từ 0 đến 1.")
                    return
                plt.subplot(1, 2, 1)
                plt.title("Ảnh gốc")
                plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                plt.axis("off")
                plt.subplot(1, 2, 2)
                plt.title("Ảnh sau thay đổi")
                plt.imshow(cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB))
                plt.axis("off")
                plt.show()
            else:
                messagebox.showerror("Lỗi", "Chỉ số thay đổi màu sắc phải nằm trong khoảng từ 0 đến 21.")
        else:
            messagebox.showerror("Lỗi", "Không thể đọc ảnh. Vui lòng chắc chắn rằng tệp ảnh đúng định dạng.")
    else:
        messagebox.showinfo("Thông báo", "Không có tệp ảnh nào được chọn.")

def main():
    root = tk.Tk()
    root.title("Change and Combine Images")
    global scale, scale_alpha
    label = Label(root, text="Chọn chỉ số thay đổi màu sắc (0 - 21):")
    label.pack()
    scale = Scale(root, from_=0, to=21, orient=tk.HORIZONTAL)
    scale.pack()
    alpha_label = Label(root, text="Chọn hệ số alpha (0 - 1):")
    alpha_label.pack()
    scale_alpha = Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL)
    scale_alpha.pack()
    show_button = Button(root, text="Chọn ảnh", command=change_color_map)
    show_button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
