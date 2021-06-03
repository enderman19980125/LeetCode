import java.util.*;

class Solution {
    private boolean isDigit(String s) {
        return s.length() != 1 || !"+-()".contains(s);
    }

    public int calculate(String s) {
        Stack<String> chain = new Stack<>();
        for (int i = 0; i < s.length(); ++i) {
            String v = s.substring(i, i + 1);
            if (" ".equals(v))
                continue;
            if ("+-()".contains(v)) {
                chain.add(v);
                continue;
            }
            int j = i;
            while (j + 1 < s.length() && '0' <= s.charAt(j + 1) && s.charAt(j + 1) <= '9') ++j;
            chain.add(s.substring(i, j + 1));
            i = j;
        }

        Stack<String> st = new Stack<>();

        for (String e : chain) {
            if (isDigit(e)) {
                int val = Integer.parseInt(e);
                while (!st.empty() && "+-".contains(st.peek())) {
                    String op = st.pop();
                    if ("-".equals(op)) val = -val;
                }
                if (!st.empty() && isDigit(st.peek()))
                    val += Integer.parseInt(st.pop());
                st.push(Integer.toString(val));
                continue;
            }
            if (")".equals(e)) {
                int val = Integer.parseInt(st.pop());
                st.pop();
                if (!st.empty() && "+-".contains(st.peek())) {
                    String op = st.pop();
                    int val2 = 0;
                    if (!st.empty() && isDigit(st.peek())) val2 = Integer.parseInt(st.pop());
                    if ("+".equals(op)) val = val2 + val;
                    if ("-".equals(op)) val = val2 - val;
                }
                st.push(Integer.toString(val));
                continue;
            }
            st.push(e);
        }

        return Integer.parseInt(st.peek());
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int answer, stdAnswer;

        stdAnswer = 2;
        answer = solution.calculate("1 + 1");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 3;
        answer = solution.calculate(" 2-1 + 2 ");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 23;
        answer = solution.calculate("(1+(4+5+2)-3)+(6+8)");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 0;
        answer = solution.calculate("+48 + -48");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.calculate("+1 + -1 - -1");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = 1;
        answer = solution.calculate("+1");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = -1;
        answer = solution.calculate("-1");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = -12;
        answer = solution.calculate("- (3 + (4 + 5))");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);

        stdAnswer = -1;
        answer = solution.calculate("- ( - (-1))");
        System.out.printf("%b %d %d\n", answer == stdAnswer, answer, stdAnswer);
    }
}