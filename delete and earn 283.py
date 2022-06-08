from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        curr = prev1 = prev2 = 0
        for i in range(max(count)+1):
            curr = max(prev1, i * count[i] + prev2)
            prev1, prev2 = curr, prev1
            
        return curr
