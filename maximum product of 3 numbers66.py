nums=list(map(int,input().split()))
nums.sort()
n=len(nums)
print(max(nums[0]*nums[1]*nums[n-1],nums[n-1]*nums[n-2]*nums[n-3]))
