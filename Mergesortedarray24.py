nums1=list(map(int,input().split()))
m=int(input("no. of elements"))
nums2=list(map(int,input().split()))
n=int(input("no. of elements"))
nums1=[i for i in nums1 if i!=0]
nums1.extend(nums2)
nums1.sort()
print(nums1)
