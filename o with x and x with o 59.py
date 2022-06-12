M = 6
N = 6
def floodFillUtil(mat, x, y, prevV, newV):
	if (x < 0 or x >= M or y < 0 or y >= N):
		return

	if (mat[x][y] != prevV):
		return
	mat[x][y] = newV
	floodFillUtil(mat, x + 1, y, prevV, newV)
	floodFillUtil(mat, x - 1, y, prevV, newV)
	floodFillUtil(mat, x, y + 1, prevV, newV)
	floodFillUtil(mat, x, y - 1, prevV, newV)
def replaceSurrounded(mat):
	for i in range(M):
		for j in range(N):
			if (mat[i][j] == 'O'):
				mat[i][j] = '-'
	for i in range(M):
		if (mat[i][0] == '-'):
			floodFillUtil(mat, i, 0, '-', 'O')
	for i in range(M):
		if (mat[i][N - 1] == '-'):
			floodFillUtil(mat, i, N - 1, '-', 'O')
	for i in range(N):
		if (mat[0][i] == '-'):
			floodFillUtil(mat, 0, i, '-', 'O')
	for i in range(N):
		if (mat[M - 1][i] == '-'):
			floodFillUtil(mat, M - 1, i, '-', 'O')
	for i in range(M):
		for j in range(N):
			if (mat[i][j] == '-'):
				mat[i][j] = 'X'
