public class Solution {
    public void Rotate(int[] nums, int k) {
        if (nums == null || nums.Length == 0 || k % nums.Length == 0) {
            // If the array is empty, null, or k is a multiple of the array length, no rotation needed
            return;
        }

        int n = nums.Length;
        k = k % n; // To handle cases where k is greater than the array length

        // Reverse the entire array
        Reverse(nums, 0, n - 1);

        // Reverse the first k elements
        Reverse(nums, 0, k - 1);

        // Reverse the remaining elements
        Reverse(nums, k, n - 1);
        
    }
     private void Reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}