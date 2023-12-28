class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(left,right):
            while left<=right:
                pivot = (left+right)//2
                if nums[pivot] == target:
                    return pivot
                else:
                    
                    if nums[pivot] > target:
                        right = pivot-1
                    else:
                        left = pivot+1
                    
            return -1

        def findRotate(left,right):
            if nums[left] < nums[right]:
                return 0
            while left<=right:
                pivot = (left+right)//2
                if nums[pivot] > nums[pivot+1]:
                    return pivot+1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1
        
        n = len(nums)
        
        
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        rotateIndex = findRotate(0,n-1)    
        if nums[rotateIndex] == target:
            return rotateIndex
        if rotateIndex == 0:
            return binarySearch(0,n-1)
        if target < nums[0]:
            return binarySearch(rotateIndex,n-1)
        
        return binarySearch(0,rotateIndex)
       
            