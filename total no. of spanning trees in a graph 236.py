def findDeterminant(Matrix):
    det = 0
    if (len(Matrix) == 1):
        return Matrix[0][0]

    elif (len(Matrix) == 2):
        det = (Matrix[0][0] * Matrix[1][1] - Matrix[0][1] * Matrix[1][0])
        return det

    else:

        for p in range(len(Matrix[0])):
            tempMatrix = []
            for i in range(1,len(Matrix)):
                row = []
                for j in range(0,len(Matrix[i])):
                    if (j != p):
                        row.append(Matrix[i][j])

                if (len(row) > 0):
                    tempMatrix.append(row)

            det = det + Matrix[0][p] * pow(-1, p) * findDeterminant(tempMatrix)

        return det
def spanningTrees(adjMatrix, n, m):
    degree = [0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            if (adjMatrix[i][j] == 1):
                degree[i]+=1
    for i in range(n):
        adjMatrix[i][i] = degree[i]
    for i in range(n):
        for j in range(n):
            if ((i != j) and adjMatrix[i][j] == 1):
                adjMatrix[i][j] = -1
    submatrix = [[0 for i in range(n-1)] for j in range(n-1)]
    for i in range(n):
        for j in range(n):
            submatrix[i - 1][j - 1] = adjMatrix[i][j]
    return  findDeterminant(submatrix)
