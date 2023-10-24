import cv2
import tkinter as tk 
from tkinter import filedialog, Entry, Button, Label, messagebox
import matplotlib.pyplot as plt

combined_image = None

def change_color_map():
    global combined_image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path, 1)
        if image is not None:
            color_map_index = int(entry.get())

            if 0 <= color_map_index <= 21:
                color_mapped_image = cv2.applyColorMap(image, color_map_index)

                height, width, _ = image.shape
                desired_size = (width, height)

                image = cv2.resize(image, desired_size)
                color_mapped_image = cv2.resize(color_mapped_image, desired_size)

                # Kiểm tra giá trị alpha
                try:
                    alpha = float(alpha_entry.get())
                    if 0 <= alpha <= 1:
                        combined_image = cv2.addWeighted(image, 1 - alpha, color_mapped_image, alpha, 0)
                    else:
                        messagebox.showerror("Lỗi", "Hệ số alpha phải nằm trong khoảng từ 0 đến 1.")
                        return
                except ValueError:
                    messagebox.showerror("Lỗi", "Hệ số alpha không hợp lệ. Vui lòng nhập số từ 0 đến 1.")
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

def combine_images():
    global combined_image
    if combined_image is not None:
        file_path = filedialog.askopenfilename()
        if file_path:
            second_image = cv2.imread(file_path, 1)
            if second_image is not None:

                second_image = cv2.resize(second_image, combined_image.shape[:2][::-1])

               
                try:
                    alpha = float(alpha_entry.get())
                    if 0 <= alpha <= 1:
                        combined_result = cv2.addWeighted(combined_image, 1 - alpha, second_image, alpha, 0)
                    else:
                        messagebox.showerror("Lỗi", "Hệ số alpha phải nằm trong khoảng từ 0 đến 1.")
                        return
                except ValueError:
                    messagebox.showerror("Lỗi", "Hệ số alpha không hợp lệ. Vui lòng nhập số từ 0 đến 1.")
                    return

                plt.figure()
                plt.title("Kết hợp ảnh")
                plt.imshow(cv2.cvtColor(combined_result, cv2.COLOR_BGR2RGB))
                plt.axis("off")
                plt.show()
            else:
                messagebox.showerror("Lỗi",
                                     "Không thể đọc hình ảnh thứ hai. Vui lòng chắc chắn rằng tệp hình ảnh đúng định dạng.")
        else:
            messagebox.showinfo("Thông báo", "Không có tệp hình ảnh thứ hai nào được chọn.")

def main():
    root = tk.Tk()
    root.title("Change and Combine Images")

    global entry, alpha_entry
    entry = Entry(root)
    entry.pack()

    label = Label(root, text="Nhập chỉ số thay đổi màu sắc (0-21):")
    label.pack()

    alpha_label = Label(root, text="Nhập hệ số alpha (0-1) alpha :")
    alpha_label.pack()

    alpha_entry = Entry(root)
    alpha_entry.pack()

    show_button = Button(root, text="Hiển thị Ảnh", command=change_color_map)
    show_button.pack()

    combine_button = Button(root, text="Kết hợp Ảnh", command=combine_images)
    combine_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
