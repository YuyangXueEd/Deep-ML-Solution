# Calculate Covariance Matrix

Write a Python function that calculates the covariance matrix from a list of vectors.
Assume that the input list represents a dataset where each vector is a feature, and vectors are of equal length.

```python
Example:
    input: vectors = [[1, 2, 3], [4, 5, 6]]
    output: [[1.0, 1.0], [1.0, 1.0]]
    reasoning: 
        #The dataset has two features with three observations each. 
        #The covariance between each pair of features (including
        #covariance with itself) is calculated and returned as 
        #a 2x2 matrix.
```

## Learn

The covariance matrix is a fundamental concept in statistics, illustrating how much two random variables change together. It is essential for understanding the relationships between variables in a dataset. 

For a dataset with $n$ features, the covariance matrix is an $n\times n$ square matrix where each element $(i, j)$ represents the covariance between the $i$-th and $j$-th features. 

Covariance is defined by the formula:

$$
\text{cov}(X,Y)=\frac{\sum^n_{i=1}(x_i-\bar{x})(y_i-\bar{y}}{n-1}
$$

where 
- $X$ and $Y$ are two random variables (features);
- $x_i$ and $y_i$ are individual observations of $X$ and $Y$; 
- $\bar{x}$ and $\bar{y}$ are the means of $X$ and $Y$;
- $n$ is the number of observations.

In the covariance matrix:
- The diagonal elements (where $i=j$) indicate the variance of each feature.
- The off-diagonal elements show the covariance between different features.
This matrix is symmetric, as the covariance between $X$ and $Y$ is equal to the covariance between $Y$ and $X$, denoted as $\text{cov}(X, Y) = \text{cov}(Y, X)$.

## My Solution

```python
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    num_of_features = len(vectors)
    num_of_observations = len(vectors[0])
    # mind the initialisation
    # don't use [[0]*num_of_features]*num_of_features
    # it will create a list of references to the same list
    covariance_matrix = [[0 for _ in range(num_of_features)] for _ in range(num_of_features)]

    # Calculate the mean vector
    mean_vector = []
    for i in range(num_of_features):
        mean_vector.append(sum(vectors[i]) / num_of_observations)

    # Calculate the covariance matrix
    cov_v = []
    for i in range(num_of_features):
        s_sum = 0
        for j in range(num_of_observations):
            s_sum += (vectors[i][j] - mean_vector[i]) ** 2
        cov_v.append((1 / (num_of_observations - 1) * s_sum))

    print(cov_v)

    for i in range(num_of_features):
        covariance_matrix[i][i] = cov_v[i]

    for i in range(num_of_features):
        for j in range(i + 1, num_of_features):
            prod_sum = sum(
                (vectors[i][k] - mean_vector[i]) * (vectors[j][k] - mean_vector[j]) for k in range(num_of_observations))
            covariance_matrix[i][j] = (1 / (num_of_observations - 1) * prod_sum)
            covariance_matrix[j][i] = covariance_matrix[i][j]

    return covariance_matrix
```

## Standard Solution

```python
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    covariance_matrix = [[0 for _ in range(n_features)] for _ in range(n_features)]

    means = [sum(feature) / n_observations for feature in vectors]

    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_observations)) / (n_observations - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance

    return covariance_matrix
```

## Note

- The initalisation of the list could be tricky. Avoid using `[[0]*num_of_features]*num_of_features` as it creates a list of references to the same list.