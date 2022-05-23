print("enter the elements of list:")
nums=list(map(int,input().split()))
k=int(input("enter the window size:"))
maxlist=[]
l=[]
for i in range(0,len(nums)):
    l=[]
    l=nums[i:i+k]
    if(len(l)==k):
        print(l)
        m=max(l)
        maxlist.append(m)
print(maxlist)
