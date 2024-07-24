# Linear Regression using Normal Equation

Write a Python function that performs linear regression using the normal equation. The function should take a matrix $X$ (feature) and a vector $y$ (target) as input, and return the coefficients of the linear regression model.

Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.

```python
Example:
    input: X = [[1, 1], [1, 2], [1, 3]], y = [1, 2, 3]
    output: [0.0, 1.0]
    reasoning:
        # The linear model is y = 0.0 + 1.0 * x,
        # perfectly fitting the input data
```

## Learn

Linear regression aims to model the relationship between a scalar dependent variable $y$ and one or more explanatory variables (or independent variables) $X$. The normal equation provides an analytical solution to finding the coefficients $\theta$ that minimize the cost function for linear regression. 

Given a matrix $X$ (with each row representing a training example and each column a feature) and a vector $y$ (representing the target values), the normal equation is:

$$
\theta = (X^T X) ^{-1} X^T y
$$

where:
- $X^T$ is the transpose of $X$,
- $(X^T X)^{-1}$ is the inverse of the matrix $X^T X$,
- $y$ is the target vector

**NOTE**: this method does not require any feature scaling, and there is no need to choose a learning rate. However, computing the inverse of $X^T X$ can be computationally expensive for large datasets.

## Practical Implementation

A practical implementation involves augmenting $X$ with a column of ones to account for the intercept term and then apply the normal equation directly to compute $\theta$.

## My Solution

```python
import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)

    theta = np.round(np.linalg.inv(X.T @ X) @ X.T @ y, 4)
    return theta.tolist()
```

## Standard Solution

```python
import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    X_transpose = X.T
    theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
    theta = np.round(theta, 4).flatten().tolist()
    return theta

```