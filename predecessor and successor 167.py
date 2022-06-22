class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
def findPreSuc(root, key):
	if root is None:
		return
	if root.key == key:
		if root.left is not None:
			tmp = root.left
			while(tmp.right):
				tmp = tmp.right
			findPreSuc.pre = tmp
		if root.right is not None:
			tmp = root.right
			while(temp.left):
				tmp = tmp.left
			findPreSuc.suc = tmp

		return
	if root.key > key :
		findPreSuc.suc = root
		findPreSuc(root.left, key)

	else: 
		findPreSuc.pre = root
		findPreSuc(root.right, key)
def insert(node , key):
	if node is None:
		return Node(key)

	if key < node.key:
		node.left = insert(node.left, key)

	else:
		node.right = insert(node.right, key)

	return node
