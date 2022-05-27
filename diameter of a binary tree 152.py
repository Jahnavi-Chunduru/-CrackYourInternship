class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class Height:
    def __init__(self):
        self.h=0
def diameter(root,height):
        lh=Height()
        rh=Height()
        if root is None:
            height.h=0
            return 0
        ldia=diameter(self.left,lh)
        rdia=diameter(self.right,rh)
        height.h=max(lh.h,rh.h)+1
        return max(lh.h+rh.h,max(ldia,rdia))
def diameter(root):
    height=Height()
    return diameter(root,height)
