class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matchMap = {}
        winAll,loseOne = [],[]
        for w,l in matches:
            matchMap.setdefault(w,0)
            
            if l in matchMap:
                matchMap[l]+=1
            else:
                matchMap[l] = 1
                
        for k in matchMap.keys():
            if matchMap[k] == 0:
                winAll.append(k)
                
            if matchMap[k] == 1:
                loseOne.append(k)
        
        return [sorted(winAll),sorted(loseOne)]
            
            
                
            
            
            
        