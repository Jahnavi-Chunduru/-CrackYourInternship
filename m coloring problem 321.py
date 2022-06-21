def graphColoring(graph, k, V):
   colorNodes=[-1]*V
   
   def Check(node,color):
       for x in range(len(graph[node])):
           if graph[node][x] and  colorNodes[x]==color:
               return False
       return True
               
       
   def B(node):
       if node==V:
           return True
       for x in range(0,k):
           if Check(node,x):
               colorNodes[node]=x
               if B(node+1):return True
               colorNodes[node]=-1
       return False
   
   if B(0):return 1
   
   return 0
