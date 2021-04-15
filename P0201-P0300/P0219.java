import java.util.*;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int value = nums[i];
            if (m.containsKey(value) && i - m.get(value) <= k) return true;
            m.put(value, i);
        }
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums;
        int k;
        boolean answer, stdAnswer;

        nums = new int[]{1, 2, 3, 1};
        k = 3;
        stdAnswer = true;
        answer = solution.containsNearbyDuplicate(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 0, 1, 1};
        k = 1;
        stdAnswer = true;
        answer = solution.containsNearbyDuplicate(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 2, 3, 1, 2, 3};
        k = 2;
        stdAnswer = false;
        answer = solution.containsNearbyDuplicate(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}