class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        
        while len(arr) >= 2:
            minV, idx = sys.maxsize, -1
            for i in range(1,len(arr)):
                if arr[i] * arr[i-1] < minV:
                    minV = arr[i] * arr[i-1]
                    idx = i
            res += minV
            arr = arr[:idx-1] + [max(arr[idx-1], arr[idx])] + arr[idx+1:]
                 
        return res
