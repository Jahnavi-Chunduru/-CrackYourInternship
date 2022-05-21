x=int(input("enter the size of list:"))
y=int(input("enter the size of sublist:"))
sub=[]
comb=[]
for i in range(x):
    for j in range(y):
        sub.append(int(input()))
    comb.append(sub)
    sub=[]
oplist=[]
for i in comb:
    oplist.extend(i)
for j in oplist:
    if(oplist.count(j)>1):
        oplist.pop(oplist.index(j))
oplist.sort()
print(oplist)
