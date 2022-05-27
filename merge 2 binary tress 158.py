class Solution:
	def mergeTrees(self, root1, root2):
		if root1 and root2:
			new_root = TreeNode(root2.val + root1.val)
			new_root.left = self.mergeTrees(root2.left, root1.left)
			new_root.right = self.mergeTrees(root2.right, root1.right)
			return new_root
		else:
			return root2 or root1
