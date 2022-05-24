from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
s=input("enter a word:")
t=input("enter the subsequence of the above:")
count=0
slist=list(s)
c=combine(slist,len(t))
c=[list(i) for i in c]
c=[''.join(i) for i in c]
for i in c:
    if(i==t):
        count=count+1

print(count)
