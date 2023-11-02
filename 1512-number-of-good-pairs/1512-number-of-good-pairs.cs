public class Solution {
    public int NumIdenticalPairs(int[] nums) {
        int tot = 0;
        Dictionary<int, List<int>> numMap = new Dictionary<int, List<int>>();
        for(int i = 0; i < nums.Length; i++)
        {
            if(numMap.ContainsKey(nums[i]))
            {
                
                numMap[nums[i]].Add(i);
            }
            else
            {
                numMap[nums[i]] = new List<int>();
                numMap[nums[i]].Add(i);
            }
            
        }
        
        foreach(var item in numMap)
        {
            int k = item.Key;
            int l = item.Value.Count;
            
            tot += ((l*(l-1))/2); 
        }
        
      return tot;  
        
    }
}