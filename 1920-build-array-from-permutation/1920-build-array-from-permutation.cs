public class Solution {
    public int[] BuildArray(int[] nums) {
        int[] a = new int[nums.Length];
        for(int i = 0; i< nums.Length; i++)
        {
            a[i] = nums[nums[i]];
        }
        
        return a;
        
    }
}