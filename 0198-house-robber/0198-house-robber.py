class Solution:
    def rob(self, nums: List[int]) -> int:
        Map = {}
        def Rob(i):
            if i >= len(nums):
                return 0
            if i in Map:
                return Map[i]
            
            Map[i] = max(nums[i] + Rob(i + 2), Rob(i + 1))
            return Map[i]
        return Rob(0)