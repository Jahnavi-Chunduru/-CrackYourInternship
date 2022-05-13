nums=list(map(int,input().split()))
counts=[]
count=0
for i in range(0,len(nums)):
    count=0
    for j in range(i+1,len(nums)):
        if(nums[i]>nums[j]):
            count+=1
    counts.append(count)
print(counts)
