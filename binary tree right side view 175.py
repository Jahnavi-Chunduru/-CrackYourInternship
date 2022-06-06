class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if(root):
            q.appendleft(root)
        while(q):
            sz = len(q) #number of nodes in current level
            while(sz > 0):
                curr = q.pop()
                
                #check if its the last node in the current level, if so, append to res
                if(sz == 1):
                    res.append(curr.val)
        
                #add current nodes children to queue (if they exist)
                if(curr.left):
                    q.appendleft(curr.left)
                if(curr.right):
                    q.appendleft(curr.right)
                sz -= 1
        return res
