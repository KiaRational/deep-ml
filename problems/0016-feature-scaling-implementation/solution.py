import numpy as np
np.set_printoptions(precision=4)
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
  # Your code here
  mean = np.mean(data, axis=0)
  std = np.std(data, axis=0)
  max = np.max(data, axis=0)
  min = np.min(data, axis=0)
  std += 1e-8
  standardized_data = (data - mean) / std
  normalized_data = (data - min) / (max - min)
  return standardized_data, normalized_data