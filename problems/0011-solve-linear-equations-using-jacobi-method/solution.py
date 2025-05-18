import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
  x = np.zeros_like(b)
  for i in range(n):
    x = (1/np.diagonal(A))*(b-np.matmul((A-np.diag(np.diagonal(A))),x))
  return x
