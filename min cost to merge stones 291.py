def mergeStones(self, stones: List[int], K: int) -> int:
        mem = {}
        n = len(stones)
        mem = {}
        
        def dp(i,j, piles):
            
            if (i,j,piles) in mem: return mem[(i,j,piles)]
            
            if i==j and piles ==1: return 0
            
            
            elif piles ==1: 
                return dp(i,j,K) +sum(stones[i:j+1])
                
            else:
                
                ans=float("inf")
                
                for mid in range(i,j,K-1):
                    temp_ans = dp(i,mid,1) + dp(mid+1, j, piles-1)
                    
                    ans = min(ans, temp_ans)
                    
                mem[(i,j,piles)]= ans
                return ans 
        if (n-1)%(K-1) !=0 : return -1
        return dp(0, n-1, 1)
