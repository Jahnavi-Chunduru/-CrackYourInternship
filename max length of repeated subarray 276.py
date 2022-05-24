from itertools  import combinations
def combine(arr,k):
    return list(combinations(arr,k))
counts=[]
print("enter the elements of array 1:")
nums1=list(map(int,input().split()))
print("enter the elements of array 2:")
nums2=list(map(int,input().split()))
clist1=[]
clist2=[]
for i in range(0,len(nums1)+1):
    c1=combine(nums1,i)
    clist1.extend(c1)
for j in range(0,len(nums2)+1):
    c2=combine(nums2,j)
    clist2.extend(c2)
clist1=[list(i) for i in clist1]
clist2=[list(i) for i in clist2]
for i in clist1:
    for j in clist2:
        if(i==j):
            counts.append(len(i))
print(max(counts))


