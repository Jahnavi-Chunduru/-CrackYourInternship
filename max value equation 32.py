 def maxValue(self, A, x):
        for i in xrange(len(A)):
            if [str(x) > A[i], str(x) < A[i]][A[0] == '-']:
                return A[:i] + str(x) + A[i:]
        return A + str(x)
