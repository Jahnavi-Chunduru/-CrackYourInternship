print("enter the elements of array:")
nums=list(map(int,input().split()))
temp=nums.copy()
count=0
temp.sort()
for i in range(0,len(nums)):
        if(nums[i]==temp[i]):
            continue
        else:
            s=temp[i]
            nums[i],nums[nums.index(s)]=nums[nums.index(s)],nums[i]
            count+=1
            
if(count%2==0):
    print(int(count/2))
else:
    print(int(count/2)+1)

