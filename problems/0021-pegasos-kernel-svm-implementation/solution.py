import numpy as np

def linear_kernel(x, y):
    return np.dot(x, y)

def rbf_kernel(x, y, sigma):
    return np.exp(-np.linalg.norm(x - y) ** 2 / (2 * sigma ** 2))

def pegasos_kernel_svm(X, y, kernel='linear', lambda_val=0.01, iterations=100, sigma=1.0):
    n_samples = X.shape[0]
    alpha = np.zeros(n_samples)
    b = 0.0

    # Precompute kernel matrix
    K = np.zeros((n_samples, n_samples))
    for i in range(n_samples):
        for j in range(n_samples):
            if kernel == 'linear':
                K[i, j] = linear_kernel(X[i], X[j])
            elif kernel == 'rbf':
                K[i, j] = rbf_kernel(X[i], X[j], sigma)
            else:
                raise ValueError("Unsupported kernel. Choose 'linear' or 'rbf'.")

    for t in range(1, iterations + 1):
        eta_t = 1.0 / (lambda_val * t)
        for i in range(n_samples):
            f_xi = np.sum(alpha * y * K[:, i]) + b
            if y[i] * f_xi < 1:
                alpha[i] += eta_t * (y[i] - lambda_val * al