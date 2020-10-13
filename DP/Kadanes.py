for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max1 = a[0]
    current = max1
    i = 1
    while(i<n):
        current = max(a[i], current+a[i])
        max1 = max(max1,current)
        i+=1
    print(max1)