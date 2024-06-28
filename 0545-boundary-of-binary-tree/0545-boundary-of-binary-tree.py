# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        
        answer = [root.val]
        
        
        def findLeftBoundary(node):
            if not node or (not node.left and not node.right):
                return
            answer.append(node.val)
            if node.left:
                findLeftBoundary(node.left)
            else:
                findLeftBoundary(node.right)
        
        
        def findRightBoundary(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                findRightBoundary(node.right)
            else:
                findRightBoundary(node.left)
            answer.append(node.val)
        
       
        def findLeaves(node):
            if not node:
                return
            if not node.left and not node.right:
                answer.append(node.val)
                return
            findLeaves(node.left)
            findLeaves(node.right)
        
        
        if root.left:
            findLeftBoundary(root.left)
        
        
        
        findLeaves(root)
       
        
        
        
        if root.right:
            findRightBoundary(root.right)
        
        
        return answer

    
    
        
            
            
            
                
            
                
            
            
        
        