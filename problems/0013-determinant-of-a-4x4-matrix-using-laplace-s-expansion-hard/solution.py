def determinant(matrix):
    if len(matrix[0]) == 1:
        return matrix[0][0]
    if len(matrix[0]) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    minor = []
    for j in range(len(matrix)):
        minor = []
        sign = (-1) ** j
        for i in range(1, len(matrix)):
            minor.append(matrix[i][:j] + matrix[i][j+1:])
        det += sign*matrix[0][j]*determinant(minor)
    return det
def determinant_4x4(matrix: list[list[int|float]]) -> float:
	return determinant(matrix)