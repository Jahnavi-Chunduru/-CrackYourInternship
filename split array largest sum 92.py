import numpy as np
print("enter the elements of array:")
nums=list(map(int,input().split()))
sums=[]
m=int(input("enter the number of splits in array:"))
nums.sort()
newnums=np.array_split(nums,m)
for i in newnums:
    s=sum(i)
    sums.append(s)
print(max(sums))
