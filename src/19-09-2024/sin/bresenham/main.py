import numpy as np
import matplotlib.pyplot as plt


# Thuật toán Bresenham để vẽ đồ thị sin(x)
def bresenham_sin(x_start, x_end, amplitude, resolution):
    points = []

    # Thiết lập điểm bắt đầu và kết thúc
    x0 = x_start
    x1 = x_end

    # Độ dài của đồ thị trên trục x
    dx = x1 - x0

    # Đi qua từng điểm trên trục x với độ phân giải
    for x in range(x_start, x_end, resolution):
        # Tính giá trị y cho sin(x)
        y = amplitude * np.sin(x * np.pi / 180)  # Chuyển độ sang radian

        # Lưu điểm (x, y)
        points.append((x, y))

    return points


# Hàm vẽ đồ thị sin(x) sử dụng thuật toán Bresenham
def draw_bresenham_sin():
    # Lấy các điểm của đồ thị sin(x) bằng thuật toán Bresenham
    points = bresenham_sin(-360, 360, 1, 1)

    # Chia các điểm thành x và y
    x_vals, y_vals = zip(*points)

    # Vẽ đồ thị sin(x)
    plt.plot(x_vals, y_vals, "ro-", label="sin(x) - Bresenham")

    # Cài đặt tiêu đề và nhãn
    plt.title("Đồ thị sin(x) sử dụng thuật toán Bresenham")
    plt.xlabel("x (degrees)")
    plt.ylabel("sin(x)")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.savefig("./src/19-09-2024/sin/bresenham/sin.png")


# Gọi hàm để vẽ đồ thị sin(x)
draw_bresenham_sin()
