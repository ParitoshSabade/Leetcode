import heapq as hq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        solution = hq.nlargest(k,num_count.items(),key = lambda x:x[1])
        solution = [k for k,v in solution]
        print(solution)
        return solution