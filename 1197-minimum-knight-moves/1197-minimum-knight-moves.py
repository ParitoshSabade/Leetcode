class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        visited = {}
        queue = []
        if abs(x)==1 and abs(y)==1:
            return 2
        queue.append((0,0,0))
        while queue:
            curr = queue.pop(0)
            
            x1,y1,cnt = curr[0],curr[1],curr[2]
            if (visited.get((x1,y1),0)) == 0:
                #print(curr)
                if x1 == x and y1 == y:
                    queue.clear()
                    return cnt
                    
                if x >= x1 and y >= y1:
                    queue.append((x1+2,y1+1,cnt+1))
                    queue.append((x1+1,y1+2,cnt+1))
                if x >=x1 and y <= y1:
                    queue.append((x1+2,y1-1,cnt+1))
                    queue.append((x1+1,y1-2,cnt+1))
                if x <= x1 and y >=y1:
                    queue.append((x1-2,y1+1,cnt+1))
                    queue.append((x1-1,y1+2,cnt+1))
                if x <= x1 and y <= y1:
                    queue.append((x1-2,y1-1,cnt+1))
                    queue.append((x1-1,y1-2,cnt+1))
                visited[(x1,y1)] = True
                
        
                
        
            
        