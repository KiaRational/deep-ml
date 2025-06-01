import numpy as np

def get_random_subsets(X, y, n_subsets, replacements, seed=None):
    if seed is not None:
        np.random.seed(seed)

    n_samples = X.shape[0]
    subset_size = n_samples if replacements else n_samples // 2

    subsets = []
    for _ in range(n_subsets):
        indices = np.random.choice(n_samples, size=subset_size, replace=replacements)
        X_subset = X[indices]
        y_subset = y[indices]
        subsets.append((X_subset, y_subset))

    return subsets
