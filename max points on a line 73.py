 def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        
        def find_slope(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            
            if dx == 0:
                return 'inf'
            
            return dy/dx
        
        for i in range(len(points)):
            slopes = collections.defaultdict(int)
            p1 = points[i]
            
            for j in range(i+1, len(points)):
                p2 = points[j]
                
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                
                ans = max(ans, slopes[slope] + 1)
                
        return ans
