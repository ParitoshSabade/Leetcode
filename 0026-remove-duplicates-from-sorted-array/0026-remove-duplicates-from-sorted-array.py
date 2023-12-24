class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        op1 = nums[0]
        cnt = 1
        for i in range(1,len(nums)):
            if (op1^nums[i]):
                nums[cnt] = nums[i]
                cnt+=1
            
            op1 = nums[i]
        print(cnt)    
        return cnt
            