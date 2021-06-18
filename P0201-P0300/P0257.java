import java.util.*;
import java.util.stream.Collectors;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new LinkedList<>();

        if (root.left == null && root.right == null) {
            paths.add(String.valueOf(root.val));
            return paths;
        }

        if (root.left != null) {
            List<String> leftPaths = binaryTreePaths(root.left);
            for (String leftPath : leftPaths) paths.add(String.format("%d->%s", root.val, leftPath));
        }

        if (root.right != null) {
            List<String> rightPaths = binaryTreePaths(root.right);
            for (String rightPath : rightPaths) paths.add(String.format("%d->%s", root.val, rightPath));
        }

        return paths;
    }
}

public class Main {
    private static boolean isEqual(List<String> list1, List<String> list2) {
        List<String> sortedList1 = list1.stream().sorted().collect(Collectors.toList());
        List<String> sortedList2 = list2.stream().sorted().collect(Collectors.toList());
        return sortedList1.equals(sortedList2);
    }

    public static void main(String[] args) {
        TreeNode n1, n2, n3, n5;
        Solution solution = new Solution();
        List<String> answer, stdAnswer;

        n5 = new TreeNode(5, null, null);
        n2 = new TreeNode(2, null, n5);
        n3 = new TreeNode(3, null, null);
        n1 = new TreeNode(1, n2, n3);
        stdAnswer = List.of("1->2->5", "1->3");
        answer = solution.binaryTreePaths(n1);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        n1 = new TreeNode(1, null, null);
        stdAnswer = List.of("1");
        answer = solution.binaryTreePaths(n1);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);
    }
}