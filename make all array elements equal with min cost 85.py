print("enter the array elements:")
arr=list(map(int,input().split()))
l=len(arr)
if(l%2==0):
    sub=(arr[(l-1)//2]+arr[((l-1)//2)+1])//2
else:
    sub=arr[(l)//2]
total=0
for i in range(0,l):
    minus=(arr[i]-sub)
    if(minus<0):
        a=0-minus
        total+=a
    else:
         total+=minus
print(total)
