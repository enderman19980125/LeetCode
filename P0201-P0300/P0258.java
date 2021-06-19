class Solution {
    public int addDigits(int num) {
        if (num <= 9) return num;
        return (num - 10) % 9 + 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 2;
        answer = solution.addDigits(38);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 0;
        answer = solution.addDigits(0);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.addDigits(1);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 5;
        answer = solution.addDigits(5);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 9;
        answer = solution.addDigits(9);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.addDigits(100);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 9;
        answer = solution.addDigits(999);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.addDigits(Integer.MAX_VALUE);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}