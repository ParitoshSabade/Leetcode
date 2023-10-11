class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        Sum = 0
        for num in nums:
            
            if Sum < 0:
                Sum = 0
            Sum += num
            
            maxSum = max(maxSum,Sum)
            
        return maxSum
            
        