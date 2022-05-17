nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
count=0
counts=[]
a=len(nums1)
b=len(nums2)
for i in range(0,a):
    count=0
    for j in range(0,b):
        for k in range(j+1,b):
            if(nums1[i]==nums2[j]):
                if(nums2[j]<nums2[k]):
                    count+=1
                else:
                    count=-1
            if(nums1[i]==nums2[-1]):
                count=-1
    counts.append(count)
print(counts)
