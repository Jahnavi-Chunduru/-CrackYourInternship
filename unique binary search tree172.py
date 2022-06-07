class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(l, r):
            if l > r: return [None]
            res = []
            for i in range(l, r + 1):
                lefts, rights = helper(l, i - 1), helper(i + 1, r)
                for leftTree in lefts:
                    for rightTree in rights:
                        res.append(TreeNode(i, leftTree, rightTree))
            return res
        return helper(1, n)
