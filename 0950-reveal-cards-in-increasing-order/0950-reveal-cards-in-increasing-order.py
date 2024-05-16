class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        n = len(deck)
        output = [0]*n
        queue = [ i for i in range(n)]
        
        for card in deck:
            output[queue.pop(0)] = card
            
            if queue:
                queue.append(queue.pop(0))
                
        return output
        
        
        
        
            
            
                
                
                
                
        
        
        