class Solution:
    def coinChange(self, a: List[int], t: int) -> int:
        d=deque([(t,0)])
        v=set()
        while d:
            x,y=d.popleft()
            if x==0:
                return y
            for i in a:
                o=x-i
                if o>=0 and o not in v:
                    v.add(o)
                    d.append((x-i,y+1))
        return -1
