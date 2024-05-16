
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        chr_count = Counter(s)
        
        chr_heap = [(-count, ch) for ch, count in chr_count.items()]
        heapq.heapify(chr_heap)
        
        answer = 0
        p = 0
        
        while chr_heap:
            p += 1
            for _ in range(9):
                if not chr_heap:
                    break
                count, ch = heapq.heappop(chr_heap)
                answer += p * abs(count)
        
        return answer
        
        
        
        
        
        
            
        