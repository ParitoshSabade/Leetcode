class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mymap = {}
        answer = []
        for i in nums:
            if i in mymap:
                mymap[i]+=1
            else:
                mymap[i] = 1
        #print(mymap)    
        while mymap.values():
            row = []
            for k in mymap:
                if mymap[k] > 0:
                    row.append(k)
                    mymap[k] -= 1
            mymap = {k:v for k,v in mymap.items() if v!=0}       
            
            answer.append(row)
            
        
        print(answer)
        return answer
                
            