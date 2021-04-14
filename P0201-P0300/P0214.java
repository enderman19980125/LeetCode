class Solution {
    public String shortestPalindrome(String s) {
        s = new StringBuilder(s).reverse().toString();

        char[] a = new char[s.length() * 2 + 3];
        a[0] = '^';
        a[s.length() * 2 + 2] = '$';
        for (int i = 1; i < a.length - 1; i++) a[i] = '#';
        for (int i = 0; i < s.length(); i++) a[2 * i + 2] = s.charAt(i);

        int[] p = new int[a.length];
        int C = 0, R = 0;
        for (int i = 1; i < a.length - 1; i++) {
            int mirrorI = 2 * C - i;
            if (i < R)
                p[i] = Math.min(p[mirrorI], R - i);
            else
                p[i] = 0;
            while (a[i - p[i] - 1] == a[i + p[i] + 1]) p[i]++;
            if (i + p[i] > R) {
                R = i + p[i];
                C = i;
            }
        }

        int[] q = new int[s.length() * 2 + 3];
        for (int i = 0; i < q.length; i++) q[i] = q.length - 2 - i;

        String appendStr = "";
        for (int i = 0; i < q.length; i++)
            if (p[i] == q[i]) {
                appendStr = s.substring(0, (i - p[i]) / 2);
                break;
            }

        s = new StringBuilder(s).reverse().toString();
        s = appendStr + s;
        return s;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String s, answer, stdAnswer;

        s = "aacecaaa";
        stdAnswer = "aaacecaaa";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "abcd";
        stdAnswer = "dcbabcd";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "";
        stdAnswer = "";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "a";
        stdAnswer = "a";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "aa";
        stdAnswer = "aa";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "ab";
        stdAnswer = "bab";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "aaa";
        stdAnswer = "aaa";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "aab";
        stdAnswer = "baab";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "abb";
        stdAnswer = "bbabb";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "abac";
        stdAnswer = "cabac";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        s = "abadabc";
        stdAnswer = "cbadabadabc";
        answer = solution.shortestPalindrome(s);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);
    }
}