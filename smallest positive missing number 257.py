print("enter the elements of array")
nums=list(map(int,input().split()))
nums.sort()
missed=[]
for i in range(1,nums[-1]):
    if i not in nums:
        missed.append(i)
    else:
        missed.append(nums[-1]+1)
print(min(missed))
