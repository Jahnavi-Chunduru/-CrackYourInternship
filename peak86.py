n=int(input("enter the length of array:"))
a=list(map(int,input().split()))
l1=[]
for i in range(0,n):
    l1.append(a)
for i in range(0,len(l1)):
     if(a[i-1]<a[i] and a[i]>a[i+1]):
         print(i)
