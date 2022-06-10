from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.numOfWays = 0
        cache = defaultdict(int)
        cache[0] = 1
        
        def dfs(node, currSum):
            if not node:
                return
            
            currSum += node.val
            complement = currSum - targetSum
            self.numOfWays += cache[complement]
            
            cache[currSum] += 1
            dfs(node.left, currSum)
            dfs(node.right, currSum)
            cache[currSum] -= 1
        
        dfs(root, 0)
            
        return self.numOfWays
