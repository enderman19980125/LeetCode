import java.util.*;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        List<Integer> a = new ArrayList<>();

        while (head != null) {
            a.add(head.val);
            head = head.next;
        }

        for (int i = 0; i < a.size() - 1 - i; ++i)
            if (!Objects.equals(a.get(i), a.get(a.size() - 1 - i)))
                return false;

        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode n1, n2, n3, n4;
        boolean answer, stdAnswer;

        n4 = new ListNode(1, null);
        n3 = new ListNode(2, n4);
        n2 = new ListNode(2, n3);
        n1 = new ListNode(1, n2);
        stdAnswer = true;
        answer = solution.isPalindrome(n1);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        n2 = new ListNode(2, null);
        n1 = new ListNode(1, n2);
        stdAnswer = false;
        answer = solution.isPalindrome(n1);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        n1 = new ListNode(1, null);
        stdAnswer = true;
        answer = solution.isPalindrome(n1);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);
    }
}