import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    m = (matrix[0][0]+matrix[1][1])/2
    p = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    eigenvalues = [m+math.sqrt(m*m-p),m-math.sqrt(m*m-p)]
	return eigenvalues