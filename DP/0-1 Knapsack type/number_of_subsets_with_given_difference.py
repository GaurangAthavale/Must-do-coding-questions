for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	diff = int(input())
	sum1 = (diff + sum(a))//2
	t = [[0 for i in range(sum1+1)] for j in range(n+1)]
	for i in range(n+1):
		t[i][0] = 1
	for i in range(1,n+1):
		for j in range(1,sum1+1):
			if(a[i-1]>j):
				t[i][j] = t[i-1][j]
			else:
				t[i][j] = t[i-1][j-a[i-1]] + t[i-1][j]
	print(t[-1][-1])
