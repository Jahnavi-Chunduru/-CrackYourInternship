def postorder(root):
    if root==None:
        return
    postorder(root.left)
    print(root.data,end=" ")
    postorder(root.right)

def preordertoposorder(a,n):
    root=Node(a[0])
    top=Node(0)
    temp=Node(0)
    temp=None
    stack=[]
    stack.append(root)
    for i in range(1,len(a)):
        while len(stack)!=0 and a[i]>stack[-1].data:
            temp=stack.pop()
        if temp!=None:
            temp.right=Node(a[i])
            stack.append(temp.right)
        else:
            stack[-1].left=Node(a[i])
            stack.append(stack[-1].left)
    return root
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None  
