k=int(input("enter no. of transactions:"))
print("enter the prices list:")
prices=list(map(int,input().split()))
sub=0
add=0
for i in range(k):
    sub=0
    for j in range(0,len(prices)):
        for p in range(j+1,len(prices)):
            if(j!=-1):
              if(prices[j]<prices[p]):
                  sub=prices[p]-prices[j]
                  add=add+sub
                  prices=prices[p:len(prices)]
                  print(prices)
print(add)
