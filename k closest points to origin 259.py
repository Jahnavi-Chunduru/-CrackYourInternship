from math import sqrt
x=int(input("enter number of points:"))
y=2
k=int(input("enter no. of closest pts:"))
o=[0,0]
points=[]
coordinates=[]
subtlist=[]
anslist=[]
for i in range(x):
    for j in range(y):
        coordinates.append(int(input()))
    points.append(coordinates)
    coordinates=[]
for i in points:
    sub=sqrt(i[1]**2+i[0]**2)
    subtlist.append(sub)
for i in range(k):
    s=min(subtlist)
    m=points[subtlist.index(s)]
    anslist.append(m)
    subtlist.remove(s)
    points.remove(m)
print(anslist)
