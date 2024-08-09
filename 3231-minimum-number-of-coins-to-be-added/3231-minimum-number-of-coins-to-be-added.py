class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        curr_max = 0
        add = 0
        i = 0
        while curr_max < target:

            if i < len(coins) and coins[i] <= (curr_max+1):
                curr_max += coins[i]
                i+=1
            else:
                curr_max += curr_max+1
                add+=1
        return add
