def minsum(arr,n):
    arr.sort()
    num1,num2=0,0
    for i in range(0,len(arr)):
        if(i%2==0):
            num1=num1*10+arr[i]
        else:
            num2=num2*10+arr[i]

    return num1+num2
nums=list(map(int,input().split()))
n=len(nums)
print(minsum(nums,n))
          
