n=int(input("enter the length of line segment:"))
x=int(input("cut len1:"))
y=int(input("cut len2:"))
z=int(input("cut len3:"))
if(x+y+z==n):
    print(n)
else:
     for i in range(1,n+1):
         if((x+y+z)==n*i):
             print(i)
             break
