public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length)
        {
            return false;
        }
        
        Dictionary<int,int> mp1 = new Dictionary<int,int>();
        
        
        for(int i=0; i < s.Length; i++)
        {
            if(mp1.ContainsKey(s[i]))
            {
                mp1[s[i]] += 1;
            }
            else
            {
                mp1[s[i]] = 1;
            }
        }
        for(int i=0; i < t.Length; i++)
        {
            if(mp1.ContainsKey(t[i]))
            {
                if(mp1[t[i]] > 0)
                    mp1[t[i]] -= 1;
                else
                    return false;
            }
            else
            {
                return false;
            }
        }
        return true;
        
        
    }
}