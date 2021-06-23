class VersionControl {
    int bad;

    void setBad(int bad) {
        this.bad = bad;
    }

    boolean isBadVersion(int version) {
        return version >= bad;
    }
}

class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if (isBadVersion(1)) return 1;
        int l = 1, r = n;
        while (l + 1 < r) {
            int k = l + (r - l) / 2;
            if (isBadVersion(k))
                r = k;
            else
                l = k;
        }

        return r;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        solution.setBad(4);
        stdAnswer = 4;
        answer = solution.firstBadVersion(5);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        solution.setBad(1);
        stdAnswer = 1;
        answer = solution.firstBadVersion(1);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        solution.setBad(5);
        stdAnswer = 5;
        answer = solution.firstBadVersion(5);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);

        solution.setBad(1);
        stdAnswer = 1;
        answer = solution.firstBadVersion(5);
        System.out.printf("%b %s %s\n", answer == stdAnswer, answer, stdAnswer);
    }
}