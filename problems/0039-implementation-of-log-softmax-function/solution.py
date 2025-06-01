import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	return (np.array(scores) - np.max(scores) - np.log(np.sum(np.exp(scores-np.max(scores)))))
