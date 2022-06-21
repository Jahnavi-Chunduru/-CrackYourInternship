_MIN=-2147483648
_MAX=2147483648								
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def insert(node,key):
	if (node == None):
		return newNode(key)
	if (key < node.data):
		node.left = insert(node.left, key)
	elif (key > node.data):
		node.right = insert(node.right, key)
	return node
def counNodes(root):
	count = 0

	if (root == None):
		return count

	current = root
	while (current != None):
	
		if (current.left == None):
			count+=1
			current = current.right
		
		else:
			pre = current.left

			while (pre.right != None and
					pre.right != current):
				pre = pre.right
			if(pre.right == None):
			
				pre.right = current
				current = current.left
			else:
			
				pre.right = None
				count += 1
				current = current.right

	return count
def findMedian(root):
	if (root == None):
		return 0
	count = counNodes(root)
	currCount = 0
	current = root

	while (current != None):
	
		if (current.left == None):
			currCount += 1
			if (count % 2 != 0 and
				currCount == (count + 1)//2):
				return prev.data
			elif (count % 2 == 0 and
					currCount == (count//2)+1):
				return (prev.data + current.data)//2
			prev = current
			current = current.right
		
		else:
			pre = current.left
			while (pre.right != None and
					pre.right != current):
				pre = pre.right
			if (pre.right == None):
			
				pre.right = current
				current = current.left
			else:
			
				pre.right = None

				prev = pre
				currCount+= 1
				if (count % 2 != 0 and
					currCount == (count + 1) // 2 ):
					return current.data

				elif (count%2 == 0 and
					currCount == (count // 2) + 1):
					return (prev.data+current.data)//2
				prev = current
				current = current.right
