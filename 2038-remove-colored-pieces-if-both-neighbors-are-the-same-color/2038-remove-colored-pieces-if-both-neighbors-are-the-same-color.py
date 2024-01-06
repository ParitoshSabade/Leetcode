class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        totalCountA = 0
        totalCountB = 0
        countA = 0
        countB = 0
        for i in range(len(colors)):
            if colors[i] == "A":
                countA += 1
                countB = 0
            elif colors[i] == "B":
                countB += 1
                countA = 0
                    
            if countB > 2:
                    totalCountB+=countB - 2
                    
            if countA > 2:
                    totalCountA+=countA - 2
        
        if totalCountA > totalCountB:
            return True
        else:
            return False
            
            