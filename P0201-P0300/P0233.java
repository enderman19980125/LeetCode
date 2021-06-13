class SolutionSearch {
    private int countNum(int n) {
        int num = 0;
        while (n > 0) {
            if (n % 10 == 1) ++num;
            n /= 10;
        }
        return num;
    }

    public int countDigitOne(int n) {
        int num = 0;
        for (int i = 0; i <= n; ++i) num += countNum(i);
        return num;
    }
}

class Solution {
    public int countDigitOne(int n) {
        if (n == 0) return 0;
        if (1 <= n && n <= 9) return 1;

        int m = 1;
        while (m * 10 <= n && m != 1000000000) m *= 10;
        int n0 = (int) (Math.log10(m) * m / 10);
        if (n == m) return n0 + 1;

        int k = n / m;
        if (k == 1) return n0 + (n - m + 1) + countDigitOne(n % m);
        return k * n0 + m + countDigitOne(n % m);
    }
}

public class Main {
    public static void main(String[] args) {
        // SolutionSearch solution = new SolutionSearch();
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 6;
        answer = solution.countDigitOne(13);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 0;
        answer = solution.countDigitOne(0);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 2;
        answer = solution.countDigitOne(10);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 21;
        answer = solution.countDigitOne(100);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 23;
        answer = solution.countDigitOne(101);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 57;
        answer = solution.countDigitOne(123);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 689;
        answer = solution.countDigitOne(1234);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 8121;
        answer = solution.countDigitOne(12345);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 93553;
        answer = solution.countDigitOne(123456);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 11824417;
        answer = solution.countDigitOne(12345678);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 2080000001;
        answer = solution.countDigitOne(1600000000);
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);
    }
}