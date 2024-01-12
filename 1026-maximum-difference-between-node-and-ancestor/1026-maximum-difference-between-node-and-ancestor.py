# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        valueMap = {}
        maxValue = float('-inf')
        def DFS(node,parent):
            if parent:
                if parent.val in valueMap:
                    valueMap[node.val] = valueMap[parent.val]+[parent.val]
                else:
                    valueMap[node.val] = [parent.val]
            else:
                valueMap[node.val] = []
                
            if node.left:
                DFS(node.left,node)
                
            if node.right:
                DFS(node.right,node)
                
        
        DFS(root,None)
        
        for key in valueMap:
            for num in valueMap[key]:
                maxValue = max(maxValue,abs(key-num))
        #print(valueMap)
        return maxValue
            
            