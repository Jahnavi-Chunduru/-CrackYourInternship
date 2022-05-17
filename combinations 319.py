from itertools import combinations
def combine(arr,k):
    return list(combinations(arr,k))
n=int(input("enter a number:"))
k=int(input("enter a number to make sets:"))
list1=[]
for i in range(1,n+1):
    list1.append(i)
print(combine(list1,k))
