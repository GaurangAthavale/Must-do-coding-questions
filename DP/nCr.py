#code

for _ in range(int(input())):
    a = list(map(int, input().split()))
    val = 1
    for i in range(a[0],a[0]-a[1],-1):
        val *= i
    for i in range(a[1],0,-1):
        val //= i
    print(val%(10**9+7))