from itertools import combinations
from itertools import product
def getkey(val):
    for key,value in combodict.items():
        if val==value:
            return key
    return "doesn't exist"
def combine(arr,k):
    return list(combinations(arr,k))
n=int(input("enter the target:"))
print("enter the elements of array:")
nums=list(map(int,input().split()))
combolist=[]
sums=[]
for i in range(1,n+1):
    clist=combine(nums,i)
    combolist.extend(clist)
for j in combolist:
    s=sum(j)
    sums.append(s)
combodict=dict(zip(combolist,sums))
sollist=[k for k,v in combodict.items() if v==n]
sollist2=[list(m) for m in sollist]
print(sollist2)
