#code

for _ in range(int(input())):
    n = int(input())
    a = [1]*n
    for i in range(2,n):
        a[i] = a[i-1] + a[i-2]
    print(a[-1]%1000000007)