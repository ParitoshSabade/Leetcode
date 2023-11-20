public class Solution {
    public int MaxProfit(int[] prices) {
        int length = prices.Length;
        int maxProfit = 0;

        for (int i = 1; i < length; i++) {
            if (prices[i] > prices[i - 1]) {
                maxProfit += prices[i] - prices[i - 1];
            }
        }

        return maxProfit;
        
    }
}