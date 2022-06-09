from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
nums=list(map(int,input().split()))
l=[]
for i in range(0,len(nums)+1):
    s=combine(nums,i)
    s=[list(i) for i in s]
    l.extend(s)
print(l)
