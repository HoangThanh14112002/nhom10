import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = array(df.iloc[:, :])

# Tạo cửa sổ chính và đặt kích thước
root = tk.Tk()
root.title("Ứng dụng Thông tin và Biểu đồ")
root.geometry("800x600")  # Đặt kích thước cửa sổ là 800x600 pixel

# Tạo hàm để hiển thị thông tin sinh viên
def hien_thi_thong_tin():
    info_window = tk.Toplevel(root)
    info_window.title("Thông tin sinh viên")

    tongsv = np.sum(in_data[:, 1])
    diemA = sum(in_data[:, 3])
    diemF = sum(in_data[:, 10])
    chuanL1 = sum(in_data[:, 11])
    chuanL2 = sum(in_data[:, 12])

    info_label = tk.Label(info_window, text=f"Tổng số sinh viên đi thi: {tongsv}\n"
                                           f"Tổng số sinh viên đạt điểm A: {diemA}\n"
                                           f"Tổng số sinh viên đạt điểm F: {diemF}\n"
                                           f"Tổng số sinh viên đạt chuẩn L1: {chuanL1}\n"
                                           f"Tổng số sinh viên đạt chuẩn L2: {chuanL2}\n")
    info_label.pack()

# Tạo hàm để hiển thị biểu đồ
def hien_thi_bieu_do():
    chart_window = tk.Toplevel(root)
    chart_window.title("Biểu đồ")

    diemA = in_data[:, 3]
    diemF = in_data[:, 10]

    fig, ax = plt.subplots(figsize=(8, 6))  # Đặt kích thước biểu đồ là 800x600 pixel
    ax.plot(range(len(diemA)), diemA, 'r-', label="Diem A")
    ax.plot(range(len(diemF)), diemF, 'g-', label="Diem F")
    ax.set_xlabel('Lơp')
    ax.set_ylabel('So sv dat diem')
    ax.legend(loc='upper right')

    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.get_tk_widget().pack()

# Tạo các nút để chuyển đổi giữa cửa sổ thông tin và cửa sổ biểu đồ
button_thong_tin = ttk.Button(root, text="Thông tin sinh viên", command=hien_thi_thong_tin)
button_thong_tin.pack()

button_bieu_do = ttk.Button(root, text="Biểu đồ", command=hien_thi_bieu_do)
button_bieu_do.pack()

root.mainloop()
