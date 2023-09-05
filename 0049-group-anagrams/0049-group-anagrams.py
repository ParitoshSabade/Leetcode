class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        str_map = {}
        for str1 in strs:
            
            for char in str1:
                if char in str_map:
                    str_map[char]+=1
                else:
                    str_map[char] = 1
            key = tuple(sorted(str_map.items()))
            if key in store:
                store[key].append(str1)
            else:
                store[key] = [str1]
            
            str_map.clear()
            
            
        return store.values()
                
            