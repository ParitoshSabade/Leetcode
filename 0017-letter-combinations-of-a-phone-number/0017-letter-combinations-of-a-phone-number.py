class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" or digits == "1":
            return []
        phone_map = {"2": ["a","b","c"],"3": ["d","e","f"],"4": ["g","h","i"],"5": ["j","k","l"],"6": ["m","n","o"],"7": ["p","q","r",'s'],"8": ["t","u","v"],"9": ["w","x","y","z"]}
        
        digitsList = list(digits)
        tmp1 = phone_map[digitsList[0]]
        
        
        for i in range(1,len(digitsList)):
            tmp2 = []
            for t in tmp1:
                for k in phone_map[digitsList[i]]:
                    tmp2.append(t+k)
                    
            tmp1 = tmp2
            
            
        return tmp1
            
        
        
        
        
        