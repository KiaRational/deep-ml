import numpy as np
def precision(y_true, y_pred):
  # Your code here

  true_positive = np.sum((y_true == 1) & (y_pred == 1))
  false_positive = np.sum((y_true == 0) & (y_pred == 1))

  precision = true_positive / (true_positive + false_positive)

  return precision