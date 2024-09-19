import numpy as np
import matplotlib.pyplot as plt


# Hàm vẽ đồ thị parabol sử dụng thuật toán Bresenham
def bresenham_parabola(a, b, c, x_min, x_max, step):
    x = np.arange(x_min, x_max, step)
    y = a * x**2 + b * x + c

    # Chuyển đổi các giá trị y sang tọa độ pixel
    scale_factor = 100  # Hệ số scale để làm rõ đồ thị
    y_pixel = np.round(y * scale_factor).astype(int)
    x_pixel = np.round(x * scale_factor).astype(int)

    # Danh sách lưu trữ các điểm parabol
    points_x = []
    points_y = []

    for i in range(len(x) - 1):
        x1, y1 = x_pixel[i], y_pixel[i]
        x2, y2 = x_pixel[i + 1], y_pixel[i + 1]

        # Bresenham cho đoạn thẳng giữa (x1, y1) và (x2, y2)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            points_x.append(x1 / scale_factor)  # Chuyển ngược lại tỉ lệ để vẽ đúng x
            points_y.append(y1 / scale_factor)

            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    # Vẽ đồ thị parabol
    plt.plot(points_x, points_y, "bo-", label=f"y = {a}x^2 + {b}x + {c}")
    plt.title("Đồ thị parabol sử dụng thuật toán Bresenham")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.savefig("./src/19-09-2024/parabol/bresenham/parabol.png")


# Gọi hàm để vẽ đồ thị parabol với a=1, b=0, c=0, x từ -10 đến 10, bước nhảy 0.1
bresenham_parabola(1, 0, 0, -10, 10, 0.1)
