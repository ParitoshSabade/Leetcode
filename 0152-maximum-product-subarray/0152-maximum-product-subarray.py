class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        localMax,localMin = nums[0],nums[0]
        result =localMax
        for i in range(1,len(nums)):
            tempMax = max(nums[i],localMax*nums[i],localMin*nums[i])
            localMin = min(nums[i],localMax*nums[i],localMin*nums[i])
            localMax = tempMax
            result = max(result,localMax)
        return result
        