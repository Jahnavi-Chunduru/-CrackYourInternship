class Solution(object):
    def minInsertions(self, s):

        n = len(s)
        dp = [[0 for c in range(n)] for r in range(n)]
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):
                dp[start][end] = 1 + min(dp[start][end-1], dp[start+1][end]) if s[start] != s[end] else dp[start+1][end-1]
        return dp[0][n-1]
