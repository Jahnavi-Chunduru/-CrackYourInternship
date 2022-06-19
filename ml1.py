input2=input()
r=list(input2)
b=[]
k=[]
while(len(r)!=0):
    b.append(r[0])
    r.remove(r[0])
    if(len(b)>1):
        k.append(b[-1])
        b.remove(b[-1])
    else:
        continue
r.sort()
for i in r:
    print(i,end="")
