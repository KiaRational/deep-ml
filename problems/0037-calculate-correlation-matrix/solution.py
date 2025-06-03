import numpy as np

def calculate_correlation_matrix(X, Y=None):
  # Your code here
  if Y is None:
    normalized_X = X - np.mean(X, axis=0)
    Cov = (1/(X.shape[0]-1)) * normalized_X.T @ normalized_X
    variance = (1/(X.shape[0]-1)) * np.sum(( normalized_X ** 2) , axis = 0) 
    v = np.sqrt(variance)

    corr = Cov / np.outer(v,v)
  else:
    A = X
    B = Y
    A_centered = A - A.mean(axis=0)
    B_centered = B - B.mean(axis=0)

    A_norm = A_centered / A_centered.std(axis=0, ddof=1)
    B_norm = B_centered / B_centered.std(axis=0, ddof=1)

    corr = A_norm.T @ B_norm / (A.shape[0] - 1)
  return corr