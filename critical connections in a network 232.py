def help(self,l,n):
    adj = [[] for _ in range(n)]
    for i in l:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
    return adj
    
def criticalConnections(self, n: int, arr: List[List[int]]) -> List[List[int]]:
    adj = self.help(arr,n)
    
    vis = [0]*(n+1)
    low = [0]*(n+1)
    intime = [0]*(n+1)
    time=[0]
    
    
    ans = []
    
    def dfs(v,par,time):
        vis[v]=1
        intime[v]=low[v]=time[0]
        time[0]+=1
        for i in range(len(adj[v])):
            if adj[v][i]==par:
                continue
            if vis[adj[v][i]]==1:
                low[v]=min(low[v],intime[adj[v][i]])
            else:
                dfs(adj[v][i],v,time)
                if low[adj[v][i]]>intime[v]:
                    ans.append([adj[v][i],v])
                else:
                    low[v]=min(low[v],low[adj[v][i]])
    x = dfs(0,-1,time)
    return ans
