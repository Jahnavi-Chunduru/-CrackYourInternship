s=input("enter a string:")
t=input("enter 2nd string:")
l1=list(s)
l2=list(t)
for i in l1:
    c1=l1.count('#')
for j in l2:
    c2=l2.count('#')
if(c1==c2):
    print("true")
else:
    print("false")
