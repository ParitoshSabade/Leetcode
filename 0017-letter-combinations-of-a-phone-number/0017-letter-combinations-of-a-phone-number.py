class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" or digits == "1":
            return []
        phone_map = {"2": ["a","b","c"],"3": ["d","e","f"],"4": ["g","h","i"],"5": ["j","k","l"],"6": ["m","n","o"],"7": ["p","q","r",'s'],"8": ["t","u","v"],"9": ["w","x","y","z"]}
        digits_list = list(digits)
        temp_list = phone_map[digits_list[0]]
        
        
        for i in range(1,len(digits_list)):
            if digits_list[i] == 1:
                continue
            temp_list2 = []
            for j in temp_list:
                for k in phone_map[digits_list[i]]:
                    
                    temp_list2.append(j+k)
                
                
            temp_list = temp_list2
            
            
        return temp_list
            
            
        
            
                
        
        