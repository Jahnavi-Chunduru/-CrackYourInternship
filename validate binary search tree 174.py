class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, min, max):
            if root is None:
                return True
            if root.val <= min or root.val >= max: 
                return False
            else:
                return isValid(root.left, min, root.val) and isValid(root.right, root.val, max)
        
        return isValid(root, -float("inf"), float("inf"))
