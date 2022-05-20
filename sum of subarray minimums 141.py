def sublist(l):
    lists=[[]]
    for i in range(len(l)+1):
        for j in range(i):
            lists.append(l[j:i])
    return lists
arr=list(map(int,input().split()))
minslist=[]
listt=sublist(arr)
for i in listt:
    if(len(i)==0):
        continue
    else:
       m=min(i)
       minslist.append(m)
print(sum(minslist))
