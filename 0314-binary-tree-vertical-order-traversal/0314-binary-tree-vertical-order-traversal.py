# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
            
            
        q = []
        q.append((root,0))
        answer = []
        answer2 = {}
        while q:
            node,col = q.pop(0)
            answer.append((node.val,col))
            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
                
        print(answer)
        for val,col in answer:
            if col in answer2:
                answer2[col].append(val)     
            else:
                answer2[col] = [val]
                
        return [values for key, values in sorted(answer2.items())]
    
                
                
            