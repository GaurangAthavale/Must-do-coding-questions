#code
for _ in range(int(input())):
    n1,n2 = list(map(int, input().split()))
    s1 = input()
    s2 = input()
    t = [[0 for i in range(n2+1)] for j in range(n1+1)]
    result = 0
    pos_i,pos_j = 0,0
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if(s1[i-1] == s2[j-1]):
                t[i][j] = 1+t[i-1][j-1]
                # result = max(result,t[i][j])
                if(result<t[i][j]):
                    result = t[i][j]
                    pos_i = i
                    pos_j = j
            else:
                t[i][j] = 0
    # for i in t:
    #     print(i)
    print(t[pos_i][pos_j])
    str = ""
    while(t[pos_i][pos_j]!=0):
        str+=s1[pos_i-1]
        pos_j-=1
        pos_i-=1
    print(str[::-1])