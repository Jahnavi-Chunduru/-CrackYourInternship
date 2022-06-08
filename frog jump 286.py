class Solution:
	def canCross(self, stones: List[int]) -> bool:
		target = stones[-1]
		if stones[1] != 1:
			return False
		stones = set(stones)
		@lru_cache(None)
		def solve(i, last):
			if last == 0:
				return False
			if i == target:
				return True
			val = i + last+1
			if val in stones:
				if solve(val, last+1):
					return True
			val -= 1
			if val in stones:
				if solve(val, last):
					return True
			val -= 1
			if val in stones:
				if solve(val, last-1):
					return True
			return False
		return solve(1, 1)
