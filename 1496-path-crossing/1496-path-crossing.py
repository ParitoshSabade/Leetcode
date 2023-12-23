class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = [0,0]
        dir_store = {}
        dir_store[str(curr)] = True
        for direction in path:
            
            if direction == "N":
                curr[1]+=1
                
            elif direction == "S":
                curr[1]-=1
                
            elif direction == "E":
                curr[0]+=1
                
            elif direction == "W":
                curr[0]-=1
            if str(curr) in dir_store:
                return True
            else:
                dir_store[str(curr)] = True 
            
            

        return False
                
        