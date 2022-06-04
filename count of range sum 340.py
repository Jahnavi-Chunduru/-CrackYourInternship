from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        acc,ans = 0,0
        sl = SortedList()
        sl.add(0)
        for num in nums:
            acc += num
            i = sl.bisect_right(acc-lower)
            j = sl.bisect_left(acc-upper)
            ans += abs(i-j)
            sl.add(acc)
        return ans+
