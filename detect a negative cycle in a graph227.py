class Edge:
      
    def __init__(self):
        self.src = 0
        self.dest = 0
        self.weight = 0
class Graph:
      
    def __init__(self):
        self.V = 0
        self.E = 0
        self.edge = None
def createGraph(V, E):
  
    graph = Graph()
    graph.V = V;
    graph.E = E;
    graph.edge =[Edge() for i in range(graph.E)]
    return graph;
def isNegCycleBellmanFord(graph, src):
    V = graph.V;
    E = graph.E;
    dist = [1000000 for i in range(V)];
    dist[src] = 0;
    for i in range(1, V):
        for j in range(E):
          
            u = graph.edge[j].src;
            v = graph.edge[j].dest;
            weight = graph.edge[j].weight;
            if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
                dist[v] = dist[u] + weight;
    for i in range(E):
      
        u = graph.edge[i].src;
        v = graph.edge[i].dest;
        weight = graph.edge[i].weight;
        if (dist[u] != 1000000 and dist[u] + weight < dist[v]):
            return True;
  
    return False;
