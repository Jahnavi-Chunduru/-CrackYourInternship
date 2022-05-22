from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
def sublist(A,B):
    n=len(A)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))
print("enter the array elements:")
nums=list(map(int,input().split()))
l=len(nums)
clist=[]
for i in range(1,l+1):
       c=combine(nums,i)
       clist.extend(c)
clist=[list(i) for i in clist]
nums.sort()
for i in clist:
    i.reverse()
    if(sublist(i,nums)):
        print("Yes")
        break
    else:
        print("No")
        break
