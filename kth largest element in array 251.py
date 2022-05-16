nums=list(map(int,input().split()))
k=int(input("enter the kth max term"))
nums.sort()
for i in nums:
    if(nums.count(i)>1):
        nums.pop(nums.index(i))
print(nums[0-k])
