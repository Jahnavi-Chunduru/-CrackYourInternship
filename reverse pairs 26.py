print("enter the elements of array")
nums=list(map(int,input().split()))
count=0
for i in range(0,len(nums)):
    for j in range(0,len(nums)):
        if(i<j):
            if(nums[i]>2*nums[j]):
                count+=1
print(count)
