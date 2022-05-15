nums=list(map(int,input().split()))
l1=[]
for i  in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[j]>nums[i]):
            d=nums[j]-nums[i]
            l1.append(d)
if(len(l1)==0):
    print("0")
else: 
    print(max(l1))
