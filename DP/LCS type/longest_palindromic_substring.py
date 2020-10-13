def check_pal(s):
    flag = 1
    for i in range(len(s)//2):
        if(s[i] != s[len(s)-i-1]):
            flag = 0
    if(flag == 1):
        return len(s)
    else:
        return 0

for _ in range(int(input())):
    s = input()
    pal = 1
    str = s[0]
    for i in range(len(s)):
        for j in range(i,len(s)):
            # print(s[i:j+1])
            if(len(s[i:j+1]) > 1):
                val = check_pal(s[i:j+1])
                if(pal<val):
                    pal = val
                    str = s[i:j+1]                    
    # print(pal)
    print(str)