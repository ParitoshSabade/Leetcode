class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        l = len(arr)
        PreviousMin = [-1]*l
        result = [0]*l
        MOD = 10**9 + 7
        
        stack = []
        
        for i in range(l):
            
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                PreviousMin[i] = stack[-1]
                
            stack.append(i)
            
        for i in range(l):
            result[i] = (result[PreviousMin[i]] if PreviousMin[i]!=-1 else 0) + (i-PreviousMin[i])*arr[i]
        
       
        return sum(result)%MOD
        
            
        
                    
                
            
        
            