#code

def palindrome(a):
    for i in range(len(a)//2):
        if(a[i]!=a[len(a)-i-1]):
            return False
    return True

def solve(a,i,j):
    if(i>j):
        return 0
    if(palindrome(a[i:j+1])):
        return 0
    if(t[i][j]!=-1):
        return t[i][j]
    min1 = float("inf")
    for k in range(i,j):
        # temp = 1 + solve(a,i,k) + solve(a,k+1,j)
        temp = 1
        if(t[i][k]!=-1):
            temp += t[i][k]
        else:
            t[i][k] = solve(a,i,k)
            temp += t[i][k]
        if(t[k+1][j]!=-1):
            temp+=t[k+1][j]
        else:
            t[k+1][j] = solve(a,k+1,j)
            temp+=t[k+1][j]
        
        if(temp<min1):
            min1 = temp
    t[i][j] = min1
    return min1

for _ in range(int(input())):
    s = input()
    t = [[-1 for i in range(1001)] for j in range(1001)]
    ans = solve(s,0,len(s)-1)
    print(ans)