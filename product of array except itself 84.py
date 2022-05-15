nums=list(map(int,input().split()))
pdts=[]
pdt=1
for i in range(0,len(nums)):
    pdt=1
    if(i==0):
       for j in range(i+1,len(nums)):
             pdt=pdt*nums[j]
    elif(i>0):
        for j in range(0,len(nums)):
            if(i==j):
                 continue
            else:
               pdt=pdt*nums[j]
    else:
        pass
    pdts.append(pdt)
print(pdts)
