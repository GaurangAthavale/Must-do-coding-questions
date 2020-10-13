#code
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    j = 1
    max1 = 1
    count = 1
    while(j<n):
        # print(a[i],a[j])
        if(a[i]<a[j]):
            j+=1
            i+=1
            count+=1
        else:
            i = j
            j = i+1
            count = 1
        max1 = max(max1,count)
        # print(max1)
    print(max1)
    

# 1 2 1 3 4
# max1 = 2
# count = 2