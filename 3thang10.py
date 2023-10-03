import tkinter as tk
from sympy import *


def open_limit_window():
    limit_window = tk.Toplevel(app)
    limit_window.title("Tính Giới Hạn")

    limit_label = tk.Label(limit_window, text="Nhập biểu thức cần tính giới hạn:")
    limit_label.pack()

    limit_entry = tk.Entry(limit_window)
    limit_entry.pack()

    limit_value_label = tk.Label(limit_window, text="Nhập giá trị tiến đến:")
    limit_value_label.pack()

    limit_value_entry = tk.Entry(limit_window)
    limit_value_entry.pack()

    calculate_limit_button = tk.Button(limit_window, text="Tính Giới Hạn",
                                       command=lambda: calculate_limit(limit_entry.get(), limit_value_entry.get()))
    calculate_limit_button.pack()


def open_derivative_window():
    derivative_window = tk.Toplevel(app)
    derivative_window.title("Tính Đạo Hàm")

    derivative_label = tk.Label(derivative_window, text="Nhập biểu thức cần tính đạo hàm:")
    derivative_label.pack()

    derivative_entry = tk.Entry(derivative_window)
    derivative_entry.pack()

    calculate_derivative_button = tk.Button(derivative_window, text="Tính Đạo Hàm",
                                            command=lambda: calculate_derivative(derivative_entry.get()))
    calculate_derivative_button.pack()


def open_integral_window():
    integral_window = tk.Toplevel(app)
    integral_window.title("Tính Tích Phân")

    integral_label = tk.Label(integral_window, text="Nhập biểu thức cần tính tích phân:")
    integral_label.pack()

    integral_entry = tk.Entry(integral_window)
    integral_entry.pack()

    calculate_integral_button = tk.Button(integral_window, text="Tính Tích Phân",
                                          command=lambda: calculate_integral(integral_entry.get()))
    calculate_integral_button.pack()


def open_polynomial_division_window():
    division_window = tk.Toplevel(app)
    division_window.title("Chia Đa Thức")

    dividend_label = tk.Label(division_window, text="Nhập biểu thức cho số tử của đa thức:")
    dividend_label.pack()

    dividend_entry = tk.Entry(division_window)
    dividend_entry.pack()

    divisor_label = tk.Label(division_window, text="Nhập biểu thức cho số mẫu của đa thức:")
    divisor_label.pack()

    divisor_entry = tk.Entry(division_window)
    divisor_entry.pack()

    calculate_polynomial_division_button = tk.Button(division_window, text="Chia Đa Thức",
                                                     command=lambda: calculate_polynomial_division(dividend_entry.get(),
                                                                                                   divisor_entry.get()))
    calculate_polynomial_division_button.pack()


def calculate_limit(expression, limit_value):
    x = Symbol('x')
    result = limit(sympify(expression), x, float(limit_value))
    result_label.config(text=f"Giới hạn của {expression} khi x tiến đến {limit_value} là: {result}")


def calculate_derivative(expression):
    x = Symbol('x')
    result = diff(sympify(expression), x)
    result_label.config(text=f"Đạo hàm của {expression} là: {result}")


def calculate_integral(expression):
    x = Symbol('x')
    result = integrate(sympify(expression), x)
    result_label.config(text=f"Tích phân của {expression} là: {result}")


def calculate_polynomial_division(dividend, divisor):
    x = Symbol('x')
    quotient, remainder = div(sympify(dividend), sympify(divisor))
    result_label.config(text=f"Kết quả chia đa thức {dividend} cho {divisor} là:\nKết quả: {quotient}\nDư: {remainder}")


app = tk.Tk()
app.title("Ứng dụng Giải Tích")
app.geometry("900x500")
app.tk.call('tk', 'scaling', 1.5)  


result_label = tk.Label(app, text="", wraplength=400)
result_label.grid(column=0, row=0, padx=10, pady=10)


limit_button = tk.Button(app, text="Tính Giới Hạn", command=open_limit_window)
limit_button.grid(column=0, row=1, padx=10, pady=10)

derivative_button = tk.Button(app, text="Tính Đạo Hàm", command=open_derivative_window)
derivative_button.grid(column=0, row=2, padx=10, pady=10)

integral_button = tk.Button(app, text="Tính Tích Phân", command=open_integral_window)
integral_button.grid(column=0, row=3, padx=10, pady=10)

division_button = tk.Button(app, text="Chia Đa Thức", command=open_polynomial_division_window)
division_button.grid(column=0, row=4, padx=10, pady=10)

app.mainloop()

