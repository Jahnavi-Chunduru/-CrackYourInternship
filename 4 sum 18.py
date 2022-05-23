from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
print("enter the elements of an array:")
nums=list(map(int,input().split()))
target=int(input("sum val please:"))
clist=[]
c=combine(nums,4)
c=[list(i) for i in c]
for i in c:
    if(sum(i)==target):
        clist.append(i)
op=set(tuple(sorted(x))for x in clist)
op=[list(i) for i in op]
print(op)
