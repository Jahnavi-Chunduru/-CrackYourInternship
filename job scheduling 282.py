from functools import cmp_to_key
class Job:

	def __init__(self, start, finish, profit):

		self.start = start
		self.finish = finish
		self.profit = profit

def jobComparator(s1, s2):

	return s1.finish < s2.finish
def latestNonConflict(arr, i):

	for j in range(i - 1, -1, -1):
		if arr[j].finish <= arr[i - 1].start:
			return j

	return -1
def findMaxProfit(arr, n):
	arr = sorted(arr, key=cmp_to_key(jobComparator))
	table = [None] * n
	table[0] = arr[0].profit
	for i in range(1, n):
		inclProf = arr[i].profit
		l = latestNonConflict(arr, i)

		if l != -1:
			inclProf += table[l]
		table[i] = max(inclProf, table[i - 1])
	result = table[n - 1]

	return result


