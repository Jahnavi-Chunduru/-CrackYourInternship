print("enter the elements of list1")
list1=list(map(int,input().strip('[]').split(',')))
print("enter the elements of list2")
list2=list(map(int,input().strip('[]').split(',')))
list1.extend(list2)
list1.sort()
print(list1)