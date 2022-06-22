class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def zigZagList(head):
	flag = True
	current = head
	while (current.next != None):
	
		if (flag):
			if (current.data > current.next.data):
				t = current.data
				current.data = current.next.data
				current.next.data = t
			
		
		else :
                    
			if (current.data < current.next.data):
				t = current.data
				current.data = current.next.data
				current.next.data = t
			
		current = current.next
		if(flag):
			flag = False 
		else:
			flag = True
	return head
def push(head, k):

	tem = Node(0)
	tem.data = k
	tem.next = head
	head = tem
	return head
def display( head):

	curr = head
	while (curr != None):
		print( curr.data, "->", end =" ")
		curr = curr.next
	
	print("None")


