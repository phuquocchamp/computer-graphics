import numpy as np
import matplotlib.pyplot as plt


# Hàm vẽ đồ thị hyperbola sử dụng thuật toán Bresenham
def bresenham_hyperbola(a, b, x_min, x_max, step):
    x = np.arange(x_min, x_max, step)

    # Tính giá trị y tương ứng cho phần dương của hyperbola
    y_pos = np.sqrt((x**2 / a**2 - 1) * b**2)
    y_neg = -y_pos

    # Chuyển đổi giá trị thành tọa độ pixel
    scale_factor = 50  # Hệ số scale để phóng to đồ thị
    x_pixel = np.round(x * scale_factor).astype(int)
    y_pos_pixel = np.round(y_pos * scale_factor).astype(int)
    y_neg_pixel = np.round(y_neg * scale_factor).astype(int)

    # Danh sách lưu trữ các điểm hyperbola
    points_x = []
    points_y = []

    # Áp dụng thuật toán Bresenham cho đoạn thẳng giữa các điểm
    def bresenham(x1, y1, x2, y2):
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

    for i in range(len(x) - 1):
        x1, y1_pos = x_pixel[i], y_pos_pixel[i]
        x2, y2_pos = x_pixel[i + 1], y_pos_pixel[i + 1]
        x1, y1_neg = x_pixel[i], y_neg_pixel[i]
        x2, y2_neg = x_pixel[i + 1], y_neg_pixel[i + 1]

        # Vẽ các đoạn thẳng cho cả hai phần dương và âm
        bresenham(x1, y1_pos, x2, y2_pos)
        bresenham(x1, y1_neg, x2, y2_neg)

    # Vẽ đồ thị hyperbola
    plt.plot(points_x, points_y, "bo-", label=f"Hyperbola: x^2/{a}^2 - y^2/{b}^2 = 1")
    plt.title("Đồ thị Hyperbola sử dụng thuật toán Bresenham")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.savefig("./src/19-09-2024/hyperpol/bresenham/hyperpol.png")


# Gọi hàm để vẽ đồ thị hyperbola với a=3, b=2, x từ 4 đến 10, bước nhảy 0.1
bresenham_hyperbola(3, 2, 4, 10, 0.1)
