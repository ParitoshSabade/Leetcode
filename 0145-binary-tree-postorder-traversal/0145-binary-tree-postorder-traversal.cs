/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<int> PostorderTraversal(TreeNode root) {
        
        List<int>postorder = new List<int>();
        
        void postordertraversal(TreeNode node)
        {
            if(node.left != null)
                postordertraversal(node.left);
            
            if(node.right != null)
                postordertraversal(node.right);
            
            postorder.Add(node.val);
        }
        if(root == null)
            return postorder;
        postordertraversal(root);
        return postorder;
    }
        
    
}