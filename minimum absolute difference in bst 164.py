class Solution:
    def getMinimumDifference(self, root):
        self.ans = 10**5
        self.l = []
        def helper(root):
            if root:
                left = helper(root.left)
                self.l.append(root.val)
                right = helper(root.right)
        helper(root)
        for i in range(1,len(self.l)):
            self.ans = min(self.ans,self.l[i]-self.l[i-1])
        return self.ans
