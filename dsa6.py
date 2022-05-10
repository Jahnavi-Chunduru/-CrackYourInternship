#reversing the order of words in a sentence
s=input()
l1=s.split()
l2=[]
l2.extend(l1)
l2.reverse()
for i in l2:
    print(i,end=" ")

