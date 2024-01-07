class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        beams = 0
        for row in bank:
            if row.count("1"):
                nxt = row.count("1")
                beams += prev*nxt
                prev = nxt
        return beams
                
        
            
        
        
                    
        
        