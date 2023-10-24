public class Solution {
    public void ReverseString(char[] s) {
        int start = 0;
        int end = s.Length-1;
        char tmp = 'a';
        
        while(start < end)
        {
            tmp  = s[end];
            s[end] = s[start];
            s[start] = tmp;
            start++;
            end--;
        }
        
    }
}