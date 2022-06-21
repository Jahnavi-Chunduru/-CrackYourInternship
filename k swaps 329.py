def findMaximumNum(string, k, maxm, ctr):
	if k == 0:
		return

	n = len(string)
	mx = string[ctr]

	for i in range(ctr+1,n):
		if int(string[i]) > int(mx):
			mx=string[i]
	if(mx!=string[ctr]):
		k=k-1
	for i in range(ctr,n):
		if(string[i]==mx):
			string[ctr], string[i] = string[i], string[ctr]
			new_str = "".join(string)
			if int(new_str) > int(maxm[0]):
				maxm[0] = new_str
			findMaximumNum(string, k , maxm, ctr+1)
			string[ctr], string[i] = string[i], string[ctr]
