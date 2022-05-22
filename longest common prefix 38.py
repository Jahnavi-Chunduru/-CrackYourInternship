def longprefix(arr):
    l=len(arr)
    if(l==0):
        return ""
    if(l==1):
        return arr[0]
    arr.sort()
    end=min(len(arr[0]),len(arr[l-1]))
    i=0
    while(i<end and arr[0][i]==arr[l-1][i]):
        i+=1
    pre=arr[0][0:i]
    return pre
print("enter  the array elements:")
arr=list(map(str,input().split()))
print(longprefix(arr))
