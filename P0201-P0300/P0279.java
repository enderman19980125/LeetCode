class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= 100 && i * i <= n; ++i) dp[i * i] = 1;

        for (int i = 1; i <= n; ++i) {
            if (dp[i] > 0) continue;
            dp[i] = Integer.MAX_VALUE;
            for (int j = 1; i - j * j >= 1; --j)
                dp[i] = Math.min(dp[i], 1 + dp[i - j * j]);
        }

        return dp[n];
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 3;
        answer = solution.numSquares(12);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 2;
        answer = solution.numSquares(13);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.numSquares(1);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 3;
        answer = solution.numSquares(3);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 3;
        answer = solution.numSquares(6);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.numSquares(10000);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 3;
        answer = solution.numSquares(99);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}