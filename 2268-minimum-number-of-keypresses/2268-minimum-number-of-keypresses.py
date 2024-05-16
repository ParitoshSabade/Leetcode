
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        chr_count = defaultdict(int)
        chr_map = defaultdict(int)
        answer = 0
        p = 0
        for ch in s:
            chr_count[ch] += 1
            
        sorted_chrs = sorted(chr_count, key=lambda k: chr_count[k], reverse=True)
        
        for i,ch in enumerate(sorted_chrs):
            if i%9 == 0:
                p+=1
            chr_map[ch] = p
            
        for ch in s:
            answer += chr_map[ch]
            
        return answer
        
        
        
        
        
        
            
        