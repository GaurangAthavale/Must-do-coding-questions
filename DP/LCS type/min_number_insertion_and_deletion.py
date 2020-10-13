#code
for _ in range(int(input())):
    n1,n2 = list(map(int, input().split()))
    s = input()
    s3 = s.split(" ")
    s1 = s3[0]
    s2 = s3[1]
    # print(s1)
    t = [[0 for i in range(n2+1)] for j in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if(s1[i-1] == s2[j-1]):
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    i = len(s1)
    j = len(s2)
    str = ""
    while(t[i][j]!=0):
        if(s1[i-1] == s2[j-1]):
            str+=s1[i-1]
            i-=1
            j-=1
        else:
            if(t[i-1][j]>t[i][j-1]):
                i-=1
            else:
                j-=1
    # str = str[::-1]
    print(n1+n2-2*len(str))