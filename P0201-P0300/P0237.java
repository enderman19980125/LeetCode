import java.util.*;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}

public class Main {
    private static List<ListNode> generateLinkedList(int[] nums) {
        List<ListNode> list = new LinkedList<>();
        if (nums.length == 0) return list;
        for (int i = 0; i < nums.length; ++i) {
            list.add(new ListNode(nums[i]));
            if (i != 0) list.get(i - 1).next = list.get(i);
        }
        return list;
    }

    private static String toString(List<ListNode> list) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("[");
        ListNode node = list.get(0);
        while (node != null) {
            stringBuilder.append(node.val).append(",");
            node = node.next;
        }
        stringBuilder.append("]");
        return stringBuilder.toString();
    }

    private static boolean isSameValue(List<ListNode> list1, List<ListNode> list2) {
        ListNode node1 = list1.get(0), node2 = list2.get(0);
        while (true) {
            if (node1 == null && node2 != null) return false;
            if (node1 != null && node2 == null) return false;
            if (node1 == null) return true;
            if (node1.val != node2.val) return false;
            node1 = node1.next;
            node2 = node2.next;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<ListNode> answer, stdAnswer;

        answer = generateLinkedList(new int[]{4, 5, 1, 9});
        stdAnswer = generateLinkedList(new int[]{4, 1, 9});
        solution.deleteNode(answer.get(1));
        System.out.printf("%b %s %s\n", isSameValue(answer, stdAnswer), toString(answer), toString(stdAnswer));

        answer = generateLinkedList(new int[]{4, 5, 1, 9});
        stdAnswer = generateLinkedList(new int[]{4, 5, 9});
        solution.deleteNode(answer.get(2));
        System.out.printf("%b %s %s\n", isSameValue(answer, stdAnswer), toString(answer), toString(stdAnswer));

        answer = generateLinkedList(new int[]{1, 2, 3, 4});
        stdAnswer = generateLinkedList(new int[]{1, 2, 4});
        solution.deleteNode(answer.get(2));
        System.out.printf("%b %s %s\n", isSameValue(answer, stdAnswer), toString(answer), toString(stdAnswer));

        answer = generateLinkedList(new int[]{0, 1});
        stdAnswer = generateLinkedList(new int[]{1});
        solution.deleteNode(answer.get(0));
        System.out.printf("%b %s %s\n", isSameValue(answer, stdAnswer), toString(answer), toString(stdAnswer));

        answer = generateLinkedList(new int[]{-3, 5, -99});
        stdAnswer = generateLinkedList(new int[]{5, -99});
        solution.deleteNode(answer.get(0));
        System.out.printf("%b %s %s\n", isSameValue(answer, stdAnswer), toString(answer), toString(stdAnswer));
    }
}