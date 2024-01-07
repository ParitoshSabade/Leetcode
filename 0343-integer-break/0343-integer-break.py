class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.cache
        def recurse(k):
            maxProduct = 0
            if k==1:
                return -1
            if k == 2:
                return 1
            for i in range(1,(k//2)+1):
                op1 = max(i,recurse(i))
                op2 = max(k-i,recurse(k-i))
                maxProduct = max(maxProduct,op1*op2)
                
            return maxProduct
        return recurse(n)
                
                
            