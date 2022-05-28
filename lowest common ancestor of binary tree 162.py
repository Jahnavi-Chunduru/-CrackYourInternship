class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        if root is p or root is q: 
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: 
            return root

        return left or right
