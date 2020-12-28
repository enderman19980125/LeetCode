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
    public ListNode removeElements(ListNode head, int val) {
        ListNode root = new ListNode(0);
        root.next = head;

        ListNode pre = root, cnt = head;
        while (cnt != null) {
            if (cnt.val == val)
                pre.next = cnt.next;
            else
                pre = cnt;
            cnt = cnt.next;
        }

        return root.next;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode head, answer;
        ArrayList<Integer> nums = new ArrayList<>();

        Collections.addAll(nums, 1, 2, 6, 3, 4, 5, 6);
        head = arrayListToListNode(nums);
        answer = solution.removeElements(head, 6);
        System.out.print(listNodeToString(answer));
        System.out.println(" [1,2,3,4,5]");
        nums.clear();

        Collections.addAll(nums, 6, 6, 6);
        head = arrayListToListNode(nums);
        answer = solution.removeElements(head, 6);
        System.out.print(listNodeToString(answer));
        System.out.println(" []");
        nums.clear();

        head = arrayListToListNode(nums);
        answer = solution.removeElements(head, 6);
        System.out.print(listNodeToString(answer));
        System.out.println(" []");
        nums.clear();

        Collections.addAll(nums, 6);
        head = arrayListToListNode(nums);
        answer = solution.removeElements(head, 6);
        System.out.print(listNodeToString(answer));
        System.out.println(" []");
        nums.clear();

        Collections.addAll(nums, 6, 1, 6);
        head = arrayListToListNode(nums);
        answer = solution.removeElements(head, 6);
        System.out.print(listNodeToString(answer));
        System.out.println(" [1]");
        nums.clear();

        Collections.addAll(nums, 1, 6, 6, 2, 6, 6, 3);
        head = arrayListToListNode(nums);
        answer = solution.removeElements(head, 6);
        System.out.print(listNodeToString(answer));
        System.out.println(" [1,2,3]");
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