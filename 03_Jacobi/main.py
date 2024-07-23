import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = np.zeros(len(A))
    tmp = np.zeros(len(A))
    for _ in range(n):
        for i in range(len(A)):
            tmp[i] = np.round((1 / A[i, i]) * (b[i] - sum(A[i, j] * x[j] for j in range(len(A)) if j != i)), 4)
        x = tmp.copy()
    return x.tolist()

if __name__ == "__main__":
    A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
    b = np.array([-1, 2, 3])
    n = 2
    x = solve_jacobi(A, b, n)
    print(x)