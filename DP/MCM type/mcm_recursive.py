#code

def solve(a,i,j):
    if(i>=j):
        return 0
    if(t[i][j]!=-1):
        return t[i][j]
    min1 = float("inf")
    for k in range(i,j):
        temp = solve(a,i,k) + solve(a,k+1,j) + a[i-1]*a[k]*a[j]
        if(temp<min1):
            min1 = temp
    t[i][j] = min1
    return min1
    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t = [[-1 for i in range(101)] for j in range(101)]
    ans = solve(a,1,n-1)
    print(ans)
    