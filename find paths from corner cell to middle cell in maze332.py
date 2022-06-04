def printPath(maze, i, j, ans):
	if (i == len(maze) // 2 and j == len(maze) // 2):
		ans += "(" + str(i) + ", " + str(j) + ") -> MID";
		print(ans);
		return;
	if (maze[i][j] == 0):
		return;
	k = maze[i][j];
	maze[i][j] = 0;
	if (j + k < len(maze)):
		printPath(maze, i, j + k, ans + "(" + str(i) + ", " + str(j) + ") -> ");
	if (i + k < len(maze)):
		printPath(maze, i + k, j, ans + "(" + str(i) + ", " + str(j) + ") -> ");
	if (j - k > 0):
		printPath(maze, i, j - k, ans + "(" + str(i) + ", " + str(j) + ") -> ");
	if (i - k > 0):
		printPath(maze, i - k, j, ans + "(" + str(i) + ", " + str(j) + ") -> ");
	maze[i][j] = k;


