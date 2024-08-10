class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        pal = 0
        og = x
        
        while x:
            pal = pal * 10 + x % 10
            x = x // 10
        
        if pal == og:
            return True
        return False