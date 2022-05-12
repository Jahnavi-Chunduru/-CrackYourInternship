def permute(a,b,n,k):
    n=len(a)
    for i in range(0,n):
        if(a[i]+b[i]>k):
             return True
    return False
print("enter the elements of first array:")
a=list(map(int,input().split()))
print("enter the elements of second array with same length as 1st:")
b=list(map(int,input().split()))
k=int(input("enter the sum value:"))
n=len(a)
if(permute(a,b,n,k)):
    print("Yes")
else:
    print("No")
