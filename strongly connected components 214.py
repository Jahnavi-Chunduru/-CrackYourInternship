from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited[v]= True
        print v,
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    def fillOrder(self,v,visited, stack):
        visited[v]= True
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
    def printSCCs(self):
        
         stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
         gr = self.getTranspose()
         visited =[False]*(self.V)
         while stack:
             i = stack.pop()
             if visited[i]==False:
                gr.DFSUtil(i, visited)
                print""
 
