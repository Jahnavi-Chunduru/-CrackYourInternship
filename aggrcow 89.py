from sys import stdin

def isDistance(x):

	cowsplaced,previous = 1,positions[0]

	for i in xrange(1,N):
		
		if positions[i]-previous >= x:	
			cowsplaced += 1
			if cowsplaced == C:
				return True

			previous = positions[i]

	return False

test = int(stdin.readline())
while test:
	N,C = map(int,stdin.readline().split())
	positions = []

	for i in xrange(N):
		positions.append(int(stdin.readline()))

	positions = sorted(positions)

	begin,end = 0,positions[N-1]-positions[0]+1

	while end-1 > begin:
		mid = ((begin+end)/2)
		if isDistance(mid):
			begin = mid
		else:
			end = mid

	print begin
	test -= 1
