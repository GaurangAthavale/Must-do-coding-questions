# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# The function returns the root of the BST (currently rooted at 'root') 
# after inserting a new Node with value 'Key' into it. 
def insert(root, Key):
    # code here
    if(root == None):
        root = Node(Key)
    else:
        if(root.data<Key):
            if(root.right == None):
                root.right = Node(Key)
            else:
                insert(root.right,Key)
        elif(root.data>Key):
            if(root.left == None):
                root.left = Node(Key)
            else:
                insert(root.left,Key)
    return root

def inorder(root):
    if(root != None):
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = None
root = insert(root,5)
root = insert(root,1)
root = insert(root,4)
root = insert(root,2)
root = insert(root,3)
# print(root)
inorder(root)