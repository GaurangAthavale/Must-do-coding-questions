
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Your task is to complete this function
# Function should return the level order of the tree in the form of a list of integers
def levelOrder(root):
    # Code here
    q = []
    q.append(root)
    lvl = []
    while(len(q)>0):
        temp = q.pop(0)
        # print(temp.data)
        lvl.append(temp.data)
        if(temp.left!=None):
            q.append(temp.left)
        if(temp.right!=None):
            q.append(temp.right)
    return lvl