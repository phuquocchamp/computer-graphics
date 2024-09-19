import numpy as np
import matplotlib.pyplot as plt


# Hàm vẽ đồ thị sin(x) sử dụng thuật toán midpoint
def draw_sin_midpoint():
    # Tạo giá trị x từ -2pi đến 2pi
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

    # Tính giá trị sin(x) tại các điểm x
    y = np.sin(x)

    # Tạo danh sách điểm bằng phương pháp midpoint
    points_x = []
    points_y = []

    for i in range(len(x) - 1):
        # Lấy điểm hiện tại và điểm kế tiếp
        x1, y1 = x[i], y[i]
        x2, y2 = x[i + 1], y[i + 1]

        # Tính điểm giữa
        xm = (x1 + x2) / 2
        ym = np.sin(xm)

        # Lưu các điểm: điểm hiện tại, điểm giữa, và điểm kế tiếp
        points_x.extend([x1, xm])
        points_y.extend([y1, ym])

    # Vẽ đồ thị sin(x) sử dụng các điểm midpoint
    plt.plot(points_x, points_y, "bo-", label="Midpoint sin(x)")

    # Cài đặt tiêu đề và nhãn cho đồ thị
    plt.title("Đồ thị sin(x) sử dụng thuật toán Midpoint")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.savefig("./src/19-09-2024/sin/midpoint/sin.png")


# Gọi hàm để vẽ đồ thị sin(x)
draw_sin_midpoint()
