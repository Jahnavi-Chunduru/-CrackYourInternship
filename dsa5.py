#find the number of duplicates in a word
s=input("string please...")
l1=[x for x in s]
for i in l1:
    if(l1.count(i)>1):
        print(i,l1.count(i))
        l1=list(filter((i).__ne__,l1))
        
