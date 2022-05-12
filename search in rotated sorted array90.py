print("enter the elements of array")
nums=list(map(int,input().split()))
target=int(input("enter the index of the element to be searched"))
for i in range(len(nums)):
    if(i==target):
        print(nums[i])
        break
    else:
        print(-1)
        break
