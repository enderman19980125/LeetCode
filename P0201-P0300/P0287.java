class Solution {
    private int findBit(int[] nums, int k, int extraStart, int extraEnd) {
        int v = 1;
        for (int i = 1; i < k; ++i) v *= 10;

        int[] bins = new int[10];
        for (int num : nums) {
            int bit = num % (v * 10) / v;
            ++bins[bit];
        }

        for (int num = extraStart; num <= extraEnd; ++num) {
            int bit = num % (v * 10) / v;
            ++bins[bit];
        }

        int bit = 0;
        for (int i = 0; i < 10; ++i) if (bins[i] > bins[bit]) bit = i;

        return bit;
    }

    public int findDuplicate(int[] nums) {
        int extraStart = nums.length;
        int extraEnd = (int) (Math.pow(10, 1 + (int) Math.log10(extraStart)) - 1);

        int ans = 0;
        for (int k = 1 + (int) Math.log10(nums.length); k >= 1; --k)
            ans = ans * 10 + findBit(nums, k, extraStart, extraEnd);
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 2;
        answer = solution.findDuplicate(new int[]{1, 3, 4, 2, 2});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 3;
        answer = solution.findDuplicate(new int[]{3, 1, 3, 4, 2});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.findDuplicate(new int[]{1, 1});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.findDuplicate(new int[]{1, 1, 2});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.findDuplicate(new int[]{1, 1, 2});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 9;
        answer = solution.findDuplicate(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 9});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 10;
        answer = solution.findDuplicate(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 12;
        answer = solution.findDuplicate(new int[]{1, 12, 3, 4, 5, 6, 7, 8, 9, 12, 12, 12, 12});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}