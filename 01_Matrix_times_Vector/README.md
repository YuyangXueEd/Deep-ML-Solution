# Matrix times Vector

Difficulty: `Easy`

Category: `Linear Algebra`

Reviewed: No

Solved: Yes

# Matrix times Vector

Write a Python function that takes the dot product of a matrix and a vector.

Return `-1` if the matrix could not be dotted with the vector.

## Example

```python
Example:
		input: a = [[1, 2], [2, 4]], b = [1, 2]
		output: [5, 10]
		reasoning: 1 * 1 + 2 * 2 = 5;
		           1 * 2 + 2 * 4 = 10
```

## Learn

Consider a matrix $A$ and a vector $v$, where $A = \begin{pmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}
\end{pmatrix}$, vector $v = \begin{pmatrix}
v_{1}\\
v_{2}
\end{pmatrix}$.

The dot product of $A$ and $v$ results in a new vector: 

$$
A \cdot v = \begin{pmatrix}
a_{11}v_1 + a_{12}v_2\\
a_{21}v_1 + a_{22}v_2
\end{pmatrix}
$$

An $n\times m$ matrix will need to be multiplied by a vector of size $m$ or else this will not work.

## My Solution

```python
def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # first try whether these two multipliable
    if len(a[0]) != len(b):
        return -1
    # get an empty list for the result
    result = []
    for k, v in enumerate(a):
			  # get each horizontal vector from matrix
        tmp = 0
        # multiply and sum
        for i in range(len(b)):
            tmp += v[i] * b[i]
        # append to get the final vector
        result.append(tmp)

    return result

# test code
if __name__ == '__main__':
    a = [[1, 2], [2, 4]]
    b = [1, 2]
    print(matrix_dot_vector(a, b)) # [5, 10]
```

## Standard Solution

```python
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    vals = []
    for i in a:
        hold = 0
        for j in range(len(i)):
            hold+=(i[j] * b[j])
        vals.append(hold)

    return vals
```