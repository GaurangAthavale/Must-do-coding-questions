"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = []
        ans = []
        if(root==None):
            return ans
        else:
            q.append(root)
            while(len(q)!=0):
                length = len(q)
                a = []
                while(length!=0):   
                    popped = q.pop(0)
                    a.append(popped.val)
                    for i in popped.children:
                        if(i!=None):
                            q.append(i)
                    length-=1
                ans.append(a)
        return ans
                