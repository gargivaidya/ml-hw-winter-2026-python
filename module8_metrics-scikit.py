"""
Module 8 
Author : Gargi Vaidya
"""
import numpy as np
from sklearn.metrics import precision_score, recall_score

class ClassificationMetrics:
    def __init__(self, N):
        self.N = N
        self.y_true = np.zeros(N, dtype=int)
        self.y_pred = np.zeros(N, dtype=int)
        self.index = 0

    def insert_point(self, true_label, predicted_label):
        self.y_true[self.index] = true_label
        self.y_pred[self.index] = predicted_label
        self.index += 1

    def compute_metrics(self):
        precision = precision_score(self.y_true, self.y_pred)
        recall = recall_score(self.y_true, self.y_pred)
        return precision, recall


def main():
    N = int(input("Enter N (number of points): "))

    if N <= 0:
        print("Error: N must be positive.")
        return

    model = ClassificationMetrics(N)

    print("Enter points (x then y):")
    print("(x = ground truth label, y = predicted label, both 0 or 1)")

    for _ in range(N):
        x_val = int(input())
        y_val = int(input())

        if x_val not in [0, 1] or y_val not in [0, 1]:
            print("Error: Labels must be 0 or 1.")
            return

        model.insert_point(x_val, y_val)

    precision, recall = model.compute_metrics()

    print("Precision:", precision)
    print("Recall:", recall)


if __name__ == "__main__":
    main()