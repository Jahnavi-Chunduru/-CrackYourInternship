def checkPalindrome(string):
	length = len(string)
	length -= 1
	for i in range(length):
		if string[i] != string[length]:
			return False
		length -= 1
	return True

def printSolution(partitions):
	for i in range(len(partitions)):
		for j in range(len(partitions[i])):
			print(partitions[i][j], end = " ")
		print()

def addStrings(v, s, temp, index):
	length = len(s)
	string = ""

	current = temp[:]

	if index == 0:
		temp = []
	for i in range(index, length):
		string += s[i]
		if checkPalindrome(string):
			temp.append(string)
			if i + 1 < length:
				addStrings(v, s, temp[:], i + 1)
			else:
				v.append(temp)
			temp = current

def partition(s, v):
	temp = []
	addStrings(v, s, temp[:], 0)
	printSolution(v)


