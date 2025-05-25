import numpy as np

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    # Your code here
    updated_weights = initial_weights
    updated_bias = initial_bias
    n = features.shape[0]
    mse_values = []
    y = labels

    for epoch in range(epochs):

        z = features @ updated_weights + updated_bias

        activation = 1 / ( 1 + np.exp(-z))
        MSE = (1/n)*(np.sum((activation-y)**2))

        dastan = (activation - y)*(activation*(1-activation))
        
        # Gradients
        dastan = (activation - labels) * activation * (1 - activation)
        w_partial_derv = (2/n) * (features.T @ dastan)
        b_partial_derv = (2/n) * np.sum(dastan)

        # Update parameters
        updated_weights -= learning_rate * w_partial_derv
        updated_bias -= learning_rate * b_partial_derv
        mse_values.append(MSE)

    return np.round(updated