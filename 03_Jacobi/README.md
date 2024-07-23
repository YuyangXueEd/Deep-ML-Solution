# Solve Linear Equations using Jacobi Method

Write a Python function that uses the Jacobi method to solve a system of linear equations given by $Ax = b$. The function should iterate 10 times, rounding each intermediate solution to four decimal places, and return the approximate solution $x$.

## Example 

```python
Example:
    input: A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]], b = [-1, 2, 3], n=2
    output: [0.146, 0.2032, -0.5175]
    reasoning:
        # The jacobi method iteratively solves each equation for x[i] using the formula 
        # x[i]= (1/a_ii) * (b[i] - sum(a_ij * x[j] for j != i)),
        # where a_ii is the diagonal element of A and a_ij is the off-diagonal element.
```

## Learn

The jacobi method is an iterative algorithm used for solving a system of linear equations $Ax = b$. This method is particularly useful for large systems where direct methods like Gaussian elimination are computationally expensive.

### Algorithm Overview

For a system of equations represented by $Ax = b$, where $A$ is a matrix and $x$ and $b$ are vectors, the Jacobi method involves the following steps:
1. Initialisation: Start with an initial guess for $x$.
2. Iteration: For each equation $i$, update $x[i]$ using:

$$ x[i]=\frac{1}{a_{ii}}(b[i]- \sum_{j\neq i} a_{ij}x[j])$$

where $a_{ii}$ is the diagonal element of $A$ and $a_{ij}$ is the off-diagonal element.
3. Convergence: Repeat the iteration until the changes in $x$ are below a certain tolerance or until a maximum number of iterations is reached.

This method assumes that all diagonal elements of $A$ are non-zero and that the matrix is diagonally dominant or properly conditioned for convergence.

### Practical Considerations

- The method may not converge for all matrices.
- Choosing a good initial guess can improve convergence.
- Diagonal dominance of $A$ ensures convergence of the Jacobi method.


## My Solution

```python
import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = np.zeros(len(A))
    # Use a temporary array to store the updated values of x
    tmp = np.zeros(len(A))
    for _ in range(n):
        for i in range(len(A)):
            # Update tmp[i] using the Jacobi method formula
            tmp[i] = np.round((1 / A[i, i]) * (b[i] - sum(A[i, j] * x[j] for j in range(len(A)) if j != i)), 4)
        # Update x with the values from tmp
        x = tmp.copy()
        
    return x.tolist()
```

## Standard Solution

```python
import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    d_a = np.diag(A)
    nda = A - np.diag(d_a)
    x = np.zeros(len(b))
    x_hold = np.zeros(len(b))
    for _ in range(n):
        for i in range(len(A)):
            x_hold[i] = (1/d_a[i]) * (b[i] - sum(nda[i]*x))
        x = x_hold.copy()
    return np.round(x,4).tolist()
```