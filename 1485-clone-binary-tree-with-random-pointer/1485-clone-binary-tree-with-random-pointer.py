# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        hp = {}
        if not root:
            return None
        
        def DFS(node):
            if not node:
                return
            hp[node] = [NodeCopy(node.val), node.left, node.right, node.random]
            DFS(node.left)
            DFS(node.right)
            
        DFS(root)
        
        def DFS2(node):
            if not node:
                return
            copyNode = hp[node][0]
            copyNode.left = hp[node.left][0] if node.left else None
            copyNode.right = hp[node.right][0] if node.right else None
            copyNode.random = hp[node.random][0] if node.random else None
            DFS2(node.left)
            DFS2(node.right)
        
        DFS2(root)
        return hp[root][0]
        
            