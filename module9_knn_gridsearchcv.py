"""
Module 9 
Author : Gargi Vaidya
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def main():

    N = int(input("Enter N (number of training pairs): "))

    if N <= 0:
        print("Error: N must be positive.")
        return

    X_train = np.zeros((N, 1))
    y_train = np.zeros(N, dtype=int)

    print("Enter training pairs (x then y):")

    for i in range(N):
        try:
            x_val = float(input())
            y_val = int(input())
        except ValueError:
            print("Error: Invalid input.")
            return

        if y_val < 0:
            print("Error: Y must be non-negative.")
            return

        X_train[i, 0] = x_val
        y_train[i] = y_val

    M = int(input("Enter M (number of test pairs): "))

    if M <= 0:
        print("Error: M must be positive.")
        return

    X_test = np.zeros((M, 1))
    y_test = np.zeros(M, dtype=int)

    print("Enter test pairs (x then y):")

    for i in range(M):
        try:
            x_val = float(input())
            y_val = int(input())
        except ValueError:
            print("Error: Invalid input.")
            return

        if y_val < 0:
            print("Error: Y must be non-negative.")
            return

        X_test[i, 0] = x_val
        y_test[i] = y_val

    param_grid = {'n_neighbors': list(range(1, 11))}

    model = KNeighborsClassifier()

    grid = GridSearchCV(
        model,
        param_grid,
        scoring='accuracy',
        cv=min(3, N)
    )

    grid.fit(X_train, y_train)

    best_k = grid.best_params_['n_neighbors']

    best_model = grid.best_estimator_

    test_accuracy = best_model.score(X_test, y_test)

    print("Best k:", best_k)
    print("Test Accuracy:", test_accuracy)


if __name__ == "__main__":
    main()