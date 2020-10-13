#code

for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    mx = list(map(int, input().split()))
    wt = [[0 for i in range(m)] for j in range(n)]
    index = 0
    cost = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            wt[i][j] = mx[index]
            index+=1
    # print(wt)
    for col in range(m-1,-1,-1):
        for row in range(n):
            if(col == m-1):
                right = 0
            else:
                right = cost[row][col+1]
            
            if(col == m-1 or row == 0):
                ru = 0
            else:
                ru = cost[row-1][col+1]
            
            if(col == m-1 or row == n-1):
                rd = 0
            else:
                rd = cost[row+1][col+1]
            cost[row][col] = wt[row][col] + max(right,ru,rd)
        # print(cost)    
    res = -1
    for i in range(n):
        res = max(res,cost[i][0])
    print(res)
            
        