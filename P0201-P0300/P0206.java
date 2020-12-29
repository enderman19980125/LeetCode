import java.util.ArrayList;
import java.util.Collections;

//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode pre = null, next;
        while (head != null) {
            next = head.next;
            head.next = pre;
            pre = head;
            head = next;
        }
        return pre;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode head, answer;
        ArrayList<Integer> nums = new ArrayList<>();

        Collections.addAll(nums, 1, 2, 3, 4, 5);
        head = arrayListToListNode(nums);
        answer = solution.reverseList(head);
        System.out.print(listNodeToString(answer));
        System.out.println(" [5,4,3,2,1]");
        nums.clear();

        head = arrayListToListNode(nums);
        answer = solution.reverseList(head);
        System.out.print(listNodeToString(answer));
        System.out.println(" []");
        nums.clear();

        Collections.addAll(nums, 1);
        head = arrayListToListNode(nums);
        answer = solution.reverseList(head);
        System.out.print(listNodeToString(answer));
        System.out.println(" [1]");
        nums.clear();

        Collections.addAll(nums, 1, 2);
        head = arrayListToListNode(nums);
        answer = solution.reverseList(head);
        System.out.print(listNodeToString(answer));
        System.out.println(" [2,1]");
        nums.clear();

        Collections.addAll(nums, 1, 2, 3);
        head = arrayListToListNode(nums);
        answer = solution.reverseList(head);
        System.out.print(listNodeToString(answer));
        System.out.println(" [3,2,1]");
        nums.clear();
    }

    private static ListNode arrayListToListNode(ArrayList<Integer> nums) {
        if (nums.isEmpty()) return null;
        ListNode[] nodes = new ListNode[nums.size()];
        for (int i = 0; i < nums.size(); ++i) nodes[i] = new ListNode(nums.get(i));
        for (int i = 0; i < nums.size() - 1; ++i) nodes[i].next = nodes[i + 1];
        return nodes[0];
    }

    private static String listNodeToString(ListNode head) {
        if (head == null) return "[]";
        StringBuilder ans = new StringBuilder("[");
        while (head != null) {
            ans.append(head.val).append(",");
            head = head.next;
        }
        ans.delete(ans.length() - 1, ans.length());
        ans.append("]");
        return ans.toString();
    }
}