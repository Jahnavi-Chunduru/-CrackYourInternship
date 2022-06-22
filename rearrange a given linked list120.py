class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.next = None

left = None
def printlist(head):
	
	while (head != None):
		print(head.data, end = " ")
		if (head.next != None):
			print("->", end = "")
			
		head = head.next
		
	print()
def rearrange(head):
	
	global left
	if (head != None):
		left = head
		reorderListUtil(left)

def reorderListUtil(right):
	
	global left
	if (right == None):
		return
	
	reorderListUtil(right.next)
	if (left == None):
		return
	if (left != right and left.next != right):
		temp = left.next
		left.next = right
		right.next = temp
		left = temp
	else:
		if (left.next == right):
			left.next.next = None
			left = None
		else:
			left.next = None
			left = None

