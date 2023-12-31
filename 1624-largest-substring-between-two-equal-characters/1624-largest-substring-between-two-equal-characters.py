class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dict1 = {}
        dict2 = {}
        maxDiff = -1
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = i
                
        for i in range(len(s)-1,-1,-1):
            if s[i] not in dict2:
                dict2[s[i]] = i
        
        for k in dict1:
            if dict2[k] > dict1[k]:
                Diff = dict2[k] - dict1[k]
                maxDiff = max(maxDiff,Diff)
        if maxDiff == -1:
            return maxDiff
        return maxDiff - 1
                
        
            
            
        
        