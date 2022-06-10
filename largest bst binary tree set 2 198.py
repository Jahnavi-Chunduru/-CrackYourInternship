INT_MIN = -2147483648
INT_MAX = 2147483647
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def largestBSTBT(root):
	if (root == None):
		return 0, INT_MIN, INT_MAX, 0, True
	if (root.left == None and root.right == None) :
		return 1, root.data, root.data, 1, True
	l = largestBSTBT(root.left)
	r = largestBSTBT(root.right)
	ret = [0, 0, 0, 0, 0]
	ret[0] = (1 + l[0] + r[0])
	if (l[4] and r[4] and l[1] <
		root.data and r[2] > root.data) :
	
		ret[2] = min(l[2], min(r[2], root.data))
		ret[1] = max(r[1], max(l[1], root.data))
		ret[3] = ret[0]
		ret[4] = True

		return ret
	ret[3] = max(l[3], r[3])
	ret[4] = False

	return ret
