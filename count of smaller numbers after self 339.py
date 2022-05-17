nums=list(map(int,input().split()))
oplist=[]
for i in range(0,len(nums)):
    count=0
    for j in range(i+1,len(nums)):
        if(nums[i]>nums[j]):
            count+=1
        if(i==-1):
            count=0
    oplist.append(count)
print(oplist)
