size = 21
matrix = [[0 for col in range(size)] for row in range(size)]
for i in range(size):
	matrix[0][i] = 1
	matrix[i][0] = 1
for i in range(1, size):
	for j in range(1, size):
		matrix[i][j] =  matrix[i-1][j] + matrix[i][j-1]

assert matrix[2][2] == 6
print matrix[20][20]