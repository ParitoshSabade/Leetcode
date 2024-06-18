# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        visited = []
        visited.append(root)
        answer = []
        while visited:
            level = []

            for _ in range(len(visited)):
                node = visited.pop(0)
                level.append(node.val)
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
            answer.append(level.pop())
        return answer
            
        