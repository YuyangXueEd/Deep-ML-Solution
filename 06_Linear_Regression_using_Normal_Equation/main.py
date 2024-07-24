import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)

    theta = np.round(np.linalg.inv(X.T @ X) @ X.T @ y, 4)
    return theta.tolist()


if __name__ == "__main__":
    X = [[1, 1], [1, 2], [1, 3]]
    y = [1, 2, 3]
    theta = linear_regression_normal_equation(X, y)
    print(theta)  # Expected output: [0.0, 1.0]
