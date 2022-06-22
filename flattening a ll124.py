class Node():
	def __init__(self,data):
		self.data = data
		self.right = None
		self.down = None

class LinkedList():
	def __init__(self):
		self.head = None
	def push(self,head_ref,data):
		new_node = Node(data)
		new_node.down = head_ref
		head_ref = new_node
		return head_ref

	def printList(self):

		temp = self.head
		while(temp != None):
			print(temp.data,end=" ")
			temp = temp.down

		print()
	def merge(self, a, b):
		if(a == None):
			return b
		if(b == None):
			return a
		result = None

		if (a.data < b.data):
			result = a
			result.down = self.merge(a.down,b)
		else:
			result = b
			result.down = self.merge(a,b.down)

		result.right = None
		return result

	def flatten(self, root):
		if(root == None or root.right == None):
			return root
		root.right = self.flatten(root.right)
		root = self.merge(root, root.right)
		return root

