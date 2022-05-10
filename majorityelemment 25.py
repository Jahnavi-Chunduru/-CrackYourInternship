#find the mode of given list
list1=list(map(int,input().split()))
clist=[] #list to store the number of times each element repeated in given list
for i in list1:
    c=list1.count(i)
    clist.append(c)
#converting 2 lists into a dictionary for key value pairs
dict1=dict(zip(list1,clist))
cmax=max(zip(dict1.values(),dict1.keys()))[1]# key that has max value
print(cmax)
