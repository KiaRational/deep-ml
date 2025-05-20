import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True, random_seed=None):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """
    if random_seed != None:
        np.random.seed(random_seed)
    if shuffle:
        randomize = np.arange(len(X))
        np.random.shuffle(randomize)
        X = X[randomize]
        y = y[randomize]
    chunks_X = np.split(X,k)
    chunks_y = np.split(y,k)

    totall = []
    for split in range(k):
        train = []
        test = []
        for fold in range(k):
            if fold == split:
                test += chunks_X[fold].tolist()
            else:
                train += chunks_X[fold].tolist()
        totall.append((train, test))
    
    return(totall)
