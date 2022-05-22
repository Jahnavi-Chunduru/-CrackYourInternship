from math import sqrt
print("enter point1")
p1=list(map(int,input().split()))
print("enter point2")
p2=list(map(int,input().split()))
print("enter point3")
p3=list(map(int,input().split()))
print("enter point4")
p4=list(map(int,input().split()))
l1=int(sqrt(((p3[1]-p1[1])**2)+((p3[0]-p1[0])**2)))
l2=int(sqrt(((p4[1]-p2[1])**2)+((p4[0]-p2[0])**2)))
b1=int(sqrt(((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2)))
b2=int(sqrt(((p4[1]-p3[1])**2)+((p4[0]-p3[0])**2)))
if(l1==l2 and b1==b2):
    if(l1==b1):
        print("true")
    else:
        print("false")
else:
    print("false")
