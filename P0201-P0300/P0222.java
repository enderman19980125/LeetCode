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
    private int getLeftHeight(TreeNode p) {
        int height = 0;
        while (p != null) {
            height++;
            p = p.left;
        }
        return height;
    }

    private int getRightHeight(TreeNode p) {
        int height = 0;
        while (p != null) {
            height++;
            p = p.right;
        }
        return height;
    }

    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null) return 1;
        if (root.right == null) return 2;

        int height = getLeftHeight(root);
        int idx = 1;
        TreeNode p = root;

        while (true) {
            int ll = getLeftHeight(p.left), lr = getRightHeight(p.left);
            int rl = getLeftHeight(p.right), rr = getRightHeight(p.right);
            if (ll == 1 && lr == 1 && p.right == null) {
                idx = 2 * idx - 1;
                break;
            }
            if (ll == 1 && lr == 1 && rl == 1 && rr == 1) {
                idx = 2 * idx;
                break;
            }
            if (rl == rr + 1 || ll == rr) {
                p = p.right;
                idx = 2 * idx;
            } else {
                p = p.left;
                idx = 2 * idx - 1;
            }
        }

        return idx - 1 + (int) Math.pow(2, height - 1);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;
        TreeNode tn1, tn2, tn3, tn4, tn5, tn6, tn7, tn8;

        tn4 = new TreeNode(1, null, null);
        tn5 = new TreeNode(1, null, null);
        tn6 = new TreeNode(1, null, null);
        tn2 = new TreeNode(1, tn4, tn5);
        tn3 = new TreeNode(1, tn6, null);
        tn1 = new TreeNode(1, tn2, tn3);
        stdAnswer = 6;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        tn1 = null;
        stdAnswer = 0;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        tn1 = new TreeNode(1, null, null);
        stdAnswer = 1;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        tn2 = new TreeNode(1, null, null);
        tn1 = new TreeNode(1, tn2, null);
        stdAnswer = 2;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        tn2 = new TreeNode(1, null, null);
        tn3 = new TreeNode(1, null, null);
        tn1 = new TreeNode(1, tn2, tn3);
        stdAnswer = 3;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        tn4 = new TreeNode(1, null, null);
        tn2 = new TreeNode(1, tn4, null);
        tn3 = new TreeNode(1, null, null);
        tn1 = new TreeNode(1, tn2, tn3);
        stdAnswer = 4;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        tn4 = new TreeNode(1, null, null);
        tn5 = new TreeNode(1, null, null);
        tn2 = new TreeNode(1, tn4, tn5);
        tn3 = new TreeNode(1, null, null);
        tn1 = new TreeNode(1, tn2, tn3);
        stdAnswer = 5;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        tn4 = new TreeNode(1, null, null);
        tn5 = new TreeNode(1, null, null);
        tn6 = new TreeNode(1, null, null);
        tn7 = new TreeNode(1, null, null);
        tn2 = new TreeNode(1, tn4, tn5);
        tn3 = new TreeNode(1, tn6, tn7);
        tn1 = new TreeNode(1, tn2, tn3);
        stdAnswer = 7;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        tn8 = new TreeNode(1, null, null);
        tn4 = new TreeNode(1, tn8, null);
        tn5 = new TreeNode(1, null, null);
        tn6 = new TreeNode(1, null, null);
        tn7 = new TreeNode(1, null, null);
        tn2 = new TreeNode(1, tn4, tn5);
        tn3 = new TreeNode(1, tn6, tn7);
        tn1 = new TreeNode(1, tn2, tn3);
        stdAnswer = 8;
        answer = solution.countNodes(tn1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);
    }
}