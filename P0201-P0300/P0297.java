// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }

    TreeNode(int x, TreeNode l, TreeNode r) {
        val = x;
        left = l;
        right = r;
    }

    @Override
    public String toString() {
        return String.format("(%d,%s,%s)", val, left == null ? "" : left, right == null ? "" : right);
    }
}

class Codec {
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "()";
        return String.format("(%d,%s,%s)", root.val, serialize(root.left), serialize(root.right));
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("()")) return null;

        int left = 1, right = 1;
        while (data.charAt(right) == '-' || ('0' <= data.charAt(right) && data.charAt(right) <= '9')) ++right;
        int val = Integer.parseInt(data.substring(left, right));
        TreeNode cntNode = new TreeNode(val);

        left = right + 1;
        int k = 0;
        do {
            ++right;
            if (data.charAt(right) == '(') ++k;
            if (data.charAt(right) == ')') --k;
        } while (k > 0);
        ++right;
        cntNode.left = deserialize(data.substring(left, right));

        left = right + 1;
        k = 0;
        do {
            ++right;
            if (data.charAt(right) == ')') --k;
            if (data.charAt(right) == '(') ++k;
        } while (k > 0);
        ++right;
        cntNode.right = deserialize(data.substring(left, right));

        return cntNode;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));

public class Main {
    public static void main(String[] args) {
        String answer, stdAnswer;
        Codec codec = new Codec();
        TreeNode n1, n2, n3, n4, n5;

        n4 = new TreeNode(4, null, null);
        n5 = new TreeNode(5, null, null);
        n2 = new TreeNode(2, null, null);
        n3 = new TreeNode(3, n4, n5);
        n1 = new TreeNode(1, n2, n3);
        stdAnswer = n1.toString();
        answer = codec.deserialize(codec.serialize(n1)).toString();
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "";
        answer = codec.deserialize(codec.serialize(null)) == null ? "" : " ";
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        n1 = new TreeNode(1, null, null);
        stdAnswer = n1.toString();
        answer = codec.deserialize(codec.serialize(n1)).toString();
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        n2 = new TreeNode(2, null, null);
        n1 = new TreeNode(1, n2, null);
        stdAnswer = n1.toString();
        answer = codec.deserialize(codec.serialize(n1)).toString();
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        n1 = new TreeNode(-1, null, null);
        stdAnswer = n1.toString();
        answer = codec.deserialize(codec.serialize(n1)).toString();
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);
    }
}