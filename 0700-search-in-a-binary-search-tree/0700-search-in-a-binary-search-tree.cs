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
    public TreeNode SearchBST(TreeNode root, int val) {
        TreeNode result = null;
        void DFS(TreeNode node)
        {
            if(node.val == val)
            {
                result = node;
                
            }
            if(node.left != null)
                DFS(node.left);
            if(node.right != null)
                DFS(node.right);
            
        }
        
        DFS(root);
        return result;
        
    }
}