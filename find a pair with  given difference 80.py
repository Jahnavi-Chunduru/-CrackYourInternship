def maxsubtpair(arr,n):
    arr.sort()
    i,j=0,1
    while (i<len(arr)) and (j<len(arr)):
        if(i!=j) and arr[j]-arr[i]==n:
            print("found the pair (",arr[i],",",arr[j],")")
            return True
        elif arr[j]-arr[i]<n:
            j+=1
        else:
            i+=1
    print("not found")
    return False
print("enter the list elements:")
arr=list(map(int,input().split()))
n=int(input("the difference value is:"))
maxsubtpair(arr,n)
