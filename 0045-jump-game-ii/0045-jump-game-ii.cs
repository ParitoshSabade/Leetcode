public class Solution {
    public int Jump(int[] nums) {

int n = nums.Length;
        int jumps = 0;
        int currentFarthest = 0;
        int nextFarthest = 0;

        for (int i = 0; i < n - 1; i++) {
            nextFarthest = Math.Max(nextFarthest, i + nums[i]);

            
            if (i == currentFarthest) {
                jumps++;
                currentFarthest = nextFarthest;

                
                if (currentFarthest >= n - 1) {
                    break;
                }
            }
        }

        return jumps;
        
    }
}