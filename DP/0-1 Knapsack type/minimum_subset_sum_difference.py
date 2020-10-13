for _ in range(int(input())):
    arr = list(map(int, input().split()))
    t = [[False for i in range(sum(arr)+1)] for j in range(len(arr)+1)]
    # print(sum(arr))
    for i in range(len(arr)+1):
        t[i][0] = True
    for i in range(1,len(arr)+1):
        for j in range(1,sum(arr)+1):
            if(arr[i-1]>j):
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
    # print(t[len(arr)])
    x = []
    for i in range(len(t[len(arr)])//2+1):
        if(t[len(arr)][i] == True):
            x.append(i)
    print(x)
    min1 = float("inf")
    for i in x:
        min1 = min(abs(min1),abs(sum(arr)-2*i))
    print(min1)
    # return min1