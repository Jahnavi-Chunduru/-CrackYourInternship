class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        remain = 0
        start = 0
        n = len(gas)
        
        while True:
            i=0
            while i < n:
                remain += gas[(start+i)%n]-cost[(start+i)%n]
                if remain<0:
                    
                    start = (start+i+1)
                    remain = 0
                    break
                i+=1
            if i==n:
                return start
			
            if start >= n:
                return -1
