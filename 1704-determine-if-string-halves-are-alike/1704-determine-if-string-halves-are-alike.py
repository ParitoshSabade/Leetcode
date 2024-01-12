class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowelMap = ("a","e","i","o","u")
        leftCount,rightCount = 0,0
        s = s.lower()
        
        for i in range(len(s)//2):
            if s[i].lower() in vowelMap:
                leftCount+=1
                
        for i in range(len(s)//2,len(s)):
            if s[i].lower() in vowelMap:
                rightCount+=1
        return leftCount == rightCount
            
            
                