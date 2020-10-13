#code

for _ in range(int(input())):
    n = int(input())
    val = 1
    for i in range(2*n,2*n-n,-1):
        # print(i)
        val *= i
    # print()
    for i in range(n,0,-1):
        # print(i)
        val //= i
    print(val//(n+1))