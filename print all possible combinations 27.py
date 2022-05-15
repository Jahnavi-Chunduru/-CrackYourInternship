from itertools import combinations
def combine(arr,s):
    return list(combinations(arr,s))
print("Enter the elements of list:")
nums=list(map(int,input().split()))
k=int(input("Sets in..."))
print(combine(nums,k))
