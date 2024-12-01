class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        inc, dec = 0, 0

        if k == 0:
            return 0 if nums1 == nums2 else -1

        for i in range(n):
            diff = nums2[i] - nums1[i]
            if diff % k != 0:
                return -1
            if diff > 0:
                inc += diff
            elif diff < 0:
                dec -= diff

        if inc != dec:
            return -1

        return inc // k