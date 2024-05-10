import numpy as np


def multivariate_normal_logpdf(X, mean, covariance):
    D = mean.shape[0]
    det_cov = np.linalg.det(covariance)
    inv_cov = np.linalg.inv(covariance)

    constant_term = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_cov)
    exponent_term = -0.5 * np.sum((X - mean) @ inv_cov * (X - mean), axis=1)

    log_density = constant_term + exponent_term
    return log_density


# Пример использования функции
X = np.random.normal(size=(100, 2))  # Пример данных
mean = np.array([0, 0])  # Пример мат. ожидания
covariance = np.array([[1, 0.5], [0.5, 2]])  # Пример матрицы ковариаций

log_density_custom = multivariate_normal_logpdf(X, mean, covariance)
print("Log density (custom):", log_density_custom)