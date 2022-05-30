 def constructTree(self, n, tree):
        dict = {}
        for edge in tree:
            if edge[0] not in dict:
                dict[edge[0]] = TreeNode(edge[0])
            if edge[1] not in dict:
                dict[edge[1]] = TreeNode(edge[1])
            node0, node1 = dict[edge[0]], dict[edge[1]]
            node0.c.append(node1)
            node1.c.append(node0)
        return dict

    def sumOfDistancesInTree(self, N, edges):
        if N == 1: return [0]
        tree_dict = self.constructTree(N, edges)
        res = [0] * N
        for i in range(N):
            res[i] = self.sum_tree(tree_dict[i], None)[0] 
        return res

    def sum_tree(self, node, parent):
        s, n = 0, 0
        for child in node.c:
            if child == parent:
                continue
            if child not in node.dict:
                node.dict[child] = self.sum_tree(child, node)
            s += node.dict[child][0]
            n += node.dict[child][1]
        num_children = (len(node.c)-1 if parent else len(node.c))
        return s+n+num_children, n+num_children
