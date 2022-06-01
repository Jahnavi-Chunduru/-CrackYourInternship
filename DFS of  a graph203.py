from collections import defaultdict
class Graph:
    def __init__:
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v,end=' ')
        for neighbour in self.graph[v]:
            if neighbour not i visited:
                self.DFSUtil(neighbour,visited)
    def DFS(self,v):
        visited=set()
        self.DFSUtil(v,visited)
