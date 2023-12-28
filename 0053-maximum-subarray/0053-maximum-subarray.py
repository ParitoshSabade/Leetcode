class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = float('-inf')
        globalMax = float('-inf')
        
        for num in nums:
            localMax = max(num,localMax+num)
            
            if localMax > globalMax:
                globalMax = localMax
                
        return globalMax
        