class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,num in enumerate(nums):
            comp = target-num
            if comp in hashmap:
                return [index,hashmap[comp]]
            hashmap[num] = index

        return []
            