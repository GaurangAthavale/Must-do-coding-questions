#code

for _ in range(int(input())):
    n = int(input())
    i2,i3,i5 = 0,0,0
    a = [0]*n
    a[0] = 1
    m2,m3,m5 = 2,3,5
    for i in range(1,n):
        a[i] = min(m2,m3,m5)
        if(a[i] == m2):
            i2+=1
            m2 = a[i2] * 2
        if(a[i] == m3):
            i3+=1
            m3 = a[i3] * 3
        if(a[i] == m5):
            i5+=1
            m5 = a[i5] * 5
    # print(a)
    print(a[-1])

# Check if no. isUgly
'''def isUgly(self, num: int) -> bool:
        i2,i3,i5 = 0,0,0
        a = [0]
        a[0] = 1
        m2,m3,m5 = 2,3,5
        if(a[-1] == num):
            return True
        if(a[-1]>num):
            return False
        for i in range(1,num):
            a.append(min(m2,m3,m5))
            if(a[i] == m2):
                i2+=1
                m2 = a[i2] * 2
            if(a[i] == m3):
                i3+=1
                m3 = a[i3] * 3
            if(a[i] == m5):
                i5+=1
                m5 = a[i5] * 5
            # print(a)
            if(a[-1] == num):
                return True
            if(a[-1]>num):
                return False'''