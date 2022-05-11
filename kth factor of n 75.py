n=int(input("enter the number:"))
k=int(input("enter the index of output:"))
factorslist=[]
for i in range(1,n+1):
    if(n%i==0):
        factorslist.append(i)
print(factorslist[k-1])
