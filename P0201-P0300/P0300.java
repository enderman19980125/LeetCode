class Solution {
    public int lengthOfLIS(int[] nums) {
        int s = 0;
        int[] dp = new int[2501];
        dp[0] = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num > dp[s]) dp[++s] = num;
            for (int j = 1; j <= s; ++j)
                if (dp[j - 1] < num && num < dp[j])
                    dp[j] = num;
        }
        return s;
    }
}

class SolutionBinary {
    public int lengthOfLIS(int[] nums) {
        int s = 0;
        int[] dp = new int[2501];
        dp[0] = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num > dp[s]) {
                dp[++s] = num;
                continue;
            }
            int left = 0, right = s;
            while (left + 1 < right) {
                int mid = left + (right - left) / 2;
                if (num <= dp[mid])
                    right = mid;
                else
                    left = mid;
            }
            dp[left + 1] = num;
        }
        return s;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 4;
        answer = solution.lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 4;
        answer = solution.lengthOfLIS(new int[]{0, 1, 0, 3, 2, 3});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.lengthOfLIS(new int[]{7, 7, 7, 7, 7, 7, 7});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 6;
        answer = solution.lengthOfLIS(new int[]{1, 11, 2, 12, 3, 13, 4, 14, 5, 15});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 6;
        answer = solution.lengthOfLIS(new int[]{1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6});
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}