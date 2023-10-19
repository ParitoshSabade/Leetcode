class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0,c1,c2 =0,0,0
        for c in nums:
            if c == 0:
                c0+=1
            elif c == 1:
                c1+=1
            else:
                c2+=1
        i = 0        
        while c0!=0:
            nums[i] = 0
            c0-=1
            i+=1
        while c1!=0:
            nums[i] = 1
            c1-=1
            i+=1
        while c2!=0:
            nums[i] = 2
            c2-=1
            i+=1
            
            
            