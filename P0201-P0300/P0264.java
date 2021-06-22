import java.util.*;

class Solution {
    public int nthUglyNumber(int n) {
        long[] p2 = new long[32];
        long[] p3 = new long[21];
        long[] p5 = new long[15];
        p2[0] = 1;
        p3[0] = 1;
        p5[0] = 1;
        for (int i = 1; i <= 31; ++i) p2[i] = 2 * p2[i - 1];
        for (int i = 1; i <= 20; ++i) p3[i] = 3 * p3[i - 1];
        for (int i = 1; i <= 14; ++i) p5[i] = 5 * p5[i - 1];

        Set<Integer> nums = new TreeSet<>();

        for (int i2 = 0; i2 <= 31; ++i2) {
            for (int i3 = 0; i3 <= 20; ++i3) {
                if (p2[i2] * p3[i3] > Integer.MAX_VALUE) break;
                for (int i5 = 0; i5 <= 14; ++i5) {
                    long num = p2[i2] * p3[i3] * p5[i5];
                    if (num > Integer.MAX_VALUE) break;
                    nums.add((int) num);
                }
            }
        }

        int k = 0;
        for (Integer num : nums) {
            ++k;
            if (k == n) return num;
        }

        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 12;
        answer = solution.nthUglyNumber(10);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.nthUglyNumber(1);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 2123366400;
        answer = solution.nthUglyNumber(1690);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}