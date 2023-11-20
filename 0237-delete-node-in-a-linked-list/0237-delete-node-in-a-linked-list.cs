/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void DeleteNode(ListNode node) {
        
        if (node != null && node.next != null) {
            // Copy the value of the next node to the current node
            node.val = node.next.val;
            
            // Update the current node's next pointer to skip the next node
            node.next = node.next.next;
        }
        
    }
}