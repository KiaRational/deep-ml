import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    num_samples = X.shape[0]
    num_batches = int(np.ceil(num_samples / batch_size))
    all_batches = []

    for i in range(num_batches):
        start_index = i * batch_size
        end_index = min((i + 1) * batch_size, num_samples)

        if y is not None:
            all_batches.append([X[start_index:end_index].tolist(),y[start_index:end_index].tolist()])
        else:
            all_batches.append(X[start_index:end_index].tolist())

    return all_batches
