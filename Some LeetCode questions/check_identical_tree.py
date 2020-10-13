# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check(p,q):
    if(p==None and q==None):
        return True
    if((p==None and q!=None) or (p!=None and q==None)):
        return False
    if(p.val!=q.val):
        return False
    if(check(p.left,q.left)==False):
        return False
    if(check(p.right, q.right)==False):
        return False
    return True

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return check(p,q)