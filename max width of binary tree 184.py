class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        depth_d = dict()
        
        def traverse(root, depth=0, ind=1):
            if root == None: return 
            
            nonlocal depth_d
            if depth in depth_d.keys():
                depth_d[depth]['max'] = max(depth_d[depth]['max'], ind)
                depth_d[depth]['min'] = min(depth_d[depth]['min'], ind)
            else:
                depth_d[depth] = dict()
                depth_d[depth]['max'] = ind
                depth_d[depth]['min'] = ind
            
            traverse(root.left, depth=depth+1, ind=ind*2)
            traverse(root.right, depth=depth+1, ind=ind*2+1)
        
        traverse(root)
        
        ans = 0 
        for k,v in depth_d.items():
            width = v['max'] - v['min'] + 1
            ans = max(width, ans)
        return ans
