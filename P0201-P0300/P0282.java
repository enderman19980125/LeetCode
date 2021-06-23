import java.util.*;
import java.util.stream.Collectors;

class Solution {
    private long target;
    private final List<String> expressions = new LinkedList<>();

    public long eval(String expression) {
        Stack<Long> nums = new Stack<>();
        Stack<Character> ops = new Stack<>();

        for (int i = 0; i < expression.length(); ++i) {
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-' || expression.charAt(i) == '*') {
                ops.add(expression.charAt(i));
                continue;
            }

            int j = i;
            while (j + 1 < expression.length() && '0' <= expression.charAt(j + 1) && expression.charAt(j + 1) <= '9') ++j;
            long num = Long.parseLong(expression.substring(i, j + 1));
            nums.add(num);
            i = j;

            if (!ops.empty() && ops.peek() == '*') {
                ops.pop();
                nums.push(nums.pop() * nums.pop());
            }
            if (!ops.empty() && ops.peek() == '-') {
                ops.pop();
                ops.push('+');
                nums.push(-nums.pop());
            }
        }

        while (!ops.empty()) {
            ops.pop();
            nums.push(nums.pop() + nums.pop());
        }

        return nums.peek();
    }

    private void build(String expression, String num, String last) {
        if (num.isEmpty()) {
            if (eval(expression) == target) expressions.add(expression);
            return;
        }

        if (!last.equals("0")) {
            build(expression + num.charAt(0), num.substring(1), last + num.charAt(0));
        }

        if (!last.isEmpty()) {
            build(expression + "+" + num.charAt(0), num.substring(1), num.substring(0, 1));
            build(expression + "-" + num.charAt(0), num.substring(1), num.substring(0, 1));
            build(expression + "*" + num.charAt(0), num.substring(1), num.substring(0, 1));
        }
    }

    public List<String> addOperators(String num, int target) {
        this.target = target;
        this.expressions.clear();
        build("", num, "");
        return this.expressions;
    }
}

public class Main {
    private static boolean isEqual(List<String> list1, List<String> list2) {
        List<String> sortedList1 = list1.stream().sorted().collect(Collectors.toList());
        List<String> sortedList2 = list2.stream().sorted().collect(Collectors.toList());
        return sortedList1.equals(sortedList2);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> answer, stdAnswer;

        stdAnswer = List.of("1*2*3", "1+2+3");
        answer = solution.addOperators("123", 6);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = List.of("2*3+2", "2+3*2");
        answer = solution.addOperators("232", 8);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = List.of("1*0+5", "10-5");
        answer = solution.addOperators("105", 5);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = List.of("0*0", "0+0", "0-0");
        answer = solution.addOperators("00", 0);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = List.of();
        answer = solution.addOperators("3456237490", 9191);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = List.of("1+23-4-5", "1+2+3+4+5", "1-2*3+4*5", "1*2*3+4+5");
        answer = solution.addOperators("12345", 15);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = List.of("10*0+9", "1*0+0+9", "1*0-0+9", "1*0*0+9");
        answer = solution.addOperators("1009", 9);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);

        stdAnswer = List.of();
        answer = solution.addOperators("2147483648", -2147483648);
        System.out.printf("%b %s %s\n", isEqual(answer, stdAnswer), answer, stdAnswer);
    }
}