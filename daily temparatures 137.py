temps=list(map(int,input().split()))
count=0
counts=[]
for i in range(0,len(temps)):
    count=0
    for j in range(i+1,len(temps)):
          if(temps[i]<temps[j]):
               count=count+1
               break
          else:
              if(temps[i]>temps[j]):
                      count+=1
                      if(temps[i]<temps[j]):
                          break
                      j+=1
          if(temps[i]==temps[len(temps)-2]):
              if(temps[i]>temps[-1]):
                  count=0
    counts.append(count)
print(counts)
