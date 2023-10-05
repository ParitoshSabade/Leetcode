class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        while(start<=end):
            if target < nums[(start+end)//2]:
                end = (start+end)//2 - 1
            elif target > nums[(start+end)//2]:
                start = (start+end)//2 + 1
                
            else:
                return (start+end)//2
            
        return -1
            
            
    
        