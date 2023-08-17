class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dpTable = {}

        def rem_check(rem):
            ans = float('inf')
            if rem < 0 :
                return -1
            if rem == 0:
                return 0
            if rem in dpTable:
                return dpTable[rem]


            for coin in coins:
                cnt = rem_check(rem - coin)
                if cnt == -1:
                    continue

                ans = min(ans,cnt+1)
            if ans == float('inf'):
                ans = -1
            dpTable[rem] = ans
            return ans

        return rem_check(amount)
