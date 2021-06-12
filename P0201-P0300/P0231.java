class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) return false;
        while ((n & 1) == 0) n >>= 1;
        return n == 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean answer, stdAnswer;

        stdAnswer = true;
        answer = solution.isPowerOfTwo(1);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        answer = solution.isPowerOfTwo(16);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.isPowerOfTwo(3);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        answer = solution.isPowerOfTwo(4);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.isPowerOfTwo(5);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.isPowerOfTwo(0);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.isPowerOfTwo(-1);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        answer = solution.isPowerOfTwo(2);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.isPowerOfTwo(Integer.MAX_VALUE);
        System.out.printf("%b %b %b\n", answer == stdAnswer, answer, stdAnswer);
    }
}