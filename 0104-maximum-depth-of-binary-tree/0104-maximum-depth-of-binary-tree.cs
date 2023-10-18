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
    public int MaxDepth(TreeNode root) {
        int mx_ht = 0;
        
        if(root == null)
            return 0;
        void DFS(TreeNode node,int ht)
            {
                if(ht>mx_ht)
                    mx_ht = ht;
                if(node.left!=null)
                    DFS(node.left,ht+1);
                if(node.right!=null)
                    DFS(node.right,ht+1);
                
            }
        DFS(root,0);
        return mx_ht+1;
    }
    
}