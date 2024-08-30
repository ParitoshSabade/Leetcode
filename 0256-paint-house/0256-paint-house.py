class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        minCost = float('inf')
        @cache
        def jump(i,p,currCost):
            nonlocal minCost
            if i >= len(costs):
                minCost = min(minCost,currCost)
                return
            for ind,paint in enumerate(costs[i]):
                if ind == p:
                    continue
                jump(i+1,ind,currCost+paint)
        jump(0,0,0)
        jump(0,1,0)
        jump(0,2,0)
        return minCost
        
                