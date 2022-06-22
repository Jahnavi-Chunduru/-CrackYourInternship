class Node:
	def __init__(self, new_data):
		self.data = new_data
		self.next = None
def newNode(data):

	temp = Node(0)
	temp.data = data
	temp.next = None
	return temp
def getLength(Node):

	size = 0
	while (Node != None):
	
		Node = Node.next
		size = size + 1
	
	return size
def paddZeros( sNode, diff):

	if (sNode == None):
		return None

	zHead = newNode(0)
	diff = diff - 1
	temp = zHead
	while (diff > 0):
		diff = diff - 1
		temp.next = newNode(0)
		temp = temp.next
	
	temp.next = sNode
	return zHead

borrow = True
def subtractLinkedListHelper(l1, l2):

	global borrow
	
	if (l1 == None and l2 == None and not borrow ):
		return None

	l3 = None
	l4 = None
	if(l1 != None):
		l3 = l1.next
	if(l2 != None):
		l4 = l2.next
	previous = subtractLinkedListHelper(l3, l4)

	d1 = l1.data
	d2 = l2.data
	sub = 0
	if (borrow):
		d1 = d1 - 1
		borrow = False
	if (d1 < d2):
		borrow = True
		d1 = d1 + 10
	sub = d1 - d2
	current = newNode(sub)
	current.next = previous

	return current
def subtractLinkedList(l1, l2):
	if (l1 == None and l2 == None):
		return None
	len1 = getLength(l1)
	len2 = getLength(l2)

	lNode = None
	sNode = None

	temp1 = l1
	temp2 = l2
	if (len1 != len2):
		if(len1 > len2):
			lNode = l1
		else:
			lNode = l2
		
		if(len1 > len2):
			sNode = l2
		else:
			sNode = l1
		sNode = paddZeros(sNode, abs(len1 - len2))
	
	else:
		while (l1 != None and l2 != None):
		
			if (l1.data != l2.data):
				if(l1.data > l2.data ):
					lNode = temp1
				else:
					lNode = temp2
				
				if(l1.data > l2.data ):
					sNode = temp2
				else:
					sNode = temp1
				break
			
			l1 = l1.next
			l2 = l2.next
		
	global borrow
	borrow = False
	return subtractLinkedListHelper(lNode, sNode)
def printList(Node):

	while (Node != None):
	
		print (Node.data, end =" ")
		Node = Node.next
	
	print(" ")
