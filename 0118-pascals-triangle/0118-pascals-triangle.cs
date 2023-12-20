public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        
        IList<IList<int>> result = new List<IList<int>>();

        for (int i = 0; i < numRows; i++) {
            IList<int> row = new List<int>();
            int num = 1;

            for (int j = 0; j <= i; j++) {
                row.Add(num);
                num = num * (i - j) / (j + 1);
            }

            result.Add(row);
        }

        return result;
        
    }
}