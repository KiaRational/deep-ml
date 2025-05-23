import math
import numpy as np
def softmax(scores: list[float]) -> list[float]:
	# Your code here
    e_x = np.exp(scores)
    probabilities = e_x / np.sum(e_x)
	return probabilities