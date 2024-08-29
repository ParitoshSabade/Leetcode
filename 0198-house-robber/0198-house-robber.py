class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return nums[0]
        elif L == 2:
            return max(nums)
        
        dp = [0]*L
        dp[L-1] = nums[L-1]
        dp[L-2] = max(dp[L-1],nums[L-2])
        if L == 2:
            return dp[0]
        for i in range(L-3,-1,-1):
            dp[i] = max((nums[i] + dp[i+2]),dp[i+1])
        
        return dp[0]