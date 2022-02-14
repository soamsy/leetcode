/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValid(TreeNode node, Integer left, Integer right) {
        if (node == null)
            return true;
        
        if (left != null && node.val <= left)
            return false;
        if (right != null && right <= node.val)
            return false;
        
        return isValid(node.left, left, node.val) && isValid(node.right, node.val, right);
    }
    
    public boolean isValidBST(TreeNode root) {
        return isValid(root, null, null);
    }
}