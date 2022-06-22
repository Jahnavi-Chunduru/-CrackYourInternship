def pathToNode(root, path, k):  
    if root is None: 
        return False
    path.append(root.data) 
    if root.data == k : 
        return True
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right!= None and pathToNode(root.right, path, k))): 
        return True
    path.pop() 
    return False

class Solution:  
    def findDist(self,root, data1, data2): 
        if root: 
            path1 = [] 
            pathToNode(root, path1, data1) 
            path2 = [] 
            pathToNode(root, path2, data2) 
            i=0
            while i<len(path1) and i<len(path2): 
                if path1[i] != path2[i]: 
                    break
                i = i+1 
            return (len(path1)+len(path2)-2*i) 
        else: 
            return 0
