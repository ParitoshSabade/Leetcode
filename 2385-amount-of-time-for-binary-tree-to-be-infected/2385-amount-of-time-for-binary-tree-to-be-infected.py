# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    
        nbrMap = {}
       
        def TreeTraverse(node,parent):
            if parent:
                nbrMap[node.val] = [parent.val]
            else:
                nbrMap[node.val] = []
            if node.left:
                nbrMap[node.val].append(node.left.val)
                TreeTraverse(node.left,node)
            if node.right:
                nbrMap[node.val].append(node.right.val)
                TreeTraverse(node.right,node)
                
            
        TreeTraverse(root,None)
        #print(nbrMap)
        queue = deque()
        visited = set()
        queue.append(start)
        cnt = -1
        
        while queue:
            # print(cnt)
            # print(f"queue: {queue}")
            for i in range(len(queue)):
                nodeVal = queue.popleft()
                visited.add(nodeVal)
                # flag1 = False
                for n in nbrMap[nodeVal]:
                    if n not in visited:
                        queue.append(n)
                        # flag1 = True
                # if flag1 == True:
            cnt+=1
                # print(f"visited: {visited}")
        return cnt
            
            
            
            
        
            