import java.util.Arrays;

class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);

        int n = citations.length, i = n - 1, k = citations[i];
        while (k >= 0) {
            while (i > 0 && citations[i - 1] >= k) --i;
            if (n - i >= k) break;
            --k;
        }

        return k;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] citations;
        int answer, stdAnswer;

        citations = new int[]{3, 0, 6, 1, 5};
        stdAnswer = 3;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{1, 3, 1};
        stdAnswer = 1;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{3, 3, 1, 1, 1};
        stdAnswer = 2;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{4, 4, 4, 1, 1, 1};
        stdAnswer = 3;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{0};
        stdAnswer = 0;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{1};
        stdAnswer = 1;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{2};
        stdAnswer = 1;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}