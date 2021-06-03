import java.util.*;

class Solution {
    public int calculate(String s) {
        Stack<Long> numST = new Stack<>();
        Stack<Character> opST = new Stack<>();

        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == ' ')
                continue;
            if (s.charAt(i) == '+' || s.charAt(i) == '-' || s.charAt(i) == '*' || s.charAt(i) == '/') {
                opST.add(s.charAt(i));
                continue;
            }
            int j = i;
            while (j + 1 < s.length() && '0' <= s.charAt(j + 1) && s.charAt(j + 1) <= '9') ++j;
            long val = Long.parseLong(s.substring(i, j + 1));
            numST.add(val);
            i = j;

            if (!opST.isEmpty() && opST.peek() == '-') {
                opST.pop();
                opST.push('+');
                numST.push(-numST.pop());
            }

            while (numST.size() >= 2 && (opST.peek() == '*' || opST.peek() == '/')) {
                long v2 = numST.pop(), v1 = numST.pop();
                char op = opST.pop();
                if (op == '*') val = v1 * v2;
                if (op == '/') val = v1 / v2;
                numST.push(val);
            }
        }

        while (numST.size() >= 2) numST.push(numST.pop() + numST.pop());

        return Integer.parseInt(numST.peek().toString());
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 7;
        answer = solution.calculate("3+2*2");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.calculate(" 3/2 ");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 5;
        answer = solution.calculate(" 3+5 / 2 ");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.calculate(" 1 ");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 0;
        answer = solution.calculate(" 1 + 2/3 - 1 ");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 42;
        answer = solution.calculate("42");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.calculate("1-1+1");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 98;
        answer = solution.calculate(" 1 - 10/3 + 10*10");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = -110;
        answer = solution.calculate(" -10 -10*10");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);
    }
}