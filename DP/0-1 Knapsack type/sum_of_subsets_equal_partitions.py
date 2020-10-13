#code

#code
# with only 3 rows(1 for initialization and 2 for computation)
'''
for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    if(sum(a)%2 != 0):
        print("NO")
    elif(sum(a)//2 < max(a)):
        print("NO")
    else:
        K = sum(a)//2
        t = [[False for i in range(K+1)] for j in range(3)]
        # for i in range(K+1):
        #     t[0][i] = False
        for i in range(3):
            t[i][0] = True
        for i in range(1,N+1):
            for j in range(1,K+1):
                if(a[i-1]>j):
                    t[i%2+1][j] = t[(i-1)%2+1][j]
                else:
                    t[i%2+1][j] = t[(i-1)%2+1][j] or t[(i-1)%2+1][j-a[i-1]]
        # for i in t:
        #     print(i)
        if(t[-1][-1] == True):
            print("YES")
        else:
            print("NO")
    '''

for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    if(sum(a)%2 != 0):
        print("NO")
    elif(sum(a)//2 < max(a)):
        print("NO")
    else:
        K = sum(a)//2
        t = [[-1 for i in range(K+1)] for j in range(N+1)]
        for i in range(K+1):
            t[0][i] = False
        for i in range(N+1):
            t[i][0] = True
        for i in range(1,N+1):
            for j in range(1,K+1):
                if(a[i-1]>j):
                    t[i][j] = t[i-1][j]
                else:
                    t[i][j] = t[i-1][j] or t[i-1][j-a[i-1]]
        # for i in t:
        #     print(i)
        if(t[N][K] == True):
            print("YES")
        else:
            print("NO")


    