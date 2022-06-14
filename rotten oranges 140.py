R = 3
C = 5
def issafe(i, j):

    if (i >= 0 and i < R and 
        j >= 0 and j < C):
        return True
    return False

def rotOranges(v):

    changed = False
    no = 2
    while (True):
        for i in range(R):
            for j in range(C):
                if (v[i][j] == no):
                    if (issafe(i + 1, j) and 
                        v[i + 1][j] == 1):
                        v[i + 1][j] = v[i][j] + 1
                        changed = True

                    if (issafe(i, j + 1) and 
                        v[i][j + 1] == 1):
                        v[i][j + 1] = v[i][j] + 1
                        changed = True

                    if (issafe(i - 1, j) and 
                        v[i - 1][j] == 1):
                        v[i - 1][j] = v[i][j] + 1
                        changed = True

                    if (issafe(i, j - 1) and 
                        v[i][j - 1] == 1):
                        v[i][j - 1] = v[i][j] + 1
                        changed = True
        if (not changed):
           break
        changed = False
        no += 1

    for i in range(R):
        for j in range(C):
            if (v[i][j] == 1):
                return -1
    return no - 2
