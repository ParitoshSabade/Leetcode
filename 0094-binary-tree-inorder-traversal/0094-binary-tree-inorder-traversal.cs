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
    public IList<int> InorderTraversal(TreeNode root) {
        List<int>inorder = new List<int>();
        
        void inordertraversal(TreeNode node)
        {
            if(node.left != null)
                inordertraversal(node.left);
            inorder.Add(node.val);
            if(node.right != null)
                inordertraversal(node.right);
        }
        if(root == null)
            return inorder;
        inordertraversal(root);
        return inorder;
    }
}