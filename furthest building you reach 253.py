class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        brick_alloc = []
        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb <= 0:
                continue
            bricks -= climb
            heappush(brick_alloc, -climb)
            if bricks < 0 and ladders == 0:
                return i
            if bricks < 0:
                bricks -= heappop(brick_alloc)
                ladders -= 1
            
        return len(heights)-1
