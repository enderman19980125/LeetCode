import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new LinkedList<>();
        int[] ans = new int[nums.length - k + 1];

        for (int i = 0; i < nums.length; ++i) {
            if (!q.isEmpty() && q.peekFirst() < i - k + 1) q.pollFirst();
            while (!q.isEmpty() && nums[q.peekLast()] <= nums[i]) q.pollLast();
            q.addLast(i);
            if (!q.isEmpty() && i >= k - 1) ans[i - k + 1] = nums[q.peekFirst()];
        }

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] answer, stdAnswer;

        stdAnswer = new int[]{3, 3, 5, 5, 6, 7};
        answer = solution.maxSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{1};
        answer = solution.maxSlidingWindow(new int[]{1}, 1);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{1, -1};
        answer = solution.maxSlidingWindow(new int[]{1, -1}, 1);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{11};
        answer = solution.maxSlidingWindow(new int[]{9, 11}, 2);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{4};
        answer = solution.maxSlidingWindow(new int[]{4, -2}, 2);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{3, 4, 5, 5, 5, 4, 3};
        answer = solution.maxSlidingWindow(new int[]{1, 2, 3, 4, 5, 4, 3, 2, 1}, 3);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));
    }
}