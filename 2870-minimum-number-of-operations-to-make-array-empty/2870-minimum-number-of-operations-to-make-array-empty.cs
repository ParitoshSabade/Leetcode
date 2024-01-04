
public class Solution {
    public int MinOperations(int[] nums) {
        Dictionary <int,int> myDict = new Dictionary<int,int>();
        int ans = 0;
        for(int i = 0; i < nums.Length; i++)
        {
            if(myDict.ContainsKey(nums[i]))
            {
                myDict[nums[i]]+=1;
            }
            else
            {
                myDict[nums[i]] = 1;
                
            }
            
        }
        foreach (KeyValuePair<int, int> kvp in myDict)
        {
            if(kvp.Value == 1)
                return -1;
            else
            {
                ans += (int)Math.Ceiling((double)(kvp.Value/3.0));
            }
        }
        return ans;
            
        
    }
}