public class Solution {
    public bool CanJump(int[] nums) {

int maxReach = 0;
        int length = nums.Length;

        for (int i = 0; i < length; i++) {
            
            if (i > maxReach) {
                return false;
            }

           
            maxReach = Math.Max(maxReach, i + nums[i]);

            
            if (maxReach >= length - 1) {
                return true;
            }
        }

        return false;
        
    }
}