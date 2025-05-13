def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    column_num = len(matrix[0])
    row_num = len(matrix)
    means = []
    temp = 0
    if mode == 'column':
        for j in range(column_num):
            for i in range(row_num):
                temp += matrix[i][j]
            means.append(temp/row_num)
            temp = 0
    if mode == 'row':
        for i in range(row_num):
            for j in range(column_num):
                temp += matrix[i][j]
            means.append(temp/row_num)
            temp = 0
                  
	return means