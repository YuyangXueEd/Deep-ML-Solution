def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    if len(a[0]) != len(b):
        return -1
    result = []
    for k, v in enumerate(a):
        tmp = 0
        for i in range(len(b)):
            tmp += v[i] * b[i]
        result.append(tmp)

    return result


if __name__ == '__main__':
    a = [[1, 2], [2, 4]]
    b = [1, 2]
    print(matrix_dot_vector(a, b))
