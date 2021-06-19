import java.util.*;

class Solution {
    private int p = -1;
    private final int[] ans = new int[2];

    public void singleNumber(int[] nums, int l, int r) {
        if (l == r) {
            ans[++p] = nums[l];
            return;
        }

        if (l + 1 == r) {
            if (nums[l] == nums[r]) return;
            ans[++p] = nums[l];
            ans[++p] = nums[r];
            return;
        }

        int i = l, j = r, value = nums[l + new Random().nextInt(r - l + 1)];
        while (i < j) {
            while (i < j && nums[i] <= value) ++i;
            while (i < j && value < nums[j]) --j;
            int t = nums[i];
            nums[i] = nums[j];
            nums[j] = t;
        }

        if (value < nums[i]) --i;
        if (nums[j] < value) ++j;

        if (l <= i) {
            int xor = 0;
            for (int k = l; k <= i; ++k) xor ^= nums[k];
            if (xor != 0 && nums[i] <= value) singleNumber(nums, l, i);
        }

        if (j <= r) {
            int xor = 0;
            for (int k = j; k <= r; ++k) xor ^= nums[k];
            if (xor != 0 && value < nums[j]) singleNumber(nums, j, r);
        }
    }

    public int[] singleNumber(int[] nums) {
        p = -1;
        singleNumber(nums, 0, nums.length - 1);
        return ans;
    }
}

class SolutionBit {
    public int[] singleNumber(int[] nums) {
        int xor = 0, low = 1, a = 0, b = 0;
        for (int num : nums) xor ^= num;
        while ((low & xor) == 0) low <<= 1;
        for (int num : nums) if ((num & low) == 0) a ^= num; else b ^= num;
        return new int[]{a, b};
    }
}

public class Main {
    private static boolean isEqual(int[] a1, int[] a2) {
        Arrays.sort(a1);
        Arrays.sort(a2);
        return Arrays.equals(a1, a2);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] answer, stdAnswer;

        stdAnswer = new int[]{3, 5};
        answer = solution.singleNumber(new int[]{1, 2, 1, 3, 2, 5});
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{-1, 0};
        answer = solution.singleNumber(new int[]{-1, 0});
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{1, 0};
        answer = solution.singleNumber(new int[]{0, 1});
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{1, 2};
        answer = solution.singleNumber(new int[]{0, 0, 1, 2});
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{3, 5};
        answer = solution.singleNumber(new int[]{1, 2, 3, 4, 6, 7, 8, 9, 1, 2, 4, 5, 6, 7, 8, 9});
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{3, 5};
        answer = solution.singleNumber(new int[]{9, 8, 7, 6, 4, 3, 2, 1, 1, 2, 4, 5, 6, 7, 8, 9});
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{3, 5};
        answer = solution.singleNumber(new int[]{1, 2, 3, 4, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 2, 1});
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        stdAnswer = new int[]{3, 5};
        answer = solution.singleNumber(new int[]{4, 6, 6, 5, 1, 2, 3, 4, 2, 1, 7, 8, 9, 9, 8, 7});
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));
    }
}