class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def bfs(curr_arr, res):
            temp = []
            
            if len(curr_arr) != 0 and curr_arr[0]:
                res.append([x.val for x in curr_arr])
            
                for item in curr_arr:
                    if item.left: temp.append(item.left)
                    if item.right: temp.append(item.right)
            
                bfs(temp, res)
        
        bfs([root], res)
        return res
