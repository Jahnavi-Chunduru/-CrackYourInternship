nums=list(map(int,input().split()))
newnums=[]
while nums:
   min1=nums[0]
   for i in nums:
      if(i<min1):
           min1=i
   nums.remove(min1)
   newnums.append(min1)
print(newnums)
