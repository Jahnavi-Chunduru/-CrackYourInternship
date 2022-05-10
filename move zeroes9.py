n=int(input("enter the size of array:"))
a=list(map(int,input().split()))
b=[]
for i in a:
    n=a.count(0)
    for i in range(n):
        a.remove(0)
        b.append(0)
a.extend(b)
print(a)
