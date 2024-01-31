class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        oddCountN,evenCountN = 0,0
        oddCountM,evenCountM = 0,0
        for i in range(n):
            if i%2 == 0:
                evenCountN+=1
            else:
                oddCountN+=1
                
        for i in range(m):
            if i%2 == 0:
                evenCountM+=1
            else:
                oddCountM+=1
                
        return (oddCountN*evenCountM)+(oddCountM*evenCountN)
                
            
        