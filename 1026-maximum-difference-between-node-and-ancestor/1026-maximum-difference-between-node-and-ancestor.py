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
                valueMap[node.val] = (min(valueMap[parent.val][0],parent.val),max(valueMap[parent.val][1],parent.val))
                
            else:
                valueMap[node.val] = (float('inf'),float('-inf'))
                
            if node.left:
                DFS(node.left,node)
                
            if node.right:
                DFS(node.right,node)
                
        
        DFS(root,None)
        #print(valueMap)
        for key in valueMap:
            if key!=root.val:
                maxValue = max(maxValue,abs(valueMap[key][0]-key),abs(valueMap[key][1]-key))
        return maxValue
            
            