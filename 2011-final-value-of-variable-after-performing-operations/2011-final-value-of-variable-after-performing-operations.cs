public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int X = 0;
        for(int i = 0; i < operations.Length; i++)
        {
            if(operations[i].Contains("+"))
                X+=1;
            else
                X-=1;
            
           
        }
         return X;
        
    }
}