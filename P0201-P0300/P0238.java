import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        ans[0] = nums[0];
        for (int i = 1; i < nums.length; ++i) ans[i] = ans[i - 1] * nums[i];

        int m = nums[nums.length - 1];
        ans[nums.length - 1] = ans[nums.length - 2];
        for (int i = nums.length - 2; i >= 1; --i) {
            ans[i] = ans[i - 1] * m;
            m *= nums[i];
        }
        ans[0] = m;

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] answer, stdAnswer;

        stdAnswer = new int[]{24, 12, 8, 6};
        answer = solution.productExceptSelf(new int[]{1, 2, 3, 4});
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{0, 0, 9, 0, 0};
        answer = solution.productExceptSelf(new int[]{-1, 1, 0, -3, 3});
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{4, 3};
        answer = solution.productExceptSelf(new int[]{3, 4});
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));
    }
}