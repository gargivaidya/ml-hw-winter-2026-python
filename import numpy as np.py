import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def main():
    # Read N
    try:
        N = int(input("Enter N (number of points): "))
        if N <= 0:
            print("Error: N must be a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input for N.")
        return

    # Read k
    try:
        k = int(input("Enter k: "))
        if k <= 0:
            print("Error: k must be a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input for k.")
        return

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    # Initialize NumPy arrays
    X_train = np.zeros((N, 1))  # feature matrix
    y_train = np.zeros(N)      # label vector

    print("Enter points (x then y):")

    # Insert data using NumPy
    for i in range(N):
        try:
            x_val = float(input())
            y_val = float(input())
        except ValueError:
            print("Error: Invalid input for point values.")
            return

        X_train[i, 0] = x_val
        y_train[i] = y_val

    # Compute variance of labels
    variance = np.var(y_train)

    # ML part using Scikit-learn
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    # Query input
    try:
        X_query = float(input("Enter query X: "))
    except ValueError:
        print("Error: Invalid input for query.")
        return

    X_query_np = np.array([[X_query]])

    # Prediction
    y_pred = model.predict(X_query_np)

    print("Predicted Y:", y_pred[0])
    print("Variance of training labels:", variance)


if __name__ == "__main__":
    main()