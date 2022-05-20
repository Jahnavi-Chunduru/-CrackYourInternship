from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
n=int(input("enter the size of array:"))
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
for k in sums:
    if(sums.count(k)==2):
         print("YES")
         break
else:
        print("NO")
        
