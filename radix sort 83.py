def countingsort(arr,exp1):
    n=len(arr)
    op=[0]*(n)
    count=[0]*(10)
    for i in range(0,n):
        index=(arr[i]/exp1)
        count[int((index)%10)]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=(arr[i]/exp1)
        op[count[int((index)%10)]-1]=arr[i]
        count[int((index)%10)]-=1
        i-=1
    i=0
    for i in range(0,len(arr)):
        arr[i]=op[i]
def radix(arr):
    max1=max(arr)
    exp=1
    while max1/exp>0:
        countingsort(arr,exp)
        exp*=10
print("enter the array elements:")
nums=list(map(int,input().split()))
radix(nums)
for i in range(len(nums)):
    print(nums[i],end=" ")
 
