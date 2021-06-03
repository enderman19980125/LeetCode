// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode left = invertTree(root.left);
        TreeNode right = invertTree(root.right);
        root.right = left;
        root.left = right;
        return root;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode answer, tn1, tn2, tn3, tn4, tn6, tn7, tn9;

        tn1 = new TreeNode(1, null, null);
        tn3 = new TreeNode(3, null, null);
        tn6 = new TreeNode(6, null, null);
        tn9 = new TreeNode(9, null, null);
        tn2 = new TreeNode(2, tn1, tn3);
        tn7 = new TreeNode(7, tn6, tn9);
        tn4 = new TreeNode(4, tn2, tn7);
        answer = solution.invertTree(tn4);

        tn1 = new TreeNode(1, null, null);
        tn3 = new TreeNode(3, null, null);
        tn2 = new TreeNode(2, tn1, tn3);
        answer = solution.invertTree(tn2);

        answer = solution.invertTree(null);
    }
}