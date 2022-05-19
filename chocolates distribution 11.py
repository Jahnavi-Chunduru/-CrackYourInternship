from itertools import combinations
def combine(arr,n):
    return list(combinations(arr,n))
print("enter list elements:")
nums=list(map(int,input().split()))
n=int(input("enter the number of students:"))
anslist=[]
nums.sort()
combolist=combine(nums,n)
for i in combolist:
    ans=max(i)-min(i)
    anslist.append(ans)
print("The minimum difference is",min(anslist))
