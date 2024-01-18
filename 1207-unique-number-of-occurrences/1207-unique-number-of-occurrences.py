class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Map = {}
        for i in arr:
            if i in Map:
                Map[i]+=1
            else:
                Map[i] = 1
        
        
        return len(Map.values()) == len(set(Map.values()))
            