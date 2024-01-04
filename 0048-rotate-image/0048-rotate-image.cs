public class Solution {
    public void Rotate(int[][] matrix) {
        
        Array.Reverse(matrix);
        
        for(int i = 0; i<matrix.Length;i++)
        {
            for(int j = 0; j<i;j++)
            {
                //Console.WriteLine("hi");
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        
    }
}