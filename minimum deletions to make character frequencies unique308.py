s=input("enter a string:")
slist=list(s)
counts=[]
for i in slist:
    c=slist.count(i)
    counts.append(c)
    slist.remove(i)

for i in counts:
    a=counts.count(i)
    if(a>1):
       print(a)
       break
else:
       print(0)
       
