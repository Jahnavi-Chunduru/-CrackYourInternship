print("enter the list elements of array:")
arr=list(map(int,input().split()))
n=int(input("enter the difference value:"))
samearr=arr
for i in range(len(arr)):
    for j in range(len(samearr)):
        if(samearr[j]-arr[i]==n):
            print("(",arr[i],",",samearr[j],")")
    
