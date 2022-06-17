class pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second
def make_graph(numTasks, prerequisites):
	graph = []
	for i in range(numTasks):
		graph.append([])

	for pre in prerequisites:
		graph[pre.second].append(pre.first)

	return graph
def compute_indegree(graph):
	degrees = [0]*len(graph)

	for neighbors in graph:
		for neigh in neighbors:
			degrees[neigh] += 1

	return degrees
def canFinish(numTasks, prerequisites):
	graph = make_graph(numTasks, prerequisites)
	degrees = compute_indegree(graph)

	for i in range(numTasks):
		j = 0
		while(j < numTasks):
			if (degrees[j] == 0):
				break
			j += 1

		if (j == numTasks):
			return False

		degrees[j] = -1
		for neigh in graph[j]:
			degrees[neigh] -= 1

	return True

