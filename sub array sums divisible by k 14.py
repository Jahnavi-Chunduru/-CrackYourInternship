def subarray(array,k):
    hmap=[0]*k
    curr_sum=0
    for n in nums:
        curr_sum+=n
        hmap[curr_sum%k]+=1
    res=hmap[0]
    for i in range(k):
        res+=hmap[i]*(hmap[i]-1)//2
    return res
nums=list(map(int,input().split()))
k=int(input("sum value--"))
print(subarray(nums,k))
