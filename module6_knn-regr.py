"""
Module 6 
Author : Gargi Vaidya
"""
import numpy as np

class KNNRegression:
    def __init__(self, n_points):
        self.n_points = n_points
        self.x = np.array([], dtype=float)
        self.y = np.array([], dtype=float)

    def insert_point(self, x_value, y_value):
        self.x = np.append(self.x, x_value)
        self.y = np.append(self.y, y_value)

    def predict(self, query_x, k):
        if k > self.n_points:
            raise ValueError("Error: k cannot be greater than N.")

        distances = np.abs(self.x - query_x)
        k_indices = np.argsort(distances)[:k]
        return np.mean(self.y[k_indices])


def main():
    N = int(input("Enter N (number of points): "))

    if N <= 0:
        print("Error: N must be positive.")
        return

    k = int(input("Enter k: "))

    if k <= 0:
        print("Error: k must be positive.")
        return

    model = KNNRegression(N)

    print("Enter points (x then y):")
    for i in range(N):
        x_val = float(input())
        y_val = float(input())
        model.insert_point(x_val, y_val)

    query_x = float(input("Enter query X: "))

    try:
        result = model.predict(query_x, k)
        print("Predicted Y:", result)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()