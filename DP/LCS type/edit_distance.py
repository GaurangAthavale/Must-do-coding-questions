#code

for _ in range(int(input())):
    n1,n2 = list(map(int, input().split()))
    s = input()
    s1 = s.split(" ")
    t = [[0 for i in range(n2+1)] for j in range(n1+1)]
    for i in range(n1+1):
        t[i][0] = i
    for i in range(n2+1):
        t[0][i] = i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if(s1[0][i-1] == s1[1][j-1]):
                t[i][j] = t[i-1][j-1]
            else:
                t[i][j] = min(t[i][j-1], t[i-1][j], t[i-1][j-1]) + 1
    # for i in t:
    #     print(i)
    print(t[-1][-1])