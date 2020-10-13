#length of SCS = n1+n2-lcs

for _ in range(int(input())):
    str1 = input()
    str2 = input()
    t = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if(str1[i-1] == str2[j-1]):
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    i = len(str1)
    j = len(str2)
    str = ""
    while(t[i][j]!=0):
        if(str1[i-1] == str2[j-1]):
            str+=str1[i-1]
            i-=1
            j-=1                
        else:
            if(t[i-1][j]>t[i][j-1]):
                i-=1
            else:
                j-=1
    str = str[::-1]
    # print(str) #LCS
    SCS_length = len(str1) + len(str2) - len(str)
    print(SCS_length)
    i=0
    j=0
    x=0
    sup = ""
    while(i<len(str1) and j<len(str2) and x<len(str)):
        if(str1[i] == str2[j] and str1[i] == str[x]):
            sup+=str1[i]
            i+=1
            j+=1
            x+=1
        else:
            if(str1[i]!=str[x]):
                sup+=str1[i]
                i+=1
            if(str2[j]!=str[x]):
                sup+=str2[j]
                j+=1
    # print(sup)
    while(i<len(str1)):
        sup+=str1[i]
        i+=1
    while(j<len(str2)):
        sup+=str2[j]
        j+=1
    print(sup)
    # return sup
                    
                