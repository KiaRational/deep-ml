import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    n_samples, n_features = X.shape
    # List of all combinations of feature indices with replacement up to the given degree
    combinations = []
    for d in range(degree + 1):
        for comb in combinations_with_replacement(range(n_features), d):
            combinations.append(comb)

    # Transform each input sample
    output = np.empty((n_samples, len(combinations)))
    for i, comb in enumerate(combinations):
        # For each combination, multiply the relevant features
        feature_product = np.ones(n_samples)
        for index in comb:
            feature_product *= X[:, index]
        output[:, i] = feature_product

    return output