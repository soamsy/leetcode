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
    public boolean fn(TreeNode tree, TreeNode subTree) {
        if (tree == null && subTree == null) {
            return true;
        }
        else if (tree == null || subTree == null) {
            return false;
        }
        
        return tree.val == subTree.val && fn(tree.left, subTree.left) && fn(tree.right, subTree.right);
    }
    
    public boolean isSubtree(TreeNode tree, TreeNode subTree) {
        if (tree == null && subTree == null) {
            return true;
        } else if (tree == null || subTree == null) {
            return false;
        }

        return fn(tree, subTree) || isSubtree(tree.left, subTree) || isSubtree(tree.right, subTree);
    }
}