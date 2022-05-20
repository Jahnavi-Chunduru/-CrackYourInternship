def minmove(nums):
    if(nums.count(nums[0]==len(nums))):
        return 0
    nums.sort()
    step=0
    for i in range(nums.index(max(nums)),0,-1):
        step+=(nums[i]-nums[i-1])*(len(nums)-i)
    return step
nums=list(map(int,input().split()))
print(minmove(nums))
