from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
nums=list(map(int,input().split()))
oplist=[]
for i in range(0,len(nums)+1):
    c=combine(nums,i)
    oplist.extend(c)
oplist=[list(a) for a in oplist]
op=set(tuple(sorted(x)) for x in oplist)
finall=list(op)
finall=[list(a) for a in finall]
print(finall)
