import numpy as np
import matplotlib.pyplot as plt


# Hàm vẽ đồ thị hyperbol sử dụng thuật toán midpoint
def midpoint_hyperbola(a, b, x_min, x_max, step):
    # Tạo giá trị x từ x_min đến x_max
    x = np.arange(x_min, x_max, step)

    # Tính giá trị y tương ứng cho phần dương của hyperbola
    y_pos = np.sqrt((x**2 / a**2 - 1) * b**2)
    y_neg = -y_pos

    # Danh sách lưu trữ các điểm hyperbol
    points_x = []
    points_y = []

    # Vẽ phần hyperbola dương và âm
    for xi, yi_pos, yi_neg in zip(x, y_pos, y_neg):
        points_x.extend([xi, xi])
        points_y.extend([yi_pos, yi_neg])

    # Vẽ đồ thị hyperbola
    plt.plot(points_x, points_y, "bo-", label=f"Hyperbola: x^2/{a}^2 - y^2/{b}^2 = 1")
    plt.title("Đồ thị Hyperbola sử dụng thuật toán Midpoint")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.savefig("./src/19-09-2024/hyperpol/midpoint/hyperpol.png")


# Gọi hàm để vẽ đồ thị hyperbola với a=3, b=2, x từ 4 đến 20, bước nhảy 0.1
midpoint_hyperbola(3, 2, 4, 20, 0.1)
