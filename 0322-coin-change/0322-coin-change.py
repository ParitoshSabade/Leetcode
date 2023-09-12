class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(rem):
            ans = 1000000
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in dp:
                return dp[rem]
            
            for coin in coins:
                cnt = dfs(rem - coin)
                if cnt != -1:
                    ans = min(ans,cnt+1) 
                
            
            if ans == 1000000:
                dp[rem] = -1
                return -1
            else:
                dp[rem] = ans
                return ans
        
        
        
        return dfs(amount)  
            