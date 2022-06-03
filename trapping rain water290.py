def trap(self, height: List[int]) -> int:
        return sum(accumulate(height, max)) + sum(accumulate(reversed(height), max)) - sum(height) - max(height) * len(height)
