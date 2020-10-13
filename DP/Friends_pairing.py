for _ in range(int(input())):
    n = int(input())
    t = [-1 for i in range(n+1)]
    
    for i in range(1,n+1):
        if(i<=2):
            t[i] = i
        else:
            t[i] = t[i-1] + (i-1)*t[i-2]
    
    print(t[-1])    