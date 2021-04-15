import java.util.Set;
import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int num : nums) {
            if (s.contains(num)) return true;
            s.add(num);
        }
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums;
        boolean answer, stdAnswer;

        nums = new int[]{1, 2, 3, 1};
        stdAnswer = true;
        answer = solution.containsDuplicate(nums);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 2, 3, 4};
        stdAnswer = false;
        answer = solution.containsDuplicate(nums);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
        stdAnswer = true;
        answer = solution.containsDuplicate(nums);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}