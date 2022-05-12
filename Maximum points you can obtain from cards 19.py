print("please enter the points of cards")
cardpoints=list(map(int,input().split()))
k=int(input("number of cards:"))
selections=[]
for i in range(k):
    if(cardpoints[0]==cardpoints[-1]):
        selections.append(cardpoints[-1])
        cardpoints.pop(-1)
    else:
         selections.append(max(cardpoints[0],cardpoints[-1]))
         cardpoints.remove(max(cardpoints[0],cardpoints[-1]))
print(sum(selections))
