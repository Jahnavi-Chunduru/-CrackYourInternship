class Solution:
def __init__(self):
    self.n = pow(10,5)
    self.father = [i for i in range(self.n)]
    
def find(self, u):
    if u == self.father[u]:
        return u
    
    self.father[u] = self.find(self.father[u])
    return self.father[u]

def join(self, u, v):
    u = self.find(u)
    v = self.find(v)
    if u == v:
        return
    self.father[v] = u

def same(self, u, v):
    return self.find(u) == self.find(v)

def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    
    groups = set()
    
    redun = 0
    for u, v in connections:
        if self.same(u, v):
            redun += 1
        self.join(u, v)            
    
    for i in range(n):
        if self.find(i) not in groups:
            groups.add(self.find(i))
    
    if len(groups) == 1:
        return 0
    
    if redun >= len(groups) - 1:
        return len(groups) - 1
    else:
        return -1
