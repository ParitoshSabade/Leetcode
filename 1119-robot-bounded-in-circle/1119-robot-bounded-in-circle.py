class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        direction = "N"
        curr = [0,0]
        for i in instructions:
            if i == "G":
                if direction == "N":
                    curr[1] += 1
                elif direction == "S":
                    curr[1] -= 1
                elif direction == "E":
                    curr[0] += 1
                else:
                    curr[0] -= 1
            elif i == "L":
                if direction == "N":
                    direction = "W"
                elif direction == "S":
                    direction = "E"
                elif direction == "E":
                    direction = "N"
                else:
                    direction = "S"
            else:
                if direction == "N":
                    direction = "E"
                elif direction == "S":
                    direction = "W"
                elif direction == "E":
                    direction = "S"
                else:
                    direction = "N"
            
        
        return curr == [0, 0] or direction != "N"



