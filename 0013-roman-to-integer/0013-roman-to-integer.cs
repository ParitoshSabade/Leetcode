//using System.Collections.Generic;
public class Solution {
    public int RomanToInt(string s) {
        
        Dictionary<char, int> romanMap = new Dictionary<char, int>
{
    { 'I', 1 },
    { 'V', 5 },
    { 'X', 10 },
    { 'L', 50 },
    { 'C', 100 },
    { 'D', 500 },
    { 'M', 1000 }
};
        int prev = 0;
        int total = 0;
        
        for(int i = 0; i < s.Length; i++)
        {
            if(romanMap[s[i]] > prev)
            {
                total -= prev;
                total += romanMap[s[i]] - prev;
            }
            else
            {
                total += romanMap[s[i]];
            }
            prev = romanMap[s[i]];
        }
        return total;
        
    }
}