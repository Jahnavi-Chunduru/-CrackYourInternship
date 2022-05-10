a=input("enter a binary string:")
b=input("Enter a binary string:")
add=bin(int(a,2)+int(b,2))
l1=[x for x in str(add)]
l2=l1[2:]
def stringg(l2):
    ans=""
    for i in l2:
        ans+=i
    return str('"')+ans+str('"')
print(stringg(l2))
