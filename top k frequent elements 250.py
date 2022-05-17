def get_key(val):
    for k,v in final.items():
         if(val==v):
             return k
print("enter the array elements:")
nums=list(map(int,input().split()))
k=int(input("number of top elements:"))
counts=[]
oplist=[]
nums.sort()
for i in nums:
    count=nums.count(i)
    counts.append(count)
final=dict(zip(nums,counts))
for i in range(k):
    m=max(final.values())
    oplist.append(get_key(m))
    del final[get_key(m)]
print(oplist)
