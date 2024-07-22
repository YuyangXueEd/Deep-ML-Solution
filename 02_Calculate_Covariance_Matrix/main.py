def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    num_of_features = len(vectors)
    num_of_observations = len(vectors[0])
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

    for i in range(num_of_features):
        covariance_matrix[i][i] = cov_v[i]

    for i in range(num_of_features):
        for j in range(i + 1, num_of_features):
            prod_sum = sum(
                (vectors[i][k] - mean_vector[i]) * (vectors[j][k] - mean_vector[j]) for k in range(num_of_observations))
            covariance_matrix[i][j] = (1 / (num_of_observations - 1) * prod_sum)
            covariance_matrix[j][i] = covariance_matrix[i][j]

    return covariance_matrix


if __name__ == "__main__":
    vectors = [[1, 5, 6], [2, 3, 4], [7, 8, 9]]
    print(calculate_covariance_matrix(vectors))
