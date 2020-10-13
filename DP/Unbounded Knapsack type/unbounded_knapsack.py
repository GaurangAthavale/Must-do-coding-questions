#same as rod cutting problem
# val[] == price[](i.e. profit)
# wt[] == length[](of rod)(profit for ith length) 
# W == N(total length of rod)

for _ in range(int(input())):
	n = int(input())
	W = int(input())
	wt = list(map(int,input().split()))
	val = list(map(int,input().split()))
	t = [[0 for i in range(W+1)] for j in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,W+1):
			if(wt[i-1]>j):
				t[i][j] = t[i-1][j]
			else:
				t[i][j] = max(t[i-1][j],val[i-1] + t[i][j-wt[i-1]])
	print(t[-1][-1])