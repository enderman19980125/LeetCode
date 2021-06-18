import java.util.*;
import java.util.stream.Collectors;

class Solution {
    private List<Integer> merge(List<Integer> ans1, List<Integer> ans2, char op) {
        List<Integer> ans = new LinkedList<>();
        for (int a1 : ans1)
            for (int a2 : ans2) {
                if (op == '+') ans.add(a1 + a2);
                if (op == '-') ans.add(a1 - a2);
                if (op == '*') ans.add(a1 * a2);
            }
        return ans;
    }

    public List<Integer> diffWaysToCompute(String expression) {
        List<Integer> ans = new LinkedList<>();

        try {
            ans.add(Integer.parseInt(expression));
            return ans;
        } catch (NumberFormatException ignored) {
        }

        for (int i = 0; i < expression.length(); ++i)
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-' || expression.charAt(i) == '*') {
                List<Integer> ans1 = diffWaysToCompute(expression.substring(0, i));
                List<Integer> ans2 = diffWaysToCompute(expression.substring(i + 1));
                ans.addAll(merge(ans1, ans2, expression.charAt(i)));
            }

        return ans;
    }
}

public class Main {
    private static boolean isEqual(List<Integer> list1, List<Integer> list2) {
        List<Integer> sortedList1 = list1.stream().sorted().collect(Collectors.toList());
        List<Integer> sortedList2 = list2.stream().sorted().collect(Collectors.toList());
        return sortedList1.equals(sortedList2);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> answer, stdAnswer;

        stdAnswer = Arrays.asList(0, 2);
        answer = solution.diffWaysToCompute("2-1-1");
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = Arrays.asList(-34, -14, -10, -10, 10);
        answer = solution.diffWaysToCompute("2*3-4*5");
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = Collections.singletonList(2);
        answer = solution.diffWaysToCompute("1+1");
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);
    }
}