# simply fibonacci series

for _ in range(int(input())):
    n = int(input())
    t = [1]*(n+1)
    for i in range(2,n+1):
        t[i] = t[i-1] + t[i-2]
    print(t[-1]) 
    