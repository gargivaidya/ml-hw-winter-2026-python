"""
Module 6 
Author : Gargi Vaidya
"""

import numpy as np


class KNNRegression:
    def __init__(self):
        self.x = None
        self.y = None

    def fit(self, x_values, y_values):
        self.x = np.array(x_values, dtype=float)
        self.y = np.array(y_values, dtype=float)

    def predict(self, query_x, k):
        if k <= 0:
            raise ValueError("Error: k must be positive.")
        if k > len(self.x):
            raise ValueError("Error: k cannot be greater than N.")

        # Compute L1 (Manhattan) distance
        distances = np.abs(self.x - query_x)

        # Get indices of k smallest distances (O(N))
        k_indices = np.argpartition(distances, k)[:k]

        # Return mean of corresponding y values
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

    print("Enter points (x then y):")
    x_values = []
    y_values = []

    for _ in range(N):
        x_values.append(float(input()))
        y_values.append(float(input()))

    model = KNNRegression()
    model.fit(x_values, y_values)

    query_x = float(input("Enter query X: "))

    try:
        result = model.predict(query_x, k)
        print("Predicted Y:", result)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()