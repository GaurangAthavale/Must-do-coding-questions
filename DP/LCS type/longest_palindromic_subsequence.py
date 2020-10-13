# Same as LCS but one string straight and other will be same string in reverse

#       s k e e g
#     0 1 2 3 4 5
#   0 0 0 0 0 0 0 
# g 1 0 
# e 2 0
# e 3 0
# k 4 0
# s 5 0

# NOTE: len(str) - LPS == min. no. of deletions reqd. to make string palindrome.
# NOTE: len(str) - LPS == min. no. of insertions reqd. to make string palindrome.

s = input()
t = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]  
for i in range(1,len(s)+1):
    for j in range(1,len(s)+1):
        if(s[i-1] == s[len(s)-j]):
            t[i][j] = t[i-1][j-1] + 1
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])

for i in t:
    print(i)

i,j = len(s), len(s)
pal = ""
while(t[i][j] != 0):
    if(s[i-1] == s[len(s)-j]):
        pal+=s[i-1]
        i-=1
        j-=1
    elif(t[i-1][j]>t[i][j-1]):
        i-=1
    else:
        j-=1
print(pal)