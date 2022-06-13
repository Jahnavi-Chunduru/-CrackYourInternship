class Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def getPreIndex():
	return constructTreeUtil.preIndex


def incrementPreIndex():
	constructTreeUtil.preIndex += 1
def constructTreeUtil(pre, low, high):
	if(low > high):
		return None
	root = Node(pre[getPreIndex()])
	incrementPreIndex()
	if low == high:
		return root

	r_root = -1
	for i in range(low, high+1):
		if (pre[i] > root.data):
			r_root = i
			break
	if r_root == -1:
		r_root = getPreIndex() + (high - low)

	root.left = constructTreeUtil(pre, getPreIndex(), r_root-1)

	root.right = constructTreeUtil(pre, r_root, high)

	return root



def constructTree(pre):
	size = len(pre)
	constructTreeUtil.preIndex = 0
	return constructTreeUtil(pre, 0, size-1)


def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print (root.data,end=' ')
	printInorder(root.right)


