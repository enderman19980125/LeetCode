import java.util.*;

class Solution {
    private List<List<Integer>> ans;

    private void build(List<Integer> a, int p, int currentSum, int totalSum) {
        if (currentSum > totalSum) return;
        if (currentSum == totalSum && p == a.size()) {
            this.ans.add(new ArrayList<>(a));
            return;
        }
        if (p == a.size()) return;

        int s = 1;
        if (p != 0) s = a.get(p - 1) + 1;

        for (int k = s; k <= 9; k++) {
            a.set(p, k);
            this.build(a, p + 1, currentSum + k, totalSum);
        }
    }

    public List<List<Integer>> combinationSum3(int k, int n) {
        this.ans = new LinkedList<>();
        List<Integer> a = new ArrayList<>(Collections.nCopies(k, 0));
        build(a, 0, 0, n);
        return ans;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int k, n;
        List<List<Integer>> answer, stdAnswer;

        k = 3;
        n = 7;
        stdAnswer = new LinkedList<>();
        stdAnswer.add(new ArrayList<>(Arrays.asList(1, 2, 4)));
        answer = solution.combinationSum3(k, n);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        k = 3;
        n = 9;
        stdAnswer = new LinkedList<>();
        stdAnswer.add(new ArrayList<>(Arrays.asList(1, 2, 6)));
        stdAnswer.add(new ArrayList<>(Arrays.asList(1, 3, 5)));
        stdAnswer.add(new ArrayList<>(Arrays.asList(2, 3, 4)));
        answer = solution.combinationSum3(k, n);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        k = 4;
        n = 1;
        stdAnswer = new LinkedList<>();
        answer = solution.combinationSum3(k, n);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        k = 3;
        n = 2;
        stdAnswer = new LinkedList<>();
        answer = solution.combinationSum3(k, n);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        k = 9;
        n = 45;
        stdAnswer = new LinkedList<>();
        stdAnswer.add(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)));
        answer = solution.combinationSum3(k, n);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);

        k = 2;
        n = 18;
        stdAnswer = new LinkedList<>();
        answer = solution.combinationSum3(k, n);
        System.out.printf("%b %s %s\n", answer.equals(stdAnswer), answer, stdAnswer);
    }
}