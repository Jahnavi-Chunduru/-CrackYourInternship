n=int(input("Enter a number:"))
s=str(n)
l1=[x for x in s]
if(n<0):
    l1.pop(0)
    l1.reverse()
    l1.insert(0,"-")
    for i in l1:
        print(i,end="")
else:
    l1.reverse()
    for i in l1:
         print(i,end="")
