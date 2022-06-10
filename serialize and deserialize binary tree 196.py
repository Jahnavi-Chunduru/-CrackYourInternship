class Codec:
    def serialize(self, root):
        if root==None:
            return str(float('inf'))
        return str(root.val)+" "+self.serialize(root.left)+" "+self.serialize(root.right)
        

    def dfs(self,data):
        global index
        if data[index]==str(float('inf')):
            return None
        temp=TreeNode(int(data[index]))
        index+=1
        temp.left=self.dfs(data)
        index+=1
        temp.right=self.dfs(data)
        return temp
    def deserialize(self, data):
        data=data.split(" ")
        global index
        index=0
        return self.dfs(data)
        
