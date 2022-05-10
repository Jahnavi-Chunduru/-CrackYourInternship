n=int(input("Enter a number:"))
if(n%2==0):  
    while(n!=1):
       n=n/2
       if(n%2==0):
           n=n/2
       else:
           break
    if(n==1):
        print("true")
    elif(n!=1):
        print("false")
    else:
        print("false")
else:
    print("false")
