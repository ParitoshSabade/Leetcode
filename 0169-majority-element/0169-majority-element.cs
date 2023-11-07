public class Solution {
    public int MajorityElement(int[] nums) {
        Array.Sort(nums);
        int cnt = 0;
        int nm = nums[0];
        for(int i = 0; i < nums.Length; i++)
        {
            if(nums[i] != nm)
            {
                if(cnt > (nums.Length/2))
                {
                    return nm;
                    break;
                }
                nm = nums[i];
                cnt = 0;
            }
            cnt+=1;
        }
        return nm;
        
    }
}