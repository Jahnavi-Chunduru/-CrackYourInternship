class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        deq = collections.deque()
        j = 0
        result = -inf
        for [x,y] in points:
            while deq and x - points[j][0] > k:
                deq[0][1] -= 1
			    
                if not deq[0][1]:
                    deq.popleft()
                j += 1
                
            if deq:
                result = max(result, x + y + deq[0][0])
                
			
            delta = y - x
            num_elements = 1
            while deq and deq[-1][0] < delta:
                num_elements += deq.pop()[1]
            deq.append([delta, num_elements])
        return result
