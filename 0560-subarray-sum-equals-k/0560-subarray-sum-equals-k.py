class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0:1}
        prefix=0
        ans=0
        for i in range(len(nums)):
            prefix+=nums[i]
            
            if prefix-k in cache:
                ans+=cache[prefix-k]
                
            cache[prefix] = cache.get(prefix, 0)+1
            
        return ans