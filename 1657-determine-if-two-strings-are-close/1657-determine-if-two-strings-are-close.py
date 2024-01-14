class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        mp1,mp2 = {},{}
        for i in word1:
            if i in mp1:
                mp1[i]+=1
            else:
                mp1[i] = 1
                
        for i in word2:
            if i in mp2:
                mp2[i]+=1
            else:
                mp2[i] = 1
          
        if mp1 == mp2:
            return True
        if set(mp1.keys()) == set(mp2.keys()):
            mp1_val = sorted([v for k,v in mp1.items()])
            mp2_val = sorted([v for k,v in mp2.items()])
            if mp1_val==mp2_val:
                return True
        
        return False