class Solution(object):
    def kthSmallest(self, root, k):
        s, cur, rank = [], root, 0

        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right

        return float("-inf")
from itertools import islice
class Solution2(object):
    def kthSmallest(self, root, k):
        def gen_inorder(root):
            if root:
                for n in gen_inorder(root.left):
                    yield n

                yield root.val

                for n in gen_inorder(root.right):
                    yield n

        return next(islice(gen_inorder(root), k-1, k))
