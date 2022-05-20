n=int(input("enter a number:"))
ans=[]
for i in range(0,n+1):
    b=bin(i)
    l=list(b)
    c=l.count('1')
    ans.append(c)
print(ans)
