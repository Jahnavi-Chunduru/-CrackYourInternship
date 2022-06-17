class Solution:
    def knightDialer(self, n: int) -> int:
        Mod = 10**9 + 7
        pad = [
            (4, 6), (8, 6), (7, 9), (4, 8), (3, 9, 0),
            (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]
        def dfs(i, n):
            if n == 0: return 1
            return sum(dfs(nxt, n - 1) for nxt in pad[i]) % Mod
        return sum(dfs(i, n - 1)  for i in range(10)) % Mod
