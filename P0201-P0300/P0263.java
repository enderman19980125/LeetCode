class Solution {
    public boolean isUgly(int n) {
        if (n <= 0) return false;
        while (n % 2 == 0) n /= 2;
        while (n % 3 == 0) n /= 3;
        while (n % 5 == 0) n /= 5;
        return n == 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean answer, stdAnswer;

        stdAnswer = true;
        answer = solution.isUgly(6);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        answer = solution.isUgly(8);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = false;
        answer = solution.isUgly(14);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        answer = solution.isUgly(1);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}