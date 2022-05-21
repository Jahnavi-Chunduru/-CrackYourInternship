from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
num=input("enter a number:")
k=int(input("enter no. of digits to remove:"))
numlist=[int(i) for i in num]
opsize=len(num)-k
combolist=combine(numlist,opsize)
combolist=[list(i) for i in combolist]
m=min(combolist)
if(len(m)!=0 and m[0]==0):
    m.pop(0)
    print(str('"')+str(''.join([str(elem) for elem in m]))+str('"'))
elif(len(m)!=0):
    print(str('"')+str(''.join([str(elem) for elem in m]))+str('"'))
if(len(num)==k):
    print('"0"')


