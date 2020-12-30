import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int n = nums.length;
        int p1 = 0, p2 = 0;
        int sum = 0, ans = Integer.MAX_VALUE;

        while (p2 < n) {
            sum += nums[p2];
            while (p1 < p2 && sum - nums[p1] >= s) {
                sum -= nums[p1];
                p1++;
            }
            if (sum >= s) ans = Math.min(ans, p2 - p1 + 1);
            p2++;
        }

        if (ans == Integer.MAX_VALUE)
            return 0;
        else
            return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        ArrayList<Integer> nums = new ArrayList<>();
        int answer;

        Collections.addAll(nums, 2, 3, 1, 2, 4, 3);
        answer = solution.minSubArrayLen(7, arrayToIntArray(nums));
        System.out.printf("%d %d\n", answer, 2);
        nums.clear();

        answer = solution.minSubArrayLen(1, arrayToIntArray(nums));
        System.out.printf("%d %d\n", answer, 0);
        nums.clear();

        Collections.addAll(nums, 1);
        answer = solution.minSubArrayLen(1, arrayToIntArray(nums));
        System.out.printf("%d %d\n", answer, 1);
        nums.clear();

        Collections.addAll(nums, 1);
        answer = solution.minSubArrayLen(2, arrayToIntArray(nums));
        System.out.printf("%d %d\n", answer, 0);
        nums.clear();

        Collections.addAll(nums, 1, 2, 3, 4, 5, 4, 3, 2, 1);
        answer = solution.minSubArrayLen(5, arrayToIntArray(nums));
        System.out.printf("%d %d\n", answer, 1);
        nums.clear();

        Collections.addAll(nums, 1, 2, 3, 4, 5, 4, 3, 2, 1);
        answer = solution.minSubArrayLen(25, arrayToIntArray(nums));
        System.out.printf("%d %d\n", answer, 9);
        nums.clear();

        Collections.addAll(nums, 1, 2, 3, 4, 5, 4, 3, 2, 1);
        answer = solution.minSubArrayLen(26, arrayToIntArray(nums));
        System.out.printf("%d %d\n", answer, 0);
        nums.clear();
    }

    private static int[] arrayToIntArray(ArrayList<Integer> nums) {
        int n = nums.size();
        int[] a = new int[n];
        for (int i = 0; i < n; ++i) a[i] = nums.get(i);
        return a;
    }
}