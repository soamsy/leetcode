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
    public void fn(TreeNode root, List<Integer> list) {
        if (root == null)
            return;
        
        fn(root.left, list);
        list.add(root.val);
        fn(root.right, list);
    }
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> flattenedTree = new ArrayList<>();
        fn(root, flattenedTree);
        return flattenedTree.get(k - 1);
    }
}