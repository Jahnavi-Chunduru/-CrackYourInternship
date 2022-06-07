class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getParents(curr, key):
            if not curr:
                return []
            if curr.val == key:
                return [curr]
            else:
                leftHasNode = getParents(curr.left, key)
                rightHasNode = getParents(curr.right, key)
                if leftHasNode:
                    return [curr] + leftHasNode
                elif rightHasNode:
                    return [curr] + rightHasNode
                else:
                    return []
            
        p_rents = getParents(root, p.val)
        q_rents = getParents(root, q.val)

        lcaLevel = min(len(p_rents), len(q_rents))-1
        while lcaLevel >= 0 and p_rents[lcaLevel].val != q_rents[lcaLevel].val:
            lcaLevel -= 1
        
        return p_rents[lcaLevel]
