for _ in range(int(input())):
	n = int(input())
	mx = []
	for i in range(n):
		m = []
		for j in range(i+1):
			m.append(1)
		mx.append(m)
	for i in mx:
		print(i)
	for i in range(1,n):
		for j in range(i+1):
			if(j == 0):
				mx[i][j] = mx[i-1][-1]
			else:
				mx[i][j] = mx[i][j-1] + mx[i-1][j-1]
	for i in mx:
		print(i)
	print(mx[-1][-1])
