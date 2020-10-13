#code
for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    K = int(input())
    t = [[-1 for i in range(K+1)] for j in range(N+1)]
    for i in range(K+1):
        t[0][i] = 0
    for i in range(N+1):
        t[i][0] = 1
    for i in range(1,N+1):
        for j in range(1,K+1):
            if(a[i-1]>j):
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] + t[i][j-a[i-1]]
    # for k in t:
    #     print(k)
    print(t[N][K])
    
    