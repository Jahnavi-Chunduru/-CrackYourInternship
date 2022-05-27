class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        n = len(nums)
        if n==1:
            return TreeNode(nums[0])
        low = 0
        high = n - 1
        def insertIntoBST(low: int, high: int) -> TreeNode:
            if low == high:
                return TreeNode(nums[low])
            
            mid = low + (high-low)//2
            root = TreeNode(nums[mid])
            if mid == low:
                root.right = insertIntoBST(mid+1,high)
                return root
            root.left = insertIntoBST(low,mid-1)
            root.right = insertIntoBST(mid+1,high)
            return root
        
        return insertIntoBST(low, high)
