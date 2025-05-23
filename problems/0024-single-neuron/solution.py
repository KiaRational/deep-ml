import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
    z = np.array(features) @ np.array(weights) + bias
    probabilities = 1 / (1 + np.exp(-1*z))
    mse = np.sum(((probabilities - np.array(labels))**2))/(len(labels))

	return probabilities.tolist(), mse.tolist()