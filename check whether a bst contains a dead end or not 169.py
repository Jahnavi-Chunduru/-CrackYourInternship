all_nodes = set()
leaf_nodes = set()
class newNode:

	def __init__(self, data):
	
		self.data = data
		self.left = None
		self.right = None
def insert(node, key):
	if (node == None):
		return newNode(key)
	if (key < node.data):
		node.left = insert(node.left,
						key)
	else if (key > node.data):
		node.right = insert(node.right,key)
	return node
def storeNodes(root):

	global all_nodes
	global leaf_nodes
	if (root == None):
		return
	all_nodes.add(root.data)
	if (root.left == None and
		root.right == None):
		leaf_nodes.add(root.data)
		return
	storeNodes(root. left)
	storeNodes(root.right)
def isDeadEnd(root):

	global all_nodes
	global leaf_nodes
	if (root == None):
		return False
	all_nodes.add(0)
	storeNodes(root)
	for x in leaf_nodes:
		if ((x + 1) in all_nodes and
			(x - 1) in all_nodes):
			return True

	return False
