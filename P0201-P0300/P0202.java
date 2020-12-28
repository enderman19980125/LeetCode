import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isHappy(int n) {
        Set<Integer> s = new HashSet<>();
        s.add(n);
        while (true) {
            int m = 0;
            while (n > 0) {
                m += (n % 10) * (n % 10);
                n /= 10;
            }
            if (m == 1) return true;
            if (s.contains(m)) return false;
            s.add(m);
            n = m;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean answer;

        answer = solution.isHappy(19);
        System.out.printf("%b %b\n", answer, true);

        answer = solution.isHappy(2);
        System.out.printf("%b %b\n", answer, false);

        answer = solution.isHappy(1);
        System.out.printf("%b %b\n", answer, true);

        answer = solution.isHappy(12);
        System.out.printf("%b %b\n", answer, false);

        answer = solution.isHappy(2147483647);
        System.out.printf("%b %b\n", answer, false);
    }
}