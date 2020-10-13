coins = list(map(int, input().split()))
amount = int(input())

t = [[0 for i in range(amount+1)] for j in range(len(coins) + 1)]
for i in range(1,amount+1):
    t[0][i] = float("inf")
for i in range(1, len(coins) + 1):
    for j in range(1,amount+1):
        if(coins[i-1]>j):
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = min(t[i-1][j],t[i][j-coins[i-1]]+1)
        # print(t)
if(t[len(coins)][amount]<float("inf")):
    print(t[len(coins)][amount])
else:
    print(-1)