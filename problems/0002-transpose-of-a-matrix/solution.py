def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    output = []
    temp = []
    for j in range(len(a[0])):
        for i in range(len(a)):
            temp.append(a[i][j])
        output.append(temp)
        temp = []
    b = output
	return b