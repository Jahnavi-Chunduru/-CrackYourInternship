class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def printlist(self):
        ptr=self.head
        while(ptr!=None):
            print(ptr.data,end=" ")
            if ptr.next!=None:
                print('->',end=' ')
            ptr=ptr.next
        print()
    def pdt(first,second):
        num1=0
        num2=0
        firstptr=first.head
        secondptr=second.head
         while firstptr != None or secondptr != None:
        if firstptr != None:
            num1 = (num1 * 10) + firstptr.data
            firstptr = firstptr.next
     
        if secondptr != None:
            num2 = (num2 * 10) + secondptr.data
            secondptr = secondptr.next
    
    return num1 * num2
   
