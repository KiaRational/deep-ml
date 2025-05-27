import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    
    ATA = A.T @ A
    eigs_ATA, vecs_ATA = np.linalg.eig(ATA)
    singular_vals = np.sqrt(eigs_ATA)
    v1 = vecs_ATA[:, 0] / np.linalg.norm(vecs_ATA[:, 0])
    v2 = vecs_ATA[:, 1] / np.linalg.norm(vecs_ATA[:, 1])

    v = np.stack((v1,v2))

    u1 = A @ v1 / singular_vals[0]
    u2 = A @ v2 / singular_vals[1]
    u = np.stack((u1,u2))

    return u , singular_vals , v
