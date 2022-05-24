colors=input("enter the string of order of colors:")
print("enter the elements of list of times")
needed_time=list(map(int,input().split()))
list1=list(colors)
l=len(list1)
l1=len(needed_time)
l=l1
add=0
for i in range(0,l-1):
    if(list1[i]==list1[i+1]):
        m=(min(needed_time[i],needed_time[i+1]))
        add=add+m
print(add)



        
        
