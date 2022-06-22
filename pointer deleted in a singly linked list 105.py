class Node():
	def __init__(self, val = None):
		self.data = val
		self.next = None
def push(head, val):
	newnode = Node(val)
	newnode.next = head.next
	head.next = newnode
def print_list(head):

	temp = head.next
	while(temp != None):
		print(temp.data, end = ' ')
		temp = temp.next
	print()
def delete_node(node):

	prev = Node()

	if(node == None):
		return
	else:
		while(node.next != None):
			node.data = node.next.data
			prev = node
			node = node.next

		prev.next = None


