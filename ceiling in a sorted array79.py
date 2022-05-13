arr=list(map(int,input().split()))
k=int(input("enter a value to find it's ceiling"))
newarr=[i for i in arr if i>k]
print(newarr)
print("the ceiling of",k,"is",min(newarr))
print(arr)
