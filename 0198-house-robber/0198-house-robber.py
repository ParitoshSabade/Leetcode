class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def Rob(i):
            return max(Rob(i+1),nums[i]+Rob(i+2)) if i < len(nums) else 0
        return Rob(0)