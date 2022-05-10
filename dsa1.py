#palindrome string
s=input("Enter a string:")
l1=[x for x in s]
l2=[x for x in s]
l1.reverse()
if(l1==l2):
    print("true")
else:
    print("false")
