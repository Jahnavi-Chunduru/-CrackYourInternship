print("enter the elements of list")
nums=list(map(int,input().split()))
pdts=[]
pdt=1
for i in range(0,len(nums)):
    for j in range(0,len(nums)-1):
        if(i!=len(nums)-1):
            pdt=nums[i]*nums[i+1]
    pdts.append(pdt)
print(max(pdts))
