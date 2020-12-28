class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int[] A = new int[31];
        int[] B = new int[31];

        for (int i = 0; i < 31; i++) {
            A[30 - i] = m & 1;
            m >>= 1;
            B[30 - i] = n & 1;
            n >>= 1;
        }

        int s = 0;
        while (s <= 30 && A[s] == 0 && B[s] == 0) s++;
        int t = s - 1;
        while (t + 1 <= 30 && A[t + 1] == B[t + 1]) t++;

        int ans = 0;
        for (int i = s; i <= t; ++i) ans = (ans << 1) + A[i];
        for (int i = t + 1; i <= 30; ++i) ans <<= 1;

        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer;

        answer = solution.rangeBitwiseAnd(5, 7);
        System.out.printf("%d %d\n", answer, 4);

        answer = solution.rangeBitwiseAnd(0, 1);
        System.out.printf("%d %d\n", answer, 0);

        answer = solution.rangeBitwiseAnd(12, 13);
        System.out.printf("%d %d\n", answer, 12);

        answer = solution.rangeBitwiseAnd(128, 160);
        System.out.printf("%d %d\n", answer, 128);

        answer = solution.rangeBitwiseAnd(0, 2147483647);
        System.out.printf("%d %d\n", answer, 0);

        answer = solution.rangeBitwiseAnd(0, 0);
        System.out.printf("%d %d\n", answer, 0);

        answer = solution.rangeBitwiseAnd(2147483647, 2147483647);
        System.out.printf("%d %d\n", answer, 2147483647);
    }
}