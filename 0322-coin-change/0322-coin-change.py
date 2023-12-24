class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        ans = 0
        def DFS(rem):
            ans = float('inf')
            if rem < 0:
                return -1
            elif rem == 0:
                return 0
            elif rem in dp:
                return dp[rem]
            
            for coin in coins:
                cnt = DFS(rem - coin)
                if cnt != -1:
                    ans = min(ans,cnt+1)
            
            if ans != float('inf'):
                dp[rem] = ans
                return ans
            else:
                dp[rem] = -1
                return -1
            
            
        return DFS(amount)