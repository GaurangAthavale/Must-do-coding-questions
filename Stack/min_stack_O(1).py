s = []
# global min1
min1 = float("inf")

def push(ele,min1):
    #CODE HERE
    if(len(s)==0):
        min1 = ele
        s.append(ele)
    else:
        if(ele<min1):
            s.append(2*ele-min1)
            min1 = ele
        else:
            s.append(ele)
    return min1

def pop(min1):
    #CODE HERE
    popped = s.pop()
    ret = min1
    if(s[-1]>min1):
        min1 = 2*min1 - popped
    return ret,min1

def getMin():
    #CODE HERE
    return min1

min1 = push(5,min1)
print(getMin())
min1 = push(3,min1)
print(getMin())
min1 = push(7,min1)
print(getMin())
print(s)
popped,min1 = pop(min1)
print(getMin())
# popped,min1 = pop(min1)
# print(getMin())

