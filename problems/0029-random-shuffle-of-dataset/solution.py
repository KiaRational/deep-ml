import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
    np.random.seed(seed)
    p = np.random.permutation(len(X))  # Generate a shuffledx array

    X , y = X[p] , y[p]

	return X,y