#User function Template for python3


'''
class Node:
    def init(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the level order traversal of the binary tree in spiral order
# Note: You aren't required to print a new line after every test case
def printSpiral(root):
    # Code here
    s1 = []
    s2 = []
    if(root!=None):
        s1.append(root)
    # x = s1.pop()
    # print(x.data)
    while(len(s1)!=0 or len(s2)!=0):
        if(len(s1)!=0):
            while(len(s1)!=0):
                pop1 = s1.pop()
                print(pop1.data,end=" ")
                if(pop1.right!=None):
                    s2.append(pop1.right)
                if(pop1.left!=None):
                    s2.append(pop1.left)
        else:
            while(len(s2)!=0):
                pop1 = s2.pop()
                print(pop1.data,end=" ")
                if(pop1.left!=None):
                    s1.append(pop1.left)
                if(pop1.right!=None):
                    s1.append(pop1.right)
            
    
