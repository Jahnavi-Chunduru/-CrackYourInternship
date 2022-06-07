def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parents = {root: root}

def dfs(node):
            if node.left:
                self.parents[node.left] = node
                dfs(node.left)
            if node.right:
                self.parents[node.right] = node
                dfs(node.right)
        
        dfs(root)
        
		q = deque([target])
        dist = {target: 0}
        res = []
        while q:
            node = q.popleft()
            if dist[node] == k:
                res.append(node.val)
            for neighbor in (node.left, node.right, self.parents[node]):
                if neighbor and neighbor not in dist.keys():
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
                
        return res
