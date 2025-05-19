import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
  m, n = X.shape
  theta = np.zeros((n, 1))
  y = np.transpose(np.array([y]))
  for i in range(iterations):
      h = ((X @ theta))
      grad = (X.T @ (h-y))/m
      theta -= alpha*grad
      
  return theta