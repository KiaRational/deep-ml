import numpy as np 
np.set_printoptions(suppress=True)

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    B = A.T @ A
    if B[0, 0] == B[1, 1]:
        theta = np.pi / 4
    else:
        theta = 0.5 * np.arctan2(2 * B[0, 1], B[0, 0] - B[1, 1])
    
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    V = R
    S_raw = np.sqrt(np.abs(R.T @ B @ R))
    
    singular_values = np.diag(S_raw)

    idx = np.argsort(-singular_values)
    singular_values = singular_values[idx]
    
    S_sorted = np.diag(singular_values)
    V_sorted = V[:, idx]

    U = A @ V_sorted @ np.linalg.inv(S_sorted)

    return U, singular_values, V_sorted.T
