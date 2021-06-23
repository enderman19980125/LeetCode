class Solution {
    private boolean isValid(int[] citations, int hIndex) {
        if (hIndex == 0) return true;
        if (hIndex > citations.length) return false;
        return citations[citations.length - hIndex] >= hIndex;
    }

    public int hIndex(int[] citations) {
        int l = 0, r = 1 + Math.min(citations.length, citations[citations.length - 1]);

        while (l + 1 < r) {
            int k = l + (r - l) / 2;
            if (isValid(citations, k))
                l = k;
            else
                r = k;
        }

        return l;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] citations;
        int answer, stdAnswer;

        citations = new int[]{0, 1, 3, 5, 6};
        stdAnswer = 3;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{1, 2, 100};
        stdAnswer = 2;
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

        citations = new int[]{5, 5, 5, 5, 5};
        stdAnswer = 5;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{1, 1, 2, 3, 4};
        stdAnswer = 2;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        citations = new int[]{1, 2, 3, 4, 5};
        stdAnswer = 3;
        answer = solution.hIndex(citations);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}