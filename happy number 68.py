def happy(n):
    add=0
    s=str(n)
    l=[int(x) for x in s]
    if(len(l)==1 and n!=1):
        return "false"
    if(n==1):
        return "true"
    for i in l:
        add=add+(i**2)
    if(add==1):
        return "true"
    else:
        return happy(add)
    
n=int(input("enter a number:"))
print(happy(n))
