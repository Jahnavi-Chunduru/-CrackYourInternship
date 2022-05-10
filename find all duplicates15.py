print("Enter the elements of list")
givenlist=list(map(int,input().split()))
outlist=[]
for i in givenlist:
    if(givenlist.count(i)>1):
        givenlist.remove(i)
        outlist.append(i)
outlist.sort()
print(outlist)
