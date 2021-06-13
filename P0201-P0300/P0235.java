import java.util.*;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x, TreeNode left, TreeNode right) {
        this.val = x;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private List<TreeNode> getNodes(TreeNode root, TreeNode target) {
        List<TreeNode> list = new LinkedList<>();
        list.add(root);

        while (root != target) {
            if (target.val < root.val) {
                list.add(root.left);
                root = root.left;
            } else {
                list.add(root.right);
                root = root.right;
            }
        }

        return list;
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        List<TreeNode> tn1 = getNodes(root, p), tn2 = getNodes(root, q);
        int k = Math.min(tn1.size(), tn2.size()) - 1;
        while (k > 0 && tn1.get(k) != tn2.get(k)) --k;
        return tn1.get(k);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode answer, stdAnswer;

        TreeNode n3 = new TreeNode(3, null, null);
        TreeNode n5 = new TreeNode(5, null, null);
        TreeNode n0 = new TreeNode(0, null, null);
        TreeNode n4 = new TreeNode(4, n3, n5);
        TreeNode n7 = new TreeNode(7, null, null);
        TreeNode n9 = new TreeNode(9, null, null);
        TreeNode n2 = new TreeNode(2, n0, n4);
        TreeNode n8 = new TreeNode(8, n7, n9);
        TreeNode n6 = new TreeNode(6, n2, n8);

        stdAnswer = n6;
        answer = solution.lowestCommonAncestor(n6, n2, n8);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer.val, stdAnswer.val);

        stdAnswer = n2;
        answer = solution.lowestCommonAncestor(n6, n2, n4);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer.val, stdAnswer.val);

        TreeNode n1 = new TreeNode(1, null, null);
        n2 = new TreeNode(2, n1, null);

        stdAnswer = n2;
        answer = solution.lowestCommonAncestor(n2, n2, n1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer.val, stdAnswer.val);
    }
}