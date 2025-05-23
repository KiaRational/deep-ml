import numpy as np 

def pca(data: np.ndarray, k: int) -> np.ndarray:
    # Your code here
    n = data.shape[0]
    mean = np.mean(data,0)
    data_bar = (data - mean)/np.std(data,0)

    cov = (1/(n-1))*(data_bar.T @ data_bar)
    eigenvalues, eigenvectors = np.linalg.eig(cov)
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]
    principal_components = eigenvectors[:, :k]

    return np.round(principal_components, 4)