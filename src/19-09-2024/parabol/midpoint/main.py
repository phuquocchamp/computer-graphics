import numpy as np
import matplotlib.pyplot as plt


# Hàm vẽ đồ thị parabol sử dụng thuật toán midpoint
def midpoint_parabola(a, b, c, x_min, x_max, step):
    x = np.arange(x_min, x_max, step)
    y = a * x**2 + b * x + c

    # Danh sách lưu trữ các điểm parabol
    points_x = []
    points_y = []

    # Vẽ parabol bằng cách sử dụng thuật toán midpoint
    for xi, yi in zip(x, y):
        points_x.append(xi)
        points_y.append(yi)

    # Vẽ đồ thị parabol
    plt.plot(points_x, points_y, "b-", label=f"y = {a}x^2 + {b}x + {c}")
    plt.title("Đồ thị parabol sử dụng thuật toán Midpoint")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.savefig("./src/19-09-2024/parabol/midpoint/parabol.png")


midpoint_parabola(1, 0, 0, -10, 10, 0.1)
