class Node(object):
    def __init__(self, data, x= 0):
        self.value = data
        self.left = None
        self.right = None
        self.x_coord = x
    
    def insert(self, data):
        if (data <= self.value):
            if (self.left == None):
                self.left = Node(data, x= (self.x_coord - 1))
            else:
                self.left.insert(data)
        elif (data > self.value):
            if (self.right == None):
                self.right = Node(data, x= (self.x_coord + 1))
            else:
                self.right.insert(data)

class VerticalTraverse(object):
    def __init__(self):
        self.data = dict()
    
    def traverse(self, root):
        self._traverse(root)

        keys = sorted(self.data.keys())
        for key in keys:
            print("{}: {}".format(key, self.data[key]))
    
    def _traverse(self, node):
        x = node.x_coord
        if x in self.data.keys():
            self.data[x].append(node.value)
        else:
            self.data[x] = [node.value]
        
        if node.left is not None:
            self._traverse(node.left)
        if node.right is not None:
            self._traverse(node.right)

def main():
    root = Node(10)
    arr = [7, 4, 6, 16, 14, 8, 18, 19, 17, 15]
    for ele in arr:
        root.insert(ele)

    obj = VerticalTraverse()
    obj.traverse(root)

main()
