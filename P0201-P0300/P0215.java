import java.util.Arrays;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        Integer[] numbers = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(numbers, (i1, i2) -> (i2 - i1));
        return numbers[k - 1];
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums;
        int k, answer, stdAnswer;

        nums = new int[]{3, 2, 1, 5, 6, 4};
        k = 2;
        stdAnswer = 5;
        answer = solution.findKthLargest(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{3, 2, 3, 1, 2, 4, 5, 5, 6};
        k = 4;
        stdAnswer = 4;
        answer = solution.findKthLargest(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1};
        k = 1;
        stdAnswer = 1;
        answer = solution.findKthLargest(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 1};
        k = 1;
        stdAnswer = 1;
        answer = solution.findKthLargest(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 1};
        k = 2;
        stdAnswer = 1;
        answer = solution.findKthLargest(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 1, 2};
        k = 1;
        stdAnswer = 2;
        answer = solution.findKthLargest(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        nums = new int[]{1, 1, 2};
        k = 2;
        stdAnswer = 1;
        answer = solution.findKthLargest(nums, k);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}