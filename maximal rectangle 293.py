class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        heights = [0] * (len(matrix[0]) + 1) 
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heights[col] = heights[col] + 1 if matrix[row][col] == '1' else 0 
            
            stack = [-1] 
            for rightIdx in range(len(heights)):
                while heights[rightIdx] < heights[stack[-1]]: 
                    leftHeight = heights[stack.pop()]
                    leftIdx = stack[-1]
                    width = rightIdx - leftIdx - 1
                    result = max(result, leftHeight * width)
                stack.append(rightIdx)
        
        return result
