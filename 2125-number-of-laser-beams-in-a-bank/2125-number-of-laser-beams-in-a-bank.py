class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = []
        
        totalbeams = 0
        for i in range(len(bank)):
            count1 = 0
            for j in bank[i]:
                if j == "1":
                    count1+=1
            lasers.append(count1)
        i,j = 0,1
        lasers = [x for x in lasers if x!=0]
        if len(lasers)<2:
            return 0
        
        for i in range(1,len(lasers)):
            totalbeams += lasers[i-1]*lasers[i] 
        return totalbeams;
                
                
        
            
        
        
                    
        
        