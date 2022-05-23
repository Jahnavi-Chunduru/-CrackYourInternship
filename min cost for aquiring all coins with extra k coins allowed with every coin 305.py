print("enter the denominations of coins:")
coins=list(map(int,input().split()))
k=int(input("enter the number of coins available for free:"))
coins.sort()
summ=0
for j in range(k-1):
    summ=summ+coins[j]
print(summ)
