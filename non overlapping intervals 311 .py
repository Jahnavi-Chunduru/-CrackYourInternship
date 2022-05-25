x=int(input("size of list"))
y=2
sublist=[]
intervals=[]
subts=[]
count=0
for i in range(x):
   for j in range(y):
       sublist.append(int(input()))
   intervals.append(sublist)
   sublist=[]
for i in intervals:
    sub=i[1]-i[0]
    subts.append(sub)
subtcount=[subts.count(i) for i in subts]
dict1=dict(zip(subts,subtcount))
minkey=min(dict1,key=dict1.get)
for i in range(len(subts)):
    if(subts[i]==minkey):
        count=count+1
    if(subts.count(subts[i])==len(subts)):
        for i in intervals:
            if(intervals.count(i)>1):
               count=len(subts)-1
            else:
                count=0
print(count)
