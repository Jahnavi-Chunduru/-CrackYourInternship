import copy
n=int(input("enter the size of array:"))
inlist=list(map(int,input().split()))
inlistmod=copy.copy(inlist)
for i in inlist:
    if(inlist.count(i)>1):
        inlist.remove(i)
a=len(inlist)
for j in range(0,len(inlistmod)-len(inlist)):
    inlist.append("_")
print(a,",","inlist=","[{0}]".format(', '.join(map(str,inlist))))
