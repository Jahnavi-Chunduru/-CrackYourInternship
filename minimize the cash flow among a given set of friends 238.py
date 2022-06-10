N = 3
def getMin(arr):
	
	minInd = 0
	for i in range(1, N):
		if (arr[i] < arr[minInd]):
			minInd = i
	return minInd
def getMax(arr):

	maxInd = 0
	for i in range(1, N):
		if (arr[i] > arr[maxInd]):
			maxInd = i
	return maxInd
def minOf2(x, y):

	return x if x < y else y
def minCashFlowRec(amount):
	mxCredit = getMax(amount)
	mxDebit = getMin(amount)
	if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
		return 0
	min = minOf2(-amount[mxDebit], amount[mxCredit])
	amount[mxCredit] -=min
	amount[mxDebit] += min
	print("Person " , mxDebit , " pays " , min
		, " to " , "Person " , mxCredit)
	minCashFlowRec(amount)
def minCashFlow(graph):
	amount = [0 for i in range(N)]
	for p in range(N):
		for i in range(N):
			amount[p] += (graph[i][p] - graph[p][i])

	minCashFlowRec(amount)
	
