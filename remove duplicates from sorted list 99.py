print("enter the elements of list")
head=list(map(int,input().split()))
for i in head:
    if(head.count(i)>1):
        head.pop(head.index(i))
print(head)
