print("enter the elements of array.....")
nums=list(map(int,input().split()))
nums.sort()
for i in range(0,nums[-1]):
    if(i not in nums):
        print(i)
