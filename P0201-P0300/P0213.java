class Solution {
    public int rob(int[] nums) {
        int n = nums.length, ans;
        int[][] dp = new int[n][2];

        if (n == 1) return nums[0];

        dp[1][0] = nums[0];
        dp[1][1] = Integer.MIN_VALUE;
        for (int i = 2; i < n; ++i) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = dp[i - 1][0] + nums[i];
        }
        ans = dp[n - 1][0];

        dp[1][0] = 0;
        dp[1][1] = nums[1];
        for (int i = 2; i < n; ++i) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = dp[i - 1][0] + nums[i];
        }
        ans = Math.max(ans, Math.max(dp[n - 1][0], dp[n - 1][1]));

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums;
        int answer;

        nums = new int[]{1, 2, 3};
        answer = solution.rob(nums);
        System.out.printf("%d %d\n", answer, 3);

        nums = new int[]{1, 2, 3, 1};
        answer = solution.rob(nums);
        System.out.printf("%d %d\n", answer, 4);

        nums = new int[]{0};
        answer = solution.rob(nums);
        System.out.printf("%d %d\n", answer, 0);

        nums = new int[]{1, 2};
        answer = solution.rob(nums);
        System.out.printf("%d %d\n", answer, 2);

        nums = new int[]{2, 1};
        answer = solution.rob(nums);
        System.out.printf("%d %d\n", answer, 2);

        nums = new int[]{5, 1, 6};
        answer = solution.rob(nums);
        System.out.printf("%d %d\n", answer, 6);

        nums = new int[]{6, 1, 5};
        answer = solution.rob(nums);
        System.out.printf("%d %d\n", answer, 6);
    }
}