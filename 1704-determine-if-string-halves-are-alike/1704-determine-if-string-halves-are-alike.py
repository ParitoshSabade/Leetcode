class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowelMap = {"a":0,"e":0,"i":0,"o":0,"u":0}
        leftCount,rightCount = 0,0
        s = s.lower()
        
        for i in range(len(s)//2):
            if s[i].lower() in vowelMap:
                leftCount+=1
                
        for i in range(len(s)//2,len(s)):
            if s[i].lower() in vowelMap:
                rightCount+=1
        return leftCount == rightCount
            
            
                