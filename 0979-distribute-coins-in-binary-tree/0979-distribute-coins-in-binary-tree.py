# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        minMoves = 0
        
        def DFS(node):
            nonlocal minMoves
            if not node:
                return 0
            
            leftT = DFS(node.left)
            rightT = DFS(node.right)
           
            excess = node.val + leftT + rightT -1 
            
            minMoves += abs(excess)
            
            return excess
            
        
        DFS(root)
        return minMoves
                