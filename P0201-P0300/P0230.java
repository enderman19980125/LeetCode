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
    private int numNodes(TreeNode root) {
        if (root == null) return 0;
        return numNodes(root.left) + 1 + numNodes(root.right);
    }

    public int kthSmallest(TreeNode root, int k) {
        int numNodesLeft = numNodes(root.left);
        if (numNodesLeft + 1 == k) return root.val;
        if (k <= numNodesLeft) {
            return kthSmallest(root.left, k);
        } else {
            return kthSmallest(root.right, k - numNodesLeft - 1);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode n1, n2, n3, n4, n5, n6;
        int answer, stdAnswer;

        n2 = new TreeNode(2, null, null);
        n1 = new TreeNode(1, null, n2);
        n4 = new TreeNode(4, null, null);
        n3 = new TreeNode(3, n1, n4);
        stdAnswer = 1;
        answer = solution.kthSmallest(n3, 1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        n1 = new TreeNode(1, null, null);
        n2 = new TreeNode(2, n1, null);
        n4 = new TreeNode(4, null, null);
        n3 = new TreeNode(3, n2, n4);
        n6 = new TreeNode(6, null, null);
        n5 = new TreeNode(5, n3, n6);
        stdAnswer = 3;
        answer = solution.kthSmallest(n5, 3);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        n1 = new TreeNode(1, null, null);
        stdAnswer = 1;
        answer = solution.kthSmallest(n1, 1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);
    }
}