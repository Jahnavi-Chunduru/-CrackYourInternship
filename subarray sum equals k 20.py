nums=list(map(int,input().split()))
k=int(input("enter the sum values:"))
subarr=[]
subarrcount=0
for i in range(0,len(nums)):
    subarrcount+=1
    subarr.clear()
    for j in range(1,len(nums)):
        if(nums[i]+nums[j]==k):
            subarr.append(nums[i])
            subarr.append(nums[j])
            break
        elif(nums[i]+0==k):
            subarr.append(nums[i])
            break
    print(subarr)
print(subarrcount-1)        
   
