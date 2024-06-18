"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = dict()
        
        while p != None:
            parents.setdefault(p.val,1)
            p = p.parent
            
        while q != None:
            if q.val in parents:
                return q
            q = q.parent
        
        