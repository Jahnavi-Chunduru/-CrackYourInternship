from typing import List
MAX = 5
def isSafe(row: int, col: int, 
           m: List[List[int]], n: int,
           visited: List[List[bool]]) -> bool:

    if (row == -1 or row == n or 
        col == -1 or col == n or 
        visited[row][col] or m[row][col] == 0):
        return False

    return True

def printPathUtil(row: int, col: int, 
                  m: List[List[int]], 
                  n: int, path: str,
                  possiblePaths: List[str], 
                  visited: List[List[bool]]) -> None:
    if (row == -1 or row == n or 
        col == -1 or col == n or
        visited[row][col] or m[row][col] == 0):
        return
    if (row == n - 1 and col == n - 1):
        possiblePaths.append(path)
        return
    visited[row][col] = True
    if (isSafe(row + 1, col, m, n, visited)):
        path += 'D'
        printPathUtil(row + 1, col, m, n, 
                      path, possiblePaths, visited)
        path = path[:-1]
    if (isSafe(row, col - 1, m, n, visited)):
        path += 'L'
        printPathUtil(row, col - 1, m, n, 
                      path, possiblePaths, visited)
        path = path[:-1]
    if (isSafe(row, col + 1, m, n, visited)):
        path += 'R'
        printPathUtil(row, col + 1, m, n,
                      path, possiblePaths, visited)
        path = path[:-1]
    if (isSafe(row - 1, col, m, n, visited)):
        path += 'U'
        printPathUtil(row - 1, col, m, n,
                      path, possiblePaths, visited)
        path = path[:-1]
    visited[row][col] = False
def printPath(m: List[List[int]], n: int) -> None:
    possiblePaths = []
    path = ""
    visited = [[False for _ in range(MAX)]
                      for _ in range(n)]
    printPathUtil(0, 0, m, n, path, 
                  possiblePaths, visited)
    for i in range(len(possiblePaths)):
        print(possiblePaths[i], end = " ")
