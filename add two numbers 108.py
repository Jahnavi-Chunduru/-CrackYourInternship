print("enter the elements of list1")
l1=list(map(int,input().split()))
print("enter the elements of 2nd list")
l2=list(map(int,input().split()))
def convert(list1):
    s=[str(i) for i in list1]
    res=int("".join(s))
    return res
l1.reverse()
l2.reverse()
i1=convert(l1)
i2=convert(l2)
ans=i1+i2
s=str(ans)
anslist=[int(i) for i in s]
anslist.reverse()
print(anslist)
