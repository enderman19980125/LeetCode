import java.util.*;

class Solution {
    public void moveZeroes(int[] nums) {
        int k = -1;
        for (int i = 0; i < nums.length; ++i)
            if (nums[i] != 0) nums[++k] = nums[i];
        for (int i = k + 1; i < nums.length; ++i)
            nums[i] = 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] answer, stdAnswer;

        answer = new int[]{0, 1, 0, 3, 12};
        stdAnswer = new int[]{1, 3, 12, 0, 0};
        solution.moveZeroes(answer);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        answer = new int[]{0};
        stdAnswer = new int[]{0};
        solution.moveZeroes(answer);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        answer = new int[]{0, 0};
        stdAnswer = new int[]{0, 0};
        solution.moveZeroes(answer);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        answer = new int[]{0, 0, 0};
        stdAnswer = new int[]{0, 0, 0};
        solution.moveZeroes(answer);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        answer = new int[]{1, 0, 0};
        stdAnswer = new int[]{1, 0, 0};
        solution.moveZeroes(answer);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        answer = new int[]{0, 1, 0};
        stdAnswer = new int[]{1, 0, 0};
        solution.moveZeroes(answer);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        answer = new int[]{0, 0, 1};
        stdAnswer = new int[]{1, 0, 0};
        solution.moveZeroes(answer);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));

        answer = new int[]{1, 2, 3};
        stdAnswer = new int[]{1, 2, 3};
        solution.moveZeroes(answer);
        System.out.printf("%b %s %s\n", Arrays.equals(answer, stdAnswer), Arrays.toString(answer), Arrays.toString(stdAnswer));
    }
}