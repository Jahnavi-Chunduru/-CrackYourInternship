nums=list(map(int,input().strip('[]').split(',')))
target=int(input("enter the sum value:"))
ans=[]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
             ans.append(i)
             ans.append(j)
for k in ans:
    c=ans.count(k)
    if(c>1):
        for p in range(1,c):
            ans.remove(k)
ans.sort()
print(ans)
