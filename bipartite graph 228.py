class Graph():

	def __init__(self, V):
		self.V = V
		self.graph = [[0 for column in range(V)]
					for row in range(V)]

		self.colorArr = [-1 for i in range(self.V)]
	def isBipartiteUtil(self, src):
		queue = []
		queue.append(src)
		while queue:

			u = queue.pop()
			if self.graph[u][u] == 1:
				return False

			for v in range(self.V):
				if (self.graph[u][v] == 1 and
						self.colorArr[v] == -1):
					self.colorArr[v] = 1 - self.colorArr[u]
					queue.append(v)
				elif (self.graph[u][v] == 1 and
					self.colorArr[v] == self.colorArr[u]):
					return False
		return True

	def isBipartite(self):
		self.colorArr = [-1 for i in range(self.V)]
		for i in range(self.V):
			if self.colorArr[i] == -1:
				if not self.isBipartiteUtil(i):
					return False
		return True
