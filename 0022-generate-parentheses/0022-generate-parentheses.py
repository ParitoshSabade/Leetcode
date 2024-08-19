class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stck = []
        openP = closeP = 0
        def recursiveParenthesisGenerator(openP,closeP):
            if openP == closeP == n:
                res.append("".join(stck))
                return

            if openP < n:
                stck.append("(")
                recursiveParenthesisGenerator(openP+1,closeP)
                stck.pop()

            if closeP < openP:
                stck.append(")")
                recursiveParenthesisGenerator(openP,closeP+1)
                stck.pop()
        recursiveParenthesisGenerator(openP,closeP)
        return res    
                    
        
        
        
        
    
        
            
        
        
        
        
    