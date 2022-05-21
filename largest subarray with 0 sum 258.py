from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
n=int(input("enter the size of array:"))
print("enter the list elements")
nums=list(map(int,input().split()))
clist=[]
zerolist=[]
lenlist=[]
for i in range(1,len(nums)+1):
    c=combine(nums,i)
    clist.extend(c)
clist=[list(i) for i in clist]
for i in clist:
    if(sum(i)==0):
        zerolist.append(i)
for i in zerolist:
    lenlist.append(len(i))
print(max(lenlist))
