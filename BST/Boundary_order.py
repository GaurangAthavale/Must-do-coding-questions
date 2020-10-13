def print_left(a,root):
    if(root == None):
        return
    if(root.left!=None):
        # print(root.data,end = " ")
        a.append(root.data)
        print_left(a,root.left)
    elif(root.right!=None):
        # print(root.data,end = " ")
        a.append(root.data)
        print_left(a,root.right)
    
def print_right(r,root):
    if(root == None):
        return
    if(root.right!=None):
        # print(root.data,end = " ")
        r.append(root.data)
        print_right(r,root.right)
    elif(root.left!=None):
        # print(root.data,end = " ")
        r.append(root.data)
        print_right(r,root.left)
        
def print_leaves(a,root):
    if(root == None):
        return 
    print_leaves(a,root.left)
    if(root.left == None and root.right == None):
        # print(root.data, end = " ")
        a.append(root.data)
    print_leaves(a,root.right)
    


def printBoundaryView(root):
    # Code here
    a = [root.data]
    r = []
    # print(root.data,end = " ")
    print_left(a,root.left)
    
    print_leaves(a,root.left)
    print_leaves(a,root.right)
    
    print_right(r,root.right)
    
    r.reverse()
    a = a+r
    return a

#6 4 10 10 6 8 7 4 4 9 3 6 9 5 8
#6 4 10 10 6 8 7 4 4 9 3 6 8 5 9 