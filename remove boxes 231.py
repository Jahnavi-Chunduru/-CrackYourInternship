class Solution:
    def dfs(self, left, right, prev):
        if left > right: 
            return 0
        elif (left, right, prev) in self.memo:
            return self.memo[(left, right, prev)]
        else:
            shift = 0
            while left < right and self.boxes[left] == self.boxes[left + 1]:
                shift += 1
                left += 1
                prev += 1
            result = (prev + 1)*(prev + 1) + self.dfs(left + 1, right, 0)
            for i in range(left+1, right+1,1):
                if self.boxes[i] == self.boxes[left]:
                    result = max(result, self.dfs(left+1,i-1,0) + self.dfs(i,right,prev+1))
            for i in range(0, shift+1,1):
                if (left-i, right, prev-i) not in self.memo:
                    self.memo[(left-i, right, prev-i)] = result
            return result

    def removeBoxes(self, boxes: List[int]) -> int:
        self.memo = {}
        self.boxes = boxes
        return self.dfs(0, len(boxes)-1, 0)
