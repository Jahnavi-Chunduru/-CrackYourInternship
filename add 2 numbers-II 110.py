print("enter the elements of list1:")
l1=list(map(int,input().split()))
print("enter the elements of list2:")
l2=list(map(int,input().split()))
l1.reverse()
l2.reverse()
s1=[str(i) for i in l1]
res1=int("".join(s1))
s2=[str(i) for i in l2]
res2=int("".join(s2))
summ=res1+res2
ssumm=str(summ)
sumlist=[int(i) for i in ssumm]
sumlist.reverse()
print(sumlist)
