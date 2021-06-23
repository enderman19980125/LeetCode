class Solution {
    public String getHint(String secret, String guess) {
        int A = 0, B = 0;
        for (int i = 0; i < secret.length(); ++i) if (secret.charAt(i) == guess.charAt(i)) ++A;

        int[] secretNum = new int[10];
        int[] guessNum = new int[10];
        for (int i = 0; i < secret.length(); ++i) ++secretNum[secret.charAt(i) - '0'];
        for (int i = 0; i < guess.length(); ++i) ++guessNum[guess.charAt(i) - '0'];
        for (int i = 0; i < 10; ++i) B += Math.min(secretNum[i], guessNum[i]);
        B -= A;

        return String.format("%dA%dB", A, B);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String answer, stdAnswer;

        stdAnswer = "1A3B";
        answer = solution.getHint("1807", "7810");
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "1A1B";
        answer = solution.getHint("1123", "0111");
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "0A0B";
        answer = solution.getHint("1", "0");
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "1A0B";
        answer = solution.getHint("1", "1");
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        stdAnswer = "3A3B";
        answer = solution.getHint("112233", "122331");
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);
    }
}