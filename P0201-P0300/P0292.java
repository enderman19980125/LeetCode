class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean answer, stdAnswer;

        stdAnswer = false;
        answer = solution.canWinNim(4);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        answer = solution.canWinNim(1);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = true;
        answer = solution.canWinNim(2);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}