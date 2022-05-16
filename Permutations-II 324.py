import itertools
def combine(arr):
    return list(itertools.permutations(arr))
print("enter the elements of list:")
list1=list(map(int,input().split()))
l2=combine(list1)
for i in l2:
    if(l2.count(i)>1):
        l2.pop(l2.index(i))
l3=[list(x) for x in l2]
print(l3)
