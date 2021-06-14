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
    Map<TreeNode, Integer> depth;
    Map<TreeNode, TreeNode> father;

    private void walk(TreeNode root) {
        depth = new HashMap<>();
        father = new HashMap<>();

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        depth.put(root, 1);
        father.put(root, null);

        while (!queue.isEmpty()) {
            TreeNode p = queue.poll();
            if (p.left != null) {
                depth.put(p.left, 1 + depth.get(p));
                father.put(p.left, p);
                queue.add(p.left);
            }
            if (p.right != null) {
                depth.put(p.right, 1 + depth.get(p));
                father.put(p.right, p);
                queue.add(p.right);
            }
        }
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        walk(root);
        while (depth.get(p) > depth.get(q)) p = father.get(p);
        while (depth.get(p) < depth.get(q)) q = father.get(q);
        while (p != q) {
            p = father.get(p);
            q = father.get(q);
        }
        return p;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode answer, stdAnswer;

        TreeNode n7 = new TreeNode(7, null, null);
        TreeNode n4 = new TreeNode(4, null, null);
        TreeNode n6 = new TreeNode(6, null, null);
        TreeNode n2 = new TreeNode(2, n7, n4);
        TreeNode n0 = new TreeNode(0, null, null);
        TreeNode n8 = new TreeNode(8, null, null);
        TreeNode n5 = new TreeNode(5, n6, n2);
        TreeNode n1 = new TreeNode(1, n0, n8);
        TreeNode n3 = new TreeNode(3, n5, n1);

        stdAnswer = n3;
        answer = solution.lowestCommonAncestor(n3, n5, n1);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer.val, stdAnswer.val);

        stdAnswer = n5;
        answer = solution.lowestCommonAncestor(n3, n5, n4);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer.val, stdAnswer.val);

        n2 = new TreeNode(2, null, null);
        n1 = new TreeNode(1, n2, null);

        stdAnswer = n1;
        answer = solution.lowestCommonAncestor(n1, n1, n2);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer.val, stdAnswer.val);
    }
}