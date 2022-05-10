n=int(input("enter the size of array:"))
a=list(map(int,input().split()))
for i in a:
    if(a.count(i)>1):
        a.remove(i)
        print(i)
        break
