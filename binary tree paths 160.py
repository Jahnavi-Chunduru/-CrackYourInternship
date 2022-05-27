class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.dfs(root, [], res)
        
        return res
        
        
    def dfs(self, root, path_list, res):
        if not root:
            return
        
        path_list.append(str(root.val))
        
        if not root.left and not root.right:
            res.append("->".join(path_list))
        if root.left:
            self.dfs(root.left, path_list, res)
        if root.right:
            self.dfs(root.right, path_list, res)
        
        path_list.pop()
