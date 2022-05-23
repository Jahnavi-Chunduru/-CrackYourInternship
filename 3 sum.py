from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
print("enter the elements of an array:")
nums=list(map(int,input().split()))
clist=[]
c=combine(nums,3)
c=[list(i) for i in c]
for i in c:
    if(sum(i)==0):
        clist.append(i)
op=set(tuple(sorted(x))for x in clist)
op=[list(i) for i in op]
print(op)
