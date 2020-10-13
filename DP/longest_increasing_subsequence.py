#code

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t = [1 for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if(a[i]>a[j]):
                t[i] = max(t[i],t[j]+1)
    # print(t)
    print(max(t))
