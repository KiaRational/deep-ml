
import numpy as np

def gaussian_elimination(A):
    A = A.astype(float)  # ensure floating point division
    m, n = A.shape
    for i in range(min(m, n)):
        # Find pivot (maximum in column i from row i down)
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if A[max_row, i] == 0:
            continue  # skip column if pivot is zero
        # Swap current row with pivot row
        A[[i, max_row]] = A[[max_row, i]]
        # Eliminate entries below the pivot
        for j in range(i + 1, m):
            factor = A[j, i] / A[i, i]
            A[j] = A[j] - factor * A[i]
    return A

def matrix_image(A):
	# Write your code here
    matrixx = A
	matrixx=matrixx.transpose()
    matrix = matrixx.copy()
    matrix = gaussian_elimination(matrix)
    return(matrixx[np.nonzero(np.average((np.where(matrix ==0,0,1)),axis=1))].transpose())


