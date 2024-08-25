class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minV,minInd = float("inf"),0
        for i in range(k):
            for ind,num in enumerate(nums):
                if num < minV:
                    minV = num
                    minInd = ind
            nums[minInd] = nums[minInd]*multiplier
            minV,minInd = float("inf"),0
            print(nums)
        return nums