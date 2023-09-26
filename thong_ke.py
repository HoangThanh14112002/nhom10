import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import scrolledtext


def run_code():
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv('diemPython.csv', index_col=0, header=0)

    # Chuyển DataFrame thành mảng numpy
    in_data = np.array(df.iloc[:, :])

    # Tính tổng số sinh viên đi thi
    tong_sv = in_data[:, 1].sum()
    result_text.insert(tk.INSERT, f'Tổng số sinh viên đi thi: {tong_sv}\n')

    # Lấy dữ liệu điểm A+ đến F
    diem = {'A+': 2, 'A': 3, 'B+': 4, 'B': 5, 'C+': 6, 'C': 7, 'D+': 8, 'D': 9, 'F': 10}
    for grade, column in diem.items():
        diem_grade = in_data[:, column]
        max_diem_grade = diem_grade.max()
        lop_co_nhieu_diem_grade_nhat = np.where(diem_grade == max_diem_grade)[0]
        result_text.insert(tk.INSERT,
                           f'Lớp có nhiều điểm {grade} nhất là {in_data[lop_co_nhieu_diem_grade_nhat, 0]} với {max_diem_grade} sinh viên đạt điểm {grade}\n')

    # Tính tổng số sinh viên đạt từng loại điểm A+, A, B+, B, C+, C, D+, D, F
    for grade, column in diem.items():
        tong_diem_grade = in_data[:, column].sum()
        result_text.insert(tk.INSERT, f'Tổng số sinh viên đạt điểm {grade}: {tong_diem_grade}\n')

    # Vẽ biểu đồ
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    for grade, column in diem.items():
        ax.plot(range(len(in_data[:, column])), in_data[:, column], label=f"Điểm {grade}")
    ax.set_xlabel('Lớp')
    ax.set_ylabel('Số sv đạt điểm')
    ax.legend(loc='upper right')

    # Hiển thị biểu đồ trên giao diện tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Tạo giao diện tkinter
root = tk.Tk()
root.title("Ứng dụng Thống kê và Biểu đồ")
root.geometry("800x600")  # Đặt kích thước cửa sổ là 800x600 pixel

# Tạo khung văn bản cuộn để hiển thị kết quả
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
result_text.pack(fill=tk.BOTH, expand=True)

# Tạo các nút để chạy mã và hiển thị thông tin
button_run = tk.Button(root, text="Run Code", command=run_code)
button_run.pack()

root.mainloop()
