n=int(input("enter a number:"))
s1=str(n)
l1=[x for x in s1]
l2=[x for x in s1]
l2.reverse()
if(l1==l2):
    print("true")
else:
    print("false")
