class Solution(object):
def maxCoins(self, nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0] * (n+2) for _ in range(n+2)]
    
    for l in range(1, n+1):
        for i in range(1, n+2-l):
            j = i+l-1
            dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[k]*nums[i-1]*nums[j+1] for k in range(i, j+1))
            
    return dp[1][n]
